import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiteLLMSpendLogs")


@_attrs_define
class LiteLLMSpendLogs:
    """
    Attributes:
        request_id (str):
        api_key (str):
        call_type (str):
        start_time (Union[None, datetime.datetime, str]):
        end_time (Union[None, datetime.datetime, str]):
        model (Union[None, Unset, str]):  Default: ''.
        api_base (Union[None, Unset, str]):  Default: ''.
        spend (Union[None, Unset, float]):  Default: 0.0.
        total_tokens (Union[None, Unset, int]):  Default: 0.
        prompt_tokens (Union[None, Unset, int]):  Default: 0.
        completion_tokens (Union[None, Unset, int]):  Default: 0.
        user (Union[None, Unset, str]):  Default: ''.
        metadata (Union[None, Unset, str]):  Default: '{}'.
        cache_hit (Union[None, Unset, str]):  Default: 'False'.
        cache_key (Union[None, Unset, str]):
        request_tags (Union[None, Unset, str]):
    """

    request_id: str
    api_key: str
    call_type: str
    start_time: Union[None, datetime.datetime, str]
    end_time: Union[None, datetime.datetime, str]
    model: Union[None, Unset, str] = ""
    api_base: Union[None, Unset, str] = ""
    spend: Union[None, Unset, float] = 0.0
    total_tokens: Union[None, Unset, int] = 0
    prompt_tokens: Union[None, Unset, int] = 0
    completion_tokens: Union[None, Unset, int] = 0
    user: Union[None, Unset, str] = ""
    metadata: Union[None, Unset, str] = "{}"
    cache_hit: Union[None, Unset, str] = "False"
    cache_key: Union[None, Unset, str] = UNSET
    request_tags: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        api_key = self.api_key

        call_type = self.call_type

        start_time: Union[None, str]
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: Union[None, str]
        if isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        api_base: Union[None, Unset, str]
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        spend: Union[None, Unset, float]
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        total_tokens: Union[None, Unset, int]
        if isinstance(self.total_tokens, Unset):
            total_tokens = UNSET
        else:
            total_tokens = self.total_tokens

        prompt_tokens: Union[None, Unset, int]
        if isinstance(self.prompt_tokens, Unset):
            prompt_tokens = UNSET
        else:
            prompt_tokens = self.prompt_tokens

        completion_tokens: Union[None, Unset, int]
        if isinstance(self.completion_tokens, Unset):
            completion_tokens = UNSET
        else:
            completion_tokens = self.completion_tokens

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        metadata: Union[None, Unset, str]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        cache_hit: Union[None, Unset, str]
        if isinstance(self.cache_hit, Unset):
            cache_hit = UNSET
        else:
            cache_hit = self.cache_hit

        cache_key: Union[None, Unset, str]
        if isinstance(self.cache_key, Unset):
            cache_key = UNSET
        else:
            cache_key = self.cache_key

        request_tags: Union[None, Unset, str]
        if isinstance(self.request_tags, Unset):
            request_tags = UNSET
        else:
            request_tags = self.request_tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_id": request_id,
                "api_key": api_key,
                "call_type": call_type,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if user is not UNSET:
            field_dict["user"] = user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if cache_hit is not UNSET:
            field_dict["cache_hit"] = cache_hit
        if cache_key is not UNSET:
            field_dict["cache_key"] = cache_key
        if request_tags is not UNSET:
            field_dict["request_tags"] = request_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("request_id")

        api_key = d.pop("api_key")

        call_type = d.pop("call_type")

        def _parse_start_time(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_1 = isoparse(data)

                return start_time_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        start_time = _parse_start_time(d.pop("startTime"))

        def _parse_end_time(data: object) -> Union[None, datetime.datetime, str]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_1 = isoparse(data)

                return end_time_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime, str], data)

        end_time = _parse_end_time(d.pop("endTime"))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_api_base(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))

        def _parse_spend(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        spend = _parse_spend(d.pop("spend", UNSET))

        def _parse_total_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_tokens = _parse_total_tokens(d.pop("total_tokens", UNSET))

        def _parse_prompt_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        prompt_tokens = _parse_prompt_tokens(d.pop("prompt_tokens", UNSET))

        def _parse_completion_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        completion_tokens = _parse_completion_tokens(d.pop("completion_tokens", UNSET))

        def _parse_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_metadata(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_cache_hit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cache_hit = _parse_cache_hit(d.pop("cache_hit", UNSET))

        def _parse_cache_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cache_key = _parse_cache_key(d.pop("cache_key", UNSET))

        def _parse_request_tags(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        request_tags = _parse_request_tags(d.pop("request_tags", UNSET))

        lite_llm_spend_logs = cls(
            request_id=request_id,
            api_key=api_key,
            call_type=call_type,
            start_time=start_time,
            end_time=end_time,
            model=model,
            api_base=api_base,
            spend=spend,
            total_tokens=total_tokens,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            user=user,
            metadata=metadata,
            cache_hit=cache_hit,
            cache_key=cache_key,
            request_tags=request_tags,
        )

        lite_llm_spend_logs.additional_properties = d
        return lite_llm_spend_logs

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
