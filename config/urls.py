from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

from contributors.admin.custom import site


def trigger_error(request):
    """Trigger error for Sentry checking."""
    division_by_zero = 1 / 0  # noqa: F841


urlpatterns = [
    path('admin/', site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript_catalog'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('auth.urls')),
    path('', include('contributors.urls')),
    path('sentry-debug/', trigger_error),
    path('robots.txt', serve, {'path': 'robots.txt'}),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
