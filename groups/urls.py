from django.urls import re_path 
from groups import views 
 
urlpatterns = [ 
    re_path(r'groups$', views.group_list),
    re_path(r'groups/(?P<pk>[0-9]+)$', views.group_detail),
    re_path(r'groups/published$', views.group_list_published)
]