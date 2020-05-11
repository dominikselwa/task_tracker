from django.urls import path, include

from website.views import home, signup


urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', signup, name='signup')
]