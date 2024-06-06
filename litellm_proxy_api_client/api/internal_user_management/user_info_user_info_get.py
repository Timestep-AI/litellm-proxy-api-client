from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[None, Unset, str] = UNSET,
    view_all: Union[Unset, bool] = False,
    page: Union[None, Unset, int] = 0,
    page_size: Union[None, Unset, int] = 25,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_user_id: Union[None, Unset, str]
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    params["view_all"] = view_all

    json_page: Union[None, Unset, int]
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    json_page_size: Union[None, Unset, int]
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/user/info",
        "params": params,
    }

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
    user_id: Union[None, Unset, str] = UNSET,
    view_all: Union[Unset, bool] = False,
    page: Union[None, Unset, int] = 0,
    page_size: Union[None, Unset, int] = 25,
) -> Response[Union[Any, HTTPValidationError]]:
    """User Info

     Use this to get user information. (user row + all user key info)

    Example request
    ```
    curl -X GET 'http://localhost:8000/user/info?user_id=krrish7%40berri.ai'     --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (Union[None, Unset, str]): User ID in the request parameters
        view_all (Union[Unset, bool]): set to true to View all users. When using view_all, don't
            pass user_id Default: False.
        page (Union[None, Unset, int]): Page number for pagination. Only use when view_all is true
            Default: 0.
        page_size (Union[None, Unset, int]): Number of items per page. Only use when view_all is
            true Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        view_all=view_all,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[None, Unset, str] = UNSET,
    view_all: Union[Unset, bool] = False,
    page: Union[None, Unset, int] = 0,
    page_size: Union[None, Unset, int] = 25,
) -> Optional[Union[Any, HTTPValidationError]]:
    """User Info

     Use this to get user information. (user row + all user key info)

    Example request
    ```
    curl -X GET 'http://localhost:8000/user/info?user_id=krrish7%40berri.ai'     --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (Union[None, Unset, str]): User ID in the request parameters
        view_all (Union[Unset, bool]): set to true to View all users. When using view_all, don't
            pass user_id Default: False.
        page (Union[None, Unset, int]): Page number for pagination. Only use when view_all is true
            Default: 0.
        page_size (Union[None, Unset, int]): Number of items per page. Only use when view_all is
            true Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        view_all=view_all,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[None, Unset, str] = UNSET,
    view_all: Union[Unset, bool] = False,
    page: Union[None, Unset, int] = 0,
    page_size: Union[None, Unset, int] = 25,
) -> Response[Union[Any, HTTPValidationError]]:
    """User Info

     Use this to get user information. (user row + all user key info)

    Example request
    ```
    curl -X GET 'http://localhost:8000/user/info?user_id=krrish7%40berri.ai'     --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (Union[None, Unset, str]): User ID in the request parameters
        view_all (Union[Unset, bool]): set to true to View all users. When using view_all, don't
            pass user_id Default: False.
        page (Union[None, Unset, int]): Page number for pagination. Only use when view_all is true
            Default: 0.
        page_size (Union[None, Unset, int]): Number of items per page. Only use when view_all is
            true Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        view_all=view_all,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[None, Unset, str] = UNSET,
    view_all: Union[Unset, bool] = False,
    page: Union[None, Unset, int] = 0,
    page_size: Union[None, Unset, int] = 25,
) -> Optional[Union[Any, HTTPValidationError]]:
    """User Info

     Use this to get user information. (user row + all user key info)

    Example request
    ```
    curl -X GET 'http://localhost:8000/user/info?user_id=krrish7%40berri.ai'     --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (Union[None, Unset, str]): User ID in the request parameters
        view_all (Union[Unset, bool]): set to true to View all users. When using view_all, don't
            pass user_id Default: False.
        page (Union[None, Unset, int]): Page number for pagination. Only use when view_all is true
            Default: 0.
        page_size (Union[None, Unset, int]): Number of items per page. Only use when view_all is
            true Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            view_all=view_all,
            page=page,
            page_size=page_size,
        )
    ).parsed
