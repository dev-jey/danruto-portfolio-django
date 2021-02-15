from django.db import models
from tinymce.models import HTMLField
import datetime

from django.utils.text import slugify

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=100, default='')
    dribble = models.CharField(max_length=100, default='')
    linkedin = models.CharField(max_length=100, default='')
    behance = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100, default='Designer')
    description = HTMLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = HTMLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='')
    description = HTMLField()
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    slug = models.SlugField(db_index=True, max_length=1000, default='',
                            editable=False,
                            unique=True, blank=True, primary_key=True)
    image = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    link = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        '''Defines the ordering of the
         projects if retrieved'''
        ordering = ('date',)

    def __str__(self):
        return self.title

    def generate_slug(self):
        """generating a slug for the title of the project
            eg: this-is-an-project"""
        slug = slugify(self.title)
        new_slug = slug
        s = 1
        while Project.objects.filter(slug=new_slug).exists():
            """increase value of slug by one"""
            new_slug = f'{slug}-{s}'
            s += 1
        return new_slug

    def save(self, *args, **kwargs):
        """create a project and save to the database"""
        if not self.slug:
            self.slug = self.generate_slug()
        super(Project, self).save(*args, **kwargs)


def update_slug(sender, instance, signal, **kwargs):
    '''Signal to update an project's slug once title is updated'''
    if kwargs.get('updated', True):
        project = Project.objects.filter(slug=instance.pk)
        new_slug = slugify(instance.title)
        project.update(
            slug=new_slug
        )
