from django.contrib import admin
from .models import Enquiry
from .models import info  

# Register your models here.
admin.site.register(info)


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'feedback')
    search_fields = ('name', 'email', 'number')

# Register your models here.
