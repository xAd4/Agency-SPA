from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! VERY-IMPORTANT: Media Folder Optimization
def custom_upload_to(instance, filename):
    if instance.pk:  # Verifica si la instancia ya tiene una pk
        old_instance = Gallery.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'gallery/' + filename

# Create your models here.
 #* IMPORTANT: MODELS - APPOINTMENTS
class SelectTimeList(models.Model): # Weekdays or Weekends
    days = models.CharField(max_length=100, verbose_name="Weekdays or weekends")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"
        
    def __str__(self):
        return self.days
    
class BudgetList(models.Model): # Client Budget
    budget = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
        
    def __str__(self):
        return self.budget
    

class Appointment(models.Model): # Client Info
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    selectTimeList = models.ForeignKey(SelectTimeList, on_delete=models.CASCADE)
    budget = models.ForeignKey(BudgetList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        
    def __str__(self):
        return f"{self.firstName, self.lastName}"
    
#* IMPORTANT: MODELS - CONTACT
class Contact(models.Model): # Client Info
    titleReview = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    content = models.CharField(max_length=600)
    user_published = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Client contact"
        verbose_name_plural = "Clients contact"
        
    def __str__(self):
        return f"{self.firstName, self.lastName}"
    
#* IMPORTANT: MODELS - GALLERY
class Gallery(models.Model):
    squareFeet = models.CharField(max_length=50)
    garage = models.IntegerField()
    bedrooms = models.IntegerField() 
    pool  = models.BooleanField(choices=[(True, "Yes"), (False, "No")], default=True)
    build = models.CharField(max_length=50)
    image = models.ImageField(upload_to=custom_upload_to)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        
    def __str__(self):
        return self.title
    
#! VERY IMPORANT: Delete deleted instance photo
@receiver(post_delete, sender=Gallery)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)