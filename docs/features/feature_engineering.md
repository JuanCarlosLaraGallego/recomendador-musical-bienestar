# Feature Engineering

## Visión General

Se transformaron las variables originales en features útiles para el modelo.

---

## 1. Transformaciones Numéricas

Ejemplos:
- `bpm_clean`
- `mental_health_score` (media de variables mentales)

---

## 2. Variables Derivadas

- `high_anxiety_flag`
- `listener_intensity`
- `genre_score_total`
- `genre_diversity`
- `is_musician`

---

## 3. Codificación

### Variables categóricas

- Binarias → 0/1
- One-hot encoding:
  - `fav_genre_*`

---

## 4. Frecuencia de Géneros

Escala ordinal:

| Valor | Codificación |
|------|-------------|
| Never | 0 |
| Rarely | 1 |
| Sometimes | 2 |
| Frequently | 3 |
| Very frequently | 4 |

---

## 5. Consistencia con el Modelo

Las features se alinean con el pipeline entrenado para garantizar:
- coherencia
- compatibilidad en inferencia