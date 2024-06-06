from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiteLLMParams")


@_attrs_define
class LiteLLMParams:
    """LiteLLM Params with 'model' requirement - used for completions

    Attributes:
        model (str):
        custom_llm_provider (Union[None, Unset, str]):
        tpm (Union[None, Unset, int]):
        rpm (Union[None, Unset, int]):
        api_key (Union[None, Unset, str]):
        api_base (Union[None, Unset, str]):
        api_version (Union[None, Unset, str]):
        timeout (Union[None, Unset, float, str]):
        stream_timeout (Union[None, Unset, float, str]):
        max_retries (Union[None, Unset, int]):
        organization (Union[None, Unset, str]):
        region_name (Union[None, Unset, str]):
        vertex_project (Union[None, Unset, str]):
        vertex_location (Union[None, Unset, str]):
        aws_access_key_id (Union[None, Unset, str]):
        aws_secret_access_key (Union[None, Unset, str]):
        aws_region_name (Union[None, Unset, str]):
        watsonx_region_name (Union[None, Unset, str]):
        input_cost_per_token (Union[None, Unset, float]):
        output_cost_per_token (Union[None, Unset, float]):
        input_cost_per_second (Union[None, Unset, float]):
        output_cost_per_second (Union[None, Unset, float]):
    """

    model: str
    custom_llm_provider: Union[None, Unset, str] = UNSET
    tpm: Union[None, Unset, int] = UNSET
    rpm: Union[None, Unset, int] = UNSET
    api_key: Union[None, Unset, str] = UNSET
    api_base: Union[None, Unset, str] = UNSET
    api_version: Union[None, Unset, str] = UNSET
    timeout: Union[None, Unset, float, str] = UNSET
    stream_timeout: Union[None, Unset, float, str] = UNSET
    max_retries: Union[None, Unset, int] = UNSET
    organization: Union[None, Unset, str] = UNSET
    region_name: Union[None, Unset, str] = UNSET
    vertex_project: Union[None, Unset, str] = UNSET
    vertex_location: Union[None, Unset, str] = UNSET
    aws_access_key_id: Union[None, Unset, str] = UNSET
    aws_secret_access_key: Union[None, Unset, str] = UNSET
    aws_region_name: Union[None, Unset, str] = UNSET
    watsonx_region_name: Union[None, Unset, str] = UNSET
    input_cost_per_token: Union[None, Unset, float] = UNSET
    output_cost_per_token: Union[None, Unset, float] = UNSET
    input_cost_per_second: Union[None, Unset, float] = UNSET
    output_cost_per_second: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model = self.model

        custom_llm_provider: Union[None, Unset, str]
        if isinstance(self.custom_llm_provider, Unset):
            custom_llm_provider = UNSET
        else:
            custom_llm_provider = self.custom_llm_provider

        tpm: Union[None, Unset, int]
        if isinstance(self.tpm, Unset):
            tpm = UNSET
        else:
            tpm = self.tpm

        rpm: Union[None, Unset, int]
        if isinstance(self.rpm, Unset):
            rpm = UNSET
        else:
            rpm = self.rpm

        api_key: Union[None, Unset, str]
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        api_base: Union[None, Unset, str]
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        api_version: Union[None, Unset, str]
        if isinstance(self.api_version, Unset):
            api_version = UNSET
        else:
            api_version = self.api_version

        timeout: Union[None, Unset, float, str]
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        stream_timeout: Union[None, Unset, float, str]
        if isinstance(self.stream_timeout, Unset):
            stream_timeout = UNSET
        else:
            stream_timeout = self.stream_timeout

        max_retries: Union[None, Unset, int]
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries

        organization: Union[None, Unset, str]
        if isinstance(self.organization, Unset):
            organization = UNSET
        else:
            organization = self.organization

        region_name: Union[None, Unset, str]
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        vertex_project: Union[None, Unset, str]
        if isinstance(self.vertex_project, Unset):
            vertex_project = UNSET
        else:
            vertex_project = self.vertex_project

        vertex_location: Union[None, Unset, str]
        if isinstance(self.vertex_location, Unset):
            vertex_location = UNSET
        else:
            vertex_location = self.vertex_location

        aws_access_key_id: Union[None, Unset, str]
        if isinstance(self.aws_access_key_id, Unset):
            aws_access_key_id = UNSET
        else:
            aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key: Union[None, Unset, str]
        if isinstance(self.aws_secret_access_key, Unset):
            aws_secret_access_key = UNSET
        else:
            aws_secret_access_key = self.aws_secret_access_key

        aws_region_name: Union[None, Unset, str]
        if isinstance(self.aws_region_name, Unset):
            aws_region_name = UNSET
        else:
            aws_region_name = self.aws_region_name

        watsonx_region_name: Union[None, Unset, str]
        if isinstance(self.watsonx_region_name, Unset):
            watsonx_region_name = UNSET
        else:
            watsonx_region_name = self.watsonx_region_name

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

        input_cost_per_second: Union[None, Unset, float]
        if isinstance(self.input_cost_per_second, Unset):
            input_cost_per_second = UNSET
        else:
            input_cost_per_second = self.input_cost_per_second

        output_cost_per_second: Union[None, Unset, float]
        if isinstance(self.output_cost_per_second, Unset):
            output_cost_per_second = UNSET
        else:
            output_cost_per_second = self.output_cost_per_second

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider
        if tpm is not UNSET:
            field_dict["tpm"] = tpm
        if rpm is not UNSET:
            field_dict["rpm"] = rpm
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if stream_timeout is not UNSET:
            field_dict["stream_timeout"] = stream_timeout
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if organization is not UNSET:
            field_dict["organization"] = organization
        if region_name is not UNSET:
            field_dict["region_name"] = region_name
        if vertex_project is not UNSET:
            field_dict["vertex_project"] = vertex_project
        if vertex_location is not UNSET:
            field_dict["vertex_location"] = vertex_location
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key
        if aws_region_name is not UNSET:
            field_dict["aws_region_name"] = aws_region_name
        if watsonx_region_name is not UNSET:
            field_dict["watsonx_region_name"] = watsonx_region_name
        if input_cost_per_token is not UNSET:
            field_dict["input_cost_per_token"] = input_cost_per_token
        if output_cost_per_token is not UNSET:
            field_dict["output_cost_per_token"] = output_cost_per_token
        if input_cost_per_second is not UNSET:
            field_dict["input_cost_per_second"] = input_cost_per_second
        if output_cost_per_second is not UNSET:
            field_dict["output_cost_per_second"] = output_cost_per_second

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        model = d.pop("model")

        def _parse_custom_llm_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_llm_provider = _parse_custom_llm_provider(d.pop("custom_llm_provider", UNSET))

        def _parse_tpm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tpm = _parse_tpm(d.pop("tpm", UNSET))

        def _parse_rpm(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rpm = _parse_rpm(d.pop("rpm", UNSET))

        def _parse_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_api_base(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))

        def _parse_api_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        api_version = _parse_api_version(d.pop("api_version", UNSET))

        def _parse_timeout(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_stream_timeout(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        stream_timeout = _parse_stream_timeout(d.pop("stream_timeout", UNSET))

        def _parse_max_retries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))

        def _parse_organization(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region_name = _parse_region_name(d.pop("region_name", UNSET))

        def _parse_vertex_project(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vertex_project = _parse_vertex_project(d.pop("vertex_project", UNSET))

        def _parse_vertex_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vertex_location = _parse_vertex_location(d.pop("vertex_location", UNSET))

        def _parse_aws_access_key_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_access_key_id = _parse_aws_access_key_id(d.pop("aws_access_key_id", UNSET))

        def _parse_aws_secret_access_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_secret_access_key = _parse_aws_secret_access_key(d.pop("aws_secret_access_key", UNSET))

        def _parse_aws_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_region_name = _parse_aws_region_name(d.pop("aws_region_name", UNSET))

        def _parse_watsonx_region_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        watsonx_region_name = _parse_watsonx_region_name(d.pop("watsonx_region_name", UNSET))

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

        def _parse_input_cost_per_second(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        input_cost_per_second = _parse_input_cost_per_second(d.pop("input_cost_per_second", UNSET))

        def _parse_output_cost_per_second(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        output_cost_per_second = _parse_output_cost_per_second(d.pop("output_cost_per_second", UNSET))

        lite_llm_params = cls(
            model=model,
            custom_llm_provider=custom_llm_provider,
            tpm=tpm,
            rpm=rpm,
            api_key=api_key,
            api_base=api_base,
            api_version=api_version,
            timeout=timeout,
            stream_timeout=stream_timeout,
            max_retries=max_retries,
            organization=organization,
            region_name=region_name,
            vertex_project=vertex_project,
            vertex_location=vertex_location,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_region_name=aws_region_name,
            watsonx_region_name=watsonx_region_name,
            input_cost_per_token=input_cost_per_token,
            output_cost_per_token=output_cost_per_token,
            input_cost_per_second=input_cost_per_second,
            output_cost_per_second=output_cost_per_second,
        )

        lite_llm_params.additional_properties = d
        return lite_llm_params

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
