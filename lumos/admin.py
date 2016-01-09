from django.contrib import admin
from .models import (ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData,
                     ProjectBase, UserFeedback)


class ProgLangAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class SoftSkillsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ProgLang, ProgLangAdmin)
admin.site.register(KnowledgeBase)
admin.site.register(SoftSkills, SoftSkillsAdmin)
admin.site.register(SoftSkillsData)
admin.site.register(ProjectBase)
admin.site.register(UserFeedback)