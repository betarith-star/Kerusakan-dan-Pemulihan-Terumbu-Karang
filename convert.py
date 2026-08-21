import pandas as pd

# Baca CSV
df = pd.read_csv('terumbu_karang.csv', sep=';')
df.columns = df.columns.str.strip()

# Simpan otomatis jadi file JSON
df.to_json('data.json', orient='records', force ASCII=False)
print("Berhasil mengubah CSV ke JSON!")