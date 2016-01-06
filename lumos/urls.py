from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.hello),
   url(r'^technical/$', views.tech_landing),
   # global knowledge-base
   url(r'^technical/knowledge-base/$', views.knowledge_base),
   url(r'^technical/knowledge-base-landing/$', views.knowledge_base_landing),
   url(r'^technical/knowledge-base-landing/(?P<lang>.+)$', views.knowledge_base_opti),
   url(r'^soft-skills/$', views.soft_skills_landing),
   url(r'^soft-skills/(?P<skill>.+)$', views.soft_skill_data),
# other landing page options
   url(r'^soft-skills-col/$', views.soft_skills_landing_col),
   url(r'^soft-skills-but/$', views.soft_skills_landing_but),
   
   

]
