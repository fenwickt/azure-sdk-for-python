# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AutomationClientConfiguration
from .operations import AutomationAccountOperations
from .operations import Operations
from .operations import StatisticsOperations
from .operations import UsagesOperations
from .operations import KeysOperations
from .operations import CertificateOperations
from .operations import ConnectionOperations
from .operations import ConnectionTypeOperations
from .operations import CredentialOperations
from .operations import DscConfigurationOperations
from .operations import HybridRunbookWorkerGroupOperations
from .operations import JobScheduleOperations
from .operations import LinkedWorkspaceOperations
from .operations import ActivityOperations
from .operations import ModuleOperations
from .operations import ObjectDataTypesOperations
from .operations import FieldsOperations
from .operations import ScheduleOperations
from .operations import VariableOperations
from .operations import WebhookOperations
from .operations import WatcherOperations
from .operations import SoftwareUpdateConfigurationsOperations
from .operations import SoftwareUpdateConfigurationRunsOperations
from .operations import SoftwareUpdateConfigurationMachineRunsOperations
from .operations import SourceControlOperations
from .operations import SourceControlSyncJobOperations
from .operations import SourceControlSyncJobStreamsOperations
from .operations import JobOperations
from .operations import JobStreamOperations
from .operations import AgentRegistrationInformationOperations
from .operations import DscNodeOperations
from .operations import NodeReportsOperations
from .operations import DscCompilationJobOperations
from .operations import DscCompilationJobStreamOperations
from .operations import DscNodeConfigurationOperations
from .operations import NodeCountInformationOperations
from .operations import RunbookDraftOperations
from .operations import RunbookOperations
from .operations import TestJobStreamsOperations
from .operations import TestJobOperations
from .operations import Python2PackageOperations
from .. import models


class AutomationClient(object):
    """Automation Client.

    :ivar automation_account: AutomationAccountOperations operations
    :vartype automation_account: azure.mgmt.automation.aio.operations.AutomationAccountOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.automation.aio.operations.Operations
    :ivar statistics: StatisticsOperations operations
    :vartype statistics: azure.mgmt.automation.aio.operations.StatisticsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.automation.aio.operations.UsagesOperations
    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.automation.aio.operations.KeysOperations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure.mgmt.automation.aio.operations.CertificateOperations
    :ivar connection: ConnectionOperations operations
    :vartype connection: azure.mgmt.automation.aio.operations.ConnectionOperations
    :ivar connection_type: ConnectionTypeOperations operations
    :vartype connection_type: azure.mgmt.automation.aio.operations.ConnectionTypeOperations
    :ivar credential: CredentialOperations operations
    :vartype credential: azure.mgmt.automation.aio.operations.CredentialOperations
    :ivar dsc_configuration: DscConfigurationOperations operations
    :vartype dsc_configuration: azure.mgmt.automation.aio.operations.DscConfigurationOperations
    :ivar hybrid_runbook_worker_group: HybridRunbookWorkerGroupOperations operations
    :vartype hybrid_runbook_worker_group: azure.mgmt.automation.aio.operations.HybridRunbookWorkerGroupOperations
    :ivar job_schedule: JobScheduleOperations operations
    :vartype job_schedule: azure.mgmt.automation.aio.operations.JobScheduleOperations
    :ivar linked_workspace: LinkedWorkspaceOperations operations
    :vartype linked_workspace: azure.mgmt.automation.aio.operations.LinkedWorkspaceOperations
    :ivar activity: ActivityOperations operations
    :vartype activity: azure.mgmt.automation.aio.operations.ActivityOperations
    :ivar module: ModuleOperations operations
    :vartype module: azure.mgmt.automation.aio.operations.ModuleOperations
    :ivar object_data_types: ObjectDataTypesOperations operations
    :vartype object_data_types: azure.mgmt.automation.aio.operations.ObjectDataTypesOperations
    :ivar fields: FieldsOperations operations
    :vartype fields: azure.mgmt.automation.aio.operations.FieldsOperations
    :ivar schedule: ScheduleOperations operations
    :vartype schedule: azure.mgmt.automation.aio.operations.ScheduleOperations
    :ivar variable: VariableOperations operations
    :vartype variable: azure.mgmt.automation.aio.operations.VariableOperations
    :ivar webhook: WebhookOperations operations
    :vartype webhook: azure.mgmt.automation.aio.operations.WebhookOperations
    :ivar watcher: WatcherOperations operations
    :vartype watcher: azure.mgmt.automation.aio.operations.WatcherOperations
    :ivar software_update_configurations: SoftwareUpdateConfigurationsOperations operations
    :vartype software_update_configurations: azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationsOperations
    :ivar software_update_configuration_runs: SoftwareUpdateConfigurationRunsOperations operations
    :vartype software_update_configuration_runs: azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationRunsOperations
    :ivar software_update_configuration_machine_runs: SoftwareUpdateConfigurationMachineRunsOperations operations
    :vartype software_update_configuration_machine_runs: azure.mgmt.automation.aio.operations.SoftwareUpdateConfigurationMachineRunsOperations
    :ivar source_control: SourceControlOperations operations
    :vartype source_control: azure.mgmt.automation.aio.operations.SourceControlOperations
    :ivar source_control_sync_job: SourceControlSyncJobOperations operations
    :vartype source_control_sync_job: azure.mgmt.automation.aio.operations.SourceControlSyncJobOperations
    :ivar source_control_sync_job_streams: SourceControlSyncJobStreamsOperations operations
    :vartype source_control_sync_job_streams: azure.mgmt.automation.aio.operations.SourceControlSyncJobStreamsOperations
    :ivar job: JobOperations operations
    :vartype job: azure.mgmt.automation.aio.operations.JobOperations
    :ivar job_stream: JobStreamOperations operations
    :vartype job_stream: azure.mgmt.automation.aio.operations.JobStreamOperations
    :ivar agent_registration_information: AgentRegistrationInformationOperations operations
    :vartype agent_registration_information: azure.mgmt.automation.aio.operations.AgentRegistrationInformationOperations
    :ivar dsc_node: DscNodeOperations operations
    :vartype dsc_node: azure.mgmt.automation.aio.operations.DscNodeOperations
    :ivar node_reports: NodeReportsOperations operations
    :vartype node_reports: azure.mgmt.automation.aio.operations.NodeReportsOperations
    :ivar dsc_compilation_job: DscCompilationJobOperations operations
    :vartype dsc_compilation_job: azure.mgmt.automation.aio.operations.DscCompilationJobOperations
    :ivar dsc_compilation_job_stream: DscCompilationJobStreamOperations operations
    :vartype dsc_compilation_job_stream: azure.mgmt.automation.aio.operations.DscCompilationJobStreamOperations
    :ivar dsc_node_configuration: DscNodeConfigurationOperations operations
    :vartype dsc_node_configuration: azure.mgmt.automation.aio.operations.DscNodeConfigurationOperations
    :ivar node_count_information: NodeCountInformationOperations operations
    :vartype node_count_information: azure.mgmt.automation.aio.operations.NodeCountInformationOperations
    :ivar runbook_draft: RunbookDraftOperations operations
    :vartype runbook_draft: azure.mgmt.automation.aio.operations.RunbookDraftOperations
    :ivar runbook: RunbookOperations operations
    :vartype runbook: azure.mgmt.automation.aio.operations.RunbookOperations
    :ivar test_job_streams: TestJobStreamsOperations operations
    :vartype test_job_streams: azure.mgmt.automation.aio.operations.TestJobStreamsOperations
    :ivar test_job: TestJobOperations operations
    :vartype test_job: azure.mgmt.automation.aio.operations.TestJobOperations
    :ivar python2_package: Python2PackageOperations operations
    :vartype python2_package: azure.mgmt.automation.aio.operations.Python2PackageOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AutomationClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.automation_account = AutomationAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.statistics = StatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.keys = KeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.connection = ConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.connection_type = ConnectionTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.credential = CredentialOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dsc_configuration = DscConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.hybrid_runbook_worker_group = HybridRunbookWorkerGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.job_schedule = JobScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_workspace = LinkedWorkspaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.activity = ActivityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.module = ModuleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.object_data_types = ObjectDataTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.fields = FieldsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.variable = VariableOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.webhook = WebhookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.watcher = WatcherOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.software_update_configurations = SoftwareUpdateConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.software_update_configuration_runs = SoftwareUpdateConfigurationRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.software_update_configuration_machine_runs = SoftwareUpdateConfigurationMachineRunsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.source_control = SourceControlOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.source_control_sync_job = SourceControlSyncJobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.source_control_sync_job_streams = SourceControlSyncJobStreamsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.job = JobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.job_stream = JobStreamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.agent_registration_information = AgentRegistrationInformationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dsc_node = DscNodeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.node_reports = NodeReportsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dsc_compilation_job = DscCompilationJobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dsc_compilation_job_stream = DscCompilationJobStreamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dsc_node_configuration = DscNodeConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.node_count_information = NodeCountInformationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.runbook_draft = RunbookDraftOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.runbook = RunbookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.test_job_streams = TestJobStreamsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.test_job = TestJobOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.python2_package = Python2PackageOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutomationClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
