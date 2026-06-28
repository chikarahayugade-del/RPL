from django.db import models

# Create your models here.

class OrangTua(models.Model):
    # id_ortu otomatis jadi id (PK)
    nama = models.CharField(max_length=255)
    no_hp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class LihatRiwayatKehadiran(models.Model):
    id_ortu = models.ForeignKey(OrangTua, on_delete=models.CASCADE)
    tanggal = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Riwayat - {self.tanggal}"


class Admin(models.Model):
    # id_admin otomatis jadi id (PK)
    nama = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nama


class Laporan(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    periode = models.CharField(max_length=100)

    def __str__(self):
        return f"Laporan {self.periode}"


class Jadwal(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    hari = models.CharField(max_length=50)
    jam = models.TimeField()

    def __str__(self):
        return f"Jadwal {self.hari}"


class QRCode(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    kode_qr = models.CharField(max_length=255)
    tanggal = models.DateField()

    def __str__(self):
        return f"QR {self.tanggal}"


class Siswa(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    nis = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=255)
    kelas = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class MelakukanAbsensi(models.Model):
    id_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Absen {self.id_siswa.nama} - {self.tanggal}"


class Guru(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    nip = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nama


class KelolaStatusAbsensi(models.Model):
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Status: {self.status}"


class LihatRekapAbsensi(models.Model):
    id_guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    periode = models.CharField(max_length=100)

    def __str__(self):
        return f"Rekap {self.periode}"