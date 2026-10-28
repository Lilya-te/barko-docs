"""Unify Bohland / Serpell CSVs into one C-BARQ mini-42 session table.

One row = one questionnaire fill. Full (~100) instruments are projected onto
the 42 short items (see QUESTS/c-barq-short-full-mapping.md) and flagged
``instrument='full_mapped'``. Native mini stays ``instrument='mini'``.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "datasets"
SERPELL_DIR = DATA_DIR / "Attachments_serpell@vet.upenn.edu_2026-09-29_22-07-31"
BOHLAND_DIR = DATA_DIR / "journal.pone.0289356"
OUT_DIR = DATA_DIR / "unified"

LB_TO_KG = 0.45359237

# short item -> full item numbers. Multiple full items are merged with max.
SHORT_FROM_FULL: dict[int, list[int]] = {
    1: [66],
    2: [67],
    3: [10],
    4: [13],
    5: [17],
    6: [18],
    7: [19],
    8: [23, 24],
    9: [20],
    10: [29],
    11: [34],
    12: [35],
    13: [36],
    14: [38],
    15: [40],
    16: [42],
    17: [45],
    18: [47],
    19: [54],
    20: [49],
    21: [50],
    22: [57],
    23: [58, 59],
    24: [61],
    25: [70],
    26: [71],
    27: [2],
    28: [3],
    29: [7],
    30: [76],
    31: [77],
    32: [78],
    33: [81],
    34: [86],
    35: [87],
    36: [89],
    37: [90],
    38: [91],
    39: [92],
    40: [93],
    41: [96],
    42: [98],
}

Q_COLS = [f"q{i:02d}" for i in range(1, 43)]

META_COLS = [
    "session_id",
    "dog_id",
    "source",
    "instrument",
    "is_mapped",
    "wave",
    "survey_date",
    "adopted_date",
    "age_months",
    "sex",
    "neutered",
    "weight_kg",
    "breed",
    "shelter",
    "raw_dog_id",
    "notes",
    "n_answered",
]

SCHEMA_COLS = META_COLS[:8] + ["days_at_home", "age_months", "sex", "neutered", "weight_kg", "breed"] + Q_COLS + [
    "n_answered",
    "shelter",
    "raw_dog_id",
    "notes",
]

# Mini C-BARQ item order as stored in Bohland S4 (wave 0, no suffix).
BOHLAND_Q_BASES = [
    "Just before being taken for a walk:",
    "Just before being taken on a car trip:",
    "When approached directly by an unfamiliar person while being walked/exercised on a leash:",
    "When toys, bones or other objects are taken away by a household member:",
    "When approached directly by a household member while s/he (the dog) is eating:",
    "When mailmen or other delivery workers approach your home:",
    "When his/her food is taken away by a household member:",
    "When approached directly by an unfamiliar dog while being walked/exercised on a leash:",
    "When strangers walk past your home when your dog is outside or in the yard:",
    "When barked, growled, or lunged at by another (unfamiliar) dog:",
    "When approached while eating by another (familiar) household dog (leave blank if no other dogs):",
    "When approached while playing with/chewing a favorite toy, bone, object, etc., by another (familiar) household dog (leave blank if no other dogs):",
    "When approached directly by an unfamiliar person while away from your home:",
    "In response to sudden or loud noises (e.g. thunder, vacuum cleaner, car backfire, road drills, objects being dropped, etc.):",
    "When an unfamiliar person tries to touch or pet the dog:",
    "In response to strange or unfamiliar objects on or near the sidewalk (e.g. plastic trash bags, leaves, litter, flags flapping, etc.",
    "When approached directly by an unfamiliar dog",
    "When first exposed to unfamiliar situations (e.g. first car trip, first time in elevator, first visit to veterinarian, etc.)",
    "When barked, growled, or lunged at by an unfamiliar dog:",
    "When having nails clipped by a household member:",
    "When groomed or bathed by a household member:",
    "Restlessness/agitation/pacing:",
    "Barking or whining:",
    "Chewing/scratching at doors, floor, windows, curtains, etc:",
    "Tends to follow you (or other members of the household) about the house, from room to room:",
    "Tends to sit close to, or in contact with, you (or others) when you are sitting down:",
    "Obeys a 'sit' command immediately:",
    "Obeys a 'stay' command immediately:",
    "Easily distracted by interesting sights, sounds or smells:",
    "Chases or would chase birds, given the chance:",
    "Chases or would chase squirrels, rabbits, etc., given the chance:",
    "Escapes or would escape from home or yard, given the chance:",
    "Chews inappropriate objects:",
    "Pulls excessively hard when on the leash:",
    "Urinates against objects/ furnishings in your home:",
    "Urinates when left alone at night, or during the daytime:",
    "Defecates when left alone at night, or during the daytime:",
    "Hyperactive, restless, has trouble settling down:",
    "Playful, puppyish, boisterous:",
    "Active, energetic, always on the go:",
    "Chases own tail/hind end:",
    "Barks persistently when alarmed or excited:",
]

# event, column suffix, wave label, survey-date column
BOHLAND_WAVES = [
    ("10 days after adoption", "", "d7", "Date/Time Completed:"),
    ("30 days after adoption", ".1", "d30", "Date/Time Completed:.1"),
    ("3 months after adoption", ".2", "d90", "Date/Time Completed:.2"),
    ("6 months after adoption", ".3", "d180", "Date/Time Completed:.3"),
]

FREQ = {
    "never": 0.0,
    "seldom": 1.0,
    "sometimes": 2.0,
    "usually": 3.0,
    "always": 4.0,
    "нет, никогда": 0.0,
    "редко": 1.0,
    "иногда": 2.0,
    "обычно": 3.0,
    "всегда": 4.0,
}

RU_MONTHS = [
    ("янв", 1),
    ("фев", 2),
    ("мар", 3),
    ("апр", 4),
    ("мая", 5),
    ("май", 5),
    ("июн", 6),
    ("июл", 7),
    ("авг", 8),
    ("сен", 9),
    ("окт", 10),
    ("ноя", 11),
    ("дек", 12),
]

FULL_COL_RE = re.compile(
    r"^(?:tra|agg|fear|sep|exc|att|mis|attach|excit|train|misc)(\d+)$",
    re.IGNORECASE,
)
MINI_COL_RE = re.compile(r"^(?:exc|agg|fear|sep|att|tra|mis)(\d+)$", re.IGNORECASE)
POST_STEM_RE = re.compile(
    r"^(?:excit|agg|fear|sep|attach|train|misc)(\d+)_s(\d+)$",
    re.IGNORECASE,
)

MAPPED_NOTE = "full→mini; q08=max(full 23,24); q23=max(full 58,59)"
ONLINE_NOTE = (
    MAPPED_NOTE
    + "; source file already reverses full items 5–7; q29=full 7 is stored reversed"
)
BOHLAND_NOTE = "weight assumed lb→kg; age years→months; 10-day wave labeled d7"


def load_csv(path: Path, **kwargs) -> pd.DataFrame:
    """Load a CSV that may be ';' (Excel) or ',' separated."""
    header = kwargs.pop("header", "infer")
    for sep in (";", ","):
        try:
            df = pd.read_csv(
                path,
                sep=sep,
                encoding="utf-8",
                engine="python",
                on_bad_lines="warn",
                header=header,
            )
        except UnicodeDecodeError:
            df = pd.read_csv(
                path,
                sep=sep,
                encoding="latin1",
                engine="python",
                on_bad_lines="warn",
                header=header,
            )
        if df.shape[1] == 1 and (";" in str(df.columns[0]) or "," in str(df.columns[0])):
            continue
        return df
    raise ValueError(f"Could not parse CSV: {path}")


def _blank(value) -> bool:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return True
    text = str(value).strip()
    return text in {"", ".", "nan", "None", "NA", "N/A", "na", "-"}


def to_float(value) -> float | None:
    if _blank(value):
        return None
    text = str(value).strip().replace(",", ".")
    text = text.split("=")[0].strip()
    try:
        return float(text)
    except ValueError:
        return None


def parse_score(value) -> float | None:
    if _blank(value):
        return None
    text = str(value).strip()
    key = text.lower()
    if key in FREQ:
        return FREQ[key]
    number = to_float(text)
    if number is None:
        return None
    if 0 <= number <= 4:
        return float(number)
    return None


def parse_sex(value) -> str | None:
    if _blank(value):
        return None
    key = str(value).strip().lower()
    if key in {"m", "male", "мальчик"}:
        return "male"
    if key in {"f", "female", "девочка"}:
        return "female"
    return None


def parse_bool(value) -> bool | None:
    if _blank(value):
        return None
    key = str(value).strip().lower()
    if key in {"yes", "y", "true", "1", "да", "sterilized", "neutered", "spayed"}:
        return True
    if key in {"no", "n", "false", "0", "нет", "intact"}:
        return False
    return None


def parse_date(value) -> pd.Timestamp | None:
    if _blank(value):
        return None
    text = str(value).strip()
    match = re.match(r"(\d{1,2})-([A-Za-zА-Яа-яё.]+)-(\d{2,4})", text)
    if match:
        day = int(match.group(1))
        token = match.group(2).lower().strip(".")
        year = int(match.group(3))
        month = next((num for prefix, num in RU_MONTHS if token.startswith(prefix)), None)
        if month is not None:
            if year < 100:
                year += 2000 if year < 30 else 1900
            return pd.Timestamp(year=year, month=month, day=day)
    parsed = pd.to_datetime(text, errors="coerce", dayfirst=False)
    if pd.isna(parsed):
        return None
    return pd.Timestamp(parsed).normalize()


def age_from_parts(months, years) -> float | None:
    month_value = to_float(months)
    year_value = to_float(years)
    if month_value is not None and month_value > 0:
        return month_value
    if year_value is not None and year_value >= 0:
        return year_value * 12
    if month_value is not None:
        return month_value
    return None


def pounds_to_kg(value) -> float | None:
    number = to_float(value)
    if number is None:
        return None
    return round(number * LB_TO_KG, 3)


def norm_id(value) -> str | None:
    if _blank(value):
        return None
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    if text in {"0"}:
        return None
    return text


def col_lookup(columns: list[str], *candidates: str) -> str | None:
    lowered = {str(c).strip().lower(): c for c in columns}
    for name in candidates:
        hit = lowered.get(name.strip().lower())
        if hit is not None:
            return hit
    return None


def empty_record() -> dict:
    row = {col: None for col in SCHEMA_COLS}
    row["is_mapped"] = False
    row["n_answered"] = 0
    return row


def finalize(rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=SCHEMA_COLS)
    frame = pd.DataFrame(rows)
    for col in Q_COLS:
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    frame["n_answered"] = frame[Q_COLS].notna().sum(axis=1).astype(int)
    frame = frame.loc[frame["n_answered"] > 0].copy()
    frame["survey_date"] = pd.to_datetime(frame["survey_date"], errors="coerce")
    frame["adopted_date"] = pd.to_datetime(frame["adopted_date"], errors="coerce")
    days = (frame["survey_date"] - frame["adopted_date"]).dt.days
    frame["days_at_home"] = days.where(days >= 0)
    frame["age_months"] = pd.to_numeric(frame["age_months"], errors="coerce")
    frame["weight_kg"] = pd.to_numeric(frame["weight_kg"], errors="coerce")
    frame["is_mapped"] = frame["is_mapped"].astype(bool)
    frame["wave"] = frame["wave"].where(frame["wave"].notna(), None)
    wave_token = frame["wave"].fillna("na").astype(str)
    frame["session_id"] = frame["source"].astype(str) + ":" + frame["dog_id"].astype(str) + ":" + wave_token
    # disambiguate rare collisions
    dup = frame["session_id"].duplicated(keep=False)
    if dup.any():
        frame.loc[dup, "session_id"] = frame.loc[dup, "session_id"] + "#" + frame.loc[dup].groupby("session_id").cumcount().astype(str)
    return frame[SCHEMA_COLS].reset_index(drop=True)


def project_full_scores(scores: dict[int, float | None]) -> dict[str, float | None]:
    projected: dict[str, float | None] = {}
    for short, full_items in SHORT_FROM_FULL.items():
        values = [scores.get(item) for item in full_items]
        present = [value for value in values if value is not None]
        projected[f"q{short:02d}"] = max(present) if present else None
    return projected


def full_scores_from_row(row: pd.Series) -> dict[int, float | None]:
    scores: dict[int, float | None] = {}
    for column, value in row.items():
        match = FULL_COL_RE.match(str(column).strip())
        if not match:
            continue
        scores[int(match.group(1))] = parse_score(value)
    return scores


def mini_scores_from_numbered(row: pd.Series) -> dict[str, float | None]:
    scores = {col: None for col in Q_COLS}
    for column, value in row.items():
        match = MINI_COL_RE.match(str(column).strip())
        if not match:
            continue
        number = int(match.group(1))
        if 1 <= number <= 42:
            scores[f"q{number:02d}"] = parse_score(value)
    return scores


def _demo_common(row: pd.Series, columns: list[str]) -> dict:
    month_col = col_lookup(columns, "Age (in months)")
    year_col = col_lookup(columns, "Age (in years)")
    sex_col = col_lookup(columns, "Sex")
    neuter_col = col_lookup(columns, "Spay/Neuter", "Spay/neuter", "IsNeutered")
    weight_col = col_lookup(columns, "Weight (in pounds)", "Weight")
    breed_col = col_lookup(columns, "Breed", "BreedID")
    shelter_col = col_lookup(columns, "Shelter", "shelter")
    return {
        "age_months": age_from_parts(
            row[month_col] if month_col else None,
            row[year_col] if year_col else None,
        ),
        "sex": parse_sex(row[sex_col]) if sex_col else None,
        "neutered": parse_bool(row[neuter_col]) if neuter_col else None,
        "weight_kg": pounds_to_kg(row[weight_col]) if weight_col else None,
        "breed": None if not breed_col or _blank(row[breed_col]) else str(row[breed_col]).strip(),
        "shelter": None if not shelter_col or _blank(row[shelter_col]) else str(row[shelter_col]).strip(),
    }


def transform_shelter() -> pd.DataFrame:
    folder = SERPELL_DIR / "2009_07_17_Shelter_Study_Complete"
    rows: list[dict] = []
    for path in sorted(folder.glob("*.csv")):
        frame = load_csv(path)
        columns = list(frame.columns)
        id_col = col_lookup(columns, "ID#")
        for _, raw in frame.iterrows():
            record = empty_record()
            raw_id = norm_id(raw[id_col]) if id_col else None
            demo = _demo_common(raw, columns)
            shelter = demo["shelter"] or path.stem.split("-")[0]
            record.update(demo)
            record.update(
                {
                    "dog_id": f"{shelter}:{raw_id or 'unknown'}",
                    "source": "serpell_shelter_2009",
                    "instrument": "mini",
                    "is_mapped": False,
                    "wave": None,
                    "raw_dog_id": raw_id,
                    "notes": None,
                }
            )
            record.update(mini_scores_from_numbered(raw))
            rows.append(record)
    return finalize(rows)


def transform_postadoption() -> pd.DataFrame:
    path = SERPELL_DIR / "PostAdoptionMiniCBARQ-Deidentified.csv"
    frame = load_csv(path)
    rows: list[dict] = []
    for index, raw in frame.iterrows():
        adoption = parse_date(raw.get("AdoptionDate"))
        by_wave: dict[str, dict[str, float | None]] = {}
        for column, value in raw.items():
            match = POST_STEM_RE.match(str(column).strip())
            if not match:
                continue
            item = int(match.group(1))
            wave = f"S{match.group(2)}"
            if not 1 <= item <= 42:
                continue
            by_wave.setdefault(wave, {col: None for col in Q_COLS})
            by_wave[wave][f"q{item:02d}"] = parse_score(value)
        for wave, scores in sorted(by_wave.items()):
            survey_col = f"SurveyDate{wave[-1]}"
            record = empty_record()
            record.update(
                {
                    "dog_id": f"postmini_{int(index):03d}",
                    "source": "serpell_postadoption_mini",
                    "instrument": "mini",
                    "is_mapped": False,
                    "wave": wave,
                    "survey_date": parse_date(raw.get(survey_col)) if survey_col in frame.columns else None,
                    "adopted_date": adoption,
                    "raw_dog_id": None,
                    "notes": "deidentified; no stable external dog id or demographics",
                }
            )
            record.update(scores)
            rows.append(record)
    return finalize(rows)


def transform_owners_full() -> pd.DataFrame:
    folder = SERPELL_DIR / "2009_06_19_Adopting_Owners_complete"
    rows: list[dict] = []
    for path in sorted(folder.glob("*.csv")):
        frame = load_csv(path)
        columns = list(frame.columns)
        id_col = col_lookup(columns, "ID#")
        for _, raw in frame.iterrows():
            record = empty_record()
            raw_id = norm_id(raw[id_col]) if id_col else None
            demo = _demo_common(raw, columns)
            shelter = demo["shelter"] or path.stem.split("-")[0]
            record.update(demo)
            record.update(
                {
                    "dog_id": f"{shelter}:{raw_id or 'unknown'}",
                    "source": "serpell_owners_full",
                    "instrument": "full_mapped",
                    "is_mapped": True,
                    "wave": None,
                    "raw_dog_id": raw_id,
                    "notes": MAPPED_NOTE,
                }
            )
            record.update(project_full_scores(full_scores_from_row(raw)))
            rows.append(record)
    return finalize(rows)


def transform_online_full() -> pd.DataFrame:
    path = SERPELL_DIR / "Adopting_owners_cbarq_online.csv"
    frame = load_csv(path, header=2)
    columns = list(frame.columns)
    rows: list[dict] = []
    for _, raw in frame.iterrows():
        record = empty_record()
        raw_id = norm_id(raw.get("DogID"))
        age = to_float(raw.get("AgeAtEvaluation"))
        if age is None:
            birthday = parse_date(raw.get("Birthday"))
            if birthday is not None:
                # no survey date in this export; age relative to file year 2009
                age = (pd.Timestamp("2009-07-17") - birthday).days / 30.437
        shelter = None if _blank(raw.get("shelter")) else str(raw.get("shelter")).strip()
        breed = None if _blank(raw.get("BreedID")) else str(raw.get("BreedID")).strip()
        record.update(
            {
                "dog_id": f"{shelter or 'NA'}:{raw_id or 'unknown'}",
                "source": "serpell_online_full",
                "instrument": "full_mapped",
                "is_mapped": True,
                "wave": None,
                "age_months": age,
                "sex": parse_sex(raw.get("Sex")),
                "neutered": parse_bool(raw.get("IsNeutered")),
                "weight_kg": pounds_to_kg(raw.get("Weight")),
                "breed": breed,
                "shelter": shelter,
                "raw_dog_id": raw_id,
                "notes": ONLINE_NOTE,
            }
        )
        record.update(project_full_scores(full_scores_from_row(raw)))
        rows.append(record)
    return finalize(rows)


def _bohland_demo() -> pd.DataFrame:
    sheet = load_csv(BOHLAND_DIR / "Sheet1 (3)-Tаблица 1.csv")
    sheet = sheet.copy()
    sheet["animal_key"] = sheet["Animal_ID"].map(norm_id)
    sheet = sheet.dropna(subset=["animal_key"]).drop_duplicates("animal_key", keep="first")
    return sheet.set_index("animal_key")


def transform_bohland() -> pd.DataFrame:
    frame = load_csv(BOHLAND_DIR / "journal.pone.0289356.s004.csv")
    demo = _bohland_demo()
    consent = frame.loc[frame["Event Name"] == "Consent Form"].copy()
    consent["animal_key"] = consent["Animal ID"].map(norm_id)
    consent_by_record = consent.drop_duplicates("Record ID").set_index("Record ID")

    rows: list[dict] = []
    for event, suffix, wave, date_col in BOHLAND_WAVES:
        block = frame.loc[frame["Event Name"] == event]
        for _, raw in block.iterrows():
            record_id = raw["Record ID"]
            consent_row = consent_by_record.loc[record_id] if record_id in consent_by_record.index else None
            animal_key = None if consent_row is None else consent_row["animal_key"]
            sheet_row = demo.loc[animal_key] if animal_key in demo.index else None
            shelter_name_col = "Dog shelter name: " if suffix == "" else f"Dog shelter name: {suffix}"
            shelter_name = None
            if shelter_name_col in frame.columns and not _blank(raw.get(shelter_name_col)):
                shelter_name = str(raw.get(shelter_name_col)).strip()
            age_months = None
            sex = None
            weight_kg = None
            breed = None
            shelter = shelter_name
            if sheet_row is not None:
                age_years = to_float(sheet_row.get("Age"))
                age_months = None if age_years is None else age_years * 12
                sex = parse_sex(sheet_row.get("Sex"))
                weight_kg = pounds_to_kg(sheet_row.get("Weight"))
                breed = None if _blank(sheet_row.get("Breed")) else str(sheet_row.get("Breed")).strip()
                if not _blank(sheet_row.get("Shelter")):
                    shelter = str(sheet_row.get("Shelter")).strip()
            adoption = None
            if consent_row is not None:
                adoption = parse_date(consent_row.get("Date of adoption:  "))
            record = empty_record()
            record.update(
                {
                    "dog_id": f"rec{record_id}",
                    "source": "bohland_2023",
                    "instrument": "mini",
                    "is_mapped": False,
                    "wave": wave,
                    "survey_date": parse_date(raw.get(date_col)) if date_col in frame.columns else None,
                    "adopted_date": adoption,
                    "age_months": age_months,
                    "sex": sex,
                    "neutered": None,
                    "weight_kg": weight_kg,
                    "breed": breed,
                    "shelter": shelter,
                    "raw_dog_id": animal_key,
                    "notes": BOHLAND_NOTE,
                }
            )
            for index, base in enumerate(BOHLAND_Q_BASES, start=1):
                column = base if suffix == "" else f"{base}{suffix}"
                record[f"q{index:02d}"] = parse_score(raw[column]) if column in frame.columns else None
            rows.append(record)
    return finalize(rows)


def build_unified() -> pd.DataFrame:
    parts = [
        transform_shelter(),
        transform_postadoption(),
        transform_owners_full(),
        transform_online_full(),
        transform_bohland(),
    ]
    unified = pd.concat(parts, ignore_index=True)
    unified = unified[SCHEMA_COLS]
    return unified


def qc_summary(frame: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for source, part in frame.groupby("source", dropna=False):
        rows.append(
            {
                "source": source,
                "rows": len(part),
                "dogs": part["dog_id"].nunique(),
                "instrument": part["instrument"].iloc[0] if len(part) else None,
                "pct_age": round(100 * part["age_months"].notna().mean(), 1),
                "pct_sex": round(100 * part["sex"].notna().mean(), 1),
                "pct_neutered": round(100 * part["neutered"].notna().mean(), 1),
                "pct_weight": round(100 * part["weight_kg"].notna().mean(), 1),
                "pct_adopted_date": round(100 * part["adopted_date"].notna().mean(), 1),
                "pct_days_at_home": round(100 * part["days_at_home"].notna().mean(), 1),
                "pct_breed": round(100 * part["breed"].notna().mean(), 1),
                "mean_n_answered": round(part["n_answered"].mean(), 1),
            }
        )
    return pd.DataFrame(rows).sort_values("source").reset_index(drop=True)


def export(frame: pd.DataFrame | None = None) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if frame is None:
        frame = build_unified()
    csv_path = OUT_DIR / "cbarq_mini_sessions.csv"
    frame.to_csv(csv_path, index=False)
    try:
        frame.to_parquet(OUT_DIR / "cbarq_mini_sessions.parquet", index=False)
    except Exception:
        pass
    summary = qc_summary(frame)
    summary.to_csv(OUT_DIR / "qc_by_source.csv", index=False)
    return csv_path


if __name__ == "__main__":
    data = build_unified()
    path = export(data)
    print(path)
    print(qc_summary(data).to_string(index=False))
    print("rows", len(data), "dup session", data["session_id"].duplicated().sum())
