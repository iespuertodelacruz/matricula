from .academic_form_1ESO import AcademicForm_1ESO
from .academic_form_2ESO import AcademicForm_2ESO
from .academic_form_3ESO import AcademicForm_3ESO
from .academic_form_4ESO import AcademicForm_4ESO
from .academic_form_1CIE import AcademicForm_1CIE
from .academic_form_1CIE import AcademicForm_1CIE_CCS
from .academic_form_1CIE import AcademicForm_1CIE_TEC
from .academic_form_1SOC import AcademicForm_1SOC
from .academic_form_1SOC import AcademicForm_1SOC_HUM
from .academic_form_1SOC import AcademicForm_1SOC_SOC


def get_formclass(code):
    if code == "1ESO":
        return AcademicForm_1ESO
    if code == "2ESO":
        return AcademicForm_2ESO
    if code == "3ESO":
        return AcademicForm_3ESO
    if code == "4ESO":
        return AcademicForm_4ESO
    if code == "1CIE":
        return AcademicForm_1CIE
    if code == "1CIE_CCS":
        return AcademicForm_1CIE_CCS
    if code == "1CIE_TEC":
        return AcademicForm_1CIE_TEC
    if code == "1SOC":
        return AcademicForm_1SOC
    if code == "1SOC_HUM":
        return AcademicForm_1SOC_HUM
    if code == "1SOC_SOC":
        return AcademicForm_1SOC_SOC
