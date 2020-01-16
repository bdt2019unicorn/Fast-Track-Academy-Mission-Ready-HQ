from django.urls import path, include
from ..controller import about_controller



about_routes = \
    [
        path('', about_controller.about_controller.index),
    ]