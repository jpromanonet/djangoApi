from django.contrib import admin
from django.urls import path

from core.views import Testview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Testview.as_view(), name='test')
]
