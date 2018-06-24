import os
from django.conf import settings
import json


def glob(request):
    context = {"assets": {}}
    for asset in ("css", "js", "img"):
        manifest_path = os.path.join(
            settings.BASE_DIR,
            "common/static/dist/" + asset,
            "rev-manifest.json"
        )
        with open(manifest_path) as f:
            tmp = json.load(f)
        context["assets"] = dict(**context["assets"], **tmp)

    return context
