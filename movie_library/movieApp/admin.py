from django.contrib import admin
from .models import Code


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('codenumber', 'user')
    search_fields = ('user__email',)
