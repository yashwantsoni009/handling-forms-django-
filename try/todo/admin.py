from django.contrib import admin
from .models import profile

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile,profileAdmin)
# Register your models here.
