import os
from django.conf import settings
import json


def glob(request):
    d = {}
    for asset in ("css", "js"):
        manifest_path = os.path.join(
            settings.BASE_DIR,
            "common/static/dist/" + asset,
            "rev-manifest.json"
        )
        with open(manifest_path) as f:
            tmp = json.load(f)
        d[asset] = {os.path.splitext(k)[0]: v for k, v in tmp.items()}

    return d
