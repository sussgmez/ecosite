from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ecolibrary.views import NationalParkListView, NaturalMonumentListView, Home, NationalParkDetailView, NaturalMonumentDetailView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', Home.as_view(), name='home'),
    path('parques_nacionales/', NationalParkListView.as_view(), name='np-list'),
    path('monumentos_naturales/', NaturalMonumentListView.as_view(), name='nm-list'),

    path('parques_nacionales/<int:pk>/', NationalParkDetailView.as_view(), name='np-detail'),
    path('monumentos_naturales/<int:pk>/', NaturalMonumentDetailView.as_view(), name='nm-detail')
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
