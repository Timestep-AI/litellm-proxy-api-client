from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.invitation_model import InvitationModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    invitation_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["invitation_id"] = invitation_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/invitation/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, InvitationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InvitationModel.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, InvitationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    invitation_id: str,
) -> Response[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Info

     Allow admin to create invite links, to onboard new users to Admin UI.

    ```
    curl -X POST 'http://localhost:4000/invitation/new'         -H 'Content-Type: application/json'
    -D '{
            \"user_id\": \"1234\" // 👈 id of user in 'LiteLLM_UserTable'
        }'
    ```

    Args:
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvitationModel]]
    """

    kwargs = _get_kwargs(
        invitation_id=invitation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    invitation_id: str,
) -> Optional[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Info

     Allow admin to create invite links, to onboard new users to Admin UI.

    ```
    curl -X POST 'http://localhost:4000/invitation/new'         -H 'Content-Type: application/json'
    -D '{
            \"user_id\": \"1234\" // 👈 id of user in 'LiteLLM_UserTable'
        }'
    ```

    Args:
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvitationModel]
    """

    return sync_detailed(
        client=client,
        invitation_id=invitation_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    invitation_id: str,
) -> Response[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Info

     Allow admin to create invite links, to onboard new users to Admin UI.

    ```
    curl -X POST 'http://localhost:4000/invitation/new'         -H 'Content-Type: application/json'
    -D '{
            \"user_id\": \"1234\" // 👈 id of user in 'LiteLLM_UserTable'
        }'
    ```

    Args:
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvitationModel]]
    """

    kwargs = _get_kwargs(
        invitation_id=invitation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    invitation_id: str,
) -> Optional[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Info

     Allow admin to create invite links, to onboard new users to Admin UI.

    ```
    curl -X POST 'http://localhost:4000/invitation/new'         -H 'Content-Type: application/json'
    -D '{
            \"user_id\": \"1234\" // 👈 id of user in 'LiteLLM_UserTable'
        }'
    ```

    Args:
        invitation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvitationModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            invitation_id=invitation_id,
        )
    ).parsed
