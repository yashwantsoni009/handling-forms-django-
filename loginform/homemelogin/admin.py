from django.contrib import admin

# Register your models here.
from .models import formdata

# class profileAdmin(admin.Modeladmin):
# 	class Meta:
# 		model=formdata

admin.site.register(formdata)