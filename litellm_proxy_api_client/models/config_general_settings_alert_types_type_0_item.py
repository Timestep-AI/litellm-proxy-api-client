from enum import Enum


class ConfigGeneralSettingsAlertTypesType0Item(str, Enum):
    BUDGET_ALERTS = "budget_alerts"
    COOLDOWN_DEPLOYMENT = "cooldown_deployment"
    DAILY_REPORTS = "daily_reports"
    DB_EXCEPTIONS = "db_exceptions"
    LLM_EXCEPTIONS = "llm_exceptions"
    LLM_REQUESTS_HANGING = "llm_requests_hanging"
    LLM_TOO_SLOW = "llm_too_slow"
    NEW_MODEL_ADDED = "new_model_added"
    OUTAGE_ALERTS = "outage_alerts"
    REGION_OUTAGE_ALERTS = "region_outage_alerts"
    SPEND_REPORTS = "spend_reports"

    def __str__(self) -> str:
        return str(self.value)
