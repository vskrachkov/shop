import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from starlette import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

django_application = get_asgi_application()
fastapi_application = FastAPI()

application = routing.Router(
    [
        routing.Mount("/api", app=fastapi_application),
        routing.Mount("/", app=django_application),
    ]
)
