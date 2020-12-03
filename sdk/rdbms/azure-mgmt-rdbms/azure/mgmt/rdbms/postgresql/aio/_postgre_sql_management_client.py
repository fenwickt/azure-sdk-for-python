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

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import PostgreSQLManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class PostgreSQLManagementClient(MultiApiClientMixin, _SDKClient):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure PostgreSQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2020-01-01'
    _PROFILE_TAG = "azure.mgmt.rdbms.PostgreSQLManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = PostgreSQLManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(PostgreSQLManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2020-01-01: :mod:`v2020_01_01.models<azure.mgmt.rdbms.v2020_01_01.models>`
           * 2020-02-14-preview: :mod:`v2020_02_14_preview.models<azure.mgmt.rdbms.v2020_02_14_preview.models>`
        """
        if api_version == '2020-01-01':
            from ..v2020_01_01 import models
            return models
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def check_name_availability(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`CheckNameAvailabilityOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.CheckNameAvailabilityOperations>`
           * 2020-02-14-preview: :class:`CheckNameAvailabilityOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.CheckNameAvailabilityOperations>`
        """
        api_version = self._get_api_version('check_name_availability')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import CheckNameAvailabilityOperations as OperationClass
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import CheckNameAvailabilityOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'check_name_availability'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def configurations(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ConfigurationsOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ConfigurationsOperations>`
           * 2020-02-14-preview: :class:`ConfigurationsOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.ConfigurationsOperations>`
        """
        api_version = self._get_api_version('configurations')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ConfigurationsOperations as OperationClass
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import ConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def databases(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`DatabasesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.DatabasesOperations>`
        """
        api_version = self._get_api_version('databases')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import DatabasesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'databases'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def firewall_rules(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`FirewallRulesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.FirewallRulesOperations>`
           * 2020-02-14-preview: :class:`FirewallRulesOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.FirewallRulesOperations>`
        """
        api_version = self._get_api_version('firewall_rules')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import FirewallRulesOperations as OperationClass
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import FirewallRulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'firewall_rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def location_based_capabilities(self):
        """Instance depends on the API version:

           * 2020-02-14-preview: :class:`LocationBasedCapabilitiesOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.LocationBasedCapabilitiesOperations>`
        """
        api_version = self._get_api_version('location_based_capabilities')
        if api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import LocationBasedCapabilitiesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'location_based_capabilities'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def location_based_performance_tier(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`LocationBasedPerformanceTierOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.LocationBasedPerformanceTierOperations>`
        """
        api_version = self._get_api_version('location_based_performance_tier')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import LocationBasedPerformanceTierOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'location_based_performance_tier'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def log_files(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`LogFilesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.LogFilesOperations>`
        """
        api_version = self._get_api_version('log_files')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import LogFilesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'log_files'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`Operations<azure.mgmt.rdbms.v2020_01_01.aio.operations.Operations>`
           * 2020-02-14-preview: :class:`Operations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import Operations as OperationClass
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def replicas(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ReplicasOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ReplicasOperations>`
        """
        api_version = self._get_api_version('replicas')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ReplicasOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'replicas'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def server_administrators(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ServerAdministratorsOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ServerAdministratorsOperations>`
        """
        api_version = self._get_api_version('server_administrators')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ServerAdministratorsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'server_administrators'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def server_keys(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ServerKeysOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ServerKeysOperations>`
        """
        api_version = self._get_api_version('server_keys')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ServerKeysOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'server_keys'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def server_security_alert_policies(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ServerSecurityAlertPoliciesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ServerSecurityAlertPoliciesOperations>`
        """
        api_version = self._get_api_version('server_security_alert_policies')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ServerSecurityAlertPoliciesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'server_security_alert_policies'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def servers(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`ServersOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.ServersOperations>`
           * 2020-02-14-preview: :class:`ServersOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.ServersOperations>`
        """
        api_version = self._get_api_version('servers')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import ServersOperations as OperationClass
        elif api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import ServersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'servers'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_network_rules(self):
        """Instance depends on the API version:

           * 2020-01-01: :class:`VirtualNetworkRulesOperations<azure.mgmt.rdbms.v2020_01_01.aio.operations.VirtualNetworkRulesOperations>`
        """
        api_version = self._get_api_version('virtual_network_rules')
        if api_version == '2020-01-01':
            from ..v2020_01_01.aio.operations import VirtualNetworkRulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'virtual_network_rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def virtual_network_subnet_usage(self):
        """Instance depends on the API version:

           * 2020-02-14-preview: :class:`VirtualNetworkSubnetUsageOperations<azure.mgmt.rdbms.v2020_02_14_preview.aio.operations.VirtualNetworkSubnetUsageOperations>`
        """
        api_version = self._get_api_version('virtual_network_subnet_usage')
        if api_version == '2020-02-14-preview':
            from ..v2020_02_14_preview.aio.operations import VirtualNetworkSubnetUsageOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'virtual_network_subnet_usage'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
