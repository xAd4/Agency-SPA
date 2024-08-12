from rest_framework import routers
from api.api import AppointmentViewSets, ContactViewSets

router = routers.DefaultRouter()
router.register(r"appointments", AppointmentViewSets, basename="appointments")
router.register(r"contact/reviews", ContactViewSets, basename="contact-review")

urlpatterns = router.urls
