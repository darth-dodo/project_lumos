from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.hello),
   url(r'^technical/$', views.tech_landing),
   url(r'^technical/knowledge-base/$', views.knowledge_base),

]
