from django.urls import path, include
from ..controller import contact_controller



contact_routes = \
    [
        path('', contact_controller.contact_controller.index),
    ]