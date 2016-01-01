from django.db import models

# Create your models here.
def unicode_class(obj):
    s = ''
    for k,v in obj.__dict__.items():
        s += ('%s: %s\n' % (k,v))
    return s


def convert_to_dict(obj):
    return obj.__dict__

class ProgLang(models.Model):
    name = models.CharField(max_length=20,null=True,default=None)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return convert_to_dict(self)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'prog_lang'

class KnowledgeBase(models.Model):
    prog_lang = models.ForeignKey(ProgLang)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    desc = models.TextField()
    active = models.BooleanField(default=True)
    diff_levels = (
                (0, 'Beginner'),
                (1, 'Intermediate'),
                (2, 'Advanced')
    )
    difficulty = models.IntegerField(choices=diff_levels)
    diff_sort = models.IntegerField(default=99)
    data_type = (
                (0, 'Video'),
                (1, 'Article'),
                (2, 'Interactive Site'),
                (3, 'Other')
                )
    media_type = models.IntegerField(choices=data_type, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def __unicode__(self):
    #     return unicode_class(self)
    def __str__(self):
        return self.title
    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'tech_knowlege_base'

class SoftSkills(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return convert_to_dict(self)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'soft_skills'

class SoftSkillsData(models.Model):
    soft_skill = models.ForeignKey(SoftSkills)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    desc = models.TextField()
    active = models.BooleanField(default=True)
    diff_levels = (
                (0, 'Beginner'),
                (1, 'Intermediate'),
                (2, 'Advanced')
    )
    difficulty = models.IntegerField(choices=diff_levels, default=0)
    diff_sort = models.IntegerField(default=99)
    data_type = (
                (0, 'Video'),
                (1, 'Article'),
                (2, 'Interactive Site'),
                (3, 'Other')
                )
    media_type = models.IntegerField(choices=data_type, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def __unicode__(self):
    #     return unicode_class(self)
    def __str__(self):
        return self.title
    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'soft_knowlege_base'