import datetime
import json


def json_dump_handler(data):
    if isinstance(data, datetime.date):
        return data.strftime("%d/%m/%Y")
    else:
        return data


def expand_choices(form):
    r = {}
    for k, v in form.cleaned_data.items():
        r[k] = v
        try:
            value = dict(form.fields[k].choices)[v]
            label_key = k + "_label"
            r[label_key] = value
        except Exception:
            pass
    return r


def age(birth_date):
    today = datetime.date.today()
    return today.year -\
        birth_date.year -\
        ((today.month, today.day) < (birth_date.month, birth_date.day))


def field_verbose(choices, key):
    return dict(choices)[key]


def calculate_schoolyear():
    today = datetime.date.today()
    ref_year = today.year - (today.month < 5)
    return "{}/{}".format(ref_year, ref_year+1)


def load_session_data(session, sections):
    data = {}
    for s in sections:
        if session.get(s):
            v = json.loads(session[s])
        else:
            v = None
        data[s] = v
    return data


def add_breadcrumb(name, url, breadcrumbs_session):
    breadcrumbs = json.loads(breadcrumbs_session)
    already_inserted = False
    for bc in breadcrumbs:
        if bc["name"] == name:
            bc["active"] = True
            already_inserted = True
        else:
            bc["active"] = False
    if not already_inserted:
        if name == "Itinerario":
            breadcrumbs.insert(2, {"name": name, "url": url, "active": True})
        else:
            breadcrumbs.append({"name": name, "url": url, "active": True})
    breadcrumbs_session = json.dumps(breadcrumbs)
    return breadcrumbs, breadcrumbs_session


def update_breadcrumbs(source_edulevel_code,
                       target_edulevel_code,
                       breadcrumbs_session):
    breadcrumbs = json.loads(breadcrumbs_session)
    bc_to_remove = -1
    for i, bc in enumerate(breadcrumbs):
        if bc["name"] == "Itinerario":
            bc_to_remove = i
        else:
            bc["url"] = bc["url"].replace(
                source_edulevel_code, target_edulevel_code
            )
    if bc_to_remove != -1:
        breadcrumbs.pop(bc_to_remove)
    return json.dumps(breadcrumbs)


def add_fields_to_student(data):
    data["age"] = age(data["birth_date"])
    data["adult"] = data["age"] >= 18
    data["full_name"] = data["name"] + " " + data["surname"]
    lyi = data["lastyear_institution"].upper()
    data["attached_ceip"] = \
        (lyi.find("SAN ANTONIO") != -1) or \
        (lyi.find("TOMÁS DE IRIARTE") != -1) or \
        (lyi.find("TOMAS DE IRIARTE") != -1)
    if data["nif"]:
        data["id_label"] = "NIF"
        data["id_value"] = data["nif"]
    elif data["nie"]:
        data["id_label"] = "NIE"
        data["id_value"] = data["nie"]
    elif data["passport"]:
        data["id_label"] = "Pasaporte"
        data["id_value"] = data["passport"]
    return data


def add_fields_to_responsible(data):
    data["age"] = age(data["birth_date"])
    data["full_name"] = data["name"] + " " + data["surname"]
    data["is_tutor"] = data["link"] in ["TUO", "TUA"]
    if data["nif"]:
        data["id_label"] = "NIF"
        data["id_value"] = data["nif"]
    elif data["nie"]:
        data["id_label"] = "NIE"
        data["id_value"] = data["nie"]
    elif data["passport"]:
        data["id_label"] = "Pasaporte"
        data["id_value"] = data["passport"]
    return data


def get_responsibles_ids(session):
    try:
        r1_id = session["responsible1"]["id_value"]
    except:
        r1_id = None
    try:
        r2_id = session["responsible2"]["id_value"]
    except:
        r2_id = None
    return (r1_id, r2_id)
