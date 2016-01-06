from django.contrib import admin
from .models import (ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData,
                     ProjectBase, UserFeedback)

admin.site.register(ProgLang)
admin.site.register(KnowledgeBase)
admin.site.register(SoftSkills)
admin.site.register(SoftSkillsData)
admin.site.register(ProjectBase)
admin.site.register(UserFeedback)