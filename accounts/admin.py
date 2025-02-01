from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {
            "fields": (
                ['email','username','password','is_staff']
            ),
        }),
    )
    
        
    
admin.site.register(CustomUser, UserAdmin)