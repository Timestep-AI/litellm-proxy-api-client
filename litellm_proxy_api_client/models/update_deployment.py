from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_info import ModelInfo
    from ..models.update_lite_llm_params import UpdateLiteLLMParams


T = TypeVar("T", bound="UpdateDeployment")


@_attrs_define
class UpdateDeployment:
    """
    Attributes:
        model_name (Union[None, Unset, str]):
        litellm_params (Union['UpdateLiteLLMParams', None, Unset]):
        model_info (Union['ModelInfo', None, Unset]):
    """

    model_name: Union[None, Unset, str] = UNSET
    litellm_params: Union["UpdateLiteLLMParams", None, Unset] = UNSET
    model_info: Union["ModelInfo", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_info import ModelInfo
        from ..models.update_lite_llm_params import UpdateLiteLLMParams

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        litellm_params: Union[Dict[str, Any], None, Unset]
        if isinstance(self.litellm_params, Unset):
            litellm_params = UNSET
        elif isinstance(self.litellm_params, UpdateLiteLLMParams):
            litellm_params = self.litellm_params.to_dict()
        else:
            litellm_params = self.litellm_params

        model_info: Union[Dict[str, Any], None, Unset]
        if isinstance(self.model_info, Unset):
            model_info = UNSET
        elif isinstance(self.model_info, ModelInfo):
            model_info = self.model_info.to_dict()
        else:
            model_info = self.model_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if litellm_params is not UNSET:
            field_dict["litellm_params"] = litellm_params
        if model_info is not UNSET:
            field_dict["model_info"] = model_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_info import ModelInfo
        from ..models.update_lite_llm_params import UpdateLiteLLMParams

        d = src_dict.copy()

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("model_name", UNSET))

        def _parse_litellm_params(data: object) -> Union["UpdateLiteLLMParams", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_params_type_0 = UpdateLiteLLMParams.from_dict(data)

                return litellm_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateLiteLLMParams", None, Unset], data)

        litellm_params = _parse_litellm_params(d.pop("litellm_params", UNSET))

        def _parse_model_info(data: object) -> Union["ModelInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_info_type_0 = ModelInfo.from_dict(data)

                return model_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelInfo", None, Unset], data)

        model_info = _parse_model_info(d.pop("model_info", UNSET))

        update_deployment = cls(
            model_name=model_name,
            litellm_params=litellm_params,
            model_info=model_info,
        )

        update_deployment.additional_properties = d
        return update_deployment

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
