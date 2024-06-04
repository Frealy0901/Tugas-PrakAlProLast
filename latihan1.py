import re
from datetime import datetime

def tampilkan_tanggal(teks):
    tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', teks)
    for tgl in tanggal:
        tgl_obj = datetime.strptime(tgl, '%Y-%m-%d')
        selisih = (datetime.now() - tgl_obj).days
        print(f'{tgl} 00:00:00 selisih {selisih} hari')

teks = 'Pada tahun 2020-03-01 masa pembelajaran dilaakukan serentak secara daring, seluruh masyarakat akan diliburkan dikarenakan penerapan lockdown selama dua minggu atau sampe pada 2020-04-05, tetapi lockdown terus berlanjut sampai dengan 2021-01-10.'
tampilkan_tanggal(teks)