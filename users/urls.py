from django.urls import re_path 
from users import views 
 
urlpatterns = [ 
    re_path(r'users$', views.user_list),
    re_path(r'users/(?P<pk>[0-9]+)$', views.user_detail),
    re_path(r'users/published$', views.user_list_published)
]