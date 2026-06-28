from django.contrib import admin

# Register your models here.
from .models import (
    OrangTua, LihatRiwayatKehadiran, Admin as AppAdmin, Laporan, 
    Jadwal, QRCode, Siswa, MelakukanAbsensi, Guru, 
    KelolaStatusAbsensi, LihatRekapAbsensi
)

admin.site.register(OrangTua)
admin.site.register(LihatRiwayatKehadiran)
admin.site.register(AppAdmin) # Menggunakan alias AppAdmin agar tidak bentrok dengan modul bawaan django admin
admin.site.register(Laporan)
admin.site.register(Jadwal)
admin.site.register(QRCode)
admin.site.register(Siswa)
admin.site.register(MelakukanAbsensi)
admin.site.register(Guru)
admin.site.register(KelolaStatusAbsensi)
admin.site.register(LihatRekapAbsensi)