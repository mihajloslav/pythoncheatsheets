# Python Beleške - Kompletno Uputstvo

## Osnove Python-a

Python je interpretiran, objektno-orijentisan programski jezik koji se odlikuje čitljivošću i jednostavnošću. Nastao je 1991. godine od strane Guida van Rossuma i danas je jedan od najpopularnijih jezika za web development, data science, AI i automatizaciju.

### Fundamentalni principi
- **U Python-u je sve objekat** - brojevi, stringovi, funkcije, klase, sve su objekti sa svojim metodama i atributima
- **Paket** - folder koji sadrži `__init__.py` fajl (npr. folder `python` sa `__init__.py`). Ovaj fajl govori Python-u da tretira direktorijum kao paket. Kolekcija modula u direktorijumu sa __init__.py
- **Modul** = fajl sa definicijama funkcija/klasa, bez pozivanja tih funkcija.
- **Skripta** = fajl sa definicijama i izvršnim kodom koji poziva funkcije.

### Osnovne komande i shortcuts

| Komanda | Funkcija |
|---------|----------|
| `CTRL + ALT + ENTER` | Izvršava komandu |
| `CTRL + /` | Komentarisanje/odkomentarisanje |
| `CTRL + ENTER` | Kompajliranje koda |

### Struktura projekta
```
projekt/
├── .idea/              # Konfiguracija okruženja (PyCharm)
├── blanknotebooks/     # Prazni notebook fajlovi
└── blankscripts/       # Prazne skripte
```

---

## Komentari i dokumentacija

Dokumentovanje koda je jedna od najvažnijih praksi u programiranju. Python ima nekoliko načina za komentarisanje koji služe različitim svrhama - od običnih objašnjenja do automatski generisane dokumentacije.

### Tipovi komentara
```python
# Jednoredan komentar

""" 
Višeredan komentar (docstring)
Koristi se za dokumentaciju funkcija i klasa
"""

#%% Nova ćelija (za Jupyter-like okruženja)
```

### Built-in atributi
```python
print(__name__)     # Naziv skripte
print(__doc__)      # Dokumentacija (docstring)
print(__file__)     # Apsolutna putanja fajla

# Funkcije takođe imaju __doc__
print(print_ringo.__doc__)
```

### Razlika između modula i skripte
- **Modul**: Python fajl sa definisanim funkcijama i klasama, bez izvršnih naredbi
- **Skripta**: Python fajl sa izvršnim naredbama

### Uslovni izvršavanje koda
```python
if __name__ == '__main__':
    print_ringo()  # Izvršava se samo ako je skripta direktno pokrenuta
```

---

## Stringovi

Stringovi su jedan od najčešće korišćenih tipova podataka u Python-u. Za razliku od nekih drugih jezika, Python strignovi su immutable (nepromenjivi) - svaka operacija nad stringom kreira novi string. Python pruža neverovatno bogat skup metoda za manipulaciju teksta.

### Definisanje stringova
```python
# Oba načina su validna
string1 = 'Tekst sa jednostrukim navodnicima'
string2 = "Tekst sa dvostrukim navodnicima"
```

### String formatting

#### 1. C-style formatiranje
```python
ime = "Zoran"
godine = 25
print("Zoran ima %d godina %s" % (godine, ime))
```

#### 2. Raw stringovi (preskoče escape karaktere)
```python
print(r"C:\nobody")  # Neće interpretirati \n kao novi red
```

#### 3. Multiline stringovi
```python
print("""Zoran
Petar
Ivan""")
```

#### 4. Format metoda
```python
print("Zoran ima {} godina u {} godini".format(5, 2025))
print("Zoran ima {0} godina u {1} godini".format(5, 2025))  # Sa indeksima
```

#### 5. F-stringovi (preporučeno)
```python
godine = 25
godina = 2025
print(f"Zoran ima {godine} godina u {godina} godini")
```

### String slicing
```python
tekst = "Zoran"
print(tekst[2:])      # Iz 3. karaktera do kraja: "ran"
print(tekst[::-1])    # Obrnut string: "naroZ"
print(tekst[2::])     # Od 3. karaktera sa korakom 1: "ran"
```

### String multiplikacija
```python
print("Zoran" * 3)   # ZoranZoranZoran
```

### Str vs repr
```python
print(str('Zoran'))   # Zoran
print(repr('Zoran'))  # 'Zoran' (sa navodnicima)
```

### Korisne string metode
```python
tekst = "  Hello World  "

tekst.endswith('rec')                    # True/False
tekst.split('rec')                       # Lista reči
tekst.split()                            # Deli po whitespace
tekst.center(20, '*')                    # ***Hello World***
'rec' in tekst                           # Da li sadrži 'rec'
tekst.strip()                            # Uklanja whitespace
tekst.lstrip('karakter')                 # Uklanja sa leve strane
tekst.rstrip('karakter')                 # Uklanja sa desne strane

# Za domen iz URL-a
website = "https://example.com/"
_, suffix = website.rsplit('.', maxsplit=1)  # Deli sa desne strane
suffix = suffix.rstrip('/')                  # Uklanja trailing slash
```

---

## Range funkcija

Range funkcija je generator koji kreira sekvence brojeva. Umesto da kreira sve brojeve odjednom u memoriji, ona generiše brojeve "na zahtev" što čini rad sa velikim sekvencama izuzetno efikasnim.

```python
range(1, 5)        # 1, 2, 3, 4 (poslednja se izostavlja)
range(5)           # 0, 1, 2, 3, 4
range(1, 10, 2)    # 1, 3, 5, 7, 9 (korak 2)
```

---

## Enumerate funkcija

Enumerate je jedna od najkorisnijih Python funkcija koja vam omogućava da istovremeno dobijete i indeks i vrednost elementa tokom iteracije. Ovo je posebno korisno kada trebate da pratite poziciju elementa u listi.

```python
lista = ['a', 'b', 'c']

for i, element in enumerate(lista):
    print(f"{i}: {element}")
# 0: a
# 1: b  
# 2: c
```

---

## Input/Output funkcije

Interakcija sa korisnikom je osnova mnogih programa. Python pruža jednostavne ali moćne funkcije za čitanje input-a i prikazivanje output-a sa različitim opcijama formatiranja.

### Print funkcija
```python
# Print automatski dodaje \n na kraj
print('Ringo Starr', 'John Lennon', sep=' & ')  # Custom separator
print('Tekst', end='')  # Bez \n na kraju
```

### Input funkcija
```python
# Sa promptom
ime = input("Unesite ime: ")

# Ili odvojeno
print("Unesite ime:")
ime = input()
```

---

## Korisne built-in funkcije

Python dolazi sa velikim brojem ugrađenih funkcija koje rešavaju česte programerske zadatke. Ove funkcije su optimizovane i testirane, tako da je uvek bolje koristiti ih umesto pisanja svojih implementacija.

### Divmod
```python
# Vraća rezultat deljenja i ostatak
result, remainder = divmod(17, 5)  # result=3, remainder=2

num = 17
result, remainder = divmod(num, 2)
odd_even_str = "EVEN" if remainder == 0 else "ODD"
print(f"Broj {num} je {odd_even_str}")
```

### Sorted
```python
items = [3, 1, 4, 1, 5]
sorted_items = sorted(items)           # [1, 1, 3, 4, 5]
nth_smallest = sorted(items)[n - 1]    # n-ti najmanji element

# Sortiranje u opadajućem redosledu  
sorted_desc = sorted(items, reverse=True)  # [5, 4, 3, 1, 1]

# Iteriranje kroz sortiranu listu
for num in sorted(items, reverse=True):
    print(num)
```

### IsDigit
```python
guess_str = "123"
if guess_str.isdigit():
    number = int(guess_str)
else:
    print("Nije broj")
```

---

## Operatori

Operatori u Python-u nisu samo simboli - oni pozivaju posebne metode objekata. Na primer, `a + b` zapravo poziva `a.__add__(b)`. Razumevanje ovoga vam pomaže da bolje razumete kako Python funkcioniše "ispod haube".

### Aritmetički operatori
```python
# Stepenovanje
x = 2 ** 3  # 8

# Celobrojno deljenje  
result = 17 // 5  # 3
```

### Operatori poređenja
```python
# Poređenje po sadržaju
a == b  

# Poređenje po adresi u memoriji
a is b

# Za datume
from datetime import date
date1 = date.today()
date2 = date.today()

date1 == date2  # True (isti datum)
date1 is date2  # False (različiti objekti u memoriji)
date1 > date2   # False
```

**Napomena**: Za proste tipove (int, float, string), `==` i `is` često vraćaju isto zbog Python optimizacije.

### Logički operatori
```python
# Python ekvivalenti
# && → and
# || → or  
# !  → not

# Short-circuit evaluacija
print(1 and 4)        # 4 (ako je prvo True, vraća drugo)
print(None or [4,3])  # [4, 3] (ako je prvo False, vraća drugo)
```

### None i relacioni operatori
```python
# None se NE SME koristiti sa relacionim operatorima (<, >, <=, >=)
# Može se koristiti samo sa == i !=
```

---

## Falsy vrednosti

U Python-u, svaki objekat ima "boolean vrednost" - može se evaluirati kao True ili False. Ovo je osnova za if statement-e i while petlje. Razumevanje falsy vrednosti je ključno za pisanje elegantan Python koda.

U Python-u su sledeće vrednosti "falsy" (evaluiraju se kao False):
```python
None, [], '', 0, False, {}, set()
```

---

## Liste

Liste su verovatno najčešće korišćena struktura podataka u Python-u. One su mutable (mogu se menjati), ordered (čuvaju redosled), i mogu sadržati elemente različitih tipova. To ih čini neverovatno fleksibilnim za različite potrebe.

### Kreiranje listi
```python
ringo = []              # Prazan lista
ringo = list()          # Alternativni način
ringo = ['Ringo Starr', 1940, True, 'The Beatles']
```

### Pristupanje elementima
```python
print(ringo[1])         # Drugi element (1940)
print(ringo[1:3])       # Elementi od 2. do 3.
print(ringo[-2:])       # Poslednja dva elementa
```

### Poređenje listi
```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista1 == lista2)  # True (isti sadržaj)
print(lista1 is lista2)  # False (različiti objekti)
```

### Operacije sa listama
```python
# Spajanje listi
nova_lista = ringo + ['John Lennon']

# Dodavanje elemenata
ringo.append('John Lennon')              # Dodaje na kraj
ringo.insert(2, 'Paul McCartney')        # Ubacuje na poziciju 2
ringo.extend(['John', 'Paul'])           # Spaja sa drugom listom

# Uklanjanje elemenata  
ringo.remove('Paul McCartney')           # Briše prvi element sa tom vrednošću
element = ringo.pop()                    # Uklanja i vraća poslednji element
element = ringo.pop(1)                   # Uklanja i vraća element na poziciji 1

# Informacije o listi
print(len(ringo))                        # Dužina liste
print(ringo.count('John Lennon'))        # Broj pojavljivanja elementa
print(ringo.index('John Lennon'))        # Indeks prvog pojavljivanja
print('John Lennon' in ringo)            # Da li lista sadrži element
print('John Lennon' not in ringo)        # Da li lista NE sadrži element

# Modifikacija liste
ringo.reverse()                          # Obrće listu (in-place)
```

### Kopiranje listi
```python
original = [1, 2, 3]

# PAŽNJA: Ovo samo prebacuje pokazivač!
kopija = original  # I dalje ista lista u memoriji!

# Pravi načini kopiranja:
kopija1 = original.copy()
kopija2 = original + []  
kopija3 = original[:]
```

### Liste i random modul
```python
from random import seed, randint

l = []
seed(3546)  # Za reproducibilne rezultate
for i in range(10):
    l.append(randint(1, 100))
print(l)
```

### List comprehension
```python
songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane']

# Uzimanje prve reči iz svakog naslova
first_words = [s.split()[0] for s in songs]

# Uzimanje prvog slova iz svake reči
first_letters = [w[0] for w in first_words]

# Spajanje u string
first_letters_str = ''.join([w[0] for w in first_words])
first_letters_final = ''.join([w[0] for w in first_words]).capitalize() + '!'

# Pronalaženje indeksa određenog elementa
songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane', 'Eleanor Rigby']
indices = [i for i, title in enumerate(songs) if title == 'Eleanor Rigby']
```

### Rad sa listama - dodatne funkcije
```python
# Kreiranje liste sa predefinisanim vrednostima
valid = [False] * 5  # [False, False, False, False, False]

# Sortiranje dve liste i poređenje
sorted(l1) == sorted(l2)

# Negativni indeksi
text = "hello"
last_char = text[-(i+1)]  # Pristupanje unazad
```

---

## Zip funkcija

Zip funkcija je jedan od najkorisnijih Python alata za rad sa više sekvenci istovremeno. Ime potiče od "zipper" (rajsferšlus) jer "spaja" elementi iz različitih sekvenci kao što rajsferšlus spaja dve strane.

**Važno**: Zip pravi parove do dužine najkraće sekvence - ako su liste različite dužine, višak elemenata se ignoriše!

```python
l1 = ["M", "Na"]
l2 = ["y", "me"]  
l3 = []

# Spajanje elemenata po indeksima
for i, j in zip(l1, l2):
    l3.append(i + j)

# Kraći način
result = [i + j for i, j in zip(l1, l2)]  # ["My", "Name"]

# Zip sa više listi
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c'] 
l3 = ['x', 'y', 'z']

neki_zip = zip(l1, l2, l3)
for item1, item2, item3 in neki_zip:
    print(item1, item2, item3)

# PAŽNJA: Zip objekti rade kao iteratori - nakon korišćenja su prazni!
```

---

## Matematičke funkcije

Python pruža bogat skup matematičkih funkcija kroz built-in funkcije i math modul. Ove funkcije su optimizovane i rade sa različitim tipovima brojeva.

### Round funkcija
```python
# Osnovno zaokruživanje
broj = 3.7
print(round(broj))  # 4

# Round-to-even strategija
print(round(3.5))  # 4 (zaokružuje na paran broj)
print(round(2.5))  # 2 (zaokružuje na paran broj)

# Zaokruživanje dužine liste
print(round(len(lista)))
```

### All i Any funkcije
```python
# All - vraća True ako su SVI elementi True
def is_palindrome(text):
    midpoint = len(text) // 2
    return all([text[i] == text[-(i+1)] for i in range(midpoint)])

# Any - vraća True ako je BILO KOJI element True  
def has_no_lowercase(word):
    return not any([ch.islower() for ch in word])

# Alternativa za palindrom
def is_palindrome_alt(text):
    return text == text[::-1]
```

---

## Rad sa stringovima - character methods

Python stringovi dolaze sa velikim brojem metoda za analizu karaktera. Ove metode vraćaju True/False i često se koriste za validaciju input-a ili obradu teksta.

```python
ch = 'A'

ch.islower()    # Da li je malo slovo
ch.isupper()    # Da li je veliko slovo  
ch.isdigit()    # Da li je cifra
ch.isalnum()    # Da li je alfanumerički
```

---

## Funkcije za obradu podataka

Python excellira u obradi podataka zbog svojih moćnih built-in funkcija i library-ja. Statistics modul posebno pojednostavljuje česte statističke operacije.

### Sum funkcija
```python
# Zbir brojeva od 1 do n
total = sum(range(1, n + 1))
```

### Statistics modul
```python
from statistics import mean

members = [
    {'name': 'John', 'age': 25, 'score': 85},
    {'name': 'Paul', 'age': 24, 'score': 92}
]

# Prosečna starost
mean_age = mean(member['age'] for member in members)
```

### Max funkcija sa key parametrom
```python
# Najbolji igrač mlađi od 21 godine (po skoru)
best_under_21 = max(
    [member for member in members if member['age'] < 21], 
    key=lambda m: m['score']
)

# Sortiranje po skoru
sorted_members = sorted(members, key=lambda m: m['score'])
```

---

## Tupli (Tuples)

Tupli su immutable (nepromenjivi) sekvence u Python-u. Koriste se kada želite da grupišete podatke koji se neće menjati, za vraćanje više vrednosti iz funkcija, ili kao ključevi u rečnicima (pošto su hashable za razliku od listi).

**Kada koristiti tupli umesto listi:**
- Kada podaci nisu menjaju (koordinate, RGB vrednosti)
- Za ključeve u rečnicima
- Vraćanje više vrednosti iz funkcije
- Kada želite da sprečite slučajne izmene podataka

### Kreiranje tupla
```python
# Prazni tupli (retko se koriste)
ringo = ()
ringo = tuple()

# Tupli sa jednim elementom - VAŽNO: mora zarez!
ringo = ('Ringo',)    # Sa zarezom
ringo = 'Ringo',      # Alternativno

# Tupli sa više elemenata
the_beatles = 'John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr'
```

### Rad sa tuplima
```python
# Pristupanje elementima
print(ringo[0])

# Raspakivanje tupla
john, paul, george, ringo = the_beatles

# Pretvaranje u listu
beatles_list = list(the_beatles)
```

**Napomena**: Tupli su immutable (ne mogu se menjati nakon kreiranja).

---

## Rečnici (Dictionaries)

Rečnici su najmoćnija struktura podataka u Python-u. Oni implementiraju hash table i pružaju O(1) prosečnu složenost za pristup, dodavanje i brisanje. U Python 3.7+, rečnici čuvaju redosled unosa elemenata.

**Kada koristiti rečnike:**
- Mapiranje ključ-vrednost (kao telefonski imenik)
- Brza pretraga po ključu
- Grupiranje povezanih podataka
- Cachiranje rezultata funkcija

### Kreiranje rečnika
```python
# Prazan rečnik
ringo = {}
ringo = dict()

# Rečnik sa podacima
ringo = {'name': 'Ringo Starr', 'year': 1940}
```

### Rad sa rečnicima
```python
# Pristupanje vrednostima
print(ringo['name'])

# Dodavanje/menjanje vrednosti
ringo['city'] = 'Liverpool'

# Brisanje elemenata
del ringo['city']

# Dodavanje više elemenata odjednom
ringo.update({'city': 'Liverpool', 'band': 'The Beatles'})

# Pristupanje ključevima i vrednostima
print(ringo.keys())      # Svi ključevi
print(ringo.values())    # Sve vrednosti
print(ringo.items())     # Parovi (ključ, vrednost)

# Iteriranje kroz rečnik
for k, v in ringo.items():
    print(f"{k}: {v}")
```

### Pretty printing rečnika
```python
from pprint import pprint

pprint(ringo, width=1)  # Svaki element u novom redu
```

### Sortiranje rečnika

#### 1. Korišćenje zip funkcije
```python
# Sortiranje po ključevima
sorted_dict = dict(sorted(zip(d.keys(), d.values())))

# PAŽNJA: Sortiranje po vrednostima može da pravi problem 
# ako vrednosti nisu istog tipa
```

#### 2. Korišćenje operator.itemgetter
```python
from operator import itemgetter

# Sortiranje po ključevima (indeks 0)
sorted_by_keys = dict(sorted(d.items(), key=itemgetter(0)))

# Sortiranje po vrednostima (indeks 1)  
sorted_by_values = dict(sorted(d.items(), key=itemgetter(1)))
```

#### 3. Korišćenje lambda funkcija
```python
# Sortiranje po ključevima
sorted_by_keys = dict(sorted(d.items(), key=lambda x: x[0]))

# Sortiranje po vrednostima
sorted_by_values = dict(sorted(d.items(), key=lambda x: x[1]))
```

### Dictionary comprehension
```python
# Kreiranje rečnika od dve liste
result = {k: v for k, v in zip(l1, l2)}

# Sortiran rečnik kroz comprehension
sorted_dict = {k: v for k, v in sorted(d.items(), key=itemgetter(0))}
```

### Kreiranje rečnika od listi
```python
def lists_to_dict(l1, l2):
    d = dict()
    elem_num = min(len(l1), len(l2))  # Najmanji broj elemenata
    for i in range(elem_num):
        d[l1[i]] = l2[i]
    return d

# Alternativno sa zip
def lists_to_dict_zip(l1, l2):
    return {item1: item2 for item1, item2 in zip(l1, l2)}

# Sa strict=True za proveru dužine
def lists_to_dict_strict(l1, l2):
    d = dict()
    for item1, item2 in zip(l1, l2, strict=True):  # Baca grešku ako nisu iste dužine
        d[item1] = item2
    return d

# Za različite dužine listi sa default vrednostima
from itertools import zip_longest

def lists_to_dict_fillvalue(l1, l2):
    d = dict()
    for item1, item2 in zip_longest(l1, l2, fillvalue="unknown"):
        d[item1] = item2
    return d
```

### DefaultDict
```python
from collections import defaultdict

# Rečnik sa default int vrednostima (0)
d = defaultdict(int)

# Rečnik sa default list vrednostima ([])
d = defaultdict(list)
d['key'].append("value")  # Automatski kreira listu ako ne postoji
```

### Counter
```python
from collections import Counter

# Brojanje elemenata u listi
lista = [1, 1, 1, 2, 2, 2, 3, 3]
d = dict(Counter(lista))  # {1: 3, 2: 3, 3: 2}
```

---

## Skupovi (Sets)

Skupovi su neuredene kolekcije jedinstvenih elemenata, bazirane na matematičkom konceptu skupova. Implementirani su kao hash table, što čini membership test (provera da li element postoji) izuzetno brzom - O(1) složenost.

**Glavne prednosti skupova:**
- Automatsko uklanjanje duplikata
- Brzi membership test (`element in set`)
- Matematičke operacije (presek, unija, razlika)
- Efikasni za rad sa velikim kolekcijama

### Kreiranje skupova
```python
# Prazan skup
the_beatles = set()

# Skup sa podacima
the_beatles = {'John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr'}

# Dodavanje elementa
the_beatles.add('Pete Best')

# Uklanjanje elementa
the_beatles.remove('Pete Best')
```

### Glavna upotreba - uklanjanje duplikata
```python
the_beatles_list = ['John Lennon', 'Paul McCartney', 'John Lennon', 'Ringo Starr']
unique_beatles = list(set(the_beatles_list))
```

### Operacije sa skupovima
```python
set1 = {'John Lennon', 'Paul McCartney', 'George Harrison'}
set2 = {'George Harrison', 'Ringo Starr'}

# Presek (intersection)
print(set1 & set2)  # {'George Harrison'}

# Unija (union)  
print(set1 | set2)  # Svi elementi iz oba skupa

# XOR - elementi koji se nalaze u samo jednom skupu
print(set1 ^ set2)  # {'John Lennon', 'Paul McCartney', 'Ringo Starr'}

# Razlika - elementi iz prvog skupa koji nisu u drugom
print(set1 - set2)  # {'John Lennon', 'Paul McCartney'}
```

---

## Funkcije

Funkcije su osnova modularnog programiranja u Python-u. One enkapsuliraju logiku, omogućavaju ponovno korišćenje koda i čine programe lakšim za održavanje. Python ima vrlo fleksibilan sistem za definisanje funkcija sa različitim tipovima argumenata.

**Zašto su funkcije važne:**
- DRY princip (Don't Repeat Yourself)
- Lakše testiranje i debugging
- Enkapsulacija logike
- Mogućnost pozivanja iz drugih delova programa

### Definisanje funkcija
```python
def funkcija(title, author="Ringo", year: int = 1968):
    """
    Ovo je docstring - dokumentacija funkcije
    """
    return f"{title} by {author} ({year})"
```

### Anotacije funkcija
```python
# Pregled anotacija
print(funkcija.__annotations__)  # {'year': <class 'int'>}
```

### Tipovi argumenata

#### 1. Pozicioni argumenti (obavezni)
```python
def funkcija(band, member):  # band i member su pozicioni
    pass
```

#### 2. Default argumenti
```python
def funkcija(band, active=True, year=1960):  # active i year su default
    pass
```

#### 3. Fleksibilni argumenti (*args)
```python
def funkcija(band, *members):  # members je tuple
    print(f"Band: {band}")
    for member in members:
        print(member)

# Poziv
lista = ['John', 'Paul', 'George', 'Ringo']
funkcija('The Beatles', *lista)  # Raspakuje listu
```

#### 4. Keyword argumenti (**kwargs)
```python
def funkcija(band, *members, is_active=True, **details):
    print(f"Band: {band}")
    print(f"Members: {members}")
    print(f"Active: {is_active}")
    print(f"Details: {details}")

# Poziv
funkcija('The Beatles', 'John', 'Paul', 
         is_active=False, start=1962, end=1970)
```

### Redosled argumenata
**Prioritet (obavezni redosled)**: Pozicioni → *args → named/default → **kwargs

### Lokalne promenljive
```python
def funkcija():
    x = 10
    y = 20
    print(locals())  # {'x': 10, 'y': 20}
```

### Funkcije kao argumenti
```python
def g(h, *args):
    return h(*args)

def square(x):
    return x ** 2

result = g(square, 5)  # Prosleđuje funkciju square sa argumentom 5
```

### Nested funkcije i closures
```python
def return_func(full_name, first_name_flag):
    def first():
        return full_name.split()[0]
    
    def last():
        return full_name.split()[1]
    
    return first if first_name_flag else last

# Korišćenje
f = return_func('Ringo Starr', False)
print(f())  # "Starr"
```

---

## Dekoratori

Dekoratori su jedan od najelegantnijih Python pattern-a. Oni su funkcije koje "ukrašavaju" druge funkcije - dodaju im funkcionalnost bez menjanja originalnog koda. Ovo je implementacija Decorator pattern-a iz objektno-orijentisanog dizajna.

**Česti slučajevi korišćenja dekoratora:**
- Logovanje poziva funkcija
- Merenje vremena izvršavanja
- Validacija argumenata
- Caching rezultata
- Autentifikacija/autorizacija u web aplikacijama
- Retry logika za menjanje API pozive

**Kako dekoratori rade:**
Dekorator prima funkciju kao argument i vraća novu funkciju koja "omatava" originalnu. Ova nova funkcija može da izvršava kod pre i posle poziva originalne funkcije.

### Osnovni dekorator
```python
def simple_decorator(f):
    def wrap(*args, **kwargs):
        print('-------')
        v = f(*args, **kwargs)
        print('-------')
        return v
    return wrap

# Korišćenje bez @ sintakse
def songs(*args):
    print(', '.join(args))

decorated_songs = simple_decorator(songs)
decorated_songs('Song1', 'Song2')
```

### Dekorator sa @ sintaksom
```python
import functools

def band_details(f_to_decorate):
    @functools.wraps(f_to_decorate)  # Čuva identitet originalne funkcije
    def wrapper(*args, **kwargs):
        print('-------')
        v = f_to_decorate(*args, **kwargs)
        if kwargs:
            details = ', '.join([f"{k}: {v}" for k, v in kwargs.items()])
            print(details)
        if len(args) > 1:
            members = ', '.join(args[1:])
            print(members)
        print('-------')
        return v
    return wrapper

@band_details
def print_band(name, *members, **years_active):
    print(name)

# functools.wraps osigurava da print_band.__name__ vraća 'print_band' umesto 'wrapper'
```

### Template za dekoratore
```python
import functools

def decorator(f_to_decorate):
    @functools.wraps(f_to_decorate)
    def wrapper_decorator(*args, **kwargs):
        # Kod pre izvršavanja funkcije
        value = f_to_decorate(*args, **kwargs)
        # Kod posle izvršavanja funkcije
        return value
    return wrapper_decorator
```

---

## Klase

Klase su temelj objektno-orijentisanog programiranja (OOP) u Python-u. OOP omogućava enkapsulaciju podataka i funkcionalnosti u objekte, što čini kod organizovanijim, lakšim za održavanje i ponovno korišćenje.

**Ključni OOP koncepti:**
- **Enkapsulacija**: Grupiranje podataka i metoda koje rade sa tim podacima
- **Nasledjivanje**: Kreiranje novih klasa na osnovu postojećih
- **Polimorfizam**: Mogućnost različitih objekata da odgovore na iste poruke
- **Apstrakcija**: Sakrivanje implementacijskih detalja

**Special methods (dunder methods):**
Python koristi metode sa dvostrukim underscorovima (`__init__`, `__str__`, itd.) za implementaciju built-in funkcionalnosti kao što su kreiranje objekta, poređenje, iteracija, itd.

### Osnovna definicija klase
```python
class Musician:
    def __init__(self, name, is_band_member=True):
        self.name = name
        self.is_band_member = is_band_member
    
    def __str__(self):
        return f'{self.name}'
    
    def __eq__(self, other):
        if isinstance(other, Musician):
            return self.__dict__ == other.__dict__
        return False
    
    def play(self):
        return f"{self.name} is playing"
```

### Privatna i zaštićena polja

```python
class Musician:
    def __init__(self, name):
        self.__name = name      # Privatno polje (name mangling)
        self._protected = value # Zaštićeno polje (konvencija)
    
    @property
    def name(self):
        """Getter za name"""
        return self.__name
    
    @name.setter  
    def name(self, name):
        """Setter za name"""
        self.__name = name if isinstance(name, str) else 'Unknown'

# Pristupanje privatnom polju (ne preporučuje se)
musician = Musician("John")
print(musician._Musician__name)  # Name mangling
```

### Dodavanje atributa tokom izvršavanja
```python
musician = Musician("John")

# Tri načina dodavanja novih atributa
musician.birth_year = 1940                           # 1. Direktno
musician.__setattr__('instrument', 'guitar')         # 2. __setattr__ 
setattr(musician, 'city', 'Liverpool')              # 3. setattr funkcija

# Pristupanje atributima
print(musician.__getattribute__('birth_year'))       # __getattribute__
print(getattr(musician, 'instrument'))              # getattr funkcija
```

### Korisni atributi objekta
```python
musician = Musician("John")

print(musician.__dict__)  # Svi atributi objekta
print(musician.__dir__)   # Sve metode i atributi  
print(musician.__class__) # Tip objekta
print(musician.__class__.__name__)  # Ime klase kao string
```

### Alternativni konstruktor
```python
class Musician:
    def __init__(self, name, is_band_member=True):
        self.name = name
        self.is_band_member = is_band_member
    
    @classmethod
    def create_band_member(cls, name):
        return cls(name, is_band_member=True)
    
    @classmethod  
    def create_solo_artist(cls, name):
        return cls(name, is_band_member=False)

# Korišćenje
john = Musician.create_band_member("John Lennon")
```

### Statičke metode
```python
class Musician:
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0

# Poziv bez kreiranje objekta
if Musician.is_valid_name("John"):
    musician = Musician("John")
```

### Iteratori u klasama
```python
class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    
    def __iter__(self):
        self.__i = 0
        return self
    
    def __next__(self):
        if self.__i < len(self.members):
            member = self.members[self.__i]
            self.__i += 1
            return member
        else:
            raise StopIteration

# Korišćenje
the_beatles = Band("The Beatles", ["John", "Paul", "George", "Ringo"])

for member in the_beatles:
    print(member)
```

### Iterator van klase
```python
# Kreiranje iteratora od objekta
the_beatles = Band("The Beatles", ["John", "Paul", "George", "Ringo"])
iterator = iter(the_beatles)  # Poziva __iter__ u pozadini

# Ručno iteriranje
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
```

---

## Generatori

Generatori su poseban tip funkcija koje omogućavaju lazy evaluation - kreiraju vrednosti "na zahtev" umesto da sve kreirao odmah u memoriji. Ovo ih čini neverovatno memorijski efikasnim za rad sa velikim setovima podataka.

**Prednosti generatora:**
- **Memorijska efikasnost**: Ne drže sve podatke u memoriji istovremeno
- **Lazy evaluation**: Kreiraju podatke kada su potrebni
- **Infinite sekvence**: Mogu generisati beskonačne sekvence
- **Pipeline processing**: Lako se povezuju u lance obrade

**Kada koristiti generatore:**
- Čitanje velikih fajlova red po red
- Web scraping sa velikim brojem stranica
- Matematičke sekvence (Fibonacci, prosti brojevi)
- Stream processing podataka

### Generatorske funkcije
```python
def musician_generator(band):
    """Generator funkcija za iteriranje kroz članove benda"""
    for member in band.members:
        yield member  # Yield pauzira izvršavanje i vraća vrednost

# Korišćenje
the_beatles = Band("The Beatles", ["John", "Paul", "George", "Ringo"])
gen = musician_generator(the_beatles)

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
```

### Generatorski izrazi
```python
# Generator expression (slično list comprehension)
squares_gen = (x ** 2 for x in range(4))

while True:
    try:
        print(next(squares_gen))
    except StopIteration:
        break

# Ili jednostavno
for square in (x ** 2 for x in range(4)):
    print(square)
```

**Napomena**: Generatori se koriste za web scraping, obradu velikih datoteka, ili kad ne želimo da učitamo sve podatke u memoriju odjednom.

---

## Enumeratori (Enum)

Enumeratori su način da definiško imenovane konstante u Python-u. Oni čine kod čitljivijim i bezbednijim tako što sprečavaju korišćenje "magic numbers" i omogućavaju type checking.

**Prednosti Enum-a:**
- **Čitljivost koda**: `Status.ACTIVE` je jasnije od `1`
- **Type safety**: Sprečava greške sa pogrešnim vrednostima
- **Autocomplete**: IDE-ovi mogu da predlože opcije
- **Refactoring**: Lako menjanje vrednosti na jednom mestu

```python
from enum import Enum

class Vocals(Enum):
    LEAD_VOCALS = 1        # Mora imati vrednost
    BACKGROUND_VOCALS = 2  # Nema zareza između njih!

# Korišćenje
vocal_type = Vocals.LEAD_VOCALS
print(vocal_type.name)   # "LEAD_VOCALS"
print(vocal_type.value)  # 1

# Formatiranje za prikaz
formatted_name = vocal_type.name.lower().replace('_', ' ')  # "lead vocals"
```

---

## Nasleđivanje (Inheritance)

Nasleđivanje je jedan od stubova objektno-orijentisanog programiranja. Omogućava kreiranje novih klasa (podklasa) koje "nasleđuju" osobine postojećih klasa (nadklasa), čime se omogućava ponovno korišćenje koda i kreiranje hijerarhija klasa.

**Tipovi nasleđivanja:**
- **Jednostruko**: Klasa nasleđuje od jedne nadklase (preporučeno)
- **Višestruko**: Klasa nasleđuje od više nadklasa (kompleksno, koristiti pažljivo)

**Ključni koncepti:**
- **super()**: Pozivanje metoda nadklase
- **Method overriding**: Redefinisanje metoda u podklasi
- **MRO (Method Resolution Order)**: Redosled pretraživanja metoda
- **isinstance()**: Proverava da li je objekat instanca određene klase

### Jednostruko nasleđivanje
```python
class Singer(Musician):
    def __init__(self, name, vocals=Vocals.LEAD_VOCALS, is_band_member=True):
        super().__init__(name, is_band_member)  # Poziv konstruktora nadklase
        self.vocals = vocals
    
    def __str__(self):
        base_str = super().__str__()
        vocals_str = self.vocals.name.lower().replace('_', ' ')
        return f"{base_str} ({vocals_str})"
    
    def sing(self):
        return f"{self.name} is singing"
    
    def play(self):  # Override metode iz nadklase
        base_play = super().play()
        return f"{base_play} and singing"
```

### Višestruko nasleđivanje
Za višestruko nasleđivanje, nadklase moraju biti pripremljene:

```python
class Musician:
    def __init__(self, name, is_band_member=True, **kwargs):
        super().__init__(**kwargs)  # Prosleđuje kwargs dalje u hijerarhiji
        self.name = name
        self.is_band_member = is_band_member

class Singer(Musician):
    def __init__(self, vocals=Vocals.LEAD_VOCALS, **kwargs):
        super().__init__(**kwargs)
        self.vocals = vocals
    
    def what_do_you_do(self):
        return "I sing"

class Songwriter(Musician):
    def __init__(self, writes_music=True, **kwargs):
        super().__init__(**kwargs)
        self.writes_music = writes_music
    
    def what_do_you_do(self):
        return "I write songs"

# Kombinovana klasa
class SingerSongwriter(Singer, Songwriter):
    def __init__(self, solo_career=False, **kwargs):
        super().__init__(**kwargs)
        self.solo_career = solo_career
    
    def tell_about_yourself(self):
        # Eksplicitno pozivanje metoda iz određenih nadklasa
        print(Singer.what_do_you_do(self))
        print(Songwriter.what_do_you_do(self))

# Kreiranje objekta (svi argumenti moraju biti eksplicitno navedeni)
john = SingerSongwriter(
    name='John Lennon',
    vocals=Vocals.LEAD_VOCALS,
    writes_music=True,
    solo_career=True
)
```

### Method Resolution Order (MRO)
```python
# Redosled u kome Python traži metode
print(SingerSongwriter.__mro__)
# (<class 'SingerSongwriter'>, <class 'Singer'>, <class 'Songwriter'>, <class 'Musician'>, <class 'object'>)
```

---

## Rukovanje greškama (Exception Handling)

Exception handling je ključni aspekt pisanja robusnih programa. Umesto da program krahira kod neočekivanih situacija, možemo elegantno uhvatiti greške i nositi se sa njima.

**Zašto je važno:**
- **Robusnost**: Program ne krahira pri greškama
- **User experience**: Korisnici dobijaju smislene poruke o grešci
- **Debugging**: Lakše pronalaženje i popravljanje bugova
- **Resource cleanup**: Osiguravanje da se resursi oslobode

**Python hierarchy grešaka:**
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
```

### Osnovna try-except struktura
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except IndexError as e:
    print(f"Index error: {e}")
except Exception as e:  # Hvata sve ostale greške
    print(f"Unexpected error: {e}")
else:
    print("Ovo se izvršava ako nema greške")
finally:
    print("Ovo se izvršava uvek")
```

### Detaljnije informacije o grešci
```python
import sys

try:
    result = lista[100]
except IndexError as e:
    sys.stderr.write(f'\n\n{e.__class__.__name__}: {e.args[0]}\n')
```

### Kreiranje custom exception-a
```python
# Root exception za projekt
class BandError(Exception):
    pass

# Specifična greška
class BandNameError(BandError):
    def __init__(self, name):
        self.name = name
        super().__init__(f'Invalid band name: {name}')
        # ili: Exception.__init__(self, f'Invalid band name: {name}')

# Korišćenje
def create_band(name):
    if not name or not isinstance(name, str):
        raise BandNameError(name)
    return Band(name)

try:
    band = create_band("")
except BandNameError as e:
    print(f"Cannot create band: {e}")
```

---

## Rad sa fajlovima i putanjama

Rad sa fajlovima je osnovna potreba većine programa. Python pruža moćne alate za rad sa fajlovima kroz pathlib modul (moderni pristup) i os modul (stariji pristup). Pathlib je objektno-orijentisan i platform-independent.

**Best practices:**
- Uvek koristite `with` statement za automatsko zatvaranje fajlova
- Koristite pathlib umesto string manipulacija za putanje
- Specificirajte encoding explicitly (obično UTF-8)
- Pripremite se za greške (fajl ne postoji, nema dozvole, itd.)

### Path modul
```python
from pathlib import Path

# Osnovne putanje
home_dir = Path.home()           # Home direktorijum korisnika
current_dir = Path.cwd()         # Current working directory
project_dir = Path(__file__).parent  # Direktorijum gde je skripta

# Alternativni načini za current directory
current_alt1 = Path.cwd().absolute()
current_alt2 = Path().absolute()
current_alt3 = Path('.').absolute()

# Roditeljski direktorijum  
parent_dir = Path.cwd().parent
```

### Kreiranje direktorijuma
```python
PROJECT_DIR = Path(__file__).parent

# Kreiranje novog direktorijuma
new_dir = PROJECT_DIR / 'new_dir'
new_dir.mkdir(parents=True, exist_ok=True)

# parents=True: Kreira sve potrebne roditeljske direktorijume
# exist_ok=True: Ne baca grešku ako direktorijum već postoji

# Provera postojanja
if new_dir.exists():
    print("Direktorijum postoji")

# Brisanje praznog direktorijuma
new_dir.rmdir()  # MORA biti prazan!
```

### Upisivanje u fajlove
```python
filename = PROJECT_DIR / 'output.txt'

# Upisivanje jedan po jedan element
with open(filename, 'w') as outfile:
    for item in lista:
        outfile.write(str(item) + '\n')

# Upisivanje cele kolekcije odjednom
bands = ['The Beatles', 'The Rolling Stones', 'Led Zeppelin']
with open(filename, 'w') as outfile:
    outfile.writelines([str(band) + '\n' for band in bands])

# Direktno upisivanje
with open(filename, 'w') as outfile:
    outfile.write('Direktan tekst\n')
```

### Čitanje iz fajlova
```python
filename = PROJECT_DIR / 'input.txt'

# Čitanje celog fajla odjednom
with open(filename, 'r') as infile:
    content = infile.read()        # Ceo fajl kao string
    lines = infile.readlines()     # Lista stringova (svaki red)

# Čitanje red po red
with open(filename, 'r') as infile:
    content = ''
    while True:
        line = infile.readline()
        if line:  # Ako ima sadržaja
            content += line
        else:     # Kraj fajla
            break

# Iteriranje kroz fajl
with open(filename, 'r') as infile:
    for line in infile:
        print(line.strip())  # strip() uklanja \n
```

### Parsiranje strukturiranih podataka
```python
# Kada znamo format svakog reda
with open('servers.txt', 'r') as infile:
    for line in infile:
        # Format: "server name status location"  
        _, name, _, state = line.split()  # _ za nebitne delove
        print(f"{name} is {state}")

# Parsiranje po redovima
content = text.strip().split('\n')
for line in content:
    # Obradi svaki red...
```

---

## Serijalizacija

Serijalizacija je proces pretvaranja Python objekata u format koji može biti sačuvan na disk ili poslat preko mreže. Deserijalizacija je obrnut proces. Ovo je ključno za persistence podataka i komunikaciju između programa.

**Glavni formati:**
- **Pickle**: Python-specifičan, binarni, najviše funkcionalnosti
- **JSON**: Text-based, cross-platform, limited types
- **CSV**: Za tabele podataka
- **XML**: Structured document format

**Kada koristiti koji format:**
- **Pickle**: Interni Python objekti, cache, complex data structures
- **JSON**: Web APIs, konfiguracija, data exchange sa drugim jezicima
- **CSV**: Tabele, Excel kompatibilnost, simple data sets

### Pickle (binarni format)
```python
import pickle

# Upisivanje objekta u binarni fajl
data = ['The Beatles', 'The Rolling Stones', {'year': 1960}]

with open('data.bin', 'wb') as outfile:  # 'wb' = write binary
    pickle.dump(data, outfile)

# Čitanje objekta iz binarnog fajla  
with open('data.bin', 'rb') as infile:   # 'rb' = read binary
    loaded_data = pickle.load(infile)
    print(loaded_data)
```

### JSON serijalizacija
```python
from json_tricks import loads, dumps  # Proširena JSON biblioteka

# Kreiranje JSON stringa
python_object = {
    'name': 'John Lennon',
    'instruments': ['guitar', 'piano'],
    'birth_year': 1940
}

json_string = dumps(python_object, indent=2)  # indent za lepo formatiranje
print(json_string)

# Parsiranje JSON stringa u Python objekat
parsed_object = loads(json_string)
for key, value in parsed_object.items():
    print(f"{key}: {value}")
```

**indent parametar**: Broj razmaka za uvlačenje u JSON formatu (čini ga čitljivijim)

---

## Sortiranje i dodatne tehnike

Sortiranje je jedna od najčešćih operacija u programiranju. Python pruža moćne alate za sortiranje sa custom kriterijumima, što omogućava sortiranje složenih struktura podataka po bilo kom attributu ili kombinaciji atributa.

**Key koncepti:**
- **stable sort**: Python sort je stabilan - čuva relativni redosled jednnakih elemenata
- **key function**: Funkcija koja izvlači vrednost za poređenje
- **reverse**: Opadajući vs rastući redosled
- **in-place vs copy**: sort() menja originalnu listu, sorted() kreira novu

### Sortiranje po više kriterijuma
```python
# Najpre po jednom kriterijumu, zatim po drugom
from operator import itemgetter

# Sortiranje rečnika: prvo po vrednostima (opadajuće), zatim po ključevima
for token, freq in sorted(
    sorted(d.items(), key=itemgetter(1), reverse=True),  # Po vrednostima
    key=itemgetter(0)  # Zatim po ključevima
):
    print(f"{token}: {freq}")
```

### Lambda vs itemgetter
```python
from operator import itemgetter

# Ova dva pristupa su ekvivalentna:
key_func1 = itemgetter(1)         # Uzima drugi element tupla
key_func2 = lambda item: item[1]  # Ista funkcionalnost

sorted_data = sorted(d.items(), key=itemgetter(1))
sorted_data = sorted(d.items(), key=lambda item: item[1])
```

---

## Korisni Python trikovi

Python je poznat po svojim eleganitnim "tricks" koji omogućavaju pisanje kratkog ali čitljivog koda. Ovi idiomi su deo Python kulture i poznavanje ih čini vas boljim Python programerom.

**Python filozofija (Zen of Python):**
- Beautiful is better than ugly
- Simple is better than complex  
- Readability counts
- There should be one obvious way to do it

### Boolean aritmetika
```python
# True se ponaša kao 1, False kao 0
result = True + 1    # 2
result = False + 5   # 5

# Konverzija u brojeve
print(True.__int__())   # 1
print(False.__int__())  # 0
```

### Klase i tipovi
```python
number = 42
print(number.__class__)              # <class 'int'>
print(number.__class__.__name__)     # 'int'
print(type(number).__name__)         # 'int'
```

### Import u funkcijama
```python
def generate_random_number():
    from random import randint  # Import lokalno u funkciji
    return randint(1, 100)

# Korisno kada import nije potreban uvek
```

### Nebitan brojač u petlji
```python
# Kada ne koristimo brojač, koristimo _
for _ in range(5):
    print('Hello World')

# Ili u tuple unpacking-u kada nešto ne treba
_, name, _, state = line.split()  # Ignorišemo 1. i 3. element
```

### Spajanje stringova
```python
musicians = ['John', 'Paul', 'George', 'Ringo']

# Više načina spajanja
print(john, paul, george, ringo, sep=', ')
print(', '.join(musicians))  # Najčešće korišćen

# Za single karaktere
first_letters = ''.join([name[0] for name in musicians])
```

---

## Date i Time

Rad sa datumima i vremenom je čest zadatak u programiranju, ali može biti komplikovan zbog časovnih zona, prestupnih godina, različitih formata, itd. Python datetime modul pruža komprehensivan set alata za ove zadatke.

**Ključni moduli:**
- **datetime**: Osnovni datum i vreme
- **time**: Unix timestamp i time funkcije  
- **calendar**: Kalendarske funkcije
- **dateutil**: Prošireni parsing i manipulacije (third-party)

### Formatiranje datuma
```python
from datetime import date

FORMAT = "%Y-%m-%d"  # Primer: "2025-01-15"

def format_date(datum):
    if isinstance(datum, date):
        return datum.strftime(FORMAT)
    return datum

today = date.today()
formatted = format_date(today)
```

---

## Dodatni saveti i beste prakse

### Kada koristiti koji tip podataka

| Tip | Kada koristiti |
|-----|----------------|
| **Liste** | Kada trebate menjati sadržaj, dodavati/uklanjati elemente |
| **Tupli** | Za nepromenjive sekvence, vraćanje više vrednosti iz funkcija |
| **Rečnici** | Mapiranje ključ-vrednost, brza pretraga po ključu |
| **Skupovi** | Uklanjanje duplikata, brze set operacije (presek, unija) |

### Česti Python idiomi
```python
# Swapping vrednosti
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Defaultna vrednost iz rečnika
value = dictionary.get('key', 'default_value')

# List comprehension sa uslovom
positive_numbers = [x for x in numbers if x > 0]

# Enumeracija sa custom start
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

### Debugging saveti
```python
# Ispis svih lokalnih varijabli
def debug_function():
    x = 10
    y = 20
    print("Local variables:", locals())

# Ispis tipa i vrednosti
def debug_value(val):
    print(f"Type: {type(val)}, Value: {repr(val)}")

# Korišćenje repr() za debugging stringova
text = "Hello\nWorld"
print(repr(text))  # 'Hello\nWorld' (pokazuje \n eksplicitno)
```

### Performance saveti
```python
# Koristi set za membership testove umesto liste
if item in my_set:     # O(1) - brzo
    pass

if item in my_list:    # O(n) - sporo za velike liste
    pass

# List comprehension vs petlje
# Brže:
result = [x**2 for x in range(1000)]

# Sporije:
result = []
for x in range(1000):
    result.append(x**2)
```

---

## Zaključak

Python je moćan, fleksibilan jezik koji omogućava različite pristupe programiranju - od procedurality preko objektno-orijentisanog do funkcionalanog. Ključ uspešnog Python programiranja je razumevanje kada koristiti koji pristup i sleđene Python konvencija.

**Putanja učenja Python-a:**
1. **Osnove**: Variables, data types, control flow
2. **Strukture podataka**: Lists, dictionaries, sets
3. **Funkcije**: Definition, arguments, scope  
4. **OOP**: Classes, inheritance, special methods
5. **Napredne teme**: Decorators, generators, context managers
6. **Ecosystem**: Libraries, packages, virtual environments

Ove beleške pokrivaju ključne Python koncepte od osnovnih tipova podataka do naprednih tema kao što su klase, nasleđivanje, decoratori i file handling. 

**Ključne stvari za zapamćenje**:
1. Python je objektno-orijentisan - sve je objekat
2. Koristite list comprehensions kad god je moguće
3. Try-except blokovi su ključni za robusan kod  
4. Klase su moćne - naučite nasleđivanje i special methods
5. Context managers (`with` statement) za rad sa fajlovima
6. Generatori za efikasno procesiranje velikih podataka

**Najbolji resursi za dalje učenje**:
- Zvanična Python dokumentacija
- "Automate the Boring Stuff with Python" 
- "Python Tricks" by Dan Bader
- Real Python website

---

## Napredne tehnike iz dodatka

### Funkcionalno programiranje - Map, Filter i Reduce

Python podržava funkcionalno programiranje kroz map, filter i reduce funkcije. Ove funkcije omogućavaju elegantan kod za transformaciju i filtriranje podataka.

#### Map funkcija
Map primenjuje funkciju na svaki element u sekvenci i vraća iterator.

```python
# Map menja svaki element u nešto drugo
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Map sa ugrađenim funkcijama
strings = ['1', '2', '3', '4']
integers = list(map(int, strings))  # [1, 2, 3, 4]
```

#### Filter funkcija
Filter filtrira elemente na osnovu uslova i vraća iterator.

```python
# Osnovno filtriranje
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6, 8, 10]

# Kompleksnije filtriranje stringova
strings = ['Ana', 'Bob', 'Civic', 'deed', 'level']
threshold = 3

# Stringovi koji počinju i završavaju se istim slovom i imaju više od threshold različitih karaktera
filtered = list(filter(
    lambda s: s[0].lower() == s[-1].lower() and len(set(s)) > threshold, 
    strings
))
```

#### Reduce funkcija
Reduce primenjuje funkciju kumulativno na elemente sekvence - uzima po dva elementa iz liste i primenjuje operaciju.

```python
from functools import reduce

# Osnovno korišćenje - proizvod svih brojeva
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)  # 120

# Kombinovanje sa list comprehension
def calculate_product(numbers, squared=False):
    """Računa proizvod brojeva ili njihovih kvadrata"""
    return reduce(
        lambda a, b: a * b, 
        [num**2 if squared else num for num in numbers]
    )

result_normal = calculate_product([2, 3, 4])      # 24
result_squared = calculate_product([2, 3, 4], True)  # 576 (4*9*16)
```

### Napredne OOP tehnike

#### Pristupanje atributima klase
Atributima klase se može pristupati direktno preko naziva klase:

```python
class Band:
    founded_year = 1960  # Klasni atribut
    genre = "Rock"       # Klasni atribut
    
    def __init__(self, name):
        self.name = name  # Instance atribut

# Pristupanje klasnim atributima
print(Band.founded_year)  # 1960
print(Band.genre)         # "Rock"

# Kreiranje instance
beatles = Band("The Beatles")
print(beatles.name)           # "The Beatles"
print(beatles.founded_year)   # 1960 (nasleđuje iz klase)
```

#### Napredni getteri i setteri sa validacijom

```python
from datetime import datetime

class Let:
    poletanje_format = "%Y-%m-%d %H:%M"  # Klasni atribut za format
    
    def __init__(self):
        self.__pasos = None
        self.__poletanje = None
    
    @property
    def pasos(self):
        """Getter sa lazy initialization"""
        try:
            return self.__pasos
        except AttributeError:
            self.__pasos = None
            return self.__pasos
    
    @pasos.setter
    def pasos(self, value):
        """Setter sa validacijom za više tipova podataka"""
        # UVEK U SETERU PROVERI DA LI JE ODGOVARAJUCI TIP PODATAKA
        
        # Provera za string format (6 cifara)
        if isinstance(value, str) and len(value) == 6 and value.isdigit():
            self.__pasos = value
            return
        
        # Provera za int u određenom opsegu
        if isinstance(value, int) and 100000 <= value <= 999999:
            self.__pasos = str(value)
            return
        
        # Ako ništa ne odgovara, baci grešku
        raise ValueError(f"Pasos mora biti 6-cifreni string ili broj između 100000-999999")
    
    @property
    def poletanje(self):
        return self.__poletanje
    
    @poletanje.setter
    def poletanje(self, value):
        """Setter koji konvertuje string u datetime"""
        if isinstance(value, str):
            # String pretvara u datetime objekat
            self.__poletanje = datetime.strptime(value, Let.poletanje_format)
        elif isinstance(value, datetime):
            self.__poletanje = value
        else:
            raise TypeError("Poletanje mora biti string ili datetime objekat")

# Validacija za više tipova podataka
def validate_data(value):
    """Može se proveriti više tipova odjednom"""
    if isinstance(value, (str, int, float)):  # Tuple tipova
        return True
    return False
```

**Ključni principi za settere:**
- **Uvek proveri tip podataka** sa `isinstance()`
- **Validacija pre dodele** - ne dodeljuj nevažeće vrednosti
- **Podrška za više tipova** kada je logično
- **Konverzija tipova** kada je bezbedna (npr. int u string)

### Rad sa fajlovima - Kompletni pristup

Pri radu sa fajlovima treba pratiti `FileNotFoundError` i `OSError` exceptione.

#### Kreiranje direktorijuma za rezultate
```python
from pathlib import Path

def get_results_dir():
    """Kreira 'results' direktorijum ako ne postoji"""
    results_dir = Path.cwd() / 'results'
    if not results_dir.exists():
        results_dir.mkdir()
    return results_dir
```

#### TXT fajlovi
```python
from sys import stderr

def ucitaj_iz_txt_fajla(putanja):
    """Ucitava linije iz txt fajla sa error handling"""
    try:
        with open(putanja, 'r') as fobj:
            return [line.rstrip('\n') for line in fobj.readlines()]
    except FileNotFoundError:
        stderr.write(f"Iz ucitaj_iz_txt_fajla: fajl sa putanjom {putanja} ne postoji\n")
    except OSError as err:
        stderr.write(f"Iz ucitaj_iz_txt_fajla: greška pri učitavanju iz {putanja}\n{err}\n")
    return None

def upisi_u_txt_fajl(lista, putanja):
    """Upisuje listu stringova u txt fajl"""
    try:
        with open(putanja, 'w') as fobj:
            for linija in lista:
                fobj.write(f"{linija}\n")
    except OSError as err:
        stderr.write(f"Iz upisi_u_txt_fajla: greška pri upisu u {putanja}\n{err}\n")
```

#### Binary fajlovi (Pickle)
```python
import pickle as pkl
from sys import stderr

def serijalizuj_podatke(podaci, putanja):
    """Serijalizuje podatke u binary fajl"""
    try:
        with open(putanja, 'wb') as fobj:
            pkl.dump(podaci, fobj)
    except pkl.PicklingError as err:
        stderr.write(f"Iz serijalizuj_podatke: Pickling greška\n{err}\n")
    except OSError as err:
        stderr.write(f"Iz serijalizuj_podatke: OS greška pri serijalizaciji\n{err}\n")

def deserijalizuj_podatke(putanja):
    """Deserijalizuje podatke iz binary fajla"""
    try:
        with open(putanja, 'rb') as fobj:
            return pkl.load(fobj)
    except pkl.PickleError as err:
        stderr.write(f"Iz deserijalizuj_podatke: Pickle greška pri deserijalizaciji iz {putanja}\n{err}\n")
    except OSError as err:
        stderr.write(f"Iz deserijalizuj_podatke: OS greška pri deserijalizaciji iz {putanja}\n{err}\n")
    return None
```

#### CSV fajlovi
```python
import csv
from sys import stderr

def ucitaj_iz_csv_fajla(putanja):
    """Učitava CSV fajl kao listu rečnika"""
    try:
        with open(putanja, 'r') as fobj:
            return list(csv.DictReader(fobj))
    except OSError as err:
        stderr.write(f"Iz ucitaj_iz_csv_fajla: greška pri učitavanju iz {putanja}\n{err}\n")
    return None

def upisi_u_csv(putanja, lista_recnika):
    """Upisuje listu rečnika u CSV fajl"""
    try:
        with open(putanja, 'w', newline='') as fobj:
            header = tuple(lista_recnika[0].keys())
            csv_writer = csv.DictWriter(fobj, fieldnames=header)
            csv_writer.writeheader()
            
            for podaci in lista_recnika:
                csv_writer.writerow(podaci)
    except OSError as err:
        stderr.write(f"Greška pri upisu podataka u fajl {putanja}\n{err}\n")
```

#### Rad sa direktorijumima - pronalaženje CSV fajlova
```python
from pathlib import Path

def get_csv_files(fpath: Path) -> list:
    """Pronalazi sve CSV fajlove u direktorijumu"""
    if not fpath.is_dir():
        raise RuntimeError("Input argument is not a directory -> cannot proceed")
    
    csv_files = []
    for item in fpath.iterdir():
        if not item.is_dir() and item.suffix == '.csv':
            csv_files.append(item)
    return csv_files

# Korišćenje
directory = Path('/path/to/directory')
csv_files = get_csv_files(directory)
for csv_file in csv_files:
    data = ucitaj_iz_csv_fajla(csv_file)
    # Radi sa podacima...
```

### Napredne tehnike formatiranja stringova

#### F-string formatiranje brojeva
```python
# Zaokruživanje na decimalna mesta
broj = 3.14159
print(f"Pi je približno {broj:.2f}")  # "Pi je približno 3.14"

# Formatiranje sa paddingom
broj = 42
print(f"Broj: {broj:05d}")  # "Broj: 00042" (padding sa nulama)

# Formatiranje postotaka
procenat = 0.85
print(f"Uspešnost: {procenat:.1%}")  # "Uspešnost: 85.0%"

# Formatiranje velikih brojeva
veliki_broj = 1234567
print(f"Broj: {veliki_broj:,}")  # "Broj: 1,234,567"

# Kombinovanje različitih formatiranja
cena = 1234.567
print(f"Cena: ${cena:,.2f}")  # "Cena: $1,234.57"
```

Srećno programiranje! 🐍
