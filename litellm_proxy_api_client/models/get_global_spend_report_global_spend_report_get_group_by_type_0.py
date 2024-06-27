from enum import Enum


class GetGlobalSpendReportGlobalSpendReportGetGroupByType0(str, Enum):
    CUSTOMER = "customer"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
