from enum import Enum


class ConfigFieldUpdateConfigType(str, Enum):
    GENERAL_SETTINGS = "general_settings"

    def __str__(self) -> str:
        return str(self.value)
