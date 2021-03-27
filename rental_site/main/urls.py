from . import views
from django.urls import path
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .models import Ad

ads_dict = {
    'queryset': Ad.objects.all(),
    'date_field': 'date_added',
}


urlpatterns = [
    path('', views.Index.as_view()),
    path('apartment/', views.ApartmentList.as_view(), name='apartment_ads'),
    path('room/', views.RoomList.as_view(), name='room_ads'),
    path('garage/', views.GarageList.as_view(), name='garage_ads'),
    path('land_plot/', views.LandPlotList.as_view(), name='land_plot_ads'),
    path('ad/<str:slug>/', views.AdDetail.as_view(), name='ad_detail'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/add/', views.RealtyList.as_view(), name='choice_type'),
    path('accounts/profile/', views.UserUpdate.as_view(), name='edit_user_profile'),
    path('ad/add/apartment/', views.AddApartment.as_view(), name='add_apartment'),
    path('ad/add/room/', views.AddRoom.as_view(), name='add_room'),
    path('ad/add/garage/', views.AddGarage.as_view(), name='add_garage'),
    path('ad/add/land-plot/', views.AddLandPlot.as_view(), name='add_land_plot'),
    path('ad/add/photos/<uuid:pk>/', views.SaveImages.as_view(), name='add_image'),
    path('ad/edit/<uuid:pk>/', views.EditRealtyAd.as_view(), name='edit_ad'),
    path('sitemap.xml', sitemap, {'sitemaps': {'rental_site': GenericSitemap(ads_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", views.robots_txt)
]
