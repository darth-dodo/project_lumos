from lumos.models import ProgLang, KnowledgeBase, SoftSkills, SoftSkillsData, UserFeedback, ProjectBase, RandomStuff

def get_data_from_slug(slug):

    return_data = [("Title", "Link", "Desc")]
    req_data = []

    soft_slugs = SoftSkills.objects.filter(active=1).values_list('slug', flat=True)
    tech_slugs = ProgLang.objects.filter(active=1).values_list('slug', flat=True)
    print soft_slugs
    print tech_slugs
    
    if slug in soft_slugs:
        req_data = SoftSkillsData.objects.filter(soft_skill__slug=slug).filter(active=1).values_list("title","link","desc").order_by("soft_skill__name", "difficulty","diff_sort")
    
    if slug in tech_slugs:
        req_data = KnowledgeBase.objects.filter(prog_lang__slug=slug).filter(active=1).values_list("title","link","desc").order_by("prog_lang__name", "difficulty","diff_sort")
        return_data.extend(req_data)
    
    if req_data:
        return_data.extend(req_data)
        return return_data
    else:
        return False

def get_knowledge_base():
    return_data = [("Prog Lang", "Title", "Link", "Desc")]
    req_data = KnowledgeBase.objects.filter(active=1).values_list("prog_lang__name", "title","link","desc").order_by("prog_lang__name", "difficulty","diff_sort")
    print len(req_data)
    if req_data:
        return_data.extend(req_data)
        return return_data
    else:
        return False

def get_soft_base():
    return_data = [("Soft Skill", "Title", "Link", "Desc")]
    req_data = SoftSkillsData.objects.filter(active=1).values_list("soft_skill__name", "title","link","desc").order_by("soft_skill__name", "difficulty","diff_sort")

    if req_data:
        return_data.extend(req_data)
        return return_data
    else:
        return False

def get_csv_data(location_slug):
    print 'entering the utils'
    print location_slug
    if location_slug == "knowledge-base":
        return_data = get_knowledge_base()
    elif location_slug == "soft-skills":
        return_data = get_soft_base()
    else:
        return_data = get_data_from_slug(location_slug)
    return return_data
