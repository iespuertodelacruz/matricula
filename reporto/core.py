from jinja2 import Environment, FileSystemLoader
from subprocess import Popen, PIPE
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
            RENDERED_FILES_DIR + str(uuid.uuid4()) + ".pdf"
        kwargs["generation_time"] = self.generation_time
        kwargs["root"] = TEMPLATES_DIR
        self.rendered_template = self.template.render(kwargs)
        p = Popen(["prince", "-", self.output_filename], stdin=PIPE)
        p.stdin.write(self.rendered_template.encode("utf-8"))
        p.stdin.close()
        p.communicate()

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
