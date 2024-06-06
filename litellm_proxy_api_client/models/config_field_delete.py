from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_field_delete_config_type import ConfigFieldDeleteConfigType

T = TypeVar("T", bound="ConfigFieldDelete")


@_attrs_define
class ConfigFieldDelete:
    """
    Attributes:
        config_type (ConfigFieldDeleteConfigType):
        field_name (str):
    """

    config_type: ConfigFieldDeleteConfigType
    field_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_type = self.config_type.value

        field_name = self.field_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_type": config_type,
                "field_name": field_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_type = ConfigFieldDeleteConfigType(d.pop("config_type"))

        field_name = d.pop("field_name")

        config_field_delete = cls(
            config_type=config_type,
            field_name=field_name,
        )

        config_field_delete.additional_properties = d
        return config_field_delete

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
