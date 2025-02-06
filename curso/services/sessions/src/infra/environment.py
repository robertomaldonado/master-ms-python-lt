import os
import pathlib

from typing import Dict, Any


import yaml


class Env:
    env: Dict[str, Any]

    def __init__(self, stage: str = "local"):
        self.env = dict()
        self._load()

    def get(self, key: str, default: str = "") -> str:
        if key in self.env:
            return str(self.env[key])

        return default

    def get_int(self, key: str, default: int = 0) -> int:
        if key in self.env:
            return int(self.env[key])

        return default

    def _load(self, stage: str = "local"):
        base_path = pathlib.Path(__file__).parent.resolve()
        env_file = f"{base_path}/../config/{stage}.yml"

        with open(env_file, "r") as file:
            self.env = yaml.safe_load(file)

        for key, value in os.environ.items():
            self.env[key] = value


envs = Env(os.environ.get("STAGE", "local"))
