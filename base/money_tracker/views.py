from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.base import TemplateView
from django.views.generic import ListView


import datetime

import json

from .models import *

# Create your views here.
class IndexView(TemplateView):

    template_name = "money_tracker/index.html"

class DailyView(ListView):

    template_name = "money_tracker/daily.html"

    def get_queryset(self):
        lines = Line.objects.filter(user=self.request.user)
        user_date = datetime.date(int(self.kwargs['year']), int(self.kwargs['month']), int(self.kwargs['day']))
        lines = lines.filter(date=user_date)
        return lines

    def post(self, request, year, month, day):
        user_date = datetime.date(int(year), int(month), int(day))
        json_raw = request.POST.get('json_string')
        jsonified = json.loads(json_raw.replace('\n', '').strip())

        for i in jsonified:
            company = jsonified[i][0]
            item = jsonified[i][1]
            amount_in = float(jsonified[i][2])
            amount_out = float(jsonified[i][3])
            reason = jsonified[i][4]
            unnecessary = (False if (jsonified[i][5] == 'false') else True)
            pk = int(jsonified[i][6])

            if(pk != -1):
                line = Line.objects.get(pk=pk)
                line.date = user_date
                line.company = company
                line.item = item
                line.amount_in = amount_in
                line.amount_out = amount_out
                line.reason = reason
                line.unnecessary = unnecessary
            else:
                line = Line(user_id=self.request.user.id, date=user_date, company=company, item=item, amount_in=amount_in, reason=reason, unnecessary=unnecessary, amount_out=amount_out )

            line.save()

        return HttpResponse(json.dumps(jsonified), content_type="application/json")
