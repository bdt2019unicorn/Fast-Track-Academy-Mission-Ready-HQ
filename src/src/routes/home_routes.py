from django.urls import path, include
from ..controller import home_controller



home_routes = \
    [
        path('', home_controller.home_controller.index),
        path('home', home_controller.home_controller.index)
    ]