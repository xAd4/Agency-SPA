from django.contrib import admin
from .models import SelectTimeList, BudgetList, Appointment, Contact, Gallery

# Register your models here.
# TODO: ReadOnlyFields Option
class ReadOnlyFieldsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

#* IMPORTANT: REGISTER MODELS - APPOINTMENTS
admin.site.register(SelectTimeList, ReadOnlyFieldsAdmin)
admin.site.register(BudgetList, ReadOnlyFieldsAdmin)
admin.site.register(Appointment, ReadOnlyFieldsAdmin)

#* IMPORTANT: REGISTER MODELS - CONTACT
admin.site.register(Contact, ReadOnlyFieldsAdmin)

#* IMPORTANT: REGISTER MODELS - GALLERY
admin.site.register(Gallery, ReadOnlyFieldsAdmin)