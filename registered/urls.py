from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.events, name='events-all'),
        url(r'^events/$', views.events, name='events-all'),
        url(r'^events/(?P<event_id>[0-9]+)/',
            views.event_details, name='event-single'),
]
