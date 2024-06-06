from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_info import ModelInfo
    from ..models.model_params_litellm_params import ModelParamsLitellmParams


T = TypeVar("T", bound="ModelParams")


@_attrs_define
class ModelParams:
    """
    Attributes:
        model_name (str):
        litellm_params (ModelParamsLitellmParams):
        model_info (ModelInfo):
    """

    model_name: str
    litellm_params: "ModelParamsLitellmParams"
    model_info: "ModelInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_name = self.model_name

        litellm_params = self.litellm_params.to_dict()

        model_info = self.model_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
                "litellm_params": litellm_params,
                "model_info": model_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_info import ModelInfo
        from ..models.model_params_litellm_params import ModelParamsLitellmParams

        d = src_dict.copy()
        model_name = d.pop("model_name")

        litellm_params = ModelParamsLitellmParams.from_dict(d.pop("litellm_params"))

        model_info = ModelInfo.from_dict(d.pop("model_info"))

        model_params = cls(
            model_name=model_name,
            litellm_params=litellm_params,
            model_info=model_info,
        )

        model_params.additional_properties = d
        return model_params

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
