import pandas as pd
from sqlalchemy import create_engine
import glob
import os

data_base = r'C:\Users\Guilherme Hauck\Desktop\Projetos Power BI\Dashboard - RH\rh_analytics\data_rh'

files = glob.glob(os.path.join(data_base, 'rh_*.xlsx'))

print(f' 🔍 {len(data_base)} Arquivos encontrados:')
for f in files:
    print(" -", os.path.basename(f))

df_list = [pd.read_excel(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

print(f"\n Total de registros combinados: {len(df)}")

export_excel = df.to_excel("BaseRH.xlsx", index=False)