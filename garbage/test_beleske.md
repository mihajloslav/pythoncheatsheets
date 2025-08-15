# Python Cheatsheet 🐍

Dobrodošao u Python beleške! Ovaj dokument je stilizovan za lakše učenje i brže snalaženje. Svaka sekcija je jasno odvojena, sa objašnjenjima i primerima. Uživaj! 😃

---


## Osnovni koncepti i pojmovi

- **U Pythonu je sve objekat** 🧱
    - Svaka vrednost u Pythonu (broj, string, lista, funkcija, klasa...) je objekat. To znači da svaki podatak ima svoj tip, atribute i metode. Na primer, možeš pozvati metodu `.upper()` na stringu ili koristiti `.append()` na listi. Ovo omogućava fleksibilan i moćan rad sa podacima.

- **Paket** je folder koji sadrži fajl `__init__.py`.
    - Primer: folder `my_package/` sa fajlom `__init__.py` postaje Python paket i može se importovati. Bez tog fajla, folder nije prepoznat kao paket.
    - Paketi služe za organizaciju koda u veće projekte i omogućavaju hijerarhiju modula.

- **Modul** je Python fajl (npr. `my_module.py`) koji sadrži definicije funkcija i klasa, ali bez izvršnih naredbi.
    - Modul se koristi za organizaciju koda i ponovnu upotrebu. Možeš importovati funkcije iz modula u druge delove projekta.

- **Skripta** je Python fajl koji ima izvršne naredbe i pokreće se direktno.
    - Skripte su često ulazna tačka programa (npr. `main.py`).

- **Stringovi** se mogu definisati sa jednostrukim (`'...'`) ili dvostrukim navodnicima (`"..."`).
    - Nema razlike, koristi se ono što je praktičnije. Na primer, ako string sadrži apostrof, koristi dvostruke navodnike: `"It's Python!"`.

- **Višelinijski stringovi** koriste trostruke navodnike: `"""..."""` ili `'''...'''`.
    - Često se koriste za docstringove (dokumentaciju funkcija/klasa) ili za tekst koji zauzima više redova.

- **Komentari**:
    - Jednolinijski: `# komentar` – koristi se za kratke napomene u kodu.
    - Višelinijski (docstring): `""" komentar """` – koristi se za dokumentaciju funkcija, klasa i modula. Prvi string u funkciji ili klasi automatski postaje njen docstring.
    - Nova ćelija u Jupyteru: `#%%` – omogućava razdvajanje koda na blokove, što je korisno za eksperimentisanje i testiranje u Jupyter okruženju.

---

## Prečice na tastaturi ⌨️

- `CTRL + ALT + ENTER` – izvršava komandu
- `CTRL + /` – komentariše/dekomentariše liniju
- `CTRL + ENTER` – izvršava kod (npr. u Jupyteru)

---


## Struktura Projekta 📁

- `.idea/` – folder sa konfiguracionim fajlovima za razvojno okruženje (npr. PyCharm). Ovaj folder sadrži podešavanja projekta, kao što su verzija Pythona, virtuelna okruženja, i podešavanja za automatsko formatiranje koda. Obično se ne šalje na GitHub osim ako svi članovi tima koriste isto okruženje.
- `blanknotebooks/` – folder za prazne Jupyter beležnice (notebook-ove). Ove beležnice su korisne za eksperimentisanje, testiranje koda, vizualizaciju podataka i vođenje interaktivnih beleški.
- `blankscripts/` – folder za prazne Python skripte. Ove skripte služe kao šabloni za nove zadatke ili projekte. Organizacija skripti po folderima olakšava snalaženje i održavanje većih projekata.

> **Napomena:** Dobra organizacija projekta olakšava timski rad, testiranje i kasnije proširivanje koda. Preporučuje se da svaki veći projekat ima jasno definisanu strukturu foldera.

---


## GitHub Savet

- Da dodaš fajl na GitHub: selektuj fajl, klikni desni klik i izaberi **Add** (ili koristi komandu `git add ime_fajla` u terminalu).
    - Nakon toga, koristi `git commit -m "Poruka"` da sačuvaš promene i `git push` da ih pošalješ na server.
    - Ovaj proces je deo osnovnog Git workflow-a: **Add → Commit → Push**.
    - GitHub omogućava praćenje istorije izmena, rad u timovima i vraćanje na prethodne verzije koda.

---


## Specijalni atributi i promenljive

- `__name__` – Specijalni atribut svakog Python fajla (modula). Ako se fajl pokreće direktno, `__name__` ima vrednost `'__main__'`. Ako se fajl importuje, `__name__` je ime modula. Ovo omogućava da deo koda bude izvršen samo kada se fajl pokreće direktno, a ne pri importovanju.

    ```python
    if __name__ == '__main__':
            print('Ova skripta se pokreće direktno!')
    ```

- `__doc__` – Sadrži docstring (višelinijski komentar) modula, funkcije ili klase. Docstring je tekst koji se nalazi odmah ispod definicije funkcije/klase/modula i služi za automatsku dokumentaciju.

    ```python
    def zbir(a, b):
            """Vraća zbir dva broja."""
            return a + b
    print(zbir.__doc__)  # Ispisuje: Vraća zbir dva broja.
    ```

- `__file__` – Putanja do trenutnog Python fajla na disku. Korisno za rad sa fajlovima i određivanje lokacije skripte.

    ```python
    print(__file__)
    ```

- Funkcije i klase takođe imaju `__doc__` atribut, što omogućava automatsko generisanje dokumentacije i lakše razumevanje koda.

---


## Modul vs Skripta

- **Modul**: Python fajl koji sadrži definicije funkcija, klasa i promenljivih, ali obično nema izvršnih naredbi koje se pokreću pri importovanju. Modul služi za organizaciju i ponovnu upotrebu koda. Možeš importovati funkcije iz modula u druge delove projekta.

    ```python
    # primer_modula.py
    def zbir(a, b):
            return a + b
    ```
    - Importovanje modula:
    ```python
    from primer_modula import zbir
    print(zbir(2, 3))
    ```

- **Skripta**: Python fajl koji ima izvršne naredbe i pokreće se direktno (npr. `python main.py`). Skripte su često ulazna tačka programa i mogu koristiti module.

    ```python
    # main.py
    from primer_modula import zbir
    print(zbir(5, 7))
    ```

> **Napomena:** Svaki Python fajl može biti i modul i skripta, u zavisnosti od toga da li ga pokrećeš direktno ili ga importuješ.

---


## Importovanje i zaštita glavnog bloka

```python
from python.inception import print_ringo
```
- Kada importuješ modul, sve što nije u funkciji ili pod uslovom `if __name__ == '__main__':` biće izvršeno odmah. To znači da će se svaki kod na vrhu fajla pokrenuti i pri importovanju.
- Da bi sprečio neželjeno izvršavanje koda pri importu, koristi zaštitni blok:

```python
if __name__ == '__main__':
    print_ringo()
```
> Ovaj blok se izvršava samo ako se fajl pokreće direktno, a ne kada se importuje kao modul. Ovo je najbolja praksa za pisanje skripti koje mogu biti i modul i samostalni program.

```python
if __name__ == '__main__':
    print_ringo()
```

---


## Funkcija `print`

- `print()` ispisuje podatke na standardni izlaz (obično konzolu).
- Argument `sep` određuje separator između elemenata (podrazumevano je razmak). Na primer:
    ```python
    print('Ringo', 'Starr', sep=' & ')  # Ispisuje: Ringo & Starr
    ```
- Argument `end` određuje šta se dodaje na kraj (podrazumevano je novi red `\n`). Na primer:
    ```python
    print('Hello', end='!')  # Ispisuje: Hello!
    print('World')           # Ispisuje: World (u istom redu)
    ```
- `print` po defaultu dodaje novi red na kraj svakog poziva.
- Možeš ispisivati više tipova podataka odjednom, Python će ih automatski konvertovati u string:
    ```python
    print('Broj:', 5, True)  # Ispisuje: Broj: 5 True
    ```

---


## Funkcija `input`

- `input()` omogućava korisniku da unese podatak sa tastature. Uvek vraća string, pa je često potrebno konvertovati unos u drugi tip (npr. int):
    ```python
    broj = int(input('Unesi broj: '))
    ```
- Može imati prompt: `input('Unesi broj: ')` prikazuje tekst i čeka unos.
- Alternativno:
    ```python
    print('Unesi broj:')
    unos = input()
    ```
- Ako korisnik unese npr. "42", vrednost promenljive će biti string "42". Da bi radio sa brojevima, koristi `int()` ili `float()` za konverziju.

---


## Enumerate

- `enumerate(iterable)` vraća parove (indeks, element) iz bilo koje kolekcije (lista, tuple, string...).
- Koristi se za prolazak kroz kolekciju kada ti treba i indeks i vrednost.

```python
the_beatles = ['John', 'Paul', 'George', 'Ringo']
for i, musician in enumerate(the_beatles):
    print(i, musician)  # Ispisuje: 0 John, 1 Paul, ...
```
- Možeš zadati i početni indeks:
```python
for i, musician in enumerate(the_beatles, start=1):
    print(i, musician)  # Ispisuje: 1 John, 2 Paul, ...
```

---


## Range

- `range(start, stop, step)` generiše niz brojeva od `start` do `stop - 1` (poslednji se ne uključuje), sa zadatim korakom `step` (koji je opcionalan, podrazumevano 1).
- `range(1, 5)` – generiše: 1, 2, 3, 4
- `range(5)` – generiše: 0, 1, 2, 3, 4
- `range(1, n + 1, 2)` – generiše brojeve od 1 do n, preskačući svaki drugi (korak 2)
- `range(10, 0, -1)` – generiše brojeve od 10 do 1 (unazad)
- Najčešće se koristi u for petljama:
    ```python
    for i in range(3):
            print(i)  # Ispisuje: 0, 1, 2
    ```

---


## Divmod

- `divmod(a, b)` vraća tuple (količnik, ostatak) pri celobrojnom deljenju a sa b.
- Korisno kada želiš istovremeno i rezultat deljenja i ostatak:

```python
rezultat, ostatak = divmod(17, 5)
print(rezultat)  # 3
print(ostatak)   # 2
```
- Ekvivalentno je pisanju:
    ```python
    rezultat = 17 // 5
    ostatak = 17 % 5
    ```

---


## Sortiranje

- `sorted(lista)` vraća novu sortiranu listu, ne menja originalnu.
- `sorted(lista, reverse=True)` – sortira opadajuće (od najvećeg ka najmanjem).
- `lista.sort()` menja originalnu listu in-place.
- Možeš sortirati po vrednosti, po ključevi (za rečnike), ili po više kriterijuma koristeći argument `key`:
    ```python
    brojevi = [3, 1, 4, 2]
    print(sorted(brojevi))  # [1, 2, 3, 4]
    print(sorted(brojevi, reverse=True))  # [4, 3, 2, 1]
    brojevi.sort()
    print(brojevi)  # [1, 2, 3, 4]
    ```
- Za sortiranje rečnika po vrednosti:
    ```python
    d = {'a': 3, 'b': 1, 'c': 2}
    print(sorted(d.items(), key=lambda x: x[1]))  # [('b', 1), ('c', 2), ('a', 3)]
    ```

---


## Provera članstva

- `element in kolekcija` – proverava da li je element prisutan u kolekciji (lista, string, tuple, set, dict). Vraća True ili False.
    ```python
    if 'John' in ['John', 'Paul', 'George']:
            print('John je u listi!')
    ```
- `element not in kolekcija` – proverava da li element NIJE prisutan.
    ```python
    if 'Ringo' not in ['John', 'Paul', 'George']:
            print('Ringo nije u listi!')
    ```
- Kod rečnika, `in` proverava da li je ključ prisutan:
    ```python
    d = {'a': 1, 'b': 2}
    print('a' in d)  # True
    print(1 in d)    # False
    ```

---


## Dodavanje i uklanjanje iz liste

- `lista.append(element)` – dodaje element na kraj liste.
    ```python
    brojevi = [1, 2]
    brojevi.append(3)
    print(brojevi)  # [1, 2, 3]
    ```
- `lista.insert(index, element)` – ubacuje element na određenu poziciju.
    ```python
    brojevi.insert(1, 10)
    print(brojevi)  # [1, 10, 2, 3]
    ```
- `lista.remove(element)` – briše prvo pojavljivanje elementa.
    ```python
    brojevi.remove(10)
    print(brojevi)  # [1, 2, 3]
    ```
- `lista.pop()` – uklanja i vraća poslednji element.
    ```python
    poslednji = brojevi.pop()
    print(poslednji)  # 3
    print(brojevi)    # [1, 2]
    ```
- `lista.extend(druga_lista)` – spaja dve liste.
    ```python
    brojevi.extend([4, 5])
    print(brojevi)  # [1, 2, 4, 5]
    ```

---


## Kopiranje liste

- `r = ringo.copy()` – pravi plitku kopiju liste (sve vrednosti se kopiraju, ali ako su elementi objekti, kopira se referenca).
- `r = ringo + []` – takođe pravi novu listu.
- `r = ringo[:]` – kopija korišćenjem slice-a.
> Direktno dodeljivanje (`r = ringo`) kopira referencu, ne pravu listu! Promene na jednoj listi odraziće se i na drugu.

- Za duboku kopiju (kada lista sadrži podliste ili objekte):
    ```python
    import copy
    nova = copy.deepcopy(stara)
    ```

---


## List Comprehension (skraćeno pravljenje lista)

- Omogućava kreiranje nove liste iz postojeće, u jednoj liniji koda. Sintaksa je:
    ```python
    [izraz for element in kolekcija if uslov]
    ```
- Primeri:
    ```python
    # Prva reč svake pesme
    songs = ["Honey Don't", "Eleanor Rigby", "Penny Lane"]
    first_words = [s.split()[0] for s in songs]  # ['Honey', 'Eleanor', 'Penny']

    # Prvo slovo svake reči, spojeno u string
    first_letters = ''.join([w[0] for w in first_words]).capitalize() + '!'
    print(first_letters)  # Hep!

    # Kvadrati parnih brojeva
    kvadrati = [x**2 for x in range(10) if x % 2 == 0]
    print(kvadrati)  # [0, 4, 16, 36, 64]
    ```

---


## Zip

- `zip(l1, l2, ...)` spaja više kolekcija po indeksima u tuple-ove. Koristi se za paralelno iteriranje kroz više kolekcija.

```python
imena = ['John', 'Paul', 'George']
godine = [1940, 1942, 1943]
for ime, godina in zip(imena, godine):
    print(f"{ime} ({godina})")
# John (1940), Paul (1942), George (1943)
```
- Ako su kolekcije različite dužine, zip se zaustavlja na najkraćoj.
- Za "popunjavanje" do najduže koristi `itertools.zip_longest`.

---


## Round

- `round(broj)` – zaokružuje broj na najbliži ceo broj.
    ```python
    print(round(3.2))  # 3
    print(round(3.7))  # 4
    ```
- Možeš zadati i broj decimala: `round(broj, decimale)`
    ```python
    print(round(3.14159, 2))  # 3.14
    ```
- "Round to even" (bankarsko zaokruživanje):
    ```python
    print(round(2.5))  # 2
    print(round(3.5))  # 4
    ```
    - Kada je cifra tačno na pola, Python zaokružuje na najbliži paran broj.

---


## Negativni indeksi

- U Pythonu možeš koristiti negativne indekse za pristupanje elementima s kraja kolekcije.
- `text[-1]` – poslednji element
- `text[-2]` – pretposlednji element
- `text[-(i+1)]` – i-ti element od kraja (npr. za i=0, poslednji)
    ```python
    lista = [10, 20, 30, 40]
    print(lista[-1])  # 40
    print(lista[-2])  # 30
    ```

---


## Funkcija `all` i `any`

- `all(iterable)` – vraća True ako su svi elementi u kolekciji "istiniti" (truthy). Ako je bar jedan False, vraća False.
    ```python
    print(all([True, 1, 'tekst']))  # True
    print(all([True, 0, 'tekst']))  # False (0 je "falsey")
    ```
- `any(iterable)` – vraća True ako je bar jedan element "istinit" (truthy).
    ```python
    print(any([0, '', None, 5]))  # True (5 je "truthy")
    print(any([0, '', None]))     # False
    ```
- Korisno za validaciju podataka ili proveru uslova u listama.

---


## Stringovi – rad, metode i formatiranje

- **C-formatiranje**: `print("Zorane ima %d godina %s" % (a, b))` – stariji stil, koristi se još uvek, ali se preporučuje f-string.
- **f-string**: `print(f"Zoran ima {godine} u {godina}")` – najčešći i najsigurniji način formatiranja.
- **format()**: `print("Zoran ima {} godina u {} godini".format(5, 2025))` – fleksibilan način.
- **Raw string**: `print(r"C:\nobody")` – ignoriše escape sekvence (npr. \n neće biti novi red).
- **Multiline**: `print("""Zoran\nPetar\nIvan""")` – ispisuje više redova.
- **Slicing**: `print("Zoran"[2::])` (od trećeg slova do kraja), `print("Zoran"[::-1])` (unazad).
- **Množenje**: `print("Zoran" * 3)` – ponavlja string.
- **str() vs repr()**: `str('Zoran')` → Zoran, `repr('Zoran')` → 'Zoran' (sa navodnicima).
- **Metode**:
    - `.endswith('rec')` – proverava da li se string završava na 'rec'
    - `.split('rec')` – deli string po separatoru
    - `.center(duzina, 'znak')` – centriranje stringa
    - `.strip('karakter')`, `.lstrip()`, `.rstrip()` – uklanjaju karaktere sa početka/kraja
    - `'rec' in 'String'` – proverava da li string sadrži podstring

---


## Liste – rad, metode i primeri

- **Kreiranje**: `ringo = []` ili `ringo = list()` – prazna lista.
- **Pristup**: `ringo[1]` (drugi element), `ringo[1:3]` (drugi i treći), `ringo[-2:]` (poslednja dva).
- **Prolazak kroz listu**:
    ```python
    for e in ringo:
            print(e)
    ```
- **Brojanje**: `ringo.count('John Lennon')` – broj pojavljivanja elementa.
- **Indeks**: `ringo.index('John Lennon')` – indeks prvog pojavljivanja.
- **Obrtanje**: `ringo.reverse()` – obrće redosled elemenata in-place.
- **Dužina**: `len(ringo)` – broj elemenata u listi.
- **Provera**: `'John Lennon' in ringo` – da li lista sadrži element.
- **Spajanje**: `ringo + ['Paul']` – vraća novu listu.
- **Brisanje**: `del ringo[0]` – briše prvi element.
- **Kopiranje**: `nova = ringo.copy()` – pravi kopiju liste.

---


## Random i liste

- Za generisanje slučajnih brojeva koristi se modul `random`.
- `randint(a, b)` – vraća slučajan ceo broj između a i b (uključivo).
- `seed(vrednost)` – postavlja "seme" generatora, što omogućava da dobijemo istu sekvencu brojeva svaki put (korisno za testiranje).

```python
from random import seed, randint
l = []
seed(3546)  # Uvek ista sekvenca
for i in range(10):
    l.append(randint(1, 100))
print(l)
# Ispisuje istu listu svaki put
```

---


## String strip i rad sa redovima

- `string.strip("\n")` – uklanja nove redove (ili druge zadate karaktere) sa početka i kraja stringa.
    ```python
    tekst = "\nHello, Python!\n"
    print(tekst.strip())  # 'Hello, Python!'
    ```
- `.lstrip()` uklanja karaktere samo sa leve strane, `.rstrip()` sa desne.
- `splitlines()` – deli string po redovima i vraća listu redova.

---


## Tuple (n-torka)

- **Tuple** je nepromenljiva (immutable) kolekcija elemenata. Jednom kreiran, ne možeš menjati njegove elemente.
- **Kreiranje**: `ringo = ('Ringo',)` (zarez je obavezan za tuple sa jednim elementom), ili `ringo = 'Ringo',`.
- **Pristup**: `ringo[0]` – pristup prvom elementu.
- **Raspakivanje**: `john, paul, george, ringo = the_beatles` – dodeljuje svaki element promenljivoj.
- **Pretvaranje u listu**: `list(the_beatles)` – omogućava promenu elemenata.
- Tuple se koristi kada želiš da zaštitiš podatke od promene ili za povratak više vrednosti iz funkcije.

---


## Dictionaires (rečni) – rad sa parovima ključ-vrednost

- **Kreiranje**: `ringo = {'name': 'Ringo Starr', 'year': 1940}` – rečnik sa dva para.
- **Pristup**: `ringo['name']` – pristup vrednosti po ključu.
- **Iteracija**:
    ```python
    for k, v in ringo.items():
            print(f"{k}: {v}")
    ```
- **Dodavanje**: `ringo['city'] = 'Liverpool'` – dodaje novi par.
- **Brisanje**: `del ringo['city']` – briše par po ključu.
- **Ključevi**: `ringo.keys()` – vraća sve ključeve.
- **Vrednosti**: `ringo.values()` – vraća sve vrednosti.
- **Sortiranje**:
    - Po ključu: `dict(sorted(d.items(), key=lambda x: x[0]))`
    - Po vrednosti: `dict(sorted(d.items(), key=lambda x: x[1]))`
- **Dictionary comprehension**: `{k: v for k, v in zip(l1, l2)}` – pravljenje rečnika iz dve liste.
- **defaultdict**: automatski inicijalizuje vrednosti za nove ključeve (npr. prazna lista ili nula):
    ```python
    from collections import defaultdict
    d = defaultdict(list)
    d['key'].append('vrednost')
    ```

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
