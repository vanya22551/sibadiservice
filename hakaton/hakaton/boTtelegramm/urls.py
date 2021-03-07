from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import face_page, sibadi, omgtu, omgu, omgpu,omgups,test

urlpatterns = [
    path('', face_page, name='fasepage'),
    path(r'sibadi', sibadi, name='sibadi'),
    path(r'omgtu', omgtu, name='omgtu'),
    path(r'omgu', omgu, name='omgu'),
    path(r'omgpu', omgpu, name='omgpu'),
    path(r'omgups', omgups, name='omgups'),
    path(r'test', test, name='test'),

    #path(r'add', add, name='add')
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


