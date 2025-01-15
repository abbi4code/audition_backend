from django.urls import path
from auditionApp import views
from django.conf.urls.static import static
from django.conf import settings

# all urls
urlpatterns = [
    path('', views.auditions, name=''),
    path('api/auditionscc244b9737c2b6ef26bd0f7827653c9d27c10b7c',
         views.AuditionPortalViewSet.as_view(), name="AuditionPortal"),
    path('api/designworkshopregistrionscc244b9737c2b6ef26bd0f7827653c9d27c10b7c',
         views.DesignWorkshopViewSet.as_view(), name="DesignWorkshop"),
    path('api/valorantgamingregistrionscc244b9737c2b6ef26bd0f7827653c9d27c10b7c',
         views.ValorantGamingViewSet.as_view(), name="ValorantGaming"),
    path('api/bgmigamingregistrionscc244b9737c2b6ef26bd0f7827653c9d27c10b7c',
         views.BgmiGamingViewSet.as_view(), name="BgmiGaming"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

