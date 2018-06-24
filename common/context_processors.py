import os
from django.conf import settings
import json


ASSETS = ("css", "js", "img", "fonts", "files", "vendor/css", "vendor/js")
BASE_ASSETS_PATH = os.path.join(settings.BASE_DIR, "common/static/dist/")
STATIC_DIST_URL = "/static/dist/"


def glob(request):
    context = {"assets": {}}
    for asset in ASSETS:
        manifest_path = os.path.join(
            BASE_ASSETS_PATH, asset, "rev-manifest.json"
        )
        with open(manifest_path) as f:
            manifest_json = json.load(f)
        for k, v in manifest_json.items():
            context["assets"][k] = os.path.join(STATIC_DIST_URL, asset, v)

    return context
