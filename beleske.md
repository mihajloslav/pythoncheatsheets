# Python Cheatsheet 🐍

Dobrodošao u Python beleške! Ovaj dokument je stilizovan za lakše učenje i brže snalaženje. Svaka sekcija je jasno odvojena, sa objašnjenjima i primerima. Uživaj! 😃

---

## Osnovni Pojmovi

- **U Pythonu je sve objekat** 🧱
- **Paket** je folder koji sadrži `__init__.py` fajl (npr. folder `python` sa `__init__.py`).
- Stringovi mogu biti napisani sa `'` ili `"` (nema razlike).
- Komentari:
  - Jednolinijski: `# komentar`
  - Višelinijski (docstring): `""" komentar """`
  - Nova ćelija u Jupyteru: `#%%`

---

## Prečice na tastaturi ⌨️

- `CTRL + ALT + ENTER` – izvršava komandu
- `CTRL + /` – komentariše/dekomentariše liniju
- `CTRL + ENTER` – izvršava kod (npr. u Jupyteru)

---

## Struktura Projekta 📁

- `.idea/` – konfiguracija okruženja (PyCharm)
- `blanknotebooks/` – prazni notebook-ovi
- `blankscripts/` – prazne skripte

---

## GitHub Savet

- Da dodaš fajl na GitHub: selektuj, desni klik, pa **Add**.

---

## Specijalne promenljive

- `__name__` – ime skripte ili `'__main__'` ako se direktno izvršava
- `__doc__` – dokumentacija (docstring)
- `__file__` – putanja do fajla
- Funkcije imaju `__doc__` (npr. `print(print_ringo.__doc__)`)

---

## Modul vs Skripta

- **Modul**: fajl sa funkcijama/klasama, bez izvršnih naredbi
- **Skripta**: fajl sa izvršnim naredbama

---

## Importovanje

```python
from python.inception import print_ringo
```
- Ako u importovanom fajlu postoji poziv funkcije, on će se izvršiti.
- Da se kod ne izvršava pri importu, koristi:

```python
if __name__ == '__main__':
    print_ringo()
```

---

## Funkcija `print`

- Argumenti: `sep`, `end`
- Primer: `print('Ringo Starr', 'John Lennon', sep=' & ')`
- `print` po defaultu dodaje `\n` na kraj

---

## Funkcija `input`

- Može imati prompt: `input('Unesi broj: ')`
- Ili:
  ```python
  print('Unesi broj:')
  input()
  ```

---

## Enumerate

- Vraća (indeks, element) iz liste:

```python
for i, musician in enumerate(the_beatles):
    print(i + 1, musician)
```

---

## Range

- `range(1, 5)` – od 1 do 4
- `range(5)` – od 0 do 4
- `range(1, n + 1, 1)` – treći argument je korak

---

## Divmod

- Vraća količnik i ostatak:

```python
result, remainder = divmod(num, 2)
```

---

## Sortiranje

- `sorted(lista)` – vraća novu sortiranu listu
- `sorted(lista, reverse=True)` – opadajuće sortiranje

---

## Provera članstva

- `element not in lista` – nije u listi
- `element in lista` – jeste u listi

---

## Dodavanje u listu

- `lista.append(element)` – dodaje na kraj
- `lista.insert(index, element)` – ubacuje na poziciju
- `lista.remove(element)` – briše element
- `lista.pop()` – izbacuje poslednji
- `lista.extend(druga_lista)` – spaja dve liste

---

## Kopiranje liste

- `r = ringo.copy()`
- `r = ringo + []`
- `r = ringo[:]`

> Direktno dodeljivanje (`r = ringo`) kopira referencu, ne pravu listu! ⚠️

---

## List Comprehension

```python
first_words = [s.split()[0] for s in songs]
first_letters = ''.join([w[0] for w in first_words]).capitalize() + '!'
```

---

## Zip

- Spaja više listi po indeksima:

```python
for i, j in zip(l1, l2):
    print(i, j)
```

---

## Round

- `round(broj)` – zaokružuje na najbliži ceo broj
- "Round to even": 3.5 → 4

---

## Negativni indeksi

- `text[-1]` – poslednji element
- `text[-(i+1)]` – i-ti od kraja

---

## Funkcija `all` i `any`

- `all(lista)` – True ako su svi elementi True
- `any(lista)` – True ako je bar jedan element True

---

## Stringovi

- C-formatiranje: `print("Zorane ima %d godina %s" % (a, b))`
- Raw string: `print(r"C:\nobody")`
- Multiline: `print("""Zoran\nPetar\nIvan""")`
- Slicing: `print("Zoran"[2::])`, `print("Zoran"[::-1])`
- Množenje: `print("Zoran" * 3)`
- `str()` vs `repr()`: `str('Zoran')` → Zoran, `repr('Zoran')` → 'Zoran'
- Fancy formatiranje: `print(f"Zoran ima {godine} u {godina}")`
- Metode: `.endswith()`, `.split()`, `.center()`, `.strip()`, `.lstrip()`, `.rstrip()`, `'rec' in 'String'`

---

## Liste

- Kreiranje: `ringo = []` ili `ringo = list()`
- Pristup: `ringo[1]`, `ringo[1:3]`, `ringo[-2:]`
- Prolazak kroz listu:

```python
for e in ringo:
    print(e)
```
- Brojanje: `ringo.count('John Lennon')`
- Indeks: `ringo.index('John Lennon')`
- Obrtanje: `ringo.reverse()`
- Dužina: `len(ringo)`
- Provera: `'John Lennon' in ringo`

---

## Random i liste

```python
from random import seed, randint
l = []
seed(3546)
for i in range(10):
    l.append(randint(1, 100))
print(l)
```

- `randint` – slučajan broj
- `seed` – za ponovljivost

---

## String strip

- `string.strip("\n")` – uklanja nove redove

---

## Tuple (n-torka)

- Ne može se menjati nakon kreiranja
- Kreiranje: `ringo = ('Ringo',)` (zarez je bitan!)
- Raspakivanje: `john, paul, george, ringo = the_beatles`
- Pretvaranje u listu: `list(the_beatles)`

---

## Dictionaires (rečni)

- Kreiranje: `ringo = {'name': 'Ringo Starr', 'year': 1940}`
- Pristup: `ringo['name']`
- Iteracija:

```python
for k, v in ringo.items():
    print(f"{k}: {v}")
```
- Dodavanje: `ringo['city'] = 'Liverpool'`
- Brisanje: `del ringo['city']`
- Ključevi: `ringo.keys()`
- Vrednosti: `ringo.values()`
- Sortiranje:
  - `dict(sorted(d.items(), key=lambda x: x[0]))` – po ključu
  - `dict(sorted(d.items(), key=lambda x: x[1]))` – po vrednosti
- Dictionary comprehension: `{k: v for k, v in zip(l1, l2)}`

---

## Sets (skupovi)

- Nema duplikata
- Kreiranje: `the_beatles = {'John', 'Paul', 'George', 'Ringo'}`
- Dodavanje: `the_beatles.add('Ringo')`
- Uklanjanje: `the_beatles.remove('Ringo')`
- Operacije: presek `&`, unija `|`, razlika `-`, xor `^`
- Pretvaranje liste u skup: `list(set(the_beatles))`

---

## DefaultDict

```python
from collections import defaultdict
d = defaultdict(int)
d = defaultdict(list)
d[i].append("aaa")
```

---

## Statistika

- Suma: `sum(range(1, n+1))`
- Prosek: `from statistics import mean`
- Maksimum: `max(lista, key=lambda x: x['score'])`
- Sortiranje po više kriterijuma: `sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)`
- Counter: `from collections import Counter`

---

## Funkcije

- Anotacije: `print(funkcija.__annotations__)`
- Default argumenti: `def funkcija(title, author="Ringo", year:int=1968)`
- Fleksibilni argumenti: `def funkcija(band, *members)`
- Keyword argumenti: `def funkcija(band, *members, is_active=True, **details)`
- Prioritet: pozicioni → fleksibilni → named → keyword
- Funkcija kao argument: `def g(h, *args): return h(*args)`
- Povratak funkcije iz funkcije (closure):

```python
def return_func(full_name, first_name_flag):
    def first(): return full_name.split()[0]
    def last(): return full_name.split()[1]
    return first if first_name_flag else last
```

---

## Dekoratori

- Dekorator je funkcija koja menja ponašanje druge funkcije
- Osnovni primer:

```python
def simple_decorator(f):
    def wrap(*args):
        print('-------')
        v = f(*args)
        print('-------')
        return v
    return wrap
```

- Korišćenje:

```python
@simple_decorator
def songs(*args):
    print(', '.join(args))
```

- `functools.wraps` čuva identitet funkcije:

```python
import functools
@functools.wraps(f_to_decorate)
def wrapper(*args, **kwargs): ...
```

---

## Klase

- Konstruktor: `__init__()`
- String prikaz: `__str__()`
- Poređenje: `__eq__(self, other)`
- Privatna polja: `__name` (pristup: `obj._Klasa__name`)
- Getter/setter: `@property`, `@ime.setter`
- Dodavanje atributa: `obj.new_attr = vrednost` ili `setattr(obj, 'new_attr', vrednost)`
- Alternativni konstruktor: `@classmethod`
- Staticka metoda: `@staticmethod`
- Iteratori: `__iter__`, `__next__`

---

## Nasleđivanje

- Višestruko nasleđivanje je moguće
- Redosled pretrage metoda: `__mro__`
- `super()` poziva metodu iz nadklase

---

## Izuzeci (Exceptions)

- Osnovna struktura:

```python
try:
    ...
except Exception as e:
    print(e)
else:
    print('Nema greške!')
finally:
    print('Ovo se uvek izvršava.')
```

- Kreiranje izuzetka:

```python
class BandError(Exception): pass
class BandNameError(BandError):
    def __init__(self, name):
        super().__init__(f'Invalid band name: {name}')
```

- Podizanje izuzetka: `raise BandNameError(self.name)`

---

## Rad sa fajlovima

- Putanje:
  - `Path.home()` – home direktorijum
  - `Path.cwd()` – trenutni direktorijum
  - `.parent` – roditeljski direktorijum
- Kreiranje direktorijuma:

```python
from pathlib import Path
new_dir = Path.cwd() / 'new_dir'
new_dir.mkdir(parents=True, exist_ok=True)
```

- Provera postojanja: `new_dir.exists()`
- Brisanje: `new_dir.rmdir()` (mora biti prazan)

---

## Upis i čitanje fajlova

- Upis:

```python
with open(filename, 'w') as outfile:
    outfile.write('neki tekst')
```

- Čitanje:

```python
with open(filename, 'r') as infile:
    lines = infile.readlines()
```

---

## Serijalizacija

- Binarno: `import pickle`
- Upis: `pickle.dump(obj, outfile)`
- Čitanje: `obj = pickle.load(infile)`

- JSON:

```python
from json_tricks import loads, dumps
json_objekat = dumps(objekat, indent=2)
for i in loads(json_objekat):
    ...
```

---

## Dodatni saveti i trikovi 😎

- `None`, `[]`, `''`, `0` su "falsey" vrednosti
- Nebitan brojač u petlji: `for _ in range(5): ...`
- `a == b` poredi vrednosti, `a is b` poredi reference
- `x ** 2` – stepenovanje
- `not guess_str.isdigit()` – provera da li string NIJE broj
- `import` može biti i unutar funkcije
- `print(john, paul, sep=', ')` ili `print(', '.join(the_beatles))`
- Enumeracije: `from enum import Enum`

---

Srećno u učenju Pythona! 🚀
