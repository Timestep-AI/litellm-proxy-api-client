from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.key_request import KeyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: KeyRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/key/delete",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: KeyRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Delete Key Fn

     Delete a key from the key management system.

    Parameters::
    - keys (List[str]): A list of keys or hashed keys to delete. Example {\"keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}

    Returns:
    - deleted_keys (List[str]): A list of deleted keys. Example {\"deleted_keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}


    Raises:
        HTTPException: If an error occurs during key deletion.

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        litellm_changed_by=litellm_changed_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: KeyRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Delete Key Fn

     Delete a key from the key management system.

    Parameters::
    - keys (List[str]): A list of keys or hashed keys to delete. Example {\"keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}

    Returns:
    - deleted_keys (List[str]): A list of deleted keys. Example {\"deleted_keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}


    Raises:
        HTTPException: If an error occurs during key deletion.

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        litellm_changed_by=litellm_changed_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: KeyRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Delete Key Fn

     Delete a key from the key management system.

    Parameters::
    - keys (List[str]): A list of keys or hashed keys to delete. Example {\"keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}

    Returns:
    - deleted_keys (List[str]): A list of deleted keys. Example {\"deleted_keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}


    Raises:
        HTTPException: If an error occurs during key deletion.

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        litellm_changed_by=litellm_changed_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: KeyRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Delete Key Fn

     Delete a key from the key management system.

    Parameters::
    - keys (List[str]): A list of keys or hashed keys to delete. Example {\"keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}

    Returns:
    - deleted_keys (List[str]): A list of deleted keys. Example {\"deleted_keys\": [\"sk-
    QWrxEynunsNpV1zT48HIrw\", \"837e17519f44683334df5291321d97b8bf1098cd490e49e215f6fea935aa28be\"]}


    Raises:
        HTTPException: If an error occurs during key deletion.

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            litellm_changed_by=litellm_changed_by,
        )
    ).parsed
