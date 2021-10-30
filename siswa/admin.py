from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    forms = UserChangeForm
    model = CustomUser

    list_display = ('pk', 'email', 'username', 'first_name', 'last_name')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'agree')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'agree')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)