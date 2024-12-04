from django.contrib import admin
from .models import Contact, User, Tenant, House_detail, ImageModel, Booking, Agent

# Register your models here.
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Tenant)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(House_detail)
admin.site.register(ImageModel)
