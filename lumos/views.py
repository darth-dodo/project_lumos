from django.shortcuts import render
from django.http import HttpResponse
from .models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData
# Create your views here.
def hello(request):
    return render(request, 'patience.html')

def tech_landing(request):
    return render(request, 'tech_landing.html')

def knowledge_base(request):
    return_data = []
    all_langs = ProgLang.objects.filter(active=1).order_by('id')
    for lang in all_langs:
        entries = KnowledgeBase.objects.filter(active=1,prog_lang=lang).order_by('diff_sort')
        if entries:
            current_lang = {}
            current_lang['name'] = lang.name
            # current_lang['lang_desc'] = lang.desc
            current_lang['data'] = []
            for entry in entries:
                current_entry = {}
                current_entry['title'] = entry.title
                current_entry['link'] = entry.link
                current_entry['difficulty'] = entry.difficulty
                current_entry['diff_sort'] = entry.diff_sort
                current_entry['media_type'] = entry.media_type
                current_entry['data_desc'] = entry.desc
                
                current_lang['data'].append(current_entry)
            return_data.append(current_lang)
    return render (request, 'knowledge_base.html', {'data' : return_data})


