from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^form2/$', views.form2, name='form2'),
    url(r'^$', views.form1, name='form1'),
    url(r'^ajax/populate/$', views.populate, name='populate'),
]
