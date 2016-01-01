from django.contrib import admin
from .models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData

admin.site.register(ProgLang)
admin.site.register(KnowledgeBase)
admin.site.register(SoftSkills)
admin.site.register(SoftSkillsData)