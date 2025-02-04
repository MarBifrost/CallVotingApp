from django.contrib import admin

from users.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'allowed_ip')
    search_fields = ('username', 'email', 'allowed_ip')
    ordering=('username',)
