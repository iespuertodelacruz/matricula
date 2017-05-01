import datetime


def json_dump_handler(data):
    if isinstance(data, datetime.date):
        return data.isoformat()
    else:
        return data
