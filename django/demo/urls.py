from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from demoapp import views
import os

DYNAMIC_TEMPLATE_NAME = f"split{os.environ.get('CONTAINER_VERSION', 1)}.html"
print(DYNAMIC_TEMPLATE_NAME, os.environ.get('CONTAINER_VERSION'))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('p1/', views.homepage),
    path('p2/', TemplateView.as_view(template_name="p2.html")),
    path('split_test', TemplateView.as_view(template_name=DYNAMIC_TEMPLATE_NAME)),
]
