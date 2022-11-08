from django.urls import re_path 
from buses import views 
 
urlpatterns = [ 
    re_path(r'buses$', views.buses_list),
    re_path(r'buses/(?P<pk>[0-9]+)$', views.buses_detail),
    re_path(r'buses/published$', views.buses_list_published)
]