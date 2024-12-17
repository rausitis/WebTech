from django.contrib import admin
from .models import UserInfo, Code

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname', 'phoneNo', 'createdAt')
    search_fields = ('email', 'firstname', 'lastname', 'phoneNo')
    list_filter = ('createdAt',)

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('codenumber', 'user')
    search_fields = ('user__email',)
