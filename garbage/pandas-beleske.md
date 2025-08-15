# Pandas Beleške - Kompletna Referenca

## 📝 Uvod

**Pandas** je najvažnija biblioteka za analizu podataka u Pythonu. Omogućava nam rad sa strukturiranim podacima kroz **DataFrame** i **Series** objekte.

### Magic Komande (Jupyter Notebook)
```python
%run "../nekinotebook.ipynb"  # Izvršava kod iz drugog notebook-a
```

### Osnovni Importi
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stilizovanje grafika
plt.style.use('classic')
```

---

## 📊 Učitavanje i Osnovne Informacije o DataSet-u

### Učitavanje CSV Fajla
```python
# Osnovno učitavanje
songs = pd.read_csv("putanja/do/fajla.csv")

# Učitavanje sa parsiranjem datuma
songs = pd.read_csv("putanja/do/fajla.csv", parse_dates=['kolona_datuma'])
```

### Osnovne Informacije o DataSet-u

| Metoda | Opis | Primer |
|--------|------|--------|
| `df.shape` | Broj redova i kolona | `(1000, 5)` |
| `df.head(n)` | Prvih n redova (default: 5) | `songs.head(10)` |
| `df.tail(n)` | Poslednjih n redova | `songs.tail(10)` |
| `df.sample(n)` | n random redova | `songs.sample(10)` |
| `df.info()` | Detaljan pregled strukture | Prikazuje tipove i null vrednosti |
| `df.describe()` | Deskriptivna statistika | Count, mean, std, min, max, kvartili |
| `df.dtypes` | Tipovi podataka po kolonama | int64, float64, object, datetime64 |

### Rad sa Imenima Kolona
```python
# Pregled kolona
print(songs.columns)                # Index objekat
print(list(songs.columns))         # Lista imena
print(songs.columns.tolist())      # Alternativa za listu
print(songs.columns.values)        # NumPy array

# Pronalaženje pozicije kolone
index_kolone = list(songs.columns).index('naziv_kolone')
```

---

## 🔄 Upravljanje Strukturom DataSet-a

### Preimenovanje Kolona
```python
# Preimenovanje specifičnih kolona
songs.rename({
    'track_name': 'track',
    'album_name': 'album'
}, axis='columns', inplace=True)

# inplace=True - menja originalni DataFrame
```

### Reorganizacija Kolona
```python
# Kreiranje novog redosleda kolona
columns = ['track', 'artists', 'album', 'album_type', 'duration', 'release_year']

# Dodavanje preostalih kolona
columns.extend(list(songs.columns)[6:])

# Primena novog redosleda
songs = songs.reindex(columns=columns)
```

### Čuvanje i Učitavanje Izmenjenog DataSet-a
```python
# Čuvanje (bez index kolone)
songs.to_csv('../data/izmenjeni_fajl.csv', index=False)

# Ponovno učitavanje
songs = pd.read_csv('../data/izmenjeni_fajl.csv')
```

---

## 🔍 Analiza Nedostajućih Vrednosti

### Pronalaženje Nedostajućih Vrednosti
```python
# Pregled nedostajućih vrednosti
missing_data = songs.isna()         # True/False DataFrame
missing_count = songs.isna().sum()  # Broj nedostajućih po koloni

# Vizuelizacija sa heatmap
sns.heatmap(songs.isna(), cbar=False, cmap='viridis')
```

### Analiza Nedostajućih Podataka
```python
# Kolone sa nedostajućim podacima
has_missing = songs.isna().sum() > 0
columns_with_missing = has_missing[has_missing].index

# DataFrame samo sa kolonama koje imaju nedostajuće podatke
songs_missing = songs.loc[:, has_missing]

# Redovi koji imaju bilo koju nedostajuću vrednost
rows_with_missing = songs.loc[songs.isna().any(axis=1), :]
```

### Rukovanje Nedostajućim Vrednostima
```python
# Uklanjanje redova sa nedostajućim vrednostima
songs_clean = songs.dropna()                    # Svi redovi
songs_clean = songs.dropna(subset=['kolona1'])  # Samo za određene kolone

# Uklanjanje kolona sa nedostajućim vrednostima
songs_no_missing_cols = songs.dropna(axis=1)

# Zamena nedostajućih vrednosti
songs.loc[songs['kolona'].isna(), 'kolona'] = 'default_vrednost'
```

---

## 📈 Analiza Vrednosti i Duplikata

### Analiza Vrednosti
```python
# Brojanje pojavljivanja vrednosti
value_counts = songs['kolona'].value_counts()
value_percentages = songs['kolona'].value_counts(normalize=True)

# Za ceo DataFrame
songs.value_counts()
```

### Rukovanje Duplikatima
```python
# Pronalaženje duplikata
duplicates = songs.duplicated()                    # Po svim kolonama
track_duplicates = songs.duplicated('track')      # Po određenoj koloni

# Uklanjanje duplikata
songs_unique = songs.drop_duplicates('track')               # Prvi zadržava
songs_unique = songs.drop_duplicates('track', keep='last')  # Poslednji zadržava

# Reset indeksa nakon brisanja
songs.reset_index(drop=True, inplace=True)
```

### Filtriranje Podataka
```python
# Zadržavanje samo određenih vrednosti
songs = songs.loc[songs.album_type.isin(['studio album', 'single', 'extended play'])]

# Provera duplikata nakon filtriranja
remaining_duplicates = songs.track.duplicated().sum()
```

---

## 🎯 Selektovanje i Indeksiranje

### Osnove Indeksiranja
```python
# Pregled indeksa
print(songs.index)
print(songs.index.tolist())
```

### LOC - Label-based Selection
```python
# Osnovna sintaksa: df.loc[red_uslov, kolona_uslov]

# Selektovanje redova po uslovu
alice_songs = songs.loc[songs.artists == 'Alice in Chains']

# Kompleksni uslovi (koristiti & i |, ne and i or)
filtered = songs.loc[
    (songs.artists == 'Alice in Chains') & 
    (songs.album_type == 'studio album')
]

# Selektovanje određenih kolona
selected = songs.loc[:, ['track', 'artists', 'release_year']]

# Kombinovanje
result = songs.loc[songs.release_year > 1990, ['track', 'artists']]
```

### ILOC - Integer-based Selection
```python
# Selektovanje po poziciji
first_10_rows = songs.iloc[:10, :5]          # Prvih 10 redova, prvih 5 kolona
last_5_rows = songs.iloc[-5:, [0, 1, 4]]    # Poslednjih 5 redova, kolone 0,1,4

# Kombinovanje sa uslovima
missing_composers = songs.track_composers.isna()
missing_indices = missing_composers[missing_composers].index
result = songs.iloc[missing_indices, [0, 1, 2]]
```

### String Operacije
```python
# Rad sa string podacima (dodati .str)
starts_with = songs.track.str.startswith('Love')
contains = songs.track.str.contains('rock', case=False)
length = songs.track.str.len()
```

---

## 📊 Grupisanje i Agregacija (GroupBy)

### Osnovne GroupBy Operacije
```python
# Kreiranje grupa
songs_by_year = songs.groupby('release_year')

# Dobijanje određene grupe
songs_1989 = songs_by_year.get_group(1989)

# Brojanje po grupama
yearly_counts = songs.release_year.value_counts()
```

### Agregacija Podataka
```python
# Jedna metrika
avg_duration = songs.groupby('release_year').duration.mean()

# Multiple metrije
stats = songs.groupby('release_year').duration.agg(['count', 'mean', 'max'])

# Grupisanje po više kolona
multi_group = songs.groupby(['release_year', 'album_type']).size()
```

### Unique Vrednosti
```python
# Unique vrednosti
unique_years = songs.release_year.unique()
unique_count = songs.release_year.nunique()
```

---

## 🔢 Sortiranje

### Sortiranje Series
```python
# Po indeksu
sorted_by_index = songs.release_year.value_counts().sort_index(ascending=False)

# Po vrednostima
sorted_by_values = songs.release_year.value_counts().sort_values(ascending=False)
```

### Sortiranje DataFrame
```python
# Po jednoj koloni
songs_sorted = songs.sort_values('release_year')

# Po više kolona
songs_sorted = songs.sort_values(['release_year', 'duration'], ascending=[True, False])

# Sortiranje agregiranih rezultata
sorted_stats = songs.groupby('release_year').duration.agg(['count', 'mean']) \
                    .sort_values(by='count', ascending=False)
```

---

## 🔄 Transformacija Podataka

### Konverzija Tipova Podataka
```python
# Konverzija u numeričke tipove
try:
    df['kolona'] = pd.to_numeric(df['kolona'], errors='coerce')  # NaN za greške
except ValueError as err:
    print(f"Greška pri konverziji: {err}")

# Konverzija u datetime
df['Order_Date'] = pd.to_datetime(
    df['Order_Date'], 
    errors='coerce',
    format='%m/%d/%y %H:%M'
)
```

### Apply Funkcije
```python
# Primena funkcije na kolonu
df['nova_kolona'] = df['kolona'].apply(custom_function)

# Lambda funkcije
df['squared'] = df['number'].apply(lambda x: x**2)
```

### Rad sa DateTime
```python
# Pristup komponentama datuma
df['month'] = df.Order_Date.dt.month
df['year'] = df.Order_Date.dt.year
df['day_of_week'] = df.Order_Date.dt.dayofweek
```

---

## 📁 Rad sa Više Fajlova

### Kombinovanje CSV Fajlova
```python
from pathlib import Path

def get_csv_files(fpath: Path) -> list:
    """Dobija sve CSV fajlove iz direktorijuma."""
    if not fpath.is_dir():
        raise RuntimeError("Putanja nije direktorijum")
    
    csv_files = []
    for item in fpath.iterdir():
        if not item.is_dir() and item.suffix == '.csv':
            csv_files.append(item)
    return csv_files

# Kombinovanje fajlova
all_data = pd.DataFrame()
for csv_file in get_csv_files(data_directory):
    temp_df = pd.read_csv(csv_file)
    all_data = pd.concat([all_data, temp_df], ignore_index=True)

# Reset indeksa
all_data.reset_index(drop=True, inplace=True)
```

### Pravljenje Kopije
```python
# PAŽNJA: Ovo ne pravi kopiju!
sales = all_sales  # Samo nova referenca

# Pravljenje stvarne kopije
sales = all_sales.copy()
```

---

## 🛠️ Dodatne Operacije

### Upravljanje Kolonama
```python
# Brisanje kolona
df.drop(columns=['kolona1', 'kolona2'], inplace=True)

# Dodavanje nove kolone
df['nova_kolona'] = df['kolona1'] * df['kolona2']

# Pristup kolonama
df.kolona_bez_razmaka    # Dot notation
df['kolona sa razmakom'] # Bracket notation (uvek bezbedno)
```

### Čišćenje Podataka
```python
# Uklanjanje redova/kolona sa nedostajućim podacima
df.dropna(how='any', inplace=True, subset=['kolona1', 'kolona2'])
# how='any' - ako bilo koja vrednost nedostaje
# how='all' - ako sve vrednosti nedostaju
# subset - provera samo određenih kolona
```

---

## 📊 Napredne Tehnike

### Pretvaranje Series u DataFrame
```python
# Series u DataFrame
series_df = series_data.to_frame()
series_df.reset_index(inplace=True)
```

### Unstack za Pivot Tabele
```python
# Grupisanje po više kolona vraća Series sa multi-index
multi_grouped = df.groupby(['kolona1', 'kolona2']).vrednost.sum()

# Unstack pretvara u DataFrame
pivot_table = multi_grouped.unstack()
# Prvi nivo indeksa postaje redovi, drugi nivo kolone
```

### Faktorizacija za Boje
```python
# Kreiranje numeričkih labela za kategorije
numeric_labels, unique_categories = pd.factorize(df['kategorija'])

# Korisno za colormap-e u vizuelizaciji
import matplotlib.pyplot as plt
colors = plt.cm.viridis(numeric_labels / len(unique_categories))
```

---

## 💡 Najbolje Prakse

### ✅ Dos
- Uvek koristite `inplace=True` pažljivo - bolje eksplicitno dodeljivanje
- Pravljenje kopija podataka pre većih transformacija
- Korišćenje `errors='coerce'` pri konverziji tipova
- Reset indeksa nakon filtriranja/brisanja podataka
- Čuvanje intermediate rezultata tokom analize

### ❌ Don'ts  
- Izbegavajte `df.iterrows()` - koristite vektorizovane operacije
- Ne koristite `and`/`or` u pandas uslovima - koristite `&`/`|`
- Ne pristupajte kolonama sa razmakom bez zagrada
- Ne zanemarujte nedostajuće podatke

---

## 🔗 Korisni Resursi

- [Pandas dokumentacija](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

*Ove beleške pokrivaju 90% svakodnevnih potreba za rad sa Pandas bibliotekom. Za naprednije tehnike, konsultujte zvaničnu dokumentaciju.*