"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include('debug_toolbar.urls')),
    ]

if settings.USE_I18N:
    from django.conf.urls.i18n import i18n_patterns
    from django.utils.translation import gettext_lazy as _
        
    urlpatterns += i18n_patterns(
        path(_("accounts/"), include('allauth.urls')),
        path(_("accounts/"), include('accounts.urls')),
        path(_(""), include('pages.urls')),
        path(_("i18n/"), include('django.conf.urls.i18n')),
    )