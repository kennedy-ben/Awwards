from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('',views.index,name='Index'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('new/project',views.new_project, name='new-project'),
    path('directory/',views.directory, name='directory'),
    path('profile/',views.profile, name='profile'),
    path('site/(\d+)',views.site,name='site'),
    path('search/',views.search_results, name='search_results'),
    path('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),

    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/categories/', views.categoriesList.as_view()),
    path('api/countries/', views.countriesList.as_view()),
    path('api/technologies/', views.technologiesList.as_view()),
    path('api/colors/', views.colorsList.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)