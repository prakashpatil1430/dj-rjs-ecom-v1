from django.contrib import admin
from userauths.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'country', 'state')
    list_editable = ('gender', 'country', 'state')
    search_fields = ('full_name',)
    list_filter = ('date',)
