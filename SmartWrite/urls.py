from django.contrib import admin
from django.urls import include, path
# from formats import views

urlpatterns = [
	path('', include("userprofile.urls")),
	path('userprofile/', include('allauth.urls')),
	# path('send/', include('message.urls', namespace="sendmessage")),
    path('admin/', admin.site.urls),
    # path('auth/', include('django.contrib.auth.urls')),  # Include auth.urls for built-in authentication views
    # path('formats/', views.project_formats_list, name='project_formats_list'),
    
]
