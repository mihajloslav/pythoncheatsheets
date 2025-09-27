from pathlib import Path
from collections import Counter
from sys import stderr

DATA_DIR = Path.cwd().parent / 'data'

def read_lyrics(path : Path) -> str | None:
    try:
        with open(path, "r") as fobj:
            return fobj.read()
    except FileNotFoundError as fnf:
        stderr.write(f"FileNotFoundError:{fnf}\n\n\n")
    except OSError as ose:
        stderr.write(f"OSError:{ose}\n\n\n")


def clean(lyrics: str) -> list:
    lista_reci = lyrics.split()
    #REČENO JE DA NE TREBA ' DA SE BRIŠE
    clean_lista = [rec.replace('!', '').replace('?', '').replace('.', '').replace(',','') for rec in lista_reci]
    return clean_lista

def wordcounter(lista_reci : list) -> tuple:
    reci_dict = dict(Counter(lista_reci))
    reci_dict = dict(sorted(reci_dict.items(), key=lambda x: x[1], reverse=True))


    #NAČIN BEZ COUNTERA
    #from collections import defaultdict
    #reci_dict = defaultdict(int)

    #for rec in lista_reci:
    #   reci_dict[rec] += 1
    #reci_dict = dict(sorted(reci_dict.items(), key=lambda x: x[1], reverse=True))


    brojac = 0
    for k, v in reci_dict.items():
        brojac += 1
        print(f"{k}: ({v})")
        if brojac == 10:
            break
    return list(reci_dict.keys()), list(reci_dict.values())



if __name__ == "__main__":
    print("==========PRVA PESMA==========\n")
    pesma1 : str = read_lyrics(DATA_DIR / "placeholder1.txt")
    if pesma1: #MOŽE I BEZ OVOG IF-a, STAVIO SAM ZBOG SIGURNOSTI AKO READ_LYRICS NE VRATI NIŠTA
        print(f"#####TEKST PESME#####")
        print(pesma1)
        print(f"\n#####CLEAN REČI#####")
        print(clean(pesma1))
        print(f"\n#####TOP 10 REČI#####")
        wordcounter(clean(pesma1))

    print("\n\n\n==========DRUGA PESMA==========\n")
    pesma2 : str = read_lyrics(DATA_DIR / "placeholder2.txt")
    if pesma2:
        print(f"#####TEKST PESME#####")
        print(pesma2)
        print(f"\n#####CLEAN REČI#####")
        print(clean(pesma2))
        print(f"\n#####TOP 10 REČI#####")
        wordcounter(clean(pesma2))

