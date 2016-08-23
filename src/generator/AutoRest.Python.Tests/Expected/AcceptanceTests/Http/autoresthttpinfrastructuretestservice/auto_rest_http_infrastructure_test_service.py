# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.http_failure_operations import HttpFailureOperations
from .operations.http_success_operations import HttpSuccessOperations
from .operations.http_redirects_operations import HttpRedirectsOperations
from .operations.http_client_failure_operations import HttpClientFailureOperations
from .operations.http_server_failure_operations import HttpServerFailureOperations
from .operations.http_retry_operations import HttpRetryOperations
from .operations.multiple_responses_operations import MultipleResponsesOperations
from . import models


class AutoRestHttpInfrastructureTestServiceConfiguration(Configuration):
    """Configuration for AutoRestHttpInfrastructureTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, base_url=None, filepath=None):

        if not base_url:
            base_url = 'http://localhost'

        super(AutoRestHttpInfrastructureTestServiceConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('autoresthttpinfrastructuretestservice/{}'.format(VERSION))


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestHttpInfrastructureTestServiceConfiguration

    :ivar http_failure: HttpFailure operations
    :vartype http_failure: .operations.HttpFailureOperations
    :ivar http_success: HttpSuccess operations
    :vartype http_success: .operations.HttpSuccessOperations
    :ivar http_redirects: HttpRedirects operations
    :vartype http_redirects: .operations.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailure operations
    :vartype http_client_failure: .operations.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailure operations
    :vartype http_server_failure: .operations.HttpServerFailureOperations
    :ivar http_retry: HttpRetry operations
    :vartype http_retry: .operations.HttpRetryOperations
    :ivar multiple_responses: MultipleResponses operations
    :vartype multiple_responses: .operations.MultipleResponsesOperations

    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, base_url=None, filepath=None):

        self.config = AutoRestHttpInfrastructureTestServiceConfiguration(base_url, filepath)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.http_failure = HttpFailureOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.http_success = HttpSuccessOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.http_redirects = HttpRedirectsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.http_client_failure = HttpClientFailureOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.http_server_failure = HttpServerFailureOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.http_retry = HttpRetryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.multiple_responses = MultipleResponsesOperations(
            self._client, self.config, self._serialize, self._deserialize)