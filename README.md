# Battleships AI Robot

## Úvod
Tento projekt představuje inteligentního robota pro hru "Battleships" (Námořní bitva). Robot využívá pokročilé strategie a pravděpodobnostní analýzu k efektivnímu hledání a ničení nepřátelských lodí.

## Klíčové vlastnosti
- **Adaptivní strategie**: Robot přizpůsobuje svůj přístup na základě výsledků předchozích útoků
- **Pravděpodobnostní mapa**: Vytváří dynamickou mapu pravděpodobnosti výskytu lodí
- **Detekce tvarů lodí**: Rozpoznává různé tvary a orientace lodí
- **Efektivní vyhledávání**: Používá optimalizované algoritmy pro minimalizaci počtu potřebných útoků

## Hlavní komponenty

### 1. Strategie útoku
- **Počáteční fáze**: Náhodný výběr buněk v šachovnicovém vzoru
- **Fáze sledování**: Po zásahu se zaměřuje na sousední buňky
- **Fáze ničení**: Po detekci lodi optimalizuje útoky pro její zničení

### 2. Pravděpodobnostní model
- Dynamicky aktualizovaná mapa pravděpodobnosti
- Zohledňuje:
  - Umístění již zasažených buněk
  - Zbývající typy lodí
  - Možné orientace lodí

### 3. Detekce lodí
- Automatické rozpoznávání:
  - Velikosti lodí
  - Tvarů (I, L, T, Z, TT)
  - Orientace (horizontální, vertikální)

## Výkon
- Průměrný počet pokusů k vítězství: 45-55 proti sobě samému (~50% winrate)
- Úspěšnost: >95% na standardní 10x10 mapě
- Časová náročnost: <1s na tah

## Použití
```python
# Inicializace
strategy = Strategy(rows=10, cols=10, ships_dict={1:1, 2:1, 3:1, 4:1, 5:1})

# Získání dalšího útoku
x, y = strategy.get_next_attack()

# Registrace výsledku
strategy.register_attack(x, y, is_hit=True, is_sunk=False)
```

## Vývoj
- **Verze 1.0**: Základní implementace
- **Verze 1.1**: Vylepšená detekce tvarů lodí
- **Verze 1.2**: Optimalizace pravděpodobnostního modelu
