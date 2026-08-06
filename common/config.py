"""多环境配置加载。支持 ${VAR} 与 ${VAR:-default} 形式的环境变量占位符。"""
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
_PLACEHOLDER = re.compile(r"\$\{(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?::-(?P<default>[^}]*))?\}")


def _expand(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _expand(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand(v) for v in value]
    if isinstance(value, str):
        def sub(match: re.Match) -> str:
            name = match.group("name")
            default = match.group("default")
            resolved = os.environ.get(name)
            if resolved is None:
                if default is None:
                    raise RuntimeError(f"缺少必需的环境变量: {name}")
                resolved = default
            return resolved

        return _PLACEHOLDER.sub(sub, value)
    return value


class Config:
    def __init__(self, raw: dict) -> None:
        self._raw = raw

    @property
    def env_name(self) -> str:
        return self._raw["env_name"]

    @property
    def timeout(self) -> int:
        return int(self._raw.get("timeout", 10))

    @property
    def retry(self) -> int:
        return int(self._raw.get("retry", 0))

    def base_url(self, service: str) -> str:
        return self._raw["services"][service]["base_url"].rstrip("/")

    def auth(self) -> dict:
        return dict(self._raw.get("auth", {}))

    def dsn(self, service: str) -> str:
        return self._raw.get("database", {}).get(service, {}).get("dsn", "")


@lru_cache(maxsize=None)
def load_config(env: str) -> Config:
    path = CONFIG_DIR / f"{env}.yaml"
    if not path.exists():
        available = ", ".join(sorted(p.stem for p in CONFIG_DIR.glob("*.yaml")))
        raise FileNotFoundError(f"未找到环境配置 {path}，可用环境: {available}")
    with path.open(encoding="utf-8") as fp:
        return Config(_expand(yaml.safe_load(fp)))
