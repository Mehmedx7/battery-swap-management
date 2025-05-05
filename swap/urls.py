from django.urls import path
from .views import MQTTPublishView

urlpatterns = [
    path('publish/', MQTTPublishView.as_view()),
]
