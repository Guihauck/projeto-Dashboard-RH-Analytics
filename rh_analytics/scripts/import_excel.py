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

db_path = r'../rh_db/rh.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)

engine = create_engine(f'sqlite:///{db_path}')

df = df.convert_dtypes()  # Ajusta tipos
df = df.applymap(lambda x: str(x) if isinstance(x, pd.Timestamp) else x)

df.to_sql("Funcionários", con=engine, if_exists="replace", index=False)

print("\n✅ Todos os arquivos Excel foram importados e combinados no banco SQLite!")

