# 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

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.Index, name='index')
]
