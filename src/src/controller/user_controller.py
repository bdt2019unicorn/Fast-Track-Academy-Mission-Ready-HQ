import inspect
import types

from . import main_controller
from . import login_authorize_class
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ..helper import database


def not_login_authorize(function):
    def general_function(request, *args, **kwargs):
        try:
            if request.session['username']:
                return main_controller.redirect_home_page(self=main_controller, request=request)
        except:
            pass
        return function(request, *args)

    return general_function


def not_login_authorize_class(cls):
    for name, function in inspect.getmembers(cls):
        if isinstance(function, types.FunctionType):
            setattr(cls, name, not_login_authorize(function))
    return cls


def modify_fields(fields):
    if isinstance(fields, list):
        return fields
    else:
        return [fields]


def http_response_check_existed(request, fields):
    fields = modify_fields(fields)
    data = get_data_POST_request(request=request, fields=fields)
    check = user_controller.check_existed(self=user_controller, data=data)
    check = str(check).lower()
    return HttpResponse(check)


def get_data_POST_request(request, fields):
    data = {}
    for field in fields:
        data[field] = request.POST.get(field)
    return data


class user_controller(main_controller):
    table = 'users'

    @login_authorize_class
    class login_required:
        def index(request):
            return render(request=request, template_name='user/login_required/index.html')

        def logout(request):
            del request.session['username']
            return main_controller.redirect_home_page(self = user_controller, request=request)

    @not_login_authorize_class
    class no_login_requied:

        def login_page(request):
            return render(request=request, template_name='user/no_login_required/login.html')

        def check_login(request):
            if request.method == 'POST':
                fields = ['username', 'password']
                response = http_response_check_existed(request, fields)
                if str(response.content) == "b'true'":
                    request.session['username'] = request.POST.get('username')
                return response
            else:
                return main_controller.redirect_home_page(self=user_controller, request=request)

        def register_page(request):
            return render(request=request, template_name='user/no_login_required/register.html')

        def check_user_existed(request):
            if request.method == 'POST':
                try:
                    return http_response_check_existed(request=request, fields='username')
                except:
                    return http_response_check_existed(request=request,
                                                       fields='email')
            else:
                return main_controller.redirect_home_page(self=user_controller, request=request)

        def register_user(request):
            if request.method == 'POST':
                fields = ['name', 'username', 'email', 'password']
                data = get_data_POST_request(request=request, fields=fields)
                mysql = user_controller.mysql_insert(self=user_controller, data=data)
                exec = database.connect.exec(mysql)
                return HttpResponse(str(exec).lower())
            else:
                return main_controller.redirect_home_page(self=user_controller, request=request)
