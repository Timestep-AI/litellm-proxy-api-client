from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.invitation_delete import InvitationDelete
from ...models.invitation_model import InvitationModel
from ...types import Response


def _get_kwargs(
    *,
    body: InvitationDelete,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invitation/delete",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: InvitationDelete,
) -> Response[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Delete

     Delete invitation link

    ```
    curl -X POST 'http://localhost:4000/invitation/delete'         -H 'Content-Type: application/json'
    -D '{
            \"invitation_id\": \"1234\" // 👈 id of invitation in 'LiteLLM_InvitationTable'
        }'
    ```

    Args:
        body (InvitationDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvitationModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InvitationDelete,
) -> Optional[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Delete

     Delete invitation link

    ```
    curl -X POST 'http://localhost:4000/invitation/delete'         -H 'Content-Type: application/json'
    -D '{
            \"invitation_id\": \"1234\" // 👈 id of invitation in 'LiteLLM_InvitationTable'
        }'
    ```

    Args:
        body (InvitationDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvitationModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InvitationDelete,
) -> Response[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Delete

     Delete invitation link

    ```
    curl -X POST 'http://localhost:4000/invitation/delete'         -H 'Content-Type: application/json'
    -D '{
            \"invitation_id\": \"1234\" // 👈 id of invitation in 'LiteLLM_InvitationTable'
        }'
    ```

    Args:
        body (InvitationDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvitationModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InvitationDelete,
) -> Optional[Union[HTTPValidationError, InvitationModel]]:
    r"""Invitation Delete

     Delete invitation link

    ```
    curl -X POST 'http://localhost:4000/invitation/delete'         -H 'Content-Type: application/json'
    -D '{
            \"invitation_id\": \"1234\" // 👈 id of invitation in 'LiteLLM_InvitationTable'
        }'
    ```

    Args:
        body (InvitationDelete):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvitationModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
