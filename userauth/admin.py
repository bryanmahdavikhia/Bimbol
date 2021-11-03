from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    forms = UserChangeForm
    model = CustomUser

    list_display = ('email', 'username', 'nama_lengkap', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'groups')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'is_staff', 'is_active', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'validasi_guru', 'nomor_telefon', 'payment', 'agree')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'validasi_guru', 'nomor_telefon', 'agree')}),
        ('Permissions', {'fields': ('is_superuser','groups')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
