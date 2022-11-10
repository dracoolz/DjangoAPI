from django.urls import re_path 
from passenger import views 
 
urlpatterns = [ 
    re_path(r'passenger$', views.passenger_list),
    re_path(r'passenger/(?P<pk>[0-9]+)$', views.passenger_detail),
    re_path(r'passenger/published$', views.passenger_list_published)
]