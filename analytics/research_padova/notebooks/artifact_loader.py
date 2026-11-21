"""Load artifact paths from artifacts/json/artifact_paths.json."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

__all__ = [
    "ROOT",
    "PATHS",
    "original_data_path",
    "df_cbarq_clean_path",
    "domain_data_path",
    "domain_scaled_data_path",
    "scaler_stats_path",
    "domain_items_path",
    "domain_scaler_path",
    "kmeans_out_path",
    "gmm_out_path",
    "cluster_comparison_path",
]


def resolve_research_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in (
        cwd,
        cwd / "analytics/research",
        cwd.parent if cwd.name == "notebooks" else None,
    ):
        if candidate is not None and (candidate / "artifacts/json/artifact_paths.json").exists():
            return candidate.resolve()
    raise FileNotFoundError(f"research root not found from cwd={cwd}")


ROOT = resolve_research_root()


@lru_cache(maxsize=1)
def PATHS() -> dict[str, Path]:
    with open(ROOT / "artifacts/json/artifact_paths.json", encoding="utf-8") as f:
        cfg = json.load(f)
    return {k: ROOT / v for k, v in cfg["paths"].items()}


def _path(key: str) -> Path:
    paths = PATHS()
    if key not in paths:
        raise KeyError(f"unknown artifact key: {key!r}; available: {sorted(paths)}")
    return paths[key]


def original_data_path() -> Path:
    return _path("original_data")


def df_cbarq_clean_path() -> Path:
    return _path("df_cbarq_clean")


def domain_data_path() -> Path:
    return _path("df_domains")


def domain_scaled_data_path() -> Path:
    return _path("df_domains_scaled")


def scaler_stats_path() -> Path:
    return _path("scaler_stats")


def domain_items_path() -> Path:
    return _path("domain_items")


def domain_scaler_path() -> Path:
    return _path("domain_scaler")


def kmeans_out_path() -> Path:
    return _path("df_domains_kmeans")


def gmm_out_path() -> Path:
    return _path("df_domains_gmm")


def cluster_comparison_path() -> Path:
    return _path("cluster_comparison")
