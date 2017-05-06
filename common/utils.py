import datetime


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
        except:
            pass
    return r


def age(birth_date):
    today = datetime.date.today()
    return today.year -\
        birth_date.year -\
        ((today.month, today.day) < (birth_date.month, birth_date.day))


def field_verbose(choices, key):
    return dict(choices)[key]
