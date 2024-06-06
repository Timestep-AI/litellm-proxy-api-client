from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_field_update_config_type import ConfigFieldUpdateConfigType

T = TypeVar("T", bound="ConfigFieldUpdate")


@_attrs_define
class ConfigFieldUpdate:
    """
    Attributes:
        field_name (str):
        field_value (Any):
        config_type (ConfigFieldUpdateConfigType):
    """

    field_name: str
    field_value: Any
    config_type: ConfigFieldUpdateConfigType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name

        field_value = self.field_value

        config_type = self.config_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "field_value": field_value,
                "config_type": config_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_name = d.pop("field_name")

        field_value = d.pop("field_value")

        config_type = ConfigFieldUpdateConfigType(d.pop("config_type"))

        config_field_update = cls(
            field_name=field_name,
            field_value=field_value,
            config_type=config_type,
        )

        config_field_update.additional_properties = d
        return config_field_update

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
