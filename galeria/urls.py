from django.conf.urls import url
from galeria.views import index, imagem

urlpatterns = [
        url('', index, name='index'),
        url('imagem/', imagem, name='imagem'),
]