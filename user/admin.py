from django.contrib import admin
from .models import Interrogator, Responder


class InterrogatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'photo']


admin.site.register(Interrogator, InterrogatorAdmin)


class ResponderAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'birth_date', 'gender', 'email']


admin.site.register(Responder, ResponderAdmin)
