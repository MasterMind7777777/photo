from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('frontPage.urls', 'frontPage'), namespace='frontPage')),
    path('catalog/', include(('photoCatalog.urls', 'photoCatalog'), namespace='photoCatalog')),
    path('misc/', include(('misc.urls', 'misc'), namespace='misc')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)