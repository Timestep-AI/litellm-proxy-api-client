from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_user_request_user_role_type_0 import UpdateUserRequestUserRoleType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_user_request_metadata_type_0 import UpdateUserRequestMetadataType0


T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
    """
    Attributes:
        models (Union[List[Any], None, Unset]):
        spend (Union[None, Unset, float]):
        max_budget (Union[None, Unset, float]):
        user_id (Union[None, Unset, str]):
        team_id (Union[None, Unset, str]):
        max_parallel_requests (Union[None, Unset, int]):
        metadata (Union['UpdateUserRequestMetadataType0', None, Unset]):
        tpm_limit (Union[None, Unset, int]):
        rpm_limit (Union[None, Unset, int]):
        budget_duration (Union[None, Unset, str]):
        allowed_cache_controls (Union[List[Any], None, Unset]):
        soft_budget (Union[None, Unset, float]):
        password (Union[None, Unset, str]):
        user_email (Union[None, Unset, str]):
        user_role (Union[None, Unset, UpdateUserRequestUserRoleType0]):
    """

    models: Union[List[Any], None, Unset] = UNSET
    spend: Union[None, Unset, float] = UNSET
    max_budget: Union[None, Unset, float] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    team_id: Union[None, Unset, str] = UNSET
    max_parallel_requests: Union[None, Unset, int] = UNSET
    metadata: Union["UpdateUserRequestMetadataType0", None, Unset] = UNSET
    tpm_limit: Union[None, Unset, int] = UNSET
    rpm_limit: Union[None, Unset, int] = UNSET
    budget_duration: Union[None, Unset, str] = UNSET
    allowed_cache_controls: Union[List[Any], None, Unset] = UNSET
    soft_budget: Union[None, Unset, float] = UNSET
    password: Union[None, Unset, str] = UNSET
    user_email: Union[None, Unset, str] = UNSET
    user_role: Union[None, Unset, UpdateUserRequestUserRoleType0] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.update_user_request_metadata_type_0 import UpdateUserRequestMetadataType0

        models: Union[List[Any], None, Unset]
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models

        else:
            models = self.models

        spend: Union[None, Unset, float]
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        max_budget: Union[None, Unset, float]
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        team_id: Union[None, Unset, str]
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        max_parallel_requests: Union[None, Unset, int]
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateUserRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        tpm_limit: Union[None, Unset, int]
        if isinstance(self.tpm_limit, Unset):
            tpm_limit = UNSET
        else:
            tpm_limit = self.tpm_limit

        rpm_limit: Union[None, Unset, int]
        if isinstance(self.rpm_limit, Unset):
            rpm_limit = UNSET
        else:
            rpm_limit = self.rpm_limit

        budget_duration: Union[None, Unset, str]
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        allowed_cache_controls: Union[List[Any], None, Unset]
        if isinstance(self.allowed_cache_controls, Unset):
            allowed_cache_controls = UNSET
        elif isinstance(self.allowed_cache_controls, list):
            allowed_cache_controls = self.allowed_cache_controls

        else:
            allowed_cache_controls = self.allowed_cache_controls

        soft_budget: Union[None, Unset, float]
        if isinstance(self.soft_budget, Unset):
            soft_budget = UNSET
        else:
            soft_budget = self.soft_budget

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        user_email: Union[None, Unset, str]
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_role: Union[None, Unset, str]
        if isinstance(self.user_role, Unset):
            user_role = UNSET
        elif isinstance(self.user_role, UpdateUserRequestUserRoleType0):
            user_role = self.user_role.value
        else:
            user_role = self.user_role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if models is not UNSET:
            field_dict["models"] = models
        if spend is not UNSET:
            field_dict["spend"] = spend
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if allowed_cache_controls is not UNSET:
            field_dict["allowed_cache_controls"] = allowed_cache_controls
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if password is not UNSET:
            field_dict["password"] = password
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_role is not UNSET:
            field_dict["user_role"] = user_role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_user_request_metadata_type_0 import UpdateUserRequestMetadataType0

        d = src_dict.copy()

        def _parse_models(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(List[Any], data)

                return models_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        models = _parse_models(d.pop("models", UNSET))

        def _parse_spend(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        spend = _parse_spend(d.pop("spend", UNSET))

        def _parse_max_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))

        def _parse_max_parallel_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))

        def _parse_metadata(data: object) -> Union["UpdateUserRequestMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateUserRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateUserRequestMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_tpm_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit", UNSET))

        def _parse_rpm_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit", UNSET))

        def _parse_budget_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))

        def _parse_allowed_cache_controls(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_cache_controls_type_0 = cast(List[Any], data)

                return allowed_cache_controls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        allowed_cache_controls = _parse_allowed_cache_controls(d.pop("allowed_cache_controls", UNSET))

        def _parse_soft_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        soft_budget = _parse_soft_budget(d.pop("soft_budget", UNSET))

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_user_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_role(data: object) -> Union[None, Unset, UpdateUserRequestUserRoleType0]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_role_type_0 = UpdateUserRequestUserRoleType0(data)

                return user_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, UpdateUserRequestUserRoleType0], data)

        user_role = _parse_user_role(d.pop("user_role", UNSET))

        update_user_request = cls(
            models=models,
            spend=spend,
            max_budget=max_budget,
            user_id=user_id,
            team_id=team_id,
            max_parallel_requests=max_parallel_requests,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            budget_duration=budget_duration,
            allowed_cache_controls=allowed_cache_controls,
            soft_budget=soft_budget,
            password=password,
            user_email=user_email,
            user_role=user_role,
        )

        update_user_request.additional_properties = d
        return update_user_request

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
