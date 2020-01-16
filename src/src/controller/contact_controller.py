from . import main_controller
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


class contact_controller(main_controller):
    def index(request):
        return render(request=request, template_name='contact/index.html')

