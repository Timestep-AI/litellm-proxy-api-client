from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_general_settings_alert_types_type_0_item import ConfigGeneralSettingsAlertTypesType0Item
from ..models.config_general_settings_database_type_type_0 import ConfigGeneralSettingsDatabaseTypeType0
from ..models.config_general_settings_ui_access_mode_type_0 import ConfigGeneralSettingsUiAccessModeType0
from ..models.key_management_system import KeyManagementSystem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_general_settings_alert_to_webhook_url_type_0 import ConfigGeneralSettingsAlertToWebhookUrlType0
    from ..models.config_general_settings_alerting_args_type_0 import ConfigGeneralSettingsAlertingArgsType0
    from ..models.dynamo_db_args import DynamoDBArgs


T = TypeVar("T", bound="ConfigGeneralSettings")


@_attrs_define
class ConfigGeneralSettings:
    """Documents all the fields supported by `general_settings` in config.yaml

    Attributes:
        completion_model (Union[None, Unset, str]): proxy level default model for all chat completion calls
        key_management_system (Union[KeyManagementSystem, None, Unset]): key manager to load keys from / decrypt keys
            with
        use_google_kms (Union[None, Unset, bool]): decrypt keys with google kms
        use_azure_key_vault (Union[None, Unset, bool]): load keys from azure key vault
        master_key (Union[None, Unset, str]): require a key for all calls to proxy
        database_url (Union[None, Unset, str]): connect to a postgres db - needed for generating temporary keys +
            tracking spend / key
        database_connection_pool_limit (Union[None, Unset, int]): default connection pool for prisma client connecting
            to postgres db Default: 100.
        database_connection_timeout (Union[None, Unset, float]): default timeout for a connection to the database
            Default: 60.0.
        database_type (Union[ConfigGeneralSettingsDatabaseTypeType0, None, Unset]): to use dynamodb instead of postgres
            db
        database_args (Union['DynamoDBArgs', None, Unset]): custom args for instantiating dynamodb client - e.g. billing
            provision
        otel (Union[None, Unset, bool]): [BETA] OpenTelemetry support - this might change, use with caution.
        custom_auth (Union[None, Unset, str]): override user_api_key_auth with your own auth script -
            https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth
        max_parallel_requests (Union[None, Unset, int]): maximum parallel requests for each api key
        global_max_parallel_requests (Union[None, Unset, int]): global max parallel requests to allow for a proxy
            instance.
        infer_model_from_keys (Union[None, Unset, bool]): for `/models` endpoint, infers available model based on
            environment keys (e.g. OPENAI_API_KEY)
        background_health_checks (Union[None, Unset, bool]): run health checks in background
        health_check_interval (Union[Unset, int]): background health check interval in seconds Default: 300.
        alerting (Union[List[Any], None, Unset]): List of alerting integrations. Today, just slack - `alerting:
            ['slack']`
        alert_types (Union[List[ConfigGeneralSettingsAlertTypesType0Item], None, Unset]): List of alerting types. By
            default it is all alerts
        alert_to_webhook_url (Union['ConfigGeneralSettingsAlertToWebhookUrlType0', None, Unset]): Mapping of alert type
            to webhook url. e.g. `alert_to_webhook_url: {'budget_alerts':
            'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'}`
        alerting_args (Union['ConfigGeneralSettingsAlertingArgsType0', None, Unset]): Controllable params for slack
            alerting - e.g. ttl in cache.
        alerting_threshold (Union[None, Unset, int]): sends alerts if requests hang for 5min+
        ui_access_mode (Union[ConfigGeneralSettingsUiAccessModeType0, None, Unset]): Control access to the Proxy UI
            Default: ConfigGeneralSettingsUiAccessModeType0.ALL.
        allowed_routes (Union[List[Any], None, Unset]): Proxy API Endpoints you want users to be able to access
        enable_public_model_hub (Union[Unset, bool]): Public model hub for users to see what models they have access to,
            supported openai params, etc. Default: False.
    """

    completion_model: Union[None, Unset, str] = UNSET
    key_management_system: Union[KeyManagementSystem, None, Unset] = UNSET
    use_google_kms: Union[None, Unset, bool] = UNSET
    use_azure_key_vault: Union[None, Unset, bool] = UNSET
    master_key: Union[None, Unset, str] = UNSET
    database_url: Union[None, Unset, str] = UNSET
    database_connection_pool_limit: Union[None, Unset, int] = 100
    database_connection_timeout: Union[None, Unset, float] = 60.0
    database_type: Union[ConfigGeneralSettingsDatabaseTypeType0, None, Unset] = UNSET
    database_args: Union["DynamoDBArgs", None, Unset] = UNSET
    otel: Union[None, Unset, bool] = UNSET
    custom_auth: Union[None, Unset, str] = UNSET
    max_parallel_requests: Union[None, Unset, int] = UNSET
    global_max_parallel_requests: Union[None, Unset, int] = UNSET
    infer_model_from_keys: Union[None, Unset, bool] = UNSET
    background_health_checks: Union[None, Unset, bool] = UNSET
    health_check_interval: Union[Unset, int] = 300
    alerting: Union[List[Any], None, Unset] = UNSET
    alert_types: Union[List[ConfigGeneralSettingsAlertTypesType0Item], None, Unset] = UNSET
    alert_to_webhook_url: Union["ConfigGeneralSettingsAlertToWebhookUrlType0", None, Unset] = UNSET
    alerting_args: Union["ConfigGeneralSettingsAlertingArgsType0", None, Unset] = UNSET
    alerting_threshold: Union[None, Unset, int] = UNSET
    ui_access_mode: Union[ConfigGeneralSettingsUiAccessModeType0, None, Unset] = (
        ConfigGeneralSettingsUiAccessModeType0.ALL
    )
    allowed_routes: Union[List[Any], None, Unset] = UNSET
    enable_public_model_hub: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.config_general_settings_alert_to_webhook_url_type_0 import (
            ConfigGeneralSettingsAlertToWebhookUrlType0,
        )
        from ..models.config_general_settings_alerting_args_type_0 import ConfigGeneralSettingsAlertingArgsType0
        from ..models.dynamo_db_args import DynamoDBArgs

        completion_model: Union[None, Unset, str]
        if isinstance(self.completion_model, Unset):
            completion_model = UNSET
        else:
            completion_model = self.completion_model

        key_management_system: Union[None, Unset, str]
        if isinstance(self.key_management_system, Unset):
            key_management_system = UNSET
        elif isinstance(self.key_management_system, KeyManagementSystem):
            key_management_system = self.key_management_system.value
        else:
            key_management_system = self.key_management_system

        use_google_kms: Union[None, Unset, bool]
        if isinstance(self.use_google_kms, Unset):
            use_google_kms = UNSET
        else:
            use_google_kms = self.use_google_kms

        use_azure_key_vault: Union[None, Unset, bool]
        if isinstance(self.use_azure_key_vault, Unset):
            use_azure_key_vault = UNSET
        else:
            use_azure_key_vault = self.use_azure_key_vault

        master_key: Union[None, Unset, str]
        if isinstance(self.master_key, Unset):
            master_key = UNSET
        else:
            master_key = self.master_key

        database_url: Union[None, Unset, str]
        if isinstance(self.database_url, Unset):
            database_url = UNSET
        else:
            database_url = self.database_url

        database_connection_pool_limit: Union[None, Unset, int]
        if isinstance(self.database_connection_pool_limit, Unset):
            database_connection_pool_limit = UNSET
        else:
            database_connection_pool_limit = self.database_connection_pool_limit

        database_connection_timeout: Union[None, Unset, float]
        if isinstance(self.database_connection_timeout, Unset):
            database_connection_timeout = UNSET
        else:
            database_connection_timeout = self.database_connection_timeout

        database_type: Union[None, Unset, str]
        if isinstance(self.database_type, Unset):
            database_type = UNSET
        elif isinstance(self.database_type, ConfigGeneralSettingsDatabaseTypeType0):
            database_type = self.database_type.value
        else:
            database_type = self.database_type

        database_args: Union[Dict[str, Any], None, Unset]
        if isinstance(self.database_args, Unset):
            database_args = UNSET
        elif isinstance(self.database_args, DynamoDBArgs):
            database_args = self.database_args.to_dict()
        else:
            database_args = self.database_args

        otel: Union[None, Unset, bool]
        if isinstance(self.otel, Unset):
            otel = UNSET
        else:
            otel = self.otel

        custom_auth: Union[None, Unset, str]
        if isinstance(self.custom_auth, Unset):
            custom_auth = UNSET
        else:
            custom_auth = self.custom_auth

        max_parallel_requests: Union[None, Unset, int]
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        global_max_parallel_requests: Union[None, Unset, int]
        if isinstance(self.global_max_parallel_requests, Unset):
            global_max_parallel_requests = UNSET
        else:
            global_max_parallel_requests = self.global_max_parallel_requests

        infer_model_from_keys: Union[None, Unset, bool]
        if isinstance(self.infer_model_from_keys, Unset):
            infer_model_from_keys = UNSET
        else:
            infer_model_from_keys = self.infer_model_from_keys

        background_health_checks: Union[None, Unset, bool]
        if isinstance(self.background_health_checks, Unset):
            background_health_checks = UNSET
        else:
            background_health_checks = self.background_health_checks

        health_check_interval = self.health_check_interval

        alerting: Union[List[Any], None, Unset]
        if isinstance(self.alerting, Unset):
            alerting = UNSET
        elif isinstance(self.alerting, list):
            alerting = self.alerting

        else:
            alerting = self.alerting

        alert_types: Union[List[str], None, Unset]
        if isinstance(self.alert_types, Unset):
            alert_types = UNSET
        elif isinstance(self.alert_types, list):
            alert_types = []
            for alert_types_type_0_item_data in self.alert_types:
                alert_types_type_0_item = alert_types_type_0_item_data.value
                alert_types.append(alert_types_type_0_item)

        else:
            alert_types = self.alert_types

        alert_to_webhook_url: Union[Dict[str, Any], None, Unset]
        if isinstance(self.alert_to_webhook_url, Unset):
            alert_to_webhook_url = UNSET
        elif isinstance(self.alert_to_webhook_url, ConfigGeneralSettingsAlertToWebhookUrlType0):
            alert_to_webhook_url = self.alert_to_webhook_url.to_dict()
        else:
            alert_to_webhook_url = self.alert_to_webhook_url

        alerting_args: Union[Dict[str, Any], None, Unset]
        if isinstance(self.alerting_args, Unset):
            alerting_args = UNSET
        elif isinstance(self.alerting_args, ConfigGeneralSettingsAlertingArgsType0):
            alerting_args = self.alerting_args.to_dict()
        else:
            alerting_args = self.alerting_args

        alerting_threshold: Union[None, Unset, int]
        if isinstance(self.alerting_threshold, Unset):
            alerting_threshold = UNSET
        else:
            alerting_threshold = self.alerting_threshold

        ui_access_mode: Union[None, Unset, str]
        if isinstance(self.ui_access_mode, Unset):
            ui_access_mode = UNSET
        elif isinstance(self.ui_access_mode, ConfigGeneralSettingsUiAccessModeType0):
            ui_access_mode = self.ui_access_mode.value
        else:
            ui_access_mode = self.ui_access_mode

        allowed_routes: Union[List[Any], None, Unset]
        if isinstance(self.allowed_routes, Unset):
            allowed_routes = UNSET
        elif isinstance(self.allowed_routes, list):
            allowed_routes = self.allowed_routes

        else:
            allowed_routes = self.allowed_routes

        enable_public_model_hub = self.enable_public_model_hub

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_model is not UNSET:
            field_dict["completion_model"] = completion_model
        if key_management_system is not UNSET:
            field_dict["key_management_system"] = key_management_system
        if use_google_kms is not UNSET:
            field_dict["use_google_kms"] = use_google_kms
        if use_azure_key_vault is not UNSET:
            field_dict["use_azure_key_vault"] = use_azure_key_vault
        if master_key is not UNSET:
            field_dict["master_key"] = master_key
        if database_url is not UNSET:
            field_dict["database_url"] = database_url
        if database_connection_pool_limit is not UNSET:
            field_dict["database_connection_pool_limit"] = database_connection_pool_limit
        if database_connection_timeout is not UNSET:
            field_dict["database_connection_timeout"] = database_connection_timeout
        if database_type is not UNSET:
            field_dict["database_type"] = database_type
        if database_args is not UNSET:
            field_dict["database_args"] = database_args
        if otel is not UNSET:
            field_dict["otel"] = otel
        if custom_auth is not UNSET:
            field_dict["custom_auth"] = custom_auth
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if global_max_parallel_requests is not UNSET:
            field_dict["global_max_parallel_requests"] = global_max_parallel_requests
        if infer_model_from_keys is not UNSET:
            field_dict["infer_model_from_keys"] = infer_model_from_keys
        if background_health_checks is not UNSET:
            field_dict["background_health_checks"] = background_health_checks
        if health_check_interval is not UNSET:
            field_dict["health_check_interval"] = health_check_interval
        if alerting is not UNSET:
            field_dict["alerting"] = alerting
        if alert_types is not UNSET:
            field_dict["alert_types"] = alert_types
        if alert_to_webhook_url is not UNSET:
            field_dict["alert_to_webhook_url"] = alert_to_webhook_url
        if alerting_args is not UNSET:
            field_dict["alerting_args"] = alerting_args
        if alerting_threshold is not UNSET:
            field_dict["alerting_threshold"] = alerting_threshold
        if ui_access_mode is not UNSET:
            field_dict["ui_access_mode"] = ui_access_mode
        if allowed_routes is not UNSET:
            field_dict["allowed_routes"] = allowed_routes
        if enable_public_model_hub is not UNSET:
            field_dict["enable_public_model_hub"] = enable_public_model_hub

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_general_settings_alert_to_webhook_url_type_0 import (
            ConfigGeneralSettingsAlertToWebhookUrlType0,
        )
        from ..models.config_general_settings_alerting_args_type_0 import ConfigGeneralSettingsAlertingArgsType0
        from ..models.dynamo_db_args import DynamoDBArgs

        d = src_dict.copy()

        def _parse_completion_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completion_model = _parse_completion_model(d.pop("completion_model", UNSET))

        def _parse_key_management_system(data: object) -> Union[KeyManagementSystem, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                key_management_system_type_0 = KeyManagementSystem(data)

                return key_management_system_type_0
            except:  # noqa: E722
                pass
            return cast(Union[KeyManagementSystem, None, Unset], data)

        key_management_system = _parse_key_management_system(d.pop("key_management_system", UNSET))

        def _parse_use_google_kms(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_google_kms = _parse_use_google_kms(d.pop("use_google_kms", UNSET))

        def _parse_use_azure_key_vault(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_azure_key_vault = _parse_use_azure_key_vault(d.pop("use_azure_key_vault", UNSET))

        def _parse_master_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        master_key = _parse_master_key(d.pop("master_key", UNSET))

        def _parse_database_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        database_url = _parse_database_url(d.pop("database_url", UNSET))

        def _parse_database_connection_pool_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        database_connection_pool_limit = _parse_database_connection_pool_limit(
            d.pop("database_connection_pool_limit", UNSET)
        )

        def _parse_database_connection_timeout(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        database_connection_timeout = _parse_database_connection_timeout(d.pop("database_connection_timeout", UNSET))

        def _parse_database_type(data: object) -> Union[ConfigGeneralSettingsDatabaseTypeType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_type_type_0 = ConfigGeneralSettingsDatabaseTypeType0(data)

                return database_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ConfigGeneralSettingsDatabaseTypeType0, None, Unset], data)

        database_type = _parse_database_type(d.pop("database_type", UNSET))

        def _parse_database_args(data: object) -> Union["DynamoDBArgs", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                database_args_type_0 = DynamoDBArgs.from_dict(data)

                return database_args_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DynamoDBArgs", None, Unset], data)

        database_args = _parse_database_args(d.pop("database_args", UNSET))

        def _parse_otel(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        otel = _parse_otel(d.pop("otel", UNSET))

        def _parse_custom_auth(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_auth = _parse_custom_auth(d.pop("custom_auth", UNSET))

        def _parse_max_parallel_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))

        def _parse_global_max_parallel_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        global_max_parallel_requests = _parse_global_max_parallel_requests(d.pop("global_max_parallel_requests", UNSET))

        def _parse_infer_model_from_keys(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        infer_model_from_keys = _parse_infer_model_from_keys(d.pop("infer_model_from_keys", UNSET))

        def _parse_background_health_checks(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        background_health_checks = _parse_background_health_checks(d.pop("background_health_checks", UNSET))

        health_check_interval = d.pop("health_check_interval", UNSET)

        def _parse_alerting(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alerting_type_0 = cast(List[Any], data)

                return alerting_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        alerting = _parse_alerting(d.pop("alerting", UNSET))

        def _parse_alert_types(data: object) -> Union[List[ConfigGeneralSettingsAlertTypesType0Item], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_types_type_0 = []
                _alert_types_type_0 = data
                for alert_types_type_0_item_data in _alert_types_type_0:
                    alert_types_type_0_item = ConfigGeneralSettingsAlertTypesType0Item(alert_types_type_0_item_data)

                    alert_types_type_0.append(alert_types_type_0_item)

                return alert_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[ConfigGeneralSettingsAlertTypesType0Item], None, Unset], data)

        alert_types = _parse_alert_types(d.pop("alert_types", UNSET))

        def _parse_alert_to_webhook_url(
            data: object,
        ) -> Union["ConfigGeneralSettingsAlertToWebhookUrlType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_to_webhook_url_type_0 = ConfigGeneralSettingsAlertToWebhookUrlType0.from_dict(data)

                return alert_to_webhook_url_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConfigGeneralSettingsAlertToWebhookUrlType0", None, Unset], data)

        alert_to_webhook_url = _parse_alert_to_webhook_url(d.pop("alert_to_webhook_url", UNSET))

        def _parse_alerting_args(data: object) -> Union["ConfigGeneralSettingsAlertingArgsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alerting_args_type_0 = ConfigGeneralSettingsAlertingArgsType0.from_dict(data)

                return alerting_args_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConfigGeneralSettingsAlertingArgsType0", None, Unset], data)

        alerting_args = _parse_alerting_args(d.pop("alerting_args", UNSET))

        def _parse_alerting_threshold(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        alerting_threshold = _parse_alerting_threshold(d.pop("alerting_threshold", UNSET))

        def _parse_ui_access_mode(data: object) -> Union[ConfigGeneralSettingsUiAccessModeType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ui_access_mode_type_0 = ConfigGeneralSettingsUiAccessModeType0(data)

                return ui_access_mode_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ConfigGeneralSettingsUiAccessModeType0, None, Unset], data)

        ui_access_mode = _parse_ui_access_mode(d.pop("ui_access_mode", UNSET))

        def _parse_allowed_routes(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_routes_type_0 = cast(List[Any], data)

                return allowed_routes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        allowed_routes = _parse_allowed_routes(d.pop("allowed_routes", UNSET))

        enable_public_model_hub = d.pop("enable_public_model_hub", UNSET)

        config_general_settings = cls(
            completion_model=completion_model,
            key_management_system=key_management_system,
            use_google_kms=use_google_kms,
            use_azure_key_vault=use_azure_key_vault,
            master_key=master_key,
            database_url=database_url,
            database_connection_pool_limit=database_connection_pool_limit,
            database_connection_timeout=database_connection_timeout,
            database_type=database_type,
            database_args=database_args,
            otel=otel,
            custom_auth=custom_auth,
            max_parallel_requests=max_parallel_requests,
            global_max_parallel_requests=global_max_parallel_requests,
            infer_model_from_keys=infer_model_from_keys,
            background_health_checks=background_health_checks,
            health_check_interval=health_check_interval,
            alerting=alerting,
            alert_types=alert_types,
            alert_to_webhook_url=alert_to_webhook_url,
            alerting_args=alerting_args,
            alerting_threshold=alerting_threshold,
            ui_access_mode=ui_access_mode,
            allowed_routes=allowed_routes,
            enable_public_model_hub=enable_public_model_hub,
        )

        config_general_settings.additional_properties = d
        return config_general_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
