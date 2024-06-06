from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dynamo_db_args_billing_mode import DynamoDBArgsBillingMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamoDBArgs")


@_attrs_define
class DynamoDBArgs:
    """
    Attributes:
        billing_mode (DynamoDBArgsBillingMode):
        region_name (str):
        read_capacity_units (Union[None, Unset, int]):
        write_capacity_units (Union[None, Unset, int]):
        ssl_verify (Union[None, Unset, bool]):
        user_table_name (Union[Unset, str]):  Default: 'LiteLLM_UserTable'.
        key_table_name (Union[Unset, str]):  Default: 'LiteLLM_VerificationToken'.
        config_table_name (Union[Unset, str]):  Default: 'LiteLLM_Config'.
        spend_table_name (Union[Unset, str]):  Default: 'LiteLLM_SpendLogs'.
        aws_role_name (Union[None, Unset, str]):
        aws_session_name (Union[None, Unset, str]):
        aws_web_identity_token (Union[None, Unset, str]):
        aws_provider_id (Union[None, Unset, str]):
        aws_policy_arns (Union[List[str], None, Unset]):
        aws_policy (Union[None, Unset, str]):
        aws_duration_seconds (Union[None, Unset, int]):
        assume_role_aws_role_name (Union[None, Unset, str]):
        assume_role_aws_session_name (Union[None, Unset, str]):
    """

    billing_mode: DynamoDBArgsBillingMode
    region_name: str
    read_capacity_units: Union[None, Unset, int] = UNSET
    write_capacity_units: Union[None, Unset, int] = UNSET
    ssl_verify: Union[None, Unset, bool] = UNSET
    user_table_name: Union[Unset, str] = "LiteLLM_UserTable"
    key_table_name: Union[Unset, str] = "LiteLLM_VerificationToken"
    config_table_name: Union[Unset, str] = "LiteLLM_Config"
    spend_table_name: Union[Unset, str] = "LiteLLM_SpendLogs"
    aws_role_name: Union[None, Unset, str] = UNSET
    aws_session_name: Union[None, Unset, str] = UNSET
    aws_web_identity_token: Union[None, Unset, str] = UNSET
    aws_provider_id: Union[None, Unset, str] = UNSET
    aws_policy_arns: Union[List[str], None, Unset] = UNSET
    aws_policy: Union[None, Unset, str] = UNSET
    aws_duration_seconds: Union[None, Unset, int] = UNSET
    assume_role_aws_role_name: Union[None, Unset, str] = UNSET
    assume_role_aws_session_name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_mode = self.billing_mode.value

        region_name = self.region_name

        read_capacity_units: Union[None, Unset, int]
        if isinstance(self.read_capacity_units, Unset):
            read_capacity_units = UNSET
        else:
            read_capacity_units = self.read_capacity_units

        write_capacity_units: Union[None, Unset, int]
        if isinstance(self.write_capacity_units, Unset):
            write_capacity_units = UNSET
        else:
            write_capacity_units = self.write_capacity_units

        ssl_verify: Union[None, Unset, bool]
        if isinstance(self.ssl_verify, Unset):
            ssl_verify = UNSET
        else:
            ssl_verify = self.ssl_verify

        user_table_name = self.user_table_name

        key_table_name = self.key_table_name

        config_table_name = self.config_table_name

        spend_table_name = self.spend_table_name

        aws_role_name: Union[None, Unset, str]
        if isinstance(self.aws_role_name, Unset):
            aws_role_name = UNSET
        else:
            aws_role_name = self.aws_role_name

        aws_session_name: Union[None, Unset, str]
        if isinstance(self.aws_session_name, Unset):
            aws_session_name = UNSET
        else:
            aws_session_name = self.aws_session_name

        aws_web_identity_token: Union[None, Unset, str]
        if isinstance(self.aws_web_identity_token, Unset):
            aws_web_identity_token = UNSET
        else:
            aws_web_identity_token = self.aws_web_identity_token

        aws_provider_id: Union[None, Unset, str]
        if isinstance(self.aws_provider_id, Unset):
            aws_provider_id = UNSET
        else:
            aws_provider_id = self.aws_provider_id

        aws_policy_arns: Union[List[str], None, Unset]
        if isinstance(self.aws_policy_arns, Unset):
            aws_policy_arns = UNSET
        elif isinstance(self.aws_policy_arns, list):
            aws_policy_arns = self.aws_policy_arns

        else:
            aws_policy_arns = self.aws_policy_arns

        aws_policy: Union[None, Unset, str]
        if isinstance(self.aws_policy, Unset):
            aws_policy = UNSET
        else:
            aws_policy = self.aws_policy

        aws_duration_seconds: Union[None, Unset, int]
        if isinstance(self.aws_duration_seconds, Unset):
            aws_duration_seconds = UNSET
        else:
            aws_duration_seconds = self.aws_duration_seconds

        assume_role_aws_role_name: Union[None, Unset, str]
        if isinstance(self.assume_role_aws_role_name, Unset):
            assume_role_aws_role_name = UNSET
        else:
            assume_role_aws_role_name = self.assume_role_aws_role_name

        assume_role_aws_session_name: Union[None, Unset, str]
        if isinstance(self.assume_role_aws_session_name, Unset):
            assume_role_aws_session_name = UNSET
        else:
            assume_role_aws_session_name = self.assume_role_aws_session_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing_mode": billing_mode,
                "region_name": region_name,
            }
        )
        if read_capacity_units is not UNSET:
            field_dict["read_capacity_units"] = read_capacity_units
        if write_capacity_units is not UNSET:
            field_dict["write_capacity_units"] = write_capacity_units
        if ssl_verify is not UNSET:
            field_dict["ssl_verify"] = ssl_verify
        if user_table_name is not UNSET:
            field_dict["user_table_name"] = user_table_name
        if key_table_name is not UNSET:
            field_dict["key_table_name"] = key_table_name
        if config_table_name is not UNSET:
            field_dict["config_table_name"] = config_table_name
        if spend_table_name is not UNSET:
            field_dict["spend_table_name"] = spend_table_name
        if aws_role_name is not UNSET:
            field_dict["aws_role_name"] = aws_role_name
        if aws_session_name is not UNSET:
            field_dict["aws_session_name"] = aws_session_name
        if aws_web_identity_token is not UNSET:
            field_dict["aws_web_identity_token"] = aws_web_identity_token
        if aws_provider_id is not UNSET:
            field_dict["aws_provider_id"] = aws_provider_id
        if aws_policy_arns is not UNSET:
            field_dict["aws_policy_arns"] = aws_policy_arns
        if aws_policy is not UNSET:
            field_dict["aws_policy"] = aws_policy
        if aws_duration_seconds is not UNSET:
            field_dict["aws_duration_seconds"] = aws_duration_seconds
        if assume_role_aws_role_name is not UNSET:
            field_dict["assume_role_aws_role_name"] = assume_role_aws_role_name
        if assume_role_aws_session_name is not UNSET:
            field_dict["assume_role_aws_session_name"] = assume_role_aws_session_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_mode = DynamoDBArgsBillingMode(d.pop("billing_mode"))

        region_name = d.pop("region_name")

        def _parse_read_capacity_units(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        read_capacity_units = _parse_read_capacity_units(d.pop("read_capacity_units", UNSET))

        def _parse_write_capacity_units(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        write_capacity_units = _parse_write_capacity_units(d.pop("write_capacity_units", UNSET))

        def _parse_ssl_verify(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        ssl_verify = _parse_ssl_verify(d.pop("ssl_verify", UNSET))

        user_table_name = d.pop("user_table_name", UNSET)

        key_table_name = d.pop("key_table_name", UNSET)

        config_table_name = d.pop("config_table_name", UNSET)

        spend_table_name = d.pop("spend_table_name", UNSET)

        def _parse_aws_role_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_role_name = _parse_aws_role_name(d.pop("aws_role_name", UNSET))

        def _parse_aws_session_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_session_name = _parse_aws_session_name(d.pop("aws_session_name", UNSET))

        def _parse_aws_web_identity_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_web_identity_token = _parse_aws_web_identity_token(d.pop("aws_web_identity_token", UNSET))

        def _parse_aws_provider_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_provider_id = _parse_aws_provider_id(d.pop("aws_provider_id", UNSET))

        def _parse_aws_policy_arns(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_policy_arns_type_0 = cast(List[str], data)

                return aws_policy_arns_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        aws_policy_arns = _parse_aws_policy_arns(d.pop("aws_policy_arns", UNSET))

        def _parse_aws_policy(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        aws_policy = _parse_aws_policy(d.pop("aws_policy", UNSET))

        def _parse_aws_duration_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        aws_duration_seconds = _parse_aws_duration_seconds(d.pop("aws_duration_seconds", UNSET))

        def _parse_assume_role_aws_role_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assume_role_aws_role_name = _parse_assume_role_aws_role_name(d.pop("assume_role_aws_role_name", UNSET))

        def _parse_assume_role_aws_session_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assume_role_aws_session_name = _parse_assume_role_aws_session_name(d.pop("assume_role_aws_session_name", UNSET))

        dynamo_db_args = cls(
            billing_mode=billing_mode,
            region_name=region_name,
            read_capacity_units=read_capacity_units,
            write_capacity_units=write_capacity_units,
            ssl_verify=ssl_verify,
            user_table_name=user_table_name,
            key_table_name=key_table_name,
            config_table_name=config_table_name,
            spend_table_name=spend_table_name,
            aws_role_name=aws_role_name,
            aws_session_name=aws_session_name,
            aws_web_identity_token=aws_web_identity_token,
            aws_provider_id=aws_provider_id,
            aws_policy_arns=aws_policy_arns,
            aws_policy=aws_policy,
            aws_duration_seconds=aws_duration_seconds,
            assume_role_aws_role_name=assume_role_aws_role_name,
            assume_role_aws_session_name=assume_role_aws_session_name,
        )

        dynamo_db_args.additional_properties = d
        return dynamo_db_args

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
