# Pandas i Matplotlib - Kompletno Uputstvo za Analizu i Vizualizaciju Podataka

## Uvod u Data Science sa Python-om

Python je vodeći jezik za analizu podataka i data science, a Pandas i Matplotlib su fundamentalne biblioteke koje omogućavaju efikasnu manipulaciju podataka i njihovu vizualizaciju. Pandas pruža strukture podataka i alate za analizu, dok Matplotlib omogućava kreiranje grafika i vizualizacija.

### Ključni koncepti
- **Dataset** - strukturisan skup podataka, obično u tabeli
- **DataFrame** - osnovna struktura podataka u Pandas-u (tabela sa imenovanim kolonama)
- **Series** - jedna kolona ili red iz DataFrame-a
- **Axis** - ose podataka (axis=0 za redove, axis=1 za kolone)

---

## PANDAS - Analiza Podataka

### Osnovne import komande

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Postavljanje stilova za crtanje
plt.style.use('classic')
sb.set_theme(palette='Pastel2')
```

---

<!-- Naprednije sekcije biće pomerene niže u dokument da bi osnove išle prve -->

### Magic funkcije u Jupyter Notebook

```python
# Izvršavanje drugog notebook-a
%run "../neki_notebook.ipynb"

# Ovo učitava sve iz te skripte u trenutno okruženje
```

---

## Učitavanje i osnovni pregled podataka

### Učitavanje CSV fajlova

```python
# Osnovno učitavanje
songs = pd.read_csv("putanja_do_csv_fajla.csv")

# Učitavanje sa parsiranjem datuma
songs = pd.read_csv("putanja.csv", parse_dates=['kolona_datuma'])

# Prikaz osnovnih informacija
songs  # Prikazuje tabelu u Jupyter notebook-u
```

### Osnovni pregled Dataset-a

| Metoda | Opis | Primer | Rezultat |
|--------|------|--------|----------|
| `df.shape` | Broj redova i kolona | `songs.shape` | `(1000, 15)` |
| `df.head(n)` | Prvih n redova (default: 5) | `songs.head(10)` | DataFrame sa 10 redova |
| `df.tail(n)` | Poslednjih n redova | `songs.tail(10)` | DataFrame sa 10 redova |
| `df.sample(n)` | n random redova | `songs.sample(10)` | Random 10 redova |
| `df.info()` | Detaljan pregled strukture | `songs.info()` | Non-null count i tipovi |
| `df.describe()` | Deskriptivna statistika | `songs.describe()` | Count, mean, std, kvartili |
| `df.dtypes` | Tipovi podataka po kolonama | `songs.dtypes` | int64, float64, object |

```python
# Dimenzije (broj redova, broj kolona)
songs.shape

# Prvi i poslednji redovi
songs.head(10)      # Prvih 10 redova
songs.tail(10)      # Poslednjih 10 redova
songs.sample(10)    # 10 random redova

# Tipovi podataka
songs.dtypes        # Tipovi svake kolone

# Detaljne informacije
songs.info()        # Non-null count i tipovi podataka

# Deskriptivna statistika (samo numeričke kolone)
songs.describe()    # count, mean, std, min, 25%, 50%, 75%, max
```

### Rad sa kolonama

```python
# Nazivi kolona
songs.columns              # Index objekat
list(songs.columns)        # Lista naziva
songs.columns.tolist()     # Lista naziva (alternativa)
songs.columns.values       # NumPy array naziva

# Pronalaženje pozicije kolone
index_pos = list(songs.columns).index('naziv_kolone')  # npr. 6

# Pristupanje kolonama
songs['track_name']         # Kada naziv ima space ili specijalne karaktere
songs.track_name           # Kada naziv nema space (kratka forma)

# ⚠️ Važno: Za kolone sa spacevima uvek koristiti bracket notaciju
songs['kolona sa razmakom']  # ✅ Bezbedno
songs.kolona_bez_razmaka    # ✅ OK ako nema space

# Vrednosti bez naziva kolona (NumPy array)
songs.values
```

### Menjanje naziva kolona

```python
# Preimenovanje kolona
songs.rename({
    'track_name': 'track', 
    'album_name': 'album'
}, axis='columns', inplace=True)

# inplace=True - menja originalni DataFrame
```

### Promena redosleda kolona

```python
# Pronalaženje indeksa kolone
index_pos = list(songs.columns).index('neka_kolona')  # npr. 6

# Kreiranje novog redosleda
columns = ['track', 'artists', 'album', 'album_type', 'duration', 'release_year']
columns.extend(list(songs.columns)[6:])  # Dodaje ostale kolone

# Primena novog redosleda
songs = songs.reindex(columns=columns)
```

### Čuvanje izmenjenog Dataset-a

```python
# Čuvanje u CSV (preporučuje se često raditi backup)
songs.to_csv('../data/novi_fajl.csv', index=False)
# index=False - ne dodaje kolonu sa indeksom

# Ponovno učitavanje
songs = pd.read_csv('../data/novi_fajl.csv')
```

---

## Rukovanje nedostajućim vrednostima (NaN)

### Otkrivanje nedostajućih vrednosti

```python
# Pregled gde su nedostajuće vrednosti
songs.isna()                    # DataFrame sa True/False
songs.isna().sum()              # Broj nedostajućih po kolonama
songs.isna().sum().sum()        # Ukupan broj nedostajućih

# Vizualizacija nedostajućih vrednosti
sb.heatmap(songs.isna(), cbar=False, cmap='viridis');

# Prebrojavanje po broju nedostajućih
songs.isna().sum().value_counts()

# Kolone sa nedostajućim vrednostima
i = songs.isna().sum() > 0
missing_cols = i[i]             # Samo True vrednosti
missing_cols.index              # Nazivi kolona sa nedostajućim
```

### 🔍 **Boolean Indeksiranje - i[i] Tehnika**

Ovo je jedna od najkorisnijih tehnika u pandas-u koju mnogi ne razumeju na početku:

```python
# VRLO VAŽNA TEHNIKA: Dobijanje samo True vrednosti iz boolean Series
i = songs.isna().sum() > 0  # Boolean Series (True/False)

# i[i] - Genijalan trik za dobijanje samo True vrednosti!
print(i[i])           # Prikazuje samo kolone sa True (imaju nedostajuće podatke)
print(i[i].index)     # Imena kolona koje imaju nedostajuće podatke
print(i[i].values)    # Array samih True vrednosti

# Praktični primeri:
missing_cols = songs.isna().sum() > 0
print("Kolone sa nedostajućim podacima:")
print(missing_cols[missing_cols])  # Samo kolone gde je True

# Ekvivalentno je sa:
print(missing_cols[missing_cols == True])  # Duži način
print(missing_cols.loc[missing_cols])      # Eksplicitniji način
```

**Objašnjenje i[i] logike:**
- `i` je Boolean Series (True/False vrednosti) 
- `i[i]` uzima Series `i` i koristi isti taj `i` kao boolean masku
- Pandas čita ovo kao: "uzmi elemente iz `i` gde je `i` True"
- Rezultat: zadržava samo elemente gde je uslov True
- Ovo je pandas idiom koji značajno skraćuje kod!

**Još primera i[i] tehnike:**
```python
# Primer 1: Kolone sa velikim brojem unique vrednosti
high_cardinality = songs.nunique() > 100
high_card_cols = high_cardinality[high_cardinality]
print("Kolone sa puno unique vrednosti:", high_card_cols.index.tolist())

# Primer 2: Numeričke kolone sa outlierima  
numeric_cols = songs.select_dtypes(include=['number']).columns
outlier_check = {}
for col in numeric_cols:
    q75 = songs[col].quantile(0.75)
    q25 = songs[col].quantile(0.25)
    iqr = q75 - q25
    outliers_exist = ((songs[col] < (q25 - 1.5 * iqr)) | 
                     (songs[col] > (q75 + 1.5 * iqr))).any()
    outlier_check[col] = outliers_exist

outlier_series = pd.Series(outlier_check)
cols_with_outliers = outlier_series[outlier_series]  # i[i] tehnika!

# Primer 3: Kolone sa malim brojem unique vrednosti (kategoričke kandidati)
low_cardinality = songs.nunique() < 10
categorical_candidates = low_cardinality[low_cardinality]
print("Kolone koje mogu biti kategoričke:", categorical_candidates.index.tolist())
```

**Zašto je i[i] bolji od alternativa:**
```python
# ❌ Duži način
missing_cols = songs.isna().sum() > 0
result = missing_cols[missing_cols == True]

# ❌ Još duži način  
missing_cols = songs.isna().sum() > 0
true_indices = missing_cols[missing_cols == True].index
result = missing_cols[true_indices]

# ✅ Pandas idiom - kratak i elegantan
missing_cols = songs.isna().sum() > 0
result = missing_cols[missing_cols]  # i[i] tehnika
```

### Rad sa nedostajućim vrednostima

```python
# Prikaz redova sa nedostajućim vrednostima
songs.loc[songs.isna().any(axis=1), :]

# Prikaz redova bez nedostajućih vrednosti  
songs.loc[songs.notna().all(axis=1)]

# Kolone sa nedostajućim vrednostima
songs.loc[:, i]  # gde je i boolean maska

# Uklanjanje redova sa nedostajućim vrednostima
songs.dropna()                  # Uklanja sve redove sa bilo kojim NaN
songs.dropna(axis=1)           # Uklanja kolone sa bilo kojim NaN
songs['producers'].dropna()     # Samo za jednu kolonu

# Popunjavanje nedostajućih vrednosti
songs.loc[mask, 'track_composers'] = 'unknown'
```

---

## Duplikati

### Otkrivanje i uklanjanje duplikata

```python
# Otkrivanje duplikata
songs.duplicated()              # Boolean Series
songs.duplicated('track')       # Po određenoj koloni
songs.track.duplicated().sum()  # Broj duplikata

# Pronalaženje duplikata
songs.loc[songs.track.duplicated()]
songs.loc[songs.track == 'Better Man']  # Svi redovi sa istim nazivom

# Uklanjanje duplikata
songs.drop_duplicates('track')                    # Čuva prvi
songs.drop_duplicates('track', keep='last')       # Čuva poslednji
songs.drop_duplicates('track', keep=False)        # Uklanja sve duplikate

# Resetovanje indeksa nakon brisanja
songs.reset_index(drop=True, inplace=True)
```

---

## Indeksi i selekcija podataka

### Osnovni pristup indeksima

```python
# Pristup indeksima
songs.index
songs.index.tolist()

# Selekcija slično SQL SELECT
# SELECT ... FROM songs WHERE uslov
songs.loc[uslov]
```

### LOC - Label-based selection

```python
# Osnovna selekcija - sintaksa: df.loc[red_uslov, kolona_uslov]
songs.loc[songs.artists == 'Alice in Chains']

# Više uslova (koristiti & umesto and, | umesto or)
songs.loc[(songs.artists == 'Alice in Chains') & (songs.album_type == 'studio')]

# ⚠️ VAŽNO: Ne koristiti 'and'/'or' u pandas uslovima!
# songs.loc[(uslov1) and (uslov2)]  # ❌ POGREŠNO
# songs.loc[(uslov1) & (uslov2)]    # ✅ ISPRAVNO

# Selekcija određenih kolona
songs.loc[songs.release_year < 1995, ['track', 'artists', 'release_year']]

# Selekcija sa isin (IN u SQL-u)
early_years = list(range(1989, 1995))
songs.loc[songs.release_year.isin(early_years)]

# String operacije (dodati .str)
songs.loc[songs.track.str.startswith('Love')]
songs.loc[songs.track.str.contains('rock', case=False)]
songs.loc[songs.track.str.len() > 20]
```

### ILOC - Position-based selection

```python
# Selekcija po poziciji
songs.iloc[:10, :5]           # Prvih 10 redova, prvih 5 kolona
songs.iloc[-5:, [0,1,4]]      # Poslednjih 5 redova, kolone 0,1,4
songs.iloc[100:200, 2:8]      # Redovi 100-199, kolone 2-7

# Kombinovanje sa boolean indeksiranjem
nan_rows = songs.track_composers.isna()
nan_indices = nan_rows[nan_rows].index
songs.iloc[nan_indices, [0,1,2]]  # Mora koristiti pozicije kolona
```

---

## Grupa operacije (GroupBy)

### Osnovne grupne operacije

```python
# Unique vrednosti
songs.release_year.unique()     # Jedinstvene vrednosti
songs.release_year.nunique()    # Broj jedinstvenih vrednosti

# Value counts
songs.release_year.value_counts()                           # Brojanje pojavljivanja
songs.release_year.value_counts(normalize=True)             # U procentima
songs.release_year.value_counts().sort_index()              # Sortiranje po indeksu
songs.release_year.value_counts().sort_values()             # Sortiranje po vrednostima
```

### GroupBy operacije

```python
# Kreiranje grupnog objekta
songs_by_year = songs.groupby('release_year')  # DataFrameGroupBy objekat

# Pristup određenoj grupi
songs_by_year.get_group(1989)  # Svi redovi za 1989. godinu

# Grupne agregacije
songs.groupby('release_year').duration.mean()                    # Prosečno trajanje po godini
songs.groupby('release_year').duration.count()                   # Broj pesama po godini
songs.groupby('release_year').size()                             # Isto kao count ali kraće

# Više agregacija odjednom
songs.groupby('release_year').duration.agg(['count', 'mean', 'max'])

# Sortiranje rezultata
songs.groupby('release_year').duration.mean().sort_values(ascending=False)
songs.groupby('release_year').duration.agg(['count', 'mean']).sort_values(by='count', ascending=False)

# Grupiranje po više kolona
sales_per_city_product = sales.groupby(['Product', 'Purchase_City']).Total_Revenue.sum()
# Ovo vraća Series sa MultiIndex

# Pretvaranje MultiIndex u DataFrame
sales_per_city_product.unstack()  # Kolone postaju druga dimenzija grupiranja
```

---

## Sortiranje podataka

### Sortiranje Series

```python
# Sortiranje po indeksu
songs.release_year.value_counts().sort_index(ascending=False)

# Sortiranje po vrednostima
songs.release_year.value_counts().sort_values(ascending=False)
```

### Sortiranje DataFrame

```python
# Sortiranje po jednoj koloni
songs.sort_values('release_year')
songs.sort_values('duration', ascending=False)

# Sortiranje po više kolona
songs.sort_values(['release_year', 'duration'], ascending=[True, False])
```

---

## Dodavanje i transformacija kolona

### Kreiranje novih kolona

```python
# Dodavanje nove kolone (mora koristiti [] notaciju)
sales['Total_Revenue'] = sales.Quantity_Ordered * sales.Price_Each

# ⚠️ VAŽNO: Za kreiranje novih kolona UVEK koristiti bracket notaciju
# sales.Total_Revenue = ...  # ❌ POGREŠNO za nove kolone
# sales['Total_Revenue'] = ... # ✅ ISPRAVNO

# Dodavanje na osnovu uslova
songs['era'] = songs.release_year.apply(lambda x: '90s' if x < 2000 else '2000s')

# Apply funkcija sa custom funkcijom
def categorize_duration(duration):
    if duration < 180000:
        return 'short'
    elif duration < 240000:
        return 'medium'
    else:
        return 'long'

songs['duration_category'] = songs['duration'].apply(categorize_duration)

# Lambda funkcije za brže transformacije
songs['squared_duration'] = songs['duration'].apply(lambda x: x**2)
```

### Pretvaranje tipova podataka

```python
# Konverzija u numeričke tipove
try:
    lista['kolona'] = pd.to_numeric(lista['kolona'], errors="coerce")
except ValueError as err:
    print(err)
# errors="coerce" - postavlja NaN za vrednosti koje ne mogu da se konvertuju

# Konverzija u datetime
sales['Order_Date'] = pd.to_datetime(
    sales['Order_Date'], 
    errors='coerce',
    format='%m/%d/%y %H:%M'
)

# Pristup komponentama datetime objekta
sales['Month'] = sales.Order_Date.dt.month
sales['Year'] = sales.Order_Date.dt.year
sales['DayOfWeek'] = sales.Order_Date.dt.dayofweek
```

---

## Napredne operacije

### Brisanje kolona i redova

```python
# Brisanje kolona
sales.drop(columns=['kolona1', 'kolona2'], inplace=True)

# Brisanje redova po indeksu
sales.drop(index=[0, 1, 2], inplace=True)

# Dropna sa dodatnim parametrima
sales.dropna(
    how="any",           # "any" - briše ako ima bilo koji NaN, "all" - samo ako su svi NaN
    inplace=True, 
    subset=["Price_Each", "Quantity_Ordered"]  # Samo provera određenih kolona
)

# ⚠️ Objašnjenje how parametra:
# how="any" - briše red ako bilo koja vrednost u redu je NaN
# how="all" - briše red samo ako su SVE vrednosti u redu NaN
```

### Rad sa direktorijumima i više CSV fajlova

```python
from pathlib import Path

def get_csv_files(fpath: Path) -> list:
    """Pronalazi sve CSV fajlove u direktorijumu"""
    if not fpath.is_dir():
        raise RuntimeError("Input argument is not a directory")
    
    csv_files = []
    for item in fpath.iterdir():
        if not item.is_dir() and item.suffix == '.csv':
            csv_files.append(item)
    return csv_files

# Spajanje više CSV fajlova
DATA_DIR = Path('data')
all_sales = pd.DataFrame()

for csv_file in get_csv_files(DATA_DIR):
    temp_df = pd.read_csv(csv_file)
    all_sales = pd.concat([all_sales, temp_df])

# Resetovanje indeksa nakon spajanja
all_sales.reset_index(drop=True, inplace=True)

# Kreiranje kopije (važno!)
sales = all_sales.copy()  # Ne: sales = all_sales (samo referenca)
```

### Kreiranje direktorijuma

```python
from pathlib import Path

# Kreiranje direktorijuma
processed_data_dir = Path('processed_data')
processed_data_dir.mkdir(parents=True, exist_ok=True)

# parents=True - kreira i parent direktorijume ako ne postoje
# exist_ok=True - ne baca grešku ako direktorijum već postoji

# Primer hijerarhije direktorijuma
project_dir = Path('my_project')
data_dir = project_dir / 'data' / 'processed'
results_dir = project_dir / 'results' / 'plots'

# Kreiranje cele hijerarhije odjednom
data_dir.mkdir(parents=True, exist_ok=True)
results_dir.mkdir(parents=True, exist_ok=True)
```

### Konverzija između Series i DataFrame

```python
# Series u DataFrame
sales_per_city_df = sales_per_city.to_frame()
sales_per_city_df.reset_index(inplace=True)  # Ako treba indeks kao kolona

# Naprednije - kreiranje DataFrame iz Series sa custom nazivom kolone
sales_df = sales_per_city.to_frame(name='total_sales')

# MultiIndex Series u DataFrame sa unstack
multi_grouped = df.groupby(['kolona1', 'kolona2']).vrednost.sum()
pivot_df = multi_grouped.unstack()  # Prvi indeks → redovi, drugi → kolone
```

### Faktorizacija za vizualizaciju

```python
# Kreiranje numeričkih labela za kategorije
numeric_labels, unique_categories = pd.factorize(df['kategorija'])

# Korisno za colormap-e u matplotlib/seaborn
import matplotlib.pyplot as plt
colors = plt.cm.viridis(numeric_labels / len(unique_categories))

# Primer korišćenja u scatter plot-u
plt.scatter(df['x'], df['y'], c=colors)
```

---

## (Naprednije) Kombinovanje i integracija podataka
### Merge / Join / Concat
```python
pd.merge(df_left, df_right, on='id', how='inner')
pd.merge(df_left, df_right, on='id', how='left')
pd.merge(df_left, df_right, left_on='id1', right_on='id2', how='outer')

df_left.join(df_right, how='inner')
df_left.join(df_right.set_index('id'), on='id')

pd.concat([df1, df2], axis=0, ignore_index=True)  # vertikalno
pd.concat([df1, df2], axis=1)                     # horizontalno
```
Kratko:
- merge: ključevi (najčešći slučaj)
- join: indeks vs kolona
- concat: slaganje (redovi) ili kombinovanje (kolone)

## (Naprednije) Preoblikovanje strukture (reshaping)
### pivot / pivot_table / melt
```python
df.pivot(index='country', columns='year', values='gdp')            # striktno
df.pivot_table(index='country', columns='year', values='gdp', aggfunc='sum', fill_value=0)
df.melt(id_vars=['country'], var_name='year', value_name='gdp')    # unpivot
```
### Crosstab
```python
pd.crosstab(df['segment'], df['outcome'], normalize='index')
```
### Explode (list -> redovi)
```python
df_expl = df.explode('tags')
```
### Napredni value_counts
```python
df['country'].value_counts(normalize=True)
df[['col1','col2']].value_counts(dropna=False)
```

## (Naprednije) Optimizacija i tipovi
### Kategorije (category dtype)
```python
df['city'] = df['city'].astype('category')
df['city'].cat.reorder_categories([...], ordered=True)
```

## (Naprednije) Analitičke tehnike
### Korelaciona matrica
```python
corr = df.select_dtypes(include='number').corr()
sb.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
```
### Rolling / EWM
```python
df['ma7'] = df['sales'].rolling(7, min_periods=1).mean()
df['ewm14'] = df['sales'].ewm(span=14, adjust=False).mean()
```
### Resample i datum slice
```python
df.index = pd.to_datetime(df['date'])
monthly = df['sales'].resample('M').sum()
df.loc['2024-05']
```
### Detekcija outlier-a (IQR)
```python
Q1, Q3 = df['val'].quantile([0.25, 0.75])
IQR = Q3 - Q1
mask = (df['val'] < Q1 - 1.5*IQR) | (df['val'] > Q3 + 1.5*IQR)
outliers = df[mask]
```
### Kardinalnost i memorija
```python
high_card = df.nunique().sort_values().tail(10)
mem_mb = (df.memory_usage(deep=True)/1024**2).sort_values()
```
### Stilizacija (prikaz)
```python
df.style.format({'price': '{:,.2f}', 'rate': '{:.2%}'}).background_gradient(cmap='Greens')
```

---

## MATPLOTLIB - Vizualizacija Podataka

Matplotlib je osnovna biblioteka za kreiranje grafika u Python-u. Svaki grafik se sastoji od **Figure** (platno) i **Axes** (koordinatni sistem sa podacima).

### Osnovni koncepti

- **Figure** - celo platno na kome se crta, može imati više grafika
- **Axes** - jedan grafik na Figure-u, ima x i y ose
- **Axis** - pojedinačne ose (x ili y) sa labelima i tick marks

### Priprema podataka za vizualizaciju

```python
# Prvo očistiti dataset od NaN vrednosti
songs.isna().sum().sum()  # Proveriti da li ima NaN

# Ako ima, izbaciti ili popuniti
songs_clean = songs.dropna()
songs_clean.to_csv('../data/clean_dataset.csv', index=False)

# Proveriti tipove podataka
type(songs.iloc[0, 4])  # Proveriti tip određene vrednosti

# Ako je string umesto int, konvertovati
songs['duration'] = pd.to_numeric(songs['duration'], errors='coerce')
```

### 🎯 **Objašnjenje matplotlib osnova**

#### Figure vs Axes - ključni koncepti
```python
# OBJAŠNJENJE: Figure je kao platno, Axes je grafik na tom platnu
fig = plt.figure(figsize=(10, 7))  # Figure = platno pozadi

# Kreiranje axes objekata (grafikona)
ax = plt.axes()  # Jedan grafik na celom Figure

# Preporučeno: plt.subplots() jer vraća i Figure i Axes
fig, ax = plt.subplots()  # Bolje jer daje kontrolu nad oba
```

#### Iz vizualizacije možemo otkriti greške
```python
# IZ VIZUALIZACIJE MOŽEMO DA VIDIMO DA LI IMAMO GREŠKE:
# - Outliere (tačke koje stoje odvojeno od ostatka)
# - Nelogične vrednosti (negativne godine, prevelike cene)
# - Pattern-e koji ukazuju na probleme u podacima

# Primer: scatter plot za pronalaženje outliera
ax.scatter(songs['duration'], songs['danceability'])
# Ako vidiš tačku daleko od ostalih, istražiti tu pesmu!
```

---

## Scatter Plot (Rasejani dijagram)

```python
import matplotlib.pyplot as plt

# Dobijanje opsega za ose iz podataka
range_info = songs.describe().loc[['min','max'], ['duration', 'danceability']]

# Kreiranje figure i axes
ax = plt.axes()

# Postavljanje parametara
ax.set(
    xlim=(range_info.loc['min', 'duration'], range_info.loc['max', 'duration']), 
    ylim=(0, 1), 
    xlabel='Duration (ms)', 
    ylabel='Danceability', 
    title='Duration vs Danceability'
)

# Alternativno, može i pojedinačno
ax.set_title('Duration vs Danceability', fontsize=12, loc='left')
ax.set_facecolor('lightgray')
ax.set_xlabel('Duration', fontsize=8)
ax.set_ylabel('Danceability', fontsize=8)
ax.set_xlim(0, 400000)
ax.set_ylim(0, 1)

# Kreiranje scatter plot-a
ax.scatter(
    songs['duration'], 
    songs['danceability'], 
    marker='o',           # Tip markera: 'o', 's', '^', 'D', itd.
    c='blue',            # Boja popune
    edgecolors='red',    # Boja ivice
    s=50,                # Veličina markera
    alpha=0.7            # Transparentnost (0-1)
)

# Formatiranje tickova (važno za velike brojeve)
ax.ticklabel_format(useOffset=False)  # Sprečava eksponencijalnu notaciju

# Veličina tick labela
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)

plt.show()
```

### Subplots - više grafika

```python
# Kreiranje figure sa više axes
fig, ax = plt.subplots(
    nrows=1, ncols=2, 
    layout='constrained',    # Automatski razmesiti elemente
    facecolor='white', 
    figsize=(12, 6)         # Širina, visina u inčima
)

# ax je sada array ako imamo više subplotova
ax[0].scatter(songs['duration'], songs['danceability'])
ax[1].scatter(songs['energy'], songs['valence'])
```

---

## Line Plot (Linijski dijagram)

```python
# VAŽNO: Podaci na x-osi moraju biti sortirani!
release_counts = songs.release_year.value_counts().sort_index()
release_year = release_counts.index
counts = release_counts.values

# Kreiranje line plot-a
ax = plt.axes()
ax.set(
    xlim=(1989, 2020), 
    ylim=(0, 40), 
    xlabel='Release Year', 
    ylabel='Number of Songs', 
    title='Songs Released Over Time'
)

ax.ticklabel_format(useOffset=False)

ax.plot(
    release_year, counts, 
    color='steelblue',    # Boja linije
    marker='*',           # Marker na tačkama
    linewidth=1.5,        # Debljina linije
    alpha=0.8             # Transparentnost
)

# Dodavanje grid-a
ax.grid(visible=True, which='major', axis='both', color='lightgrey')

plt.show()
```

### Više linija na istom grafikonu

```python
# Korišćenje twinx() za dve y-ose
fig, ax1 = plt.subplots(figsize=(8,7))

# Prva linija (leva y-osa)
col_revenue = "orchid"
ax1.plot(x, revenue_data, color=col_revenue, marker="d")
ax1.tick_params(axis='y', labelcolor=col_revenue)
ax1.set_ylabel("Revenue (million USD)", color=col_revenue)

# Druga linija (desna y-osa)
col_quantity = "teal"
ax2 = ax1.twinx()  # Kreira novi axes sa zajedničkom x-osom
ax2.plot(x, quantity_data, color=col_quantity, marker="^")
ax2.tick_params(axis='y', labelcolor=col_quantity)
ax2.set_ylabel("Quantity Ordered", color=col_quantity)

# Zajedničke postavke
ax1.tick_params(axis='x', labelrotation=90, labelsize=9)
ax1.grid(visible=True, axis='x', color='slategray', alpha=0.5)

fig.tight_layout()
plt.show()
```

### Više axes na jednoj figuri

```python
# Manuelno pozicioniranje axes
fig = plt.figure(figsize=(10, 7))

# add_axes([left, bottom, width, height]) - sve u odnosu na figuru (0-1)
ax1 = fig.add_axes([0.1, 0.579, 0.8, 0.35],
                    xlim=(1989, 2020), ylim=(0, 40),
                    xlabel='Release Year', ylabel='Count',
                    title='Upper plot')

ax2 = fig.add_axes([0.1, 0.08, 0.8, 0.35],
                    xlim=(1989, 2020), ylim=(0, 40),
                    xlabel='Release Year', ylabel='Count',
                    title='Lower plot')

ax1.plot(release_year, counts, color='steelblue', linewidth=1.5)
ax2.plot(release_year, counts, color='purple', linewidth=1.5)
```

---

## Histogram

```python
# Osnovni histogram
plt.hist(songs.duration, bins=40)

# Sa Seaborn (preporučeno)
sb.histplot(songs.duration, bins=40)

# Napredni histogram sa customizacijom
fig, ax = plt.subplots(nrows=1, ncols=1, layout='constrained', 
                       facecolor='white', figsize=(8, 6))

plt.hist(
    songs.duration, 
    bins=40,              # Broj binova
    color='teal',         # Boja popune
    edgecolor='red',      # Boja ivica
    linewidth=2,          # Debljina ivica
    alpha=0.7             # Transparentnost
)

ax.set_title('Distribution of Song Duration', fontsize=12, loc='left')
ax.set_facecolor('whitesmoke')
ax.set_xlabel('Duration (ms)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.ticklabel_format(useOffset=False)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

plt.show()
```

---

## Bar Plot

### Osnovni bar plot

```python
# Priprema podataka
df = pd.DataFrame({
    'categories': ['A', 'B', 'C', 'D'], 
    'values': [23, 45, 56, 78]
})

# Kreiranje bar plot-a
ax = df.plot.bar(
    x='categories', 
    y='values',
    figsize=(8, 6),
    rot=45,                    # Rotacija x-labela
    ylim=(0, 100),
    color='limegreen',
    edgecolor='black',
    title='Sample Bar Chart',
    xlabel='Categories',
    ylabel='Values',
    fontsize=12
)

# Dodavanje vrednosti na vrh stubova
for container in ax.containers:
    ax.bar_label(container, label_type='center')

plt.show()
```

### Horizontalni bar plot

```python
fig, ax = plt.subplots(figsize=(8, 6))

# Sortiranje podataka
sales_per_product = sales.groupby('Product').Total_Revenue.sum().sort_values()
products = sales_per_product.index.tolist()
revenue = sales_per_product.values.tolist()

ax.barh(products, revenue)  # barh za horizontalni
ax.set_title('Revenue by Product')
ax.set_xlabel('Total Revenue ($)')

plt.show()
```

### Više bar grafika sa subplotovima

```python
# Sortiranje podataka
sales_per_product.sort_values(by='Total_Revenue', inplace=True)
products = sales_per_product.index.tolist()
sold_quantity = sales_per_product.Quantity_Ordered.tolist()
total_revenue = sales_per_product.Total_Revenue.tolist()

# Kreiranje subplotova
fig, (ax_revenue, ax_quantity) = plt.subplots(
    nrows=1, ncols=2, 
    figsize=(14, 8), 
    sharey='row'  # Deli y-osu između grafika
)

ax_revenue.barh(products, total_revenue)
ax_revenue.set_title('Total Product Revenue')
ax_revenue.set_xlabel('Revenue ($)')

ax_quantity.barh(products, sold_quantity)  
ax_quantity.set_title('Total Quantity Ordered')
ax_quantity.set_xlabel('Quantity')

plt.tight_layout()
plt.show()
```

### Grid od više grafika

```python
# Kreiranje 2x4 grid-a grafika
fig, ax_grid = plt.subplots(nrows=2, ncols=4, figsize=(14, 9), sharey="all")

states = ['CA', 'NY', 'TX', 'WA', 'MA', 'OR', 'GA', 'IL']
row_index = col_index = 0

for i, state in enumerate(states):
    # Podaci za trenutnu državu
    y_data = state_sales_dict[state].values.tolist()
    x_data = range(1, 13)  # Meseci
    
    # Crtanje
    ax_grid[row_index, col_index].bar(x_data, y_data, color=f'C{i}')
    ax_grid[row_index, col_index].set_xticks(range(1, 13))
    ax_grid[row_index, col_index].set_title(state)
    ax_grid[row_index, col_index].grid(visible=True, axis='y', alpha=0.35)
    
    # Prelazak na sledeću poziciju
    col_index += 1
    if col_index == 4:
        col_index = 0
        row_index = 1

fig.suptitle("Monthly Sales by State", fontsize=16)
plt.show()
```

---

## Box Plot i Violin Plot

### Box Plot sa Seaborn

```python
# Osnovni box plot
sb.boxplot(y=songs.duration, palette='deep', legend=False)

# Više kolona odjednom
sb.boxplot(
    data=songs[['acousticness', 'energy']], 
    orient='v',        # 'v' za vertikalni, 'h' za horizontalni
    palette='Set3'
)

# Box plot sa grupiranjem
sb.boxplot(
    data=songs, 
    x='album_type', 
    y='duration', 
    palette='viridis'
)

plt.xticks(rotation=45)
plt.show()
```

### Violin Plot

```python
# Violin plot pokazuje distribuciju podataka
x_data = songs.loc[songs.release_year < 1995, 'release_year']
y_data = songs.duration

sb.violinplot(
    data=songs, 
    x=x_data, 
    y=y_data, 
    hue=x_data,        # Bojenje po grupama
    palette='Set1', 
    legend=False
)

plt.xticks(rotation=45)
plt.show()
```

---

## Heatmap

### Kreiranje kategorija za heatmap

```python
# qcut - podela na grupe sa jednakim brojem članova
songs['valence_category'] = pd.qcut(
    songs.valence, 
    q=5, 
    labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']
)

# Pristupanje kreiranim kategorijama
print(songs.valence_category.cat.categories)  # Vraća kreiranje kategorije

# cut - podela na grupe sa unapred definisanim granicama  
_, v_min, v_q1, v_median, v_q3, v_max = songs.describe()['valence'].values
bin_edges = [v_min, v_q1, v_median, v_q3, v_max]  # 5 granica za 4 kategorije
labels = ['Very Low', 'Low', 'Medium', 'High']

songs['valence_category'] = pd.cut(
    songs.valence, 
    bins=bin_edges, 
    labels=labels, 
    include_lowest=True  # Uključuje najnižu vrednost u prvi bin
)

# Promena redosleda kategorija (za logičniji prikaz u heatmap-u)
songs['valence_category'] = pd.Categorical(
    songs.valence_category, 
    categories=['Very High', 'High', 'Medium', 'Low', 'Very Low'], 
    ordered=True
)
```

**⚠️ Objašnjenje qcut vs cut:**
- **qcut**: Svaka kategorija ima približno isti broj elemenata (kvantili)
- **cut**: Kategorije imaju iste granice, ali različit broj elemenata
- **include_lowest=True**: Prvi bin uključuje i najnižu vrednost (inače bi bila isključena)
- **Ako imamo 4 kategorije, treba 5 granica (bin_edges)**

### Kreiranje pivot tabele

```python
# Pivot tabela - osnova za heatmap
pt = songs.pivot_table(
    values='acousticness',      # Vrednosti u ćelijama  
    index='valence_category',   # Redovi
    columns='release_year'      # Kolone
)

# Ćelije predstavljaju srednju vrednost acousticness-a 
# za kombinaciju valence_category i release_year
```

### Crtanje heatmap-a

```python
# Sa Seaborn (preporučeno)
plt.figure(layout='constrained', facecolor='white', figsize=(15, 5))
sb.heatmap(
    data=pt, 
    annot=True,           # Prikaži vrednosti u ćelijama
    fmt='.2f',            # Format brojeva (2 decimale) - kao %.2f za stringove
    cmap='viridis',       # Mapa boja
    cbar_kws={'label': 'Acousticness'}  # Label za color bar
)

plt.title('Acousticness by Valence and Year', loc='left', color='teal', size=16)
plt.xlabel('Release Year')
plt.ylabel('Valence Category')
plt.show()

# ⚠️ Objašnjenje parametara:
# annot=True - prikazuje vrednosti u ćelijama heatmap-a
# fmt - format string za brojeve (isto kao % formatting)
# Ćelije u heatmap-i predstavljaju srednju vrednost (default aggregation)
```

### Heatmap sa Matplotlib (napredni)

```python
# Priprema podataka
products = df.index.tolist()
cities = df.columns.tolist()

fig, ax = plt.subplots(figsize=(10, 8))

# Kreiranje heatmap-a
hm = ax.imshow(df, cmap='PuRd_r')  # imshow za matricu

# Postavljanje tick-ova i labela
ax.set_xticks(range(len(cities)), labels=cities)
ax.set_yticks(range(len(products)), labels=products)

# Rotacija labela
ax.tick_params(axis='x', labelrotation=90, labelsize=9)
ax.tick_params(axis='y', labelsize=9)

# Dodavanje color bar-a
cbar = ax.figure.colorbar(hm, ax=ax)
cbar.ax.set_ylabel("Total Revenue (USD)", rotation=-90, va="bottom")

plt.title('Revenue Heatmap')
plt.show()
```

---

## Specijalizovani plotovi

### Treemap Plot

```python
import squarify

# Priprema podataka  
sales_per_city_df = sales_per_city.to_frame()
sales_per_city_df.reset_index(inplace=True)

# Osnovna treemap
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_axis_off()  # Uklanja ose

squarify.plot(
    sizes=sales_per_city_df.Quantity_Ordered,
    label=sales_per_city_df.City,
    ax=ax
)
plt.show()

# Treemap sa bojama po državama (faktorizacija)
state_labels, unique_states = pd.factorize(sales_per_city_df.State)
colors = [plt.cm.Set3(i) for i in state_labels]

squarify.plot(
    sizes=sales_per_city_df.Quantity_Ordered,
    label=sales_per_city_df.City,
    color=colors,
    text_kwargs={'color': 'white', 'fontsize': 10},
    pad=True,           # Razmak između blokova
    ax=ax
)
```

---

## Najbolje prakse i korisni saveti

### 📋 Pandas Najbolje Prakse

#### ✅ Preporučuje se (Do's)
```python
# 1. Uvek pravi kopije pre većih transformacija
df_backup = df.copy()

# 2. Koristi eksplicitno dodeljivanje umesto inplace (lakše debugging)
df = df.dropna()  # Umesto df.dropna(inplace=True)

# 3. Koristi errors='coerce' pri konverziji tipova
df['numeric_col'] = pd.to_numeric(df['string_col'], errors='coerce')

# 4. Reset indeksa nakon filtriranja/brisanja
df = df.reset_index(drop=True)

# 5. Čuvaj intermediate rezultate tokom analize
df.to_csv('backup_step_1.csv', index=False)

# 6. Koristi bracket notaciju za kolone sa spacevima
df['kolona sa space']  # ✅ Uvek radi

# 7. Koristi vektorizovane operacije umesto petlji
df['new_col'] = df['col1'] * df['col2']  # ✅ Brzo
# for i in range(len(df)): df.iloc[i, new_col] = ...  # ❌ Sporo
```

#### ❌ Izbegavaj (Don'ts)
```python
# 1. Ne koristi and/or u pandas uslovima
# df.loc[(cond1) and (cond2)]  # ❌ GREŠKA
df.loc[(cond1) & (cond2)]      # ✅ ISPRAVNO

# 2. Ne koristi iterrows() - sporo je
# for idx, row in df.iterrows():  # ❌ Sporo
#     row['col1'] * row['col2']
df['result'] = df['col1'] * df['col2']  # ✅ Brzo

# 3. Ne zanemaruj nedostajuće podatke
# df.mean()  # ❌ Može dati pogrešan rezultat
df.dropna().mean()  # ✅ Ili eksplicitno rukovanje

# 4. Ne pravi samo reference umesto kopija
# new_df = original_df  # ❌ Samo referenca
new_df = original_df.copy()  # ✅ Prava kopija

# 5. Ne koristi dot notaciju za nove kolone
# df.new_column = values  # ❌ Može ne raditi
df['new_column'] = values   # ✅ Uvek radi
```

### 🛠️ Debugging saveti

```python
# Brza provera strukture podataka
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Missing values: {df.isna().sum().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")

# Provera tipova podataka
df.dtypes

# Sample podataka za inspekciju
df.sample(5)

# Info o memorijskoj potrošnji
df.info(memory_usage='deep')
```

### 1. Priprema podataka
```python
# Uvek prvo očisti podatke
df = df.dropna()  # ili popuni nedostajuće vrednosti
df = df.drop_duplicates()

# Proveri tipove podataka
df.dtypes
df.info()
```

### 2. Dobijanje uvida iz vizualizacije
```python
# Koristi describe() za opsege osa
range_data = df.describe().loc[['min', 'max'], ['x_col', 'y_col']]

# Pretraži outlier-e u scatter plot-u
# Ako vidiš tačke koje se izdvajaju, istrži šta one predstavljaju
```

### 3. Formatiranje i stilizovanje
```python
# Koristi plt.subplots() umesto plt.axes() (preporučeno)
fig, ax = plt.subplots(figsize=(10, 6))

# Uvek postavi useOffset=False za čiste tick labele
ax.ticklabel_format(useOffset=False)

# Koristi grid za lakše čitanje
ax.grid(visible=True, alpha=0.3)

# Rotiraj labele ako su dugački
ax.tick_params(axis='x', labelrotation=45)
```

### 4. Pronalaženje ekstremnih vrednosti
```python
# Najveća vrednost u Series
sales_per_city.idxmax()  # Vraća indeks sa najvećom vrednošću
sales_per_city.max()     # Vraća najveću vrednost

# Isto za minimum
sales_per_city.idxmin()
sales_per_city.min()
```

### 📊 **Dodatne napredne pandas tehnike**

#### Filtriranje podataka sa isin()
```python
# Filtriranje po određenim vrednostima
songs = songs.loc[songs.album_type.isin(['studio album', 'single', 'extended play'])]

# Kreiranje opsega godina za filtriranje
early_years = [y for y in range(1989, 1995)]  # Lista godina 1989-1994
songs.loc[songs.release_year.isin(early_years)]
```

#### Dodavanje novih kolona u dataset
```python
# Kreiranje nove kolone na osnovu uslova
songs['nova_kolona'] = nova_kolona_condition

# Primer: dodavanje era kolone
songs['era'] = songs.release_year.apply(
    lambda x: '80s' if x < 1990 
             else '90s' if x < 2000 
             else '2000s'
)
```

#### Provera referenci vs kopija
```python
# ⚠️ VAŽNO: Razlika između reference i kopije
sales = all_sales           # ❌ Samo referenca - menjanja utiču na original
sales = all_sales.copy()    # ✅ Prava kopija - nezavisan objekat

# Provera da li su isti objekti
print(id(sales) == id(all_sales))    # False za kopiju, True za referencu
print(sales is all_sales)            # False za kopiju, True za referencu
```

### 5. Spajanje i analiza više dataset-ova
```python
# Kada spajaš CSV fajlove, uvek resetuj indekse
combined_df = pd.concat([df1, df2, df3])
combined_df.reset_index(drop=True, inplace=True)

# Pravi kopije, ne reference
new_df = original_df.copy()  # Pravilno
# new_df = original_df        # Pogrešno - samo referenca
```

### 🔗 Korisni resursi za dalje učenje

**Pandas dokumentacija i tutoriali:**
- [Zvanična Pandas dokumentacija](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

**Matplotlib resursi:**
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Seaborn Examples](https://seaborn.pydata.org/examples/)
- [Python Graph Gallery](https://www.python-graph-gallery.com/)

Ovo je kompletno uputstvo za rad sa Pandas-om i Matplotlib-om. Pokriva sve od osnovnih operacija do naprednih vizualizacija! 🐍📊