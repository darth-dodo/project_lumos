from django.shortcuts import render
from django.http import HttpResponse
from .models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData, UserFeedback, ProjectBase, RandomStuff
from lumos.utils import get_csv_data
from django.views.decorators.csrf import csrf_exempt
import json
import csv

def hello(request):
    return render(request, 'home.html')

def tech_landing(request):
    return render(request, 'tech_listing.html')

def knowledge_base_landing(request):
    return_data = ProgLang.objects.filter(active=1).order_by('sort_id')
    return render(request, 'generic_landing.html', {'return_data' : return_data ,'page_title' : 'Technical Skills'})

def soft_skills_landing(request):
    all_soft_skills = SoftSkills.objects.filter(active=1).order_by('sort_id')
    return render(request, 'generic_landing.html', {'return_data' : all_soft_skills ,'page_title' : 'Soft Skills'})

def knowledge_base_all(request):
    return_data = []
    all_langs = ProgLang.objects.filter(active=1).order_by('name')
    for lang in all_langs:
        entries = KnowledgeBase.objects.filter(active=1,prog_lang=lang).order_by('diff_sort')
        if entries:
            current_lang = {}
            current_lang['name'] = lang.name
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
            
            current_lang['data'] = sorted(current_lang['data'], key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

            return_data.append(current_lang)
    return render (request, 'knowledge_base.html', {'data' : return_data})

def get_display_data(raw_data):
    return_data = []
    for entry in raw_data:
        current_entry = {}
        current_entry['title'] = entry.title
        current_entry['link'] = entry.link
        current_entry['difficulty'] = entry.difficulty
        current_entry['diff_sort'] = entry.diff_sort
        current_entry['media_type'] = entry.media_type
        current_entry['data_desc'] = entry.desc
        return_data.append(current_entry)
    return_data = sorted(return_data, key=lambda x: (int(x['difficulty']), int(x['diff_sort'])))

    return return_data

def knowledge_base_data(request,slug):
    display_data = {}
    display_data['type'] = 'Knowledge Base'
    slug_details = ProgLang.objects.get(slug=slug)
    raw_data = KnowledgeBase.objects.filter(active=1, prog_lang__slug=slug)
    display_data['name'] = slug_details.name
    display_data['desc'] = slug_details.desc if slug_details.desc else None
    if len(raw_data):
        display_data['data'] = get_display_data(raw_data)
    else:
        display_data['data'] = None
    
    return render(request, 'data_display.html', {"display_data" : display_data})

def soft_skills_data(request,slug):
    display_data = {}
    display_data['type'] = 'Soft Skills'
    slug_details = SoftSkills.objects.get(slug=slug)
    raw_data = SoftSkillsData.objects.filter(active=1, soft_skill__slug=slug)
    display_data['name'] = slug_details.name
    display_data['desc'] = slug_details.desc if slug_details.desc else None
    if len(raw_data):
        display_data['data'] = get_display_data(raw_data)
    else:
        display_data['data'] = None
    
    return render(request, 'data_display.html', {"display_data" : display_data})
 
def project_base(request):
    all_projects = ProjectBase.objects.filter(active=1).order_by('difficulty','diff_sort')
    return_data = []
    for project in all_projects:
        curr_proj = {}
        curr_proj['id'] = project.id
        curr_proj['title'] = project.title
        curr_proj['link'] = project.link
        curr_proj['desc'] = project.desc
        curr_proj['difficulty'] = project.difficulty
        curr_proj['all_langs'] = [lang.name for lang in project.prog_lang.all()]

        return_data.append(curr_proj)
    return render(request, 'project_base.html', {'return_data' : return_data})

@csrf_exempt
def feedback_form(request):
    if request.method == 'POST' and request.is_ajax():
        json_string = request.body.decode(encoding='UTF-8')
        data = json.loads(json_string)
        username =  str(data['username'])
        email = data['email']
        feedback = str(data['feedback'])
        user_feedback = UserFeedback(username=username, email=email, feedback_note=feedback)
        user_feedback.save()
    return HttpResponse(json.dumps(True))

def stuff_to_know(request):
    all_stuff = RandomStuff.objects.filter(active=1).order_by('id')
    return_data = []
    for stuff in all_stuff:
        curr_stuff = {}
        curr_stuff['id'] = stuff.id
        curr_stuff['title'] = stuff.title
        curr_stuff['link'] = stuff.link
        curr_stuff['desc'] = stuff.desc

        return_data.append(curr_stuff)
    return render(request, 'stuff.html', {'return_data' : return_data})

def csv_gen_view(request, location_slug):
    csv_name = "[ProjectLumos] " + location_slug + ".csv"
    csv_data = []
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + csv_name + '"'
    writer = csv.writer(response)
    csv_data = get_csv_data(location_slug)
    if csv_data:
        for row in csv_data:
            writer.writerow(row)
        return response
    else:
        return HttpResponse(False)