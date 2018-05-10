"""
10 Mei 2018
Ananda Rauf Maududi
Code Phyton The Best
Calculate Percent
"""
harga_komputer = 15000000
DP = 200000

sisa_cicilan = harga_komputer - DP

bunga = 10 # dalam persen

jumlah_bunga = sisa_cicilan * bunga / 100

total_tagihan = jumlah_bunga + sisa_cicilan

tagihan_bulanan = total_tagihan / 12

print tagihan_bulanan