from django.contrib import admin
from .models import TwoFAUser


@admin.register(TwoFAUser)
class TwoFAUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_active',
                    'is_staff',
                    'created_at', 'updated_at',)
    search_fields = ('user__email',)
