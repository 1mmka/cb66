from django.contrib import admin
from django.urls import path
from app.views import CreateHumanView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CreateHumanView.as_view(),name='create')
]
