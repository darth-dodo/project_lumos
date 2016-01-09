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
    all_prog_langs = ProgLang.objects.filter(active=1).order_by('id')
    print all_prog_langs
    return render (request, 'knowledge_base_landing.html', {"return_data" : all_prog_langs})

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

def get_display_data(raw_data):
    return_data = []
    for entry in raw_data:
        current_entry = {}
        current_entry['title'] = entry.title
        # for converting links into iframe
        # current_entry['link'] = (entry.link).replace("watch?v=","embed/").replace("&list","?list")
        current_entry['link'] = entry.link
        current_entry['difficulty'] = entry.difficulty
        current_entry['diff_sort'] = entry.diff_sort
        current_entry['media_type'] = entry.media_type
        current_entry['data_desc'] = entry.desc
        return_data.append(current_entry)
    return_data = sorted(return_data, key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

    return return_data

def knowledge_base_data(request,slug):
    print slug
    display_data = {}

    slug_details = ProgLang.objects.get(slug=slug)
    raw_data = KnowledgeBase.objects.filter(active=1, prog_lang__slug=slug)
    display_data['name'] = slug_details.name
    display_data['desc'] = slug_details.desc if slug_details.desc else None
    if len(raw_data):
        display_data['data'] = get_display_data(raw_data)
    else:
        display_data['data'] = None
    
    return render(request, 'knowledge_base_data.html', {"display_data" : display_data})

def soft_skills_landing(request):
    all_soft_skills = SoftSkills.objects.filter(active=1)
    return render(request, 'soft_skills_landing.html', {'all_soft_skills' : all_soft_skills})

def soft_skills_data(request,slug):
    print slug
    display_data = {}

    slug_details = SoftSkills.objects.get(slug=slug)
    raw_data = SoftSkillsData.objects.filter(active=1, soft_skill__slug=slug)
    display_data['name'] = slug_details.name
    display_data['desc'] = slug_details.desc if slug_details.desc else None
    if len(raw_data):
        display_data['data'] = get_display_data(raw_data)
    else:
        display_data['data'] = None
    
    return render(request, 'knowledge_base_data.html', {"display_data" : display_data})
 

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
