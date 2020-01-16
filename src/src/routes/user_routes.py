from django.urls import path, include
from ..controller import user_controller



user_routes = \
    [
        path('/', user_controller.user_controller.login_required.index),
        path('/logout', user_controller.user_controller.login_required.logout),
        path('/login', user_controller.user_controller.no_login_requied.login_page),
        path('/check_login', user_controller.user_controller.no_login_requied.check_login),
        path('/register', user_controller.user_controller.no_login_requied.register_page),
        path('/check_user_existed', user_controller.user_controller.no_login_requied.check_user_existed),
        path('/register_user', user_controller.user_controller.no_login_requied.register_user)
    ]