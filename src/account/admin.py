from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("avatar", "username", "nickname", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "nickname", "password1", "password2"),
            },
        ),
    )

    list_display = ("username", "nickname", "get_html_avatar",)

    def get_html_avatar(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width='50'>")

    get_html_avatar.short_description = 'Avatar'


admin.site.unregister(Group, )
