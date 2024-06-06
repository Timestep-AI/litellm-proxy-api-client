from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/spend/calculate",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
