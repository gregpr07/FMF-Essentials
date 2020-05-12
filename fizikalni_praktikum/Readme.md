# Kako uporabljati kodo

### Tabela negotovosti.py

Glede na local `.py` file

```
from negotovost import Negotovost

data = [
        ('alpha', 3.293, 0.001),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.05, 0.001),
        ('g', 9.81066, 0),
    ]

function = 'm*(rg*g-rg^2*alpha)/alpha'
```

`data` more imeti vsak element, ki ga uporabimo v funkciji. Lahko pisemo latex styling za variable (recimo `alpha` bo narisan kot grska crka)

`function` je string, napisan kot standardna funkcija, v python formatu, lahko pa tudi uporabljamo funkcije, kot so napisane [tukaj](https://docs.sympy.org/latest/tutorial/basic_operations.html#converting-strings-to-sympy-expressions)

##### Output

`floating_points` poljubno

`function` formatiran v latexu

```
Negotovost(data,function,floating_points=3).format_text()
```

Izracunamo napako

```
Negotovost(data,function).calculate_error()
```

Narise tabelo. Poljubni parametri.

`varible` ima lahko latex format.

```
Negotovost(data,function).draw_table(self, variable='v', text_size=15, title='', units="", display_img=False)
```
