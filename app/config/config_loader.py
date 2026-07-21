from pathlib import Path

import yaml
from jsonschema import validate

from app.config.schema import BANK_CONFIG_SCHEMA


class ConfigLoader:
    """
    Loads and validates bank configuration files.
    """

    def __init__(self, config_directory: str = "configs"):
        self.config_directory = Path(config_directory)

    def load(self, bank_code: str) -> dict:
        """
        Load configuration for a specific bank.
        """
        config_file = self.config_directory / f"{bank_code.lower()}.yaml"

        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration not found for '{bank_code}'."
            )

        with config_file.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        validate(
            instance=config,
            schema=BANK_CONFIG_SCHEMA
        )

        return config

    def load_all(self) -> dict:
        """
        Load all bank configuration files.
        """
        configs = {}

        for config_file in self.config_directory.glob("*.yaml"):

            with config_file.open("r", encoding="utf-8") as file:
                config = yaml.safe_load(file)

            validate(
                instance=config,
                schema=BANK_CONFIG_SCHEMA
            )

            configs[config_file.stem.upper()] = config

        return configs