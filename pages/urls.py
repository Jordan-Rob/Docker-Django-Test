from django.urls import path
from .views import HomepgView

urlpatterns = [
    path('', HomepgView.as_view(), name='home'),
]
