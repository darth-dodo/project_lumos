from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
def unicode_class(obj):
    s = ''
    for k,v in obj.__dict__.items():
        s += ('%s: %s\n' % (k,v))
    return s


def convert_to_dict(obj):
    return obj.__dict__

class ProgLang(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True)
    desc = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProgLang, self).save(*args, **kwargs)
    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
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

    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'tech_knowlege_base'

class SoftSkills(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True)
    desc = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
   
    def clean(self):
        self.name = self.name.title()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SoftSkills, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode_class(self)
    def to_dict(self):
        return convert_to_dict(self)
    
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

    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'soft_knowlege_base'

class ProjectBase(models.Model):
    prog_lang = models.ManyToManyField(ProgLang)
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
    notes = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'tech_project_base'

class UserFeedback(models.Model):
    username = models.CharField(max_length=200,null=True,default=None)
    email = models.EmailField()
    feedback_note = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'user_feedback'

class RandomStuff(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    desc = models.TextField()
    active = models.BooleanField(default=True)
    data_type = (
                (0, 'Video'),
                (1, 'Article'),
                (2, 'Interactive Site'),
                (3, 'Other')
                )
    media_type = models.IntegerField(choices=data_type, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode_class(self)

    def to_dict(self):
        return convert_to_dict(self)
    
    class Meta:
        db_table = 'random_stuff'
