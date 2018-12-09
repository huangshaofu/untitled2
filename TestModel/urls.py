from django.conf.urls import url
from . import views,addtest_req

app_name = 'TestM'  # 关键是这行
urlpatterns = [
    url(r'^addtest/$', addtest_req.addtest_post),
    url(r'^(?P<question_id>[0-9]+)/detail/$', views.index, name='detail'),
]