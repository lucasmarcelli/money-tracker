from django.conf.urls import url, include

from .views import *

urlpatterns = [

    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^get_data/$', IndexView.as_view(), name='post'),
    url(r'^daily/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', DailyView.as_view(), name='daily'),
    url(r'^daily/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/get_data/$', DailyView.as_view(), name='daily_post'),
]
