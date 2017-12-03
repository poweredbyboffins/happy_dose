"""happy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views import static as dv
from happy import views
from happy import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'findout', views.findout, name='findout'),
    url(r'accounts/profile/', views.findout, name='findout'),
    url(r'proc/', views.proc, name='proc'),
    url(r'assess/', views.assess, name='assess'),
    url(r'^simple_chart/$', views.simple_chart, name="simple_chart"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^static/(?P<path>.*)$', dv.serve, {'document_root': settings.STATIC_ROOT})
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'
