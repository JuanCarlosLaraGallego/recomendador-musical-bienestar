import pandas as pd

FREQUENCY_COLUMNS = [
    "frequency_classical",
    "frequency_country",
    "frequency_edm",
    "frequency_folk",
    "frequency_gospel",
    "frequency_hip_hop",
    "frequency_jazz",
    "frequency_k_pop",
    "frequency_latin",
    "frequency_lofi",
    "frequency_metal",
    "frequency_pop",
    "frequency_r&b",
    "frequency_rap",
    "frequency_rock",
    "frequency_video_game_music",
]

FAV_GENRE_DUMMIES = [
    "Classical",
    "Country",
    "EDM",
    "Folk",
    "Gospel",
    "Hip hop",
    "Jazz",
    "K pop",
    "Latin",
    "Lofi",
    "Metal",
    "Pop",
    "R&B",
    "Rap",
    "Rock",
    "Video game music",
]

YES_NO_MAP = {
    "yes": 1, "no": 0,
    "si": 1, "sí": 1,
    True: 1, False: 0,
    1: 1, 0: 0
}

FREQ_MAP = {
    "never": 0,
    "rarely": 1,
    "sometimes": 2,
    "frequently": 3,
    "very frequently": 4,
}

def encode_listener_intensity(hours: float) -> int:
    if hours < 2:
        return 0
    if hours < 5:
        return 1
    return 2

def build_input_dataframe(payload: dict) -> pd.DataFrame:
    df = pd.DataFrame([payload]).copy()

    binary_cols = [
        "while_working",
        "instrumentalist",
        "composer",
        "exploratory",
        "foreign_languages",
    ]
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map(YES_NO_MAP)

    for col in FREQUENCY_COLUMNS:
        if col in df.columns:
            df[col] = df[col].map(FREQ_MAP)

    numeric_cols = [
        "age",
        "hours_per_day",
        "bpm",
        "anxiety",
        "depression",
        "insomnia",
        "ocd",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["bpm_clean"] = df["bpm"].clip(lower=40, upper=220)
    df["mental_health_score"] = df[["anxiety", "depression", "insomnia", "ocd"]].mean(axis=1)
    df["high_anxiety_flag"] = (df["anxiety"] >= 7).astype(int)
    df["listener_intensity"] = df["hours_per_day"].apply(encode_listener_intensity)
    df["genre_score_total"] = df[FREQUENCY_COLUMNS].sum(axis=1)
    df["genre_diversity"] = (df[FREQUENCY_COLUMNS] >= 2).sum(axis=1)
    df["is_musician"] = (((df["instrumentalist"] == 1) | (df["composer"] == 1))).astype(int)
    for genre in FAV_GENRE_DUMMIES:
        col_name = f"fav_genre_{genre}"
        df[col_name] = (df["fav_genre"] == genre).astype(int)
    return df

def get_frequency_columns() -> list[str]:
    return FREQUENCY_COLUMNS.copy()
