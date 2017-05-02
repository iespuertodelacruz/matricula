import datetime


def json_dump_handler(data):
    if isinstance(data, datetime.date):
        return data.isoformat()
    else:
        return data


def age(birth_date):
    today = datetime.date.today()
    return today.year -\
        birth_date.year -\
        ((today.month, today.day) < (birth_date.month, birth_date.day))


def field_verbose(choices, key):
    return dict(choices)[key]
