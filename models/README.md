# models/

Esta carpeta está reservada para los artefactos serializados del proyecto.

## Archivos esperados
- `model_pipeline.joblib`
- `threshold.json`
- opcional:
  - `kmeans.joblib`
  - `cluster_metadata.csv`
  - `spotify_catalog.csv`

## Ejemplo de exportación desde notebook
```python
import os
import json
import joblib

os.makedirs("models", exist_ok=True)

joblib.dump(model_pipeline, "models/model_pipeline.joblib")

with open("models/threshold.json", "w", encoding="utf-8") as f:
    json.dump({"threshold": 0.60}, f)
```
