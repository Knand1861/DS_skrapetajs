# Programmas apraksts

Šī programmas uzdevums ir divu veikalu — **RDElectronics** un **Euronics** — pārlūkošana, lai atrastu vēlamu priekšmetu un tā cenu.  
Programma pati nolasa datus no interneta un ievieto tos Excel failā, augošā secībā (pēc cenas).

---

## Izmantotās bibliotēkas

- `import requests` Ļauj pieprasīt mājaslapai HTML failu, no kura ar
- `from bs4 import BeautifulSoup` var izņemt vajadzīgos datus, iepriekš zinot, kā mājaslapa ir izveidota.
- `import re` Ļauj noņemt nevajadzīgo informāciju, atstājot tikai cenu.
- `from openpyxl import load_workbook, Workbook` Palīdz strādāt ar Excel failu.

---

## Lietošanas norādes

1. **Priekšmeta ievade**  
   Kad programma tiek palaista, ekrānā parādās aicinājums ievadīt meklējamā priekšmeta nosaukumu (piemēram, `RTX 3060`). Ir jāieraksra vajadzīgo preces nosaukumu un nospiest Enter.

2. **Datu meklēšana**  
   Programma automātiski izveidos savienojumu ar RDElectronics un Euronics interneta veikaliem, izvilks html mājaslapas.

3. **Datu apstrāde un kārtošana**  
   Informācija ir izņemta un tiek apvienota vienā sarakstā, kas tiek sakārtots pēc cenas augošā secībā.

4. **Rezultātu saglabāšana**  
   Saraksts tiek saglabāts Excel failā ar nosaukumu `data.xlsx`. Ja fails jau eksistē, tas tiek pārrakstīts.

5. **Excel faila apskate**  
   Kad saglabāšana pabeigta, Excel fails ir jāatver ar savu datorā esošo Excel programmu, lai apskatītu rezultātus.
