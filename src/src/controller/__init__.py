import inspect
import types
from django.http import HttpResponseRedirect
from ..helper import database


def authorize_function(function):
    def general_function(request, *args, **kwargs):
        try:
            if request.session['username']:
                return function(request, *args)
        except Exception as e:
            url = request.build_absolute_uri('user/login')
            return HttpResponseRedirect(url)

    return general_function


def login_authorize_class(cls):
    for name, function in inspect.getmembers(cls):
        if isinstance(function, types.FunctionType):
            setattr(cls, name, authorize_function(function))
    return cls


def remove_last_value(string, value):
    last_comma = string.rfind(value)
    string = string[:last_comma]
    return string


class main_controller:
    table = ''
    id = 'id'

    def redirect_home_page(self, request):
        url = request.build_absolute_uri('/')
        print('it goes to my main controller, I just need to know why this thing not working')
        print("????????????????????????????????????????????????????????????????????????")
        print(url)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return HttpResponseRedirect(url)

    def mysql_where(self, data):
        mysql = " WHERE "
        for field, value in data.items():
            mysql += field + " = '" + value + "' AND "
        mysql = remove_last_value(mysql, 'AND')
        return mysql

    def mysql_insert(self, data):
        mysql = "INSERT INTO `" + self.table + "` ("
        values = " VALUES ("
        for field, value in data.items():
            mysql += '`' + field + '`' + ","
            values += "'" + value + "',"
        mysql = remove_last_value(mysql, ',')
        values = remove_last_value(values, ',')
        values += ");"
        mysql += ")" + values
        return mysql

    def check_existed(self, data):
        mysql = 'SELECT * FROM ' + self.table + self.mysql_where(self=self, data=data)
        data = database.connect.get_data(mysql=mysql)
        return len(data) > 0
