from django.apps import AppConfig

from watson import search as watson


class NoticiaConfig(AppConfig):
    name = 'noticia'
    verbose_name = 'Notícia'

    def ready(self):
        Post = self.get_model('Post')
        watson.register(Post)
