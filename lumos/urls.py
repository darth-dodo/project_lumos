from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.hello),
   url(r'^technical/$', views.tech_landing),
   url(r'^technical/knowledge-base/$', views.knowledge_base),
   url(r'^soft-skills/$', views.soft_skills_landing),
# other landing page options
   url(r'^soft-skills-col/$', views.soft_skills_landing_col),
   url(r'^soft-skills-but/$', views.soft_skills_landing_but),
   url(r'^soft-skills/(?P<skill>.+)$', views.soft_skill_data),
   
   

]
