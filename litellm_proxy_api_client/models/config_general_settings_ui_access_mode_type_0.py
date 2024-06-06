from enum import Enum


class ConfigGeneralSettingsUiAccessModeType0(str, Enum):
    ADMIN_ONLY = "admin_only"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
