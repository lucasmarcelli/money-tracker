from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.base import TemplateView

import json

# Create your views here.
class IndexView(TemplateView):

    template_name = "money_tracker/index.html"

class DailyView(TemplateView):

    template_name = "money_tracker/daily.html"
