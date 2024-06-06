from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_info_base_model_type_0 import ModelInfoBaseModelType0
from ..models.model_info_mode_type_0 import ModelInfoModeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelInfo")


@_attrs_define
class ModelInfo:
    """
    Attributes:
        id (Union[None, str]):
        mode (Union[ModelInfoModeType0, None]):
        base_model (Union[ModelInfoBaseModelType0, None]):
        input_cost_per_token (Union[None, Unset, float]):  Default: 0.0.
        output_cost_per_token (Union[None, Unset, float]):  Default: 0.0.
        max_tokens (Union[None, Unset, int]):  Default: 2048.
    """

    id: Union[None, str]
    mode: Union[ModelInfoModeType0, None]
    base_model: Union[ModelInfoBaseModelType0, None]
    input_cost_per_token: Union[None, Unset, float] = 0.0
    output_cost_per_token: Union[None, Unset, float] = 0.0
    max_tokens: Union[None, Unset, int] = 2048
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, str]
        id = self.id

        mode: Union[None, str]
        if isinstance(self.mode, ModelInfoModeType0):
            mode = self.mode.value
        else:
            mode = self.mode

        base_model: Union[None, str]
        if isinstance(self.base_model, ModelInfoBaseModelType0):
            base_model = self.base_model.value
        else:
            base_model = self.base_model

        input_cost_per_token: Union[None, Unset, float]
        if isinstance(self.input_cost_per_token, Unset):
            input_cost_per_token = UNSET
        else:
            input_cost_per_token = self.input_cost_per_token

        output_cost_per_token: Union[None, Unset, float]
        if isinstance(self.output_cost_per_token, Unset):
            output_cost_per_token = UNSET
        else:
            output_cost_per_token = self.output_cost_per_token

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "mode": mode,
                "base_model": base_model,
            }
        )
        if input_cost_per_token is not UNSET:
            field_dict["input_cost_per_token"] = input_cost_per_token
        if output_cost_per_token is not UNSET:
            field_dict["output_cost_per_token"] = output_cost_per_token
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        id = _parse_id(d.pop("id"))

        def _parse_mode(data: object) -> Union[ModelInfoModeType0, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_0 = ModelInfoModeType0(data)

                return mode_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ModelInfoModeType0, None], data)

        mode = _parse_mode(d.pop("mode"))

        def _parse_base_model(data: object) -> Union[ModelInfoBaseModelType0, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_model_type_0 = ModelInfoBaseModelType0(data)

                return base_model_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ModelInfoBaseModelType0, None], data)

        base_model = _parse_base_model(d.pop("base_model"))

        def _parse_input_cost_per_token(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        input_cost_per_token = _parse_input_cost_per_token(d.pop("input_cost_per_token", UNSET))

        def _parse_output_cost_per_token(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        output_cost_per_token = _parse_output_cost_per_token(d.pop("output_cost_per_token", UNSET))

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        model_info = cls(
            id=id,
            mode=mode,
            base_model=base_model,
            input_cost_per_token=input_cost_per_token,
            output_cost_per_token=output_cost_per_token,
            max_tokens=max_tokens,
        )

        model_info.additional_properties = d
        return model_info

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
