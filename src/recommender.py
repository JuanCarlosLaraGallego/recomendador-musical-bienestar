from pathlib import Path
from typing import Optional

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT_DIR / "models" / "spotify_catalog.csv"

GENRE_MAPPING = {
    "Classical": None,
    "Country": "pop",
    "EDM": "edm",
    "Folk": "pop",
    "Gospel": "r&b",
    "Hip hop": "rap",
    "Jazz": "r&b",
    "K pop": "pop",
    "Latin": "latin",
    "Lofi": "pop",
    "Metal": "rock",
    "Pop": "pop",
    "R&B": "r&b",
    "Rap": "rap",
    "Rock": "rock",
    "Video game music": "pop",
}

REQUIRED_COLUMNS = [
    "track_name",
    "track_artist",
    "playlist_genre",
    "track_popularity",
]


def load_catalog(catalog_path: Path = CATALOG_PATH) -> pd.DataFrame:
    """
    Carga el catálogo Spotify limpio desde CSV.
    """
    if not catalog_path.exists():
        raise FileNotFoundError(f"No se encontró el catálogo: {catalog_path}")

    df = pd.read_csv(catalog_path)

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Faltan columnas requeridas en el catálogo: {missing_cols}"
        )

    return df


def map_user_genre_to_spotify(fav_genre: str) -> Optional[str]:
    """
    Mapea el género favorito del formulario a una categoría disponible
    en playlist_genre del catálogo Spotify.
    """
    return GENRE_MAPPING.get(fav_genre)


def recommend_songs(
    fav_genre: str,
    top_n: int = 10,
    catalog_path: Path = CATALOG_PATH,
) -> pd.DataFrame:
    """
    Devuelve recomendaciones top-N filtradas por género Spotify
    y ordenadas por popularidad descendente.
    """
    spotify_genre = map_user_genre_to_spotify(fav_genre)

    if spotify_genre is None:
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    df = load_catalog(catalog_path).copy()

    df["track_popularity"] = pd.to_numeric(df["track_popularity"], errors="coerce")
    df = df.dropna(subset=["track_name", "track_artist", "playlist_genre", "track_popularity"])

    filtered = df[df["playlist_genre"].str.lower() == spotify_genre.lower()].copy()

    if filtered.empty:
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    # Evita repetir la misma canción/artista demasiadas veces
    filtered = filtered.sort_values(
        by="track_popularity",
        ascending=False
    ).drop_duplicates(
        subset=["track_name", "track_artist"]
    )

    recommendations = filtered[REQUIRED_COLUMNS].head(top_n).reset_index(drop=True)
    return recommendations