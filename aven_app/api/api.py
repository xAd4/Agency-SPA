from rest_framework import viewsets
from app.models import Appointment, Contact
from api.serializers import AppointmentSerializers, ContactSerializers

#*IMPORTANT: APPOINTMENT SERIALIZER VIEWSETS
class AppointmentViewSets(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    
#*IMPORTANT: CONTACT SERIALIZER VIEWSETS
class ContactViewSets(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers