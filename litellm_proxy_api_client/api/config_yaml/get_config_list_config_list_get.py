from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_list import ConfigList
from ...models.get_config_list_config_list_get_config_type import GetConfigListConfigListGetConfigType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    config_type: GetConfigListConfigListGetConfigType,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_config_type = config_type.value
    params["config_type"] = json_config_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/config/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["ConfigList"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConfigList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, List["ConfigList"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    config_type: GetConfigListConfigListGetConfigType,
) -> Response[Union[HTTPValidationError, List["ConfigList"]]]:
    """Get Config List

     List the available fields + current values for a given type of setting (currently just
    'general_settings'user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),)

    Args:
        config_type (GetConfigListConfigListGetConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ConfigList']]]
    """

    kwargs = _get_kwargs(
        config_type=config_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    config_type: GetConfigListConfigListGetConfigType,
) -> Optional[Union[HTTPValidationError, List["ConfigList"]]]:
    """Get Config List

     List the available fields + current values for a given type of setting (currently just
    'general_settings'user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),)

    Args:
        config_type (GetConfigListConfigListGetConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ConfigList']]
    """

    return sync_detailed(
        client=client,
        config_type=config_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    config_type: GetConfigListConfigListGetConfigType,
) -> Response[Union[HTTPValidationError, List["ConfigList"]]]:
    """Get Config List

     List the available fields + current values for a given type of setting (currently just
    'general_settings'user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),)

    Args:
        config_type (GetConfigListConfigListGetConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ConfigList']]]
    """

    kwargs = _get_kwargs(
        config_type=config_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    config_type: GetConfigListConfigListGetConfigType,
) -> Optional[Union[HTTPValidationError, List["ConfigList"]]]:
    """Get Config List

     List the available fields + current values for a given type of setting (currently just
    'general_settings'user_api_key_dict: UserAPIKeyAuth = Depends(user_api_key_auth),)

    Args:
        config_type (GetConfigListConfigListGetConfigType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ConfigList']]
    """

    return (
        await asyncio_detailed(
            client=client,
            config_type=config_type,
        )
    ).parsed
