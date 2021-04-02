import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    # Django admin
    path('anything-but-admin/', admin.site.urls),

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
    #path('accounts/', include('users.urls')),

    # User management
    #path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/', include('allauth.urls')), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
