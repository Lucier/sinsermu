from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.conf.urls.static import static

from core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^noticia/', include('noticia.urls', namespace='noticia')),
    url(r'^admin/', admin.site.urls),
]


