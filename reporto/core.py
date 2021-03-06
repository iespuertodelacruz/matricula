from jinja2 import Environment, FileSystemLoader
import uuid
import os
import datetime
from .filters import boolean


TEMPLATES_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "templates"
)
RENDERED_FILES_DIR = "/tmp/"

ENV = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
ENV.filters["boolean"] = boolean


class PdfReport():
    def __init__(self, template_filepath, http_response=None):
        """
        http_response: instance of django.http.HttpResponse (optional)
        """
        self.template = ENV.get_template(template_filepath)
        self.generation_time = datetime.datetime.now()
        self.response = http_response

    def render(self, **kwargs):
        """
        output_filename: in case you want to save the output (optional)
        """
        self.output_filename = kwargs.get("output_filename", None) or \
            os.path.join(RENDERED_FILES_DIR, str(uuid.uuid4()) + '.pdf')
        rendered_filename = \
            os.path.join(RENDERED_FILES_DIR, str(uuid.uuid4()) + '.html')
        kwargs["generation_time"] = self.generation_time
        kwargs["root"] = TEMPLATES_DIR
        self.rendered_template = self.template.render(kwargs)
        # Estas dos líneas no funcionan así en producción. El problema viene
        # con uwsgi ya que no exporta las variables de entorno LC_ALL y LANG
        # Habría que incluirlas en el fichero de configuración de uwsgi.
        # Ejemplo: https://gist.github.com/davesque/4477301
        # with open(rendered_filename, 'w') as f:
        #     f.write(self.rendered_template)
        with open(rendered_filename, 'wb') as f:
            f.write(self.rendered_template.encode('utf-8'))
        os.system(f'prince {rendered_filename} -o {self.output_filename}')
        os.remove(rendered_filename)

    def http_response(self, output_filename=None, delete=True):
        """
        Use this method if you want to return a http response through django
        """
        response = self.response(open(self.output_filename, "rb"))
        if delete:
            os.remove(self.output_filename)
        response["Content-Type"] = "application/pdf"
        user_filename = output_filename or os.path.splitext(
                os.path.basename(self.template.filename))[0]
        response["Content-Disposition"] = \
            "attachment; filename='{}.pdf'".format(user_filename)
        return response
