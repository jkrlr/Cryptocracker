"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from crypto import views as crypto_views
from django.conf.urls.static import static
from django.conf import settings

app_name='crypto'
import quiz
urlpatterns = [
    path('', crypto_views.base, name='base'),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('signup/', crypto_views.signup, name='signup'),
    path('login/', crypto_views.loginm, name='loginm'),
    path('logout/', crypto_views.logoutm, name='logoutm'),
    path('make_admin/', crypto_views.make_admin, name='make_admin'),
    path('admin-form/', crypto_views.admin_form, name='admin_form'),
    # url(r'^create_contest/',views.create_contest,name='create_contest'),
    # url('(?P<uname>[0-z]+)/', views.index, name='index'),
    re_path(r'^(?P<uname>[0-z]+)/$', crypto_views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
