from django.urls import re_path, include 
 
urlpatterns = [ 
    re_path(r'^api/', include('users.urls')),
    re_path(r'^api/', include('groups.urls')),
    re_path(r'^api/', include('buses.urls')),
    re_path(r'^api/', include('operation.urls')),
    re_path(r'^api/', include('passenger.urls')),
    re_path(r'^api/', include('family.urls')),
]