from django.urls import re_path 
from family import views 
 
urlpatterns = [ 
    re_path(r'family$', views.family_list),
    re_path(r'family/(?P<pk>[0-9]+)$', views.family_detail),
    re_path(r'family/published$', views.family_list_published)
]