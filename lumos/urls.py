from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.hello),
   url(r'^technical/$', views.tech_landing),
   url(r'^technical/knowledge-base/$', views.knowledge_base_landing),
   url(r'^technical/project-base/$', views.project_base),
   url(r'^technical/knowledge-base/(?P<slug>.+)$', views.knowledge_base_data),
   url(r'^soft-skills/$', views.soft_skills_landing),
   url(r'^soft-skills/(?P<slug>.+)$', views.soft_skills_data),
   url(r'^feedback-form/$', views.feedback_form), 
   url(r'^technical/awesome-stuff/$', views.stuff_to_know),
   ]
