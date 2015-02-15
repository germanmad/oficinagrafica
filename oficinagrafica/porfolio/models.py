# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms

# A simple contact form with four fields.
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField()
    
class Work(models.Model):
    
    CATEGORIAS = (
        ('Sitios Web', 'SW'),
        ('Identidad Corporativa', 'IC'),
        ('Diseño Gráfico', 'DG'),
        ('Ilustración','IL'),
        ('Diseño 3D', 'D3'),
    )
    title = models.CharField(max_length=200)
    imageurl = models.CharField(max_length=200)
    thumburl = models.CharField(max_length=200)
    intro = models.CharField(max_length=400)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=30,
                                      choices=CATEGORIAS,
                                      default='Sitios Web')
    featured = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    