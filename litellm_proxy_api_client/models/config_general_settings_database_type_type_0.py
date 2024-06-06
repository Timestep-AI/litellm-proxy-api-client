from enum import Enum


class ConfigGeneralSettingsDatabaseTypeType0(str, Enum):
    DYNAMO_DB = "dynamo_db"

    def __str__(self) -> str:
        return str(self.value)
