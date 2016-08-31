from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    DataListAPIView
    )

urlpatterns = [
    url(r'^$', DataListAPIView.as_view(), name='list'),
    # url(r'^(?P<indicator_name>[\w, ]+)/name/$', IndicatorDetailAPIView.as_view(), name='indicator_name'),
]

urlpatterns = format_suffix_patterns(urlpatterns)