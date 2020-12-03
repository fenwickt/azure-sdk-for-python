# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AccessRights(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The permissions assigned to the shared access policy.
    """

    REGISTRY_READ = "RegistryRead"
    REGISTRY_WRITE = "RegistryWrite"
    SERVICE_CONNECT = "ServiceConnect"
    DEVICE_CONNECT = "DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE = "RegistryRead, RegistryWrite"
    REGISTRY_READ_SERVICE_CONNECT = "RegistryRead, ServiceConnect"
    REGISTRY_READ_DEVICE_CONNECT = "RegistryRead, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT = "RegistryWrite, ServiceConnect"
    REGISTRY_WRITE_DEVICE_CONNECT = "RegistryWrite, DeviceConnect"
    SERVICE_CONNECT_DEVICE_CONNECT = "ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect"
    REGISTRY_READ_REGISTRY_WRITE_DEVICE_CONNECT = "RegistryRead, RegistryWrite, DeviceConnect"
    REGISTRY_READ_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, ServiceConnect, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryWrite, ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect"

class Capabilities(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The capabilities and features enabled for the IoT hub.
    """

    NONE = "None"
    DEVICE_MANAGEMENT = "DeviceManagement"

class IotHubNameUnavailabilityReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for unavailability.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class IotHubScaleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the scaling enabled.
    """

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"

class IotHubSku(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the SKU.
    """

    F1 = "F1"
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"

class IotHubSkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing tier for the IoT hub.
    """

    FREE = "Free"
    STANDARD = "Standard"

class IpFilterActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The desired action for requests captured by this rule.
    """

    ACCEPT = "Accept"
    REJECT = "Reject"

class JobStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the job.
    """

    UNKNOWN = "unknown"
    ENQUEUED = "enqueued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class JobType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the job.
    """

    UNKNOWN = "unknown"
    EXPORT = "export"
    IMPORT_ENUM = "import"
    BACKUP = "backup"
    READ_DEVICE_PROPERTIES = "readDeviceProperties"
    WRITE_DEVICE_PROPERTIES = "writeDeviceProperties"
    UPDATE_DEVICE_CONFIGURATION = "updateDeviceConfiguration"
    REBOOT_DEVICE = "rebootDevice"
    FACTORY_RESET_DEVICE = "factoryResetDevice"
    FIRMWARE_UPDATE = "firmwareUpdate"

class OperationMonitoringLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operations monitoring level.
    """

    NONE = "None"
    ERROR = "Error"
    INFORMATION = "Information"
    ERROR_INFORMATION = "Error, Information"

class RoutingSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The source that the routing rule is to be applied to, such as DeviceMessages.
    """

    DEVICE_MESSAGES = "DeviceMessages"
    TWIN_CHANGE_EVENTS = "TwinChangeEvents"
    DEVICE_LIFECYCLE_EVENTS = "DeviceLifecycleEvents"
    DEVICE_JOB_LIFECYCLE_EVENTS = "DeviceJobLifecycleEvents"
