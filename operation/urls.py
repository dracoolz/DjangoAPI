from django.urls import re_path 
from operation import views 
 
urlpatterns = [ 
    re_path(r'operation$', views.operation_list),
    re_path(r'operation/(?P<pk>[0-9]+)$', views.operation_detail),
    re_path(r'operation/published$', views.operation_list_published)
]