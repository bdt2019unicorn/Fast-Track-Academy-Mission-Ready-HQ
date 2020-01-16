from django.urls import path, include
from .home_routes import home_routes
from .about_routes import about_routes
from .contact_routes import contact_routes
from .user_routes import user_routes

routes = \
    [
        path('', include(home_routes)),
        path('about', include(about_routes)),
        path('contact', include(contact_routes)),
        path('user', include(user_routes) )
    ]