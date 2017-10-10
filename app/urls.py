from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from . import views,upload

app_name= 'app'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^category/$', views.category, name='category'),
    url(r'^article/$', views.article, name='article'),
    url(r'^tag/$', views.tag, name='tag'),
    url(r'uploads/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'),
]