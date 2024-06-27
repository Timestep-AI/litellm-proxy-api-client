from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spend_calculate_request_completion_response_type_0 import SpendCalculateRequestCompletionResponseType0


T = TypeVar("T", bound="SpendCalculateRequest")


@_attrs_define
class SpendCalculateRequest:
    """
    Attributes:
        model (Union[None, Unset, str]):
        messages (Union[List[Any], None, Unset]):
        completion_response (Union['SpendCalculateRequestCompletionResponseType0', None, Unset]):
    """

    model: Union[None, Unset, str] = UNSET
    messages: Union[List[Any], None, Unset] = UNSET
    completion_response: Union["SpendCalculateRequestCompletionResponseType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.spend_calculate_request_completion_response_type_0 import (
            SpendCalculateRequestCompletionResponseType0,
        )

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        messages: Union[List[Any], None, Unset]
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = self.messages

        else:
            messages = self.messages

        completion_response: Union[Dict[str, Any], None, Unset]
        if isinstance(self.completion_response, Unset):
            completion_response = UNSET
        elif isinstance(self.completion_response, SpendCalculateRequestCompletionResponseType0):
            completion_response = self.completion_response.to_dict()
        else:
            completion_response = self.completion_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if messages is not UNSET:
            field_dict["messages"] = messages
        if completion_response is not UNSET:
            field_dict["completion_response"] = completion_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.spend_calculate_request_completion_response_type_0 import (
            SpendCalculateRequestCompletionResponseType0,
        )

        d = src_dict.copy()

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_messages(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = cast(List[Any], data)

                return messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        messages = _parse_messages(d.pop("messages", UNSET))

        def _parse_completion_response(
            data: object,
        ) -> Union["SpendCalculateRequestCompletionResponseType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                completion_response_type_0 = SpendCalculateRequestCompletionResponseType0.from_dict(data)

                return completion_response_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SpendCalculateRequestCompletionResponseType0", None, Unset], data)

        completion_response = _parse_completion_response(d.pop("completion_response", UNSET))

        spend_calculate_request = cls(
            model=model,
            messages=messages,
            completion_response=completion_response,
        )

        spend_calculate_request.additional_properties = d
        return spend_calculate_request

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
