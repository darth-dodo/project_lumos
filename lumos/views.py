from django.shortcuts import render
from django.http import HttpResponse
from .models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData, UserFeedback
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def hello(request):
    return render(request, 'home.html')

def tech_landing(request):
    return render(request, 'tech_landing.html')

def knowledge_base_landing(request):
    all_prog_langs = ProgLang.objects.filter(active=1).order_by('id').values_list('name',flat=True)
    print all_prog_langs
    return render (request, 'knowledge_base_landing.html', {"all_prog_langs" : all_prog_langs})

def knowledge_base_all(request):
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

def knowledge_base_data(request,lang):
    print lang
    display_data = {}

    entries = KnowledgeBase.objects.filter(active=1,prog_lang__name=lang).order_by('diff_sort')
    display_data['name'] = lang

    lang_desc = ProgLang.objects.filter(name=lang).values_list('desc',flat=True)
    print lang_desc
    if lang_desc:
        display_data['desc'] = lang_desc[0]
    else:
        display_data['desc'] = None
    print display_data
    if entries:
        display_data['data'] = []
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
            display_data['data'].append(current_entry)

            display_data['data'] = sorted(display_data['data'], key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))
    return render(request, 'knowledge_base_data.html', {"display_data" : display_data})
 
def soft_skills_landing(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing.html', {'all_soft_skills' : all_soft_skills})


def soft_skill_data(request, skill):
    print skill
    display_data = {}
    display_data['name'] = skill
    skill_desc = SoftSkills.objects.filter(name=skill).values_list('desc',flat=True)
    if skill_desc:
        display_data['desc'] = skill_desc[0]
    else:
        display_data['desc'] = None
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

def soft_skills_landing_col(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing_column.html', {'all_soft_skills' : all_soft_skills})

def soft_skills_landing_but(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).values_list('name', flat=True)
    all_soft_skills = sorted([a.title() for a in all_soft_skills])
    return render(request, 'soft_skills_landing_button.html', {'all_soft_skills' : all_soft_skills})

@csrf_exempt
def feedback_form(request):
    if request.method == 'POST' and request.is_ajax():
        json_string = request.body.decode(encoding='UTF-8')
        data = json.loads(json_string)
        print data
        username =  str(data['username'])
        email = data['email']
        feedback = str(data['feedback'])
        print feedback
        user_feedback = UserFeedback(username = username,email = email, feedback_note = feedback)
        print user_feedback
        user_feedback.save()
    return HttpResponse(json.dumps(True))
