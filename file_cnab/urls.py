from django.urls import path

from . import views

urlpatterns = [
    path('', views.UploadFileCnabView.as_view())
]
