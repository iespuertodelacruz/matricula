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
from .academic_form_2CIE import AcademicForm_2CIE
from .academic_form_2CIE import AcademicForm_2CIE_CCS
from .academic_form_2CIE import AcademicForm_2CIE_TEC
from .academic_form_2SOC import AcademicForm_2SOC
from .academic_form_2SOC import AcademicForm_2SOC_HUM
from .academic_form_2SOC import AcademicForm_2SOC_SOC
from .academic_form_PMAR import AcademicForm_1PMAR
from .academic_form_PMAR import AcademicForm_2PMAR
from .academic_form_PMAR import AcademicForm_PostPMAR
from .academic_form_FP import AcademicForm_1FPB
from .academic_form_FP import AcademicForm_2FPB
from .academic_form_FP import AcademicForm_1CFGM
from .academic_form_FP import AcademicForm_2CFGM
from .academic_form_FP import AcademicForm_1CFGS
from .academic_form_FP import AcademicForm_2CFGS
from .academic_form_FP import AcademicForm_3CFGS
from .family_forms import Responsible1Form
from .family_forms import Responsible2Form

FORMS = {
    "1ESO": AcademicForm_1ESO,
    "2ESO": AcademicForm_2ESO,
    "3ESO": AcademicForm_3ESO,
    "4ESO": AcademicForm_4ESO,
    "1CIE": AcademicForm_1CIE,
    "1CIE_CCS": AcademicForm_1CIE_CCS,
    "1CIE_TEC": AcademicForm_1CIE_TEC,
    "1SOC": AcademicForm_1SOC,
    "1SOC_HUM": AcademicForm_1SOC_HUM,
    "1SOC_SOC": AcademicForm_1SOC_SOC,
    "2CIE": AcademicForm_2CIE,
    "2CIE_CCS": AcademicForm_2CIE_CCS,
    "2CIE_TEC": AcademicForm_2CIE_TEC,
    "2SOC": AcademicForm_2SOC,
    "2SOC_HUM": AcademicForm_2SOC_HUM,
    "2SOC_SOC": AcademicForm_2SOC_SOC,
    "1PMAR": AcademicForm_1PMAR,
    "2PMAR": AcademicForm_2PMAR,
    "PostPMAR": AcademicForm_PostPMAR,
    "1FPB": AcademicForm_1FPB,
    "2FPB": AcademicForm_2FPB,
    "1CFGM": AcademicForm_1CFGM,
    "2CFGM": AcademicForm_2CFGM,
    "1CFGS": AcademicForm_1CFGS,
    "2CFGS": AcademicForm_2CFGS,
    "3CFGS": AcademicForm_3CFGS,
    "R1": Responsible1Form,
    "R2": Responsible2Form
}


def get_formclass(code):
    return FORMS[code]
