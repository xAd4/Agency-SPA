from django.db import models
from django.contrib.auth.models import User

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