from django.contrib import admin

from user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active" )
    list_display = ("username", "email", "is_staff")
    #list_filter =  ("is_staff")