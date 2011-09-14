from django.contrib import admin
from loggin.models import *

class UI(admin.ModelAdmin):
	pass

admin.site.register(userinfo,UI)