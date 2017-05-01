from .academic_form_1ESO import AcademicForm_1ESO
from .academic_form_2ESO import AcademicForm_2ESO
from .academic_form_3ESO import AcademicForm_3ESO
from .academic_form_4ESO import AcademicForm_4ESO


def get_formclass(edulevel_code):
    if edulevel_code == "1ESO":
        return AcademicForm_1ESO
    if edulevel_code == "2ESO":
        return AcademicForm_2ESO
    if edulevel_code == "3ESO":
        return AcademicForm_3ESO
    if edulevel_code == "4ESO":
        return AcademicForm_4ESO
