from django.urls import include, path
from hospitalapp.views import DoctorView,AppointmentView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctors', DoctorView)
router.register(r'appointments', AppointmentView)

urlpatterns = [
    path('', include(router.urls)),
]
