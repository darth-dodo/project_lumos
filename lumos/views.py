from django.shortcuts import render
from django.http import HttpResponse
from .models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData
# Create your views here.
def hello(request):
    return render(request, 'home.html')

def tech_landing(request):
    return render(request, 'tech_landing.html')


def knowledge_base(request):
    return_data = []
    all_langs = ProgLang.objects.filter(active=1).order_by('name')
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
                # for converting links into iframe
                # current_entry['link'] = (entry.link).replace("watch?v=","embed/").replace("&list","?list")

                current_entry['link'] = entry.link
                current_entry['difficulty'] = entry.difficulty
                current_entry['diff_sort'] = entry.diff_sort
                current_entry['media_type'] = entry.media_type
                current_entry['data_desc'] = entry.desc

                current_lang['data'].append(current_entry)
            
            current_lang['data'] = sorted(current_lang['data'], key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

            return_data.append(current_lang)
    return render (request, 'knowledge_base.html', {'data' : return_data})

def knowledge_base_landing(request):
    return_data = []
    all_langs = ProgLang.objects.filter(active=1).order_by('name')
    return render (request, 'knowledge_base_landing.html', {"return_data" : return_data})

def knowledge_base_opt(request,lang):
    print lang
    return_data = []
    entries = KnowledgeBase.objects.filter(active=1,prog_lang=lang).order_by('diff_sort')
    if entries:
        current_lang = {}
        current_lang['name'] = lang.name
        # current_lang['lang_desc'] = lang.desc
        current_lang['data'] = []
        for entry in entries:
            current_entry = {}
            current_entry['title'] = entry.title
            # for converting links into iframe
            # current_entry['link'] = (entry.link).replace("watch?v=","embed/").replace("&list","?list")
            current_entry['link'] = entry.link
            current_entry['difficulty'] = entry.difficulty
            current_entry['diff_sort'] = entry.diff_sort
            current_entry['media_type'] = entry.media_type
            current_entry['data_desc'] = entry.desc
            current_lang['data'].append(current_entry)

            current_lang['data'] = sorted(current_lang['data'], key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

            return_data.append(current_lang)
    return render(request, 'tech_data.html', {"display_data" : return_data})
    

def soft_skills_landing(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing.html', {'all_soft_skills' : all_soft_skills})

def soft_skills_landing_col(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing_column.html', {'all_soft_skills' : all_soft_skills})

def soft_skills_landing_but(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing_button.html', {'all_soft_skills' : all_soft_skills})


def soft_skill_data(request, skill):
    print skill
    display_data = {}
    display_data['name'] = skill
    display_data['desc'] = SoftSkills.objects.filter(name=skill).values_list('desc',flat=True)
    all_entries = SoftSkillsData.objects.filter(active=1,soft_skill__name=skill)
    display_data['data'] = []
    for entry in all_entries:
        current_entry = {}
        current_entry['title'] = entry.title
        # for converting links into iframe
        # current_entry['link'] = (entry.link).replace("watch?v=","embed/").replace("&list","?list")
        current_entry['link'] = entry.link
        current_entry['difficulty'] = entry.difficulty
        current_entry['diff_sort'] = entry.diff_sort
        current_entry['media_type'] = entry.media_type
        current_entry['data_desc'] = entry.desc
        display_data['data'].append(current_entry)

    display_data['data'] = sorted(display_data['data'], key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

    print display_data
    return render(request, 'soft_skills_data.html', {'display_data' : display_data})
