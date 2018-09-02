from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'conteudo', 'criada', 'modificada']
    search_fields = ['titulo', 'slug']
    list_filter = ['criada', 'modificada']

admin.site.register(Post, PostAdmin)

