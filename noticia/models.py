#coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):

    titulo = models.CharField('Título', max_length=80)
    slug = models.SlugField('Identificador', max_length=100)
    conteudo = models.TextField('Conteúdo')
    criada = models.DateTimeField('Criada em', auto_now_add=True)
    modificada = models.DateTimeField('Modificada em', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('noticia:post', kwargs={'slug': self.slug})
    
        
    
    

