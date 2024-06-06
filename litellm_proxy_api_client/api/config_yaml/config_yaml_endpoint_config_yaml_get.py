from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_yaml import ConfigYAML
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ConfigYAML,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/config/yaml",
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
    body: ConfigYAML,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Config Yaml Endpoint

     This is a mock endpoint, to show what you can set in config.yaml details in the Swagger UI.

    Parameters:

    The config.yaml object has the following attributes:
    - **model_list**: *Optional[List[ModelParams]]* - A list of supported models on the server, along
    with model-specific configurations. ModelParams includes \"model_name\" (name of the model),
    \"litellm_params\" (litellm-specific parameters for the model), and \"model_info\" (additional info
    about the model such as id, mode, cost per token, etc).

    - **litellm_settings**: *Optional[dict]*: Settings for the litellm module. You can specify multiple
    properties like \"drop_params\", \"set_verbose\", \"api_base\", \"cache\".

    - **general_settings**: *Optional[ConfigGeneralSettings]*: General settings for the server like
    \"completion_model\" (default model for chat completion calls), \"use_azure_key_vault\" (option to
    load keys from azure key vault), \"master_key\" (key required for all calls to proxy), and others.

    Please, refer to each class's description for a better understanding of the specific attributes
    within them.

    Note: This is a mock endpoint primarily meant for demonstration purposes, and does not actually
    provide or change any configurations.

    Args:
        body (ConfigYAML): Documents all the fields supported by the config.yaml

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
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
    body: ConfigYAML,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Config Yaml Endpoint

     This is a mock endpoint, to show what you can set in config.yaml details in the Swagger UI.

    Parameters:

    The config.yaml object has the following attributes:
    - **model_list**: *Optional[List[ModelParams]]* - A list of supported models on the server, along
    with model-specific configurations. ModelParams includes \"model_name\" (name of the model),
    \"litellm_params\" (litellm-specific parameters for the model), and \"model_info\" (additional info
    about the model such as id, mode, cost per token, etc).

    - **litellm_settings**: *Optional[dict]*: Settings for the litellm module. You can specify multiple
    properties like \"drop_params\", \"set_verbose\", \"api_base\", \"cache\".

    - **general_settings**: *Optional[ConfigGeneralSettings]*: General settings for the server like
    \"completion_model\" (default model for chat completion calls), \"use_azure_key_vault\" (option to
    load keys from azure key vault), \"master_key\" (key required for all calls to proxy), and others.

    Please, refer to each class's description for a better understanding of the specific attributes
    within them.

    Note: This is a mock endpoint primarily meant for demonstration purposes, and does not actually
    provide or change any configurations.

    Args:
        body (ConfigYAML): Documents all the fields supported by the config.yaml

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConfigYAML,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Config Yaml Endpoint

     This is a mock endpoint, to show what you can set in config.yaml details in the Swagger UI.

    Parameters:

    The config.yaml object has the following attributes:
    - **model_list**: *Optional[List[ModelParams]]* - A list of supported models on the server, along
    with model-specific configurations. ModelParams includes \"model_name\" (name of the model),
    \"litellm_params\" (litellm-specific parameters for the model), and \"model_info\" (additional info
    about the model such as id, mode, cost per token, etc).

    - **litellm_settings**: *Optional[dict]*: Settings for the litellm module. You can specify multiple
    properties like \"drop_params\", \"set_verbose\", \"api_base\", \"cache\".

    - **general_settings**: *Optional[ConfigGeneralSettings]*: General settings for the server like
    \"completion_model\" (default model for chat completion calls), \"use_azure_key_vault\" (option to
    load keys from azure key vault), \"master_key\" (key required for all calls to proxy), and others.

    Please, refer to each class's description for a better understanding of the specific attributes
    within them.

    Note: This is a mock endpoint primarily meant for demonstration purposes, and does not actually
    provide or change any configurations.

    Args:
        body (ConfigYAML): Documents all the fields supported by the config.yaml

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConfigYAML,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Config Yaml Endpoint

     This is a mock endpoint, to show what you can set in config.yaml details in the Swagger UI.

    Parameters:

    The config.yaml object has the following attributes:
    - **model_list**: *Optional[List[ModelParams]]* - A list of supported models on the server, along
    with model-specific configurations. ModelParams includes \"model_name\" (name of the model),
    \"litellm_params\" (litellm-specific parameters for the model), and \"model_info\" (additional info
    about the model such as id, mode, cost per token, etc).

    - **litellm_settings**: *Optional[dict]*: Settings for the litellm module. You can specify multiple
    properties like \"drop_params\", \"set_verbose\", \"api_base\", \"cache\".

    - **general_settings**: *Optional[ConfigGeneralSettings]*: General settings for the server like
    \"completion_model\" (default model for chat completion calls), \"use_azure_key_vault\" (option to
    load keys from azure key vault), \"master_key\" (key required for all calls to proxy), and others.

    Please, refer to each class's description for a better understanding of the specific attributes
    within them.

    Note: This is a mock endpoint primarily meant for demonstration purposes, and does not actually
    provide or change any configurations.

    Args:
        body (ConfigYAML): Documents all the fields supported by the config.yaml

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
        )
    ).parsed
