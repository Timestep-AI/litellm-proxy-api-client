from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_general_settings import ConfigGeneralSettings
    from ..models.config_yaml_environment_variables_type_0 import ConfigYAMLEnvironmentVariablesType0
    from ..models.config_yaml_litellm_settings_type_0 import ConfigYAMLLitellmSettingsType0
    from ..models.model_params import ModelParams
    from ..models.update_router_config import UpdateRouterConfig


T = TypeVar("T", bound="ConfigYAML")


@_attrs_define
class ConfigYAML:
    """Documents all the fields supported by the config.yaml

    Attributes:
        environment_variables (Union['ConfigYAMLEnvironmentVariablesType0', None, Unset]): Object to pass in additional
            environment variables via POST request
        model_list (Union[List['ModelParams'], None, Unset]): List of supported models on the server, with model-
            specific configs
        litellm_settings (Union['ConfigYAMLLitellmSettingsType0', None, Unset]): litellm Module settings. See
            __init__.py for all, example litellm.drop_params=True, litellm.set_verbose=True, litellm.api_base, litellm.cache
        general_settings (Union['ConfigGeneralSettings', None, Unset]):
        router_settings (Union['UpdateRouterConfig', None, Unset]): litellm router object settings. See router.py
            __init__ for all, example router.num_retries=5, router.timeout=5, router.max_retries=5, router.retry_after=5
    """

    environment_variables: Union["ConfigYAMLEnvironmentVariablesType0", None, Unset] = UNSET
    model_list: Union[List["ModelParams"], None, Unset] = UNSET
    litellm_settings: Union["ConfigYAMLLitellmSettingsType0", None, Unset] = UNSET
    general_settings: Union["ConfigGeneralSettings", None, Unset] = UNSET
    router_settings: Union["UpdateRouterConfig", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.config_general_settings import ConfigGeneralSettings
        from ..models.config_yaml_environment_variables_type_0 import ConfigYAMLEnvironmentVariablesType0
        from ..models.config_yaml_litellm_settings_type_0 import ConfigYAMLLitellmSettingsType0
        from ..models.update_router_config import UpdateRouterConfig

        environment_variables: Union[Dict[str, Any], None, Unset]
        if isinstance(self.environment_variables, Unset):
            environment_variables = UNSET
        elif isinstance(self.environment_variables, ConfigYAMLEnvironmentVariablesType0):
            environment_variables = self.environment_variables.to_dict()
        else:
            environment_variables = self.environment_variables

        model_list: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.model_list, Unset):
            model_list = UNSET
        elif isinstance(self.model_list, list):
            model_list = []
            for model_list_type_0_item_data in self.model_list:
                model_list_type_0_item = model_list_type_0_item_data.to_dict()
                model_list.append(model_list_type_0_item)

        else:
            model_list = self.model_list

        litellm_settings: Union[Dict[str, Any], None, Unset]
        if isinstance(self.litellm_settings, Unset):
            litellm_settings = UNSET
        elif isinstance(self.litellm_settings, ConfigYAMLLitellmSettingsType0):
            litellm_settings = self.litellm_settings.to_dict()
        else:
            litellm_settings = self.litellm_settings

        general_settings: Union[Dict[str, Any], None, Unset]
        if isinstance(self.general_settings, Unset):
            general_settings = UNSET
        elif isinstance(self.general_settings, ConfigGeneralSettings):
            general_settings = self.general_settings.to_dict()
        else:
            general_settings = self.general_settings

        router_settings: Union[Dict[str, Any], None, Unset]
        if isinstance(self.router_settings, Unset):
            router_settings = UNSET
        elif isinstance(self.router_settings, UpdateRouterConfig):
            router_settings = self.router_settings.to_dict()
        else:
            router_settings = self.router_settings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environment_variables is not UNSET:
            field_dict["environment_variables"] = environment_variables
        if model_list is not UNSET:
            field_dict["model_list"] = model_list
        if litellm_settings is not UNSET:
            field_dict["litellm_settings"] = litellm_settings
        if general_settings is not UNSET:
            field_dict["general_settings"] = general_settings
        if router_settings is not UNSET:
            field_dict["router_settings"] = router_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_general_settings import ConfigGeneralSettings
        from ..models.config_yaml_environment_variables_type_0 import ConfigYAMLEnvironmentVariablesType0
        from ..models.config_yaml_litellm_settings_type_0 import ConfigYAMLLitellmSettingsType0
        from ..models.model_params import ModelParams
        from ..models.update_router_config import UpdateRouterConfig

        d = src_dict.copy()

        def _parse_environment_variables(data: object) -> Union["ConfigYAMLEnvironmentVariablesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_variables_type_0 = ConfigYAMLEnvironmentVariablesType0.from_dict(data)

                return environment_variables_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConfigYAMLEnvironmentVariablesType0", None, Unset], data)

        environment_variables = _parse_environment_variables(d.pop("environment_variables", UNSET))

        def _parse_model_list(data: object) -> Union[List["ModelParams"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                model_list_type_0 = []
                _model_list_type_0 = data
                for model_list_type_0_item_data in _model_list_type_0:
                    model_list_type_0_item = ModelParams.from_dict(model_list_type_0_item_data)

                    model_list_type_0.append(model_list_type_0_item)

                return model_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelParams"], None, Unset], data)

        model_list = _parse_model_list(d.pop("model_list", UNSET))

        def _parse_litellm_settings(data: object) -> Union["ConfigYAMLLitellmSettingsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_settings_type_0 = ConfigYAMLLitellmSettingsType0.from_dict(data)

                return litellm_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConfigYAMLLitellmSettingsType0", None, Unset], data)

        litellm_settings = _parse_litellm_settings(d.pop("litellm_settings", UNSET))

        def _parse_general_settings(data: object) -> Union["ConfigGeneralSettings", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                general_settings_type_0 = ConfigGeneralSettings.from_dict(data)

                return general_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConfigGeneralSettings", None, Unset], data)

        general_settings = _parse_general_settings(d.pop("general_settings", UNSET))

        def _parse_router_settings(data: object) -> Union["UpdateRouterConfig", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                router_settings_type_0 = UpdateRouterConfig.from_dict(data)

                return router_settings_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateRouterConfig", None, Unset], data)

        router_settings = _parse_router_settings(d.pop("router_settings", UNSET))

        config_yaml = cls(
            environment_variables=environment_variables,
            model_list=model_list,
            litellm_settings=litellm_settings,
            general_settings=general_settings,
            router_settings=router_settings,
        )

        config_yaml.additional_properties = d
        return config_yaml

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
