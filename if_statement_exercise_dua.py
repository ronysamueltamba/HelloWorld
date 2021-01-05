harga_bakso = 50000
kaya = False
biasa = False

if kaya:
    discount = 0.8 * harga_bakso
elif biasa:
    discount = 0.6 * harga_bakso
else:
    discount = 0.3 * harga_bakso
print(f"Di diskon jadi: Rp.{discount}")
