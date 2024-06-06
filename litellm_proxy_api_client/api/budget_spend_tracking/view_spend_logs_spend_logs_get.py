from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    api_key: Union[None, Unset, str] = UNSET,
    user_id: Union[None, Unset, str] = UNSET,
    request_id: Union[None, Unset, str] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_api_key: Union[None, Unset, str]
    if isinstance(api_key, Unset):
        json_api_key = UNSET
    else:
        json_api_key = api_key
    params["api_key"] = json_api_key

    json_user_id: Union[None, Unset, str]
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_request_id: Union[None, Unset, str]
    if isinstance(request_id, Unset):
        json_request_id = UNSET
    else:
        json_request_id = request_id
    params["request_id"] = json_request_id

    json_start_date: Union[None, Unset, str]
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: Union[None, Unset, str]
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/spend/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    api_key: Union[None, Unset, str] = UNSET,
    user_id: Union[None, Unset, str] = UNSET,
    request_id: Union[None, Unset, str] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""View Spend Logs

     View all spend logs, if request_id is provided, only logs for that request_id will be returned

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-Fn8Ej39NkBQmUagFEoUWPQ\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        api_key (Union[None, Unset, str]): Get spend logs based on api key
        user_id (Union[None, Unset, str]): Get spend logs based on user_id
        request_id (Union[None, Unset, str]): request_id to get spend logs for specific
            request_id. If none passed then pass spend logs for all requests
        start_date (Union[None, Unset, str]): Time from which to start viewing key spend
        end_date (Union[None, Unset, str]): Time till which to view key spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        user_id=user_id,
        request_id=request_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    api_key: Union[None, Unset, str] = UNSET,
    user_id: Union[None, Unset, str] = UNSET,
    request_id: Union[None, Unset, str] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""View Spend Logs

     View all spend logs, if request_id is provided, only logs for that request_id will be returned

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-Fn8Ej39NkBQmUagFEoUWPQ\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        api_key (Union[None, Unset, str]): Get spend logs based on api key
        user_id (Union[None, Unset, str]): Get spend logs based on user_id
        request_id (Union[None, Unset, str]): request_id to get spend logs for specific
            request_id. If none passed then pass spend logs for all requests
        start_date (Union[None, Unset, str]): Time from which to start viewing key spend
        end_date (Union[None, Unset, str]): Time till which to view key spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        client=client,
        api_key=api_key,
        user_id=user_id,
        request_id=request_id,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    api_key: Union[None, Unset, str] = UNSET,
    user_id: Union[None, Unset, str] = UNSET,
    request_id: Union[None, Unset, str] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""View Spend Logs

     View all spend logs, if request_id is provided, only logs for that request_id will be returned

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-Fn8Ej39NkBQmUagFEoUWPQ\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        api_key (Union[None, Unset, str]): Get spend logs based on api key
        user_id (Union[None, Unset, str]): Get spend logs based on user_id
        request_id (Union[None, Unset, str]): request_id to get spend logs for specific
            request_id. If none passed then pass spend logs for all requests
        start_date (Union[None, Unset, str]): Time from which to start viewing key spend
        end_date (Union[None, Unset, str]): Time till which to view key spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        user_id=user_id,
        request_id=request_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    api_key: Union[None, Unset, str] = UNSET,
    user_id: Union[None, Unset, str] = UNSET,
    request_id: Union[None, Unset, str] = UNSET,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""View Spend Logs

     View all spend logs, if request_id is provided, only logs for that request_id will be returned

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-Fn8Ej39NkBQmUagFEoUWPQ\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        api_key (Union[None, Unset, str]): Get spend logs based on api key
        user_id (Union[None, Unset, str]): Get spend logs based on user_id
        request_id (Union[None, Unset, str]): request_id to get spend logs for specific
            request_id. If none passed then pass spend logs for all requests
        start_date (Union[None, Unset, str]): Time from which to start viewing key spend
        end_date (Union[None, Unset, str]): Time till which to view key spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key=api_key,
            user_id=user_id,
            request_id=request_id,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
