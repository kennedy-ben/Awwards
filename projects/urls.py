from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('',views.index,name='Index'),
    url('create/profile',views.create_profile, name='create-profile'),
    url('new/project',views.new_project, name='new-project'),
    url('directory/',views.directory, name='directory'),
    url('profile/',views.profile, name='profile'),
    url('site/(\d+)',views.site,name='site'),
    url('search/',views.search_results, name='search_results'),
    url('user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),

    url('api/profiles/', views.ProfileList.as_view()),
    url('api/projects/', views.ProjectList.as_view()),
    url('api/categories/', views.categoriesList.as_view()),
    url('api/countries/', views.countriesList.as_view()),
    url('api/technologies/', views.technologiesList.as_view()),
    url('api/colors/', views.colorsList.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)