from django.urls import path
from .views import updateCount,viewCount, dropCount


urlpatterns = [
    path('updatecount', updateCount),
    path('viewcount', viewCount),
    path('dropcount', dropCount),
]