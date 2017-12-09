from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
