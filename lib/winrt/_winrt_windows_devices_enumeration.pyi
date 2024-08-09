# WARNING: Please don't edit this file. It was generated by Python/WinRT v2.1.0

import datetime
import sys
import types
import typing
import uuid as _uuid
from builtins import property as _property

import winrt._winrt
import winrt.system
import winrt.windows.applicationmodel.background as windows_applicationmodel_background
import winrt.windows.foundation as windows_foundation
import winrt.windows.foundation.collections as windows_foundation_collections
import winrt.windows.security.credentials as windows_security_credentials
import winrt.windows.storage.streams as windows_storage_streams
import winrt.windows.ui as windows_ui
import winrt.windows.ui.popups as windows_ui_popups

from winrt.windows.devices.enumeration import DeviceAccessStatus, DeviceClass, DeviceInformationKind, DevicePairingKinds, DevicePairingProtectionLevel, DevicePairingResultStatus, DevicePickerDisplayStatusOptions, DeviceUnpairingResultStatus, DeviceWatcherEventKind, DeviceWatcherStatus, Panel

Self = typing.TypeVar('Self')

@typing.final
class DeviceAccessChangedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceAccessChangedEventArgs: ...
    @_property
    def status(self) -> DeviceAccessStatus: ...
    @_property
    def id(self) -> str: ...

@typing.final
class DeviceAccessInformation_Static(type):
    def create_from_device_class(cls, device_class: DeviceClass, /) -> typing.Optional[DeviceAccessInformation]: ...
    def create_from_device_class_id(cls, device_class_id: _uuid.UUID, /) -> typing.Optional[DeviceAccessInformation]: ...
    def create_from_id(cls, device_id: str, /) -> typing.Optional[DeviceAccessInformation]: ...

@typing.final
class DeviceAccessInformation(winrt.system.Object, metaclass=DeviceAccessInformation_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceAccessInformation: ...
    def add_access_changed(self, handler: windows_foundation.TypedEventHandler[DeviceAccessInformation, DeviceAccessChangedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_access_changed(self, cookie: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def current_status(self) -> DeviceAccessStatus: ...

@typing.final
class DeviceConnectionChangeTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceConnectionChangeTriggerDetails: ...
    @_property
    def device_id(self) -> str: ...

@typing.final
class DeviceDisconnectButtonClickedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceDisconnectButtonClickedEventArgs: ...
    @_property
    def device(self) -> typing.Optional[DeviceInformation]: ...

@typing.final
class DeviceInformation_Static(type):
    @typing.overload
    def create_from_id_async(cls, device_id: str, /) -> windows_foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    def create_from_id_async(cls, device_id: str, additional_properties: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    def create_from_id_async(cls, device_id: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> windows_foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    def create_watcher(cls) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    def create_watcher(cls, device_class: DeviceClass, /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    def create_watcher(cls, aqs_filter: str, additional_properties: typing.Iterable[str], /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    def create_watcher(cls, aqs_filter: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> typing.Optional[DeviceWatcher]: ...
    @typing.overload
    def find_all_async(cls) -> windows_foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    def find_all_async(cls, device_class: DeviceClass, /) -> windows_foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    def find_all_async(cls, aqs_filter: str, additional_properties: typing.Iterable[str], /) -> windows_foundation.IAsyncOperation[DeviceInformationCollection]: ...
    @typing.overload
    def find_all_async(cls, aqs_filter: str, additional_properties: typing.Iterable[str], kind: DeviceInformationKind, /) -> windows_foundation.IAsyncOperation[DeviceInformationCollection]: ...
    def get_aqs_filter_from_device_class(cls, device_class: DeviceClass, /) -> str: ...

@typing.final
class DeviceInformation(winrt.system.Object, metaclass=DeviceInformation_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformation: ...
    def get_glyph_thumbnail_async(self) -> windows_foundation.IAsyncOperation[DeviceThumbnail]: ...
    def get_thumbnail_async(self) -> windows_foundation.IAsyncOperation[DeviceThumbnail]: ...
    def update(self, update_info: typing.Optional[DeviceInformationUpdate], /) -> None: ...
    @_property
    def enclosure_location(self) -> typing.Optional[EnclosureLocation]: ...
    @_property
    def id(self) -> str: ...
    @_property
    def is_default(self) -> bool: ...
    @_property
    def is_enabled(self) -> bool: ...
    @_property
    def name(self) -> str: ...
    @_property
    def properties(self) -> typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]]: ...
    @_property
    def kind(self) -> DeviceInformationKind: ...
    @_property
    def pairing(self) -> typing.Optional[DeviceInformationPairing]: ...

@typing.final
class DeviceInformationCollection(winrt.system.Object, winrt._winrt.Sequence[DeviceInformation]):
    def __len__(self) -> int: ...
    def __iter__(self) -> windows_foundation_collections.IIterator[DeviceInformation]: ...
    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex) -> DeviceInformation: ...
    @typing.overload
    def __getitem__(self, index: slice) -> winrt.system.Array[DeviceInformation]: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationCollection: ...
    def first(self) -> typing.Optional[windows_foundation_collections.IIterator[DeviceInformation]]: ...
    def get_at(self, index: winrt.system.UInt32, /) -> typing.Optional[DeviceInformation]: ...
    def get_many(self, start_index: winrt.system.UInt32, items: winrt.system.Array[DeviceInformation], /) -> winrt.system.UInt32: ...
    def index_of(self, value: typing.Optional[DeviceInformation], /) -> typing.Tuple[bool, winrt.system.UInt32]: ...
    @_property
    def size(self) -> winrt.system.UInt32: ...

@typing.final
class DeviceInformationCustomPairing(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationCustomPairing: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, /) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, /) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, device_pairing_settings: typing.Optional[IDevicePairingSettings], /) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    def add_pairing_requested(self, handler: windows_foundation.TypedEventHandler[DeviceInformationCustomPairing, DevicePairingRequestedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_pairing_requested(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...

@typing.final
class DeviceInformationPairing_Static(type):
    def try_register_for_all_inbound_pairing_requests(cls, pairing_kinds_supported: DevicePairingKinds, /) -> bool: ...
    def try_register_for_all_inbound_pairing_requests_with_protection_level(cls, pairing_kinds_supported: DevicePairingKinds, min_protection_level: DevicePairingProtectionLevel, /) -> bool: ...

@typing.final
class DeviceInformationPairing(winrt.system.Object, metaclass=DeviceInformationPairing_Static):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationPairing: ...
    @typing.overload
    def pair_async(self) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, min_protection_level: DevicePairingProtectionLevel, /) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    @typing.overload
    def pair_async(self, min_protection_level: DevicePairingProtectionLevel, device_pairing_settings: typing.Optional[IDevicePairingSettings], /) -> windows_foundation.IAsyncOperation[DevicePairingResult]: ...
    def unpair_async(self) -> windows_foundation.IAsyncOperation[DeviceUnpairingResult]: ...
    @_property
    def can_pair(self) -> bool: ...
    @_property
    def is_paired(self) -> bool: ...
    @_property
    def custom(self) -> typing.Optional[DeviceInformationCustomPairing]: ...
    @_property
    def protection_level(self) -> DevicePairingProtectionLevel: ...

@typing.final
class DeviceInformationUpdate(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceInformationUpdate: ...
    @_property
    def id(self) -> str: ...
    @_property
    def properties(self) -> typing.Optional[windows_foundation_collections.IMapView[str, winrt.system.Object]]: ...
    @_property
    def kind(self) -> DeviceInformationKind: ...

@typing.final
class DevicePairingRequestedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePairingRequestedEventArgs: ...
    @typing.overload
    def accept(self) -> None: ...
    @typing.overload
    def accept(self, pin: str, /) -> None: ...
    def accept_with_password_credential(self, password_credential: typing.Optional[windows_security_credentials.PasswordCredential], /) -> None: ...
    def get_deferral(self) -> typing.Optional[windows_foundation.Deferral]: ...
    @_property
    def device_information(self) -> typing.Optional[DeviceInformation]: ...
    @_property
    def pairing_kind(self) -> DevicePairingKinds: ...
    @_property
    def pin(self) -> str: ...

@typing.final
class DevicePairingResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePairingResult: ...
    @_property
    def protection_level_used(self) -> DevicePairingProtectionLevel: ...
    @_property
    def status(self) -> DevicePairingResultStatus: ...

@typing.final
class DevicePicker(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePicker: ...
    def __new__(cls: typing.Type[DevicePicker]) -> DevicePicker: ...
    def hide(self) -> None: ...
    @typing.overload
    def pick_single_device_async(self, selection: windows_foundation.Rect, /) -> windows_foundation.IAsyncOperation[DeviceInformation]: ...
    @typing.overload
    def pick_single_device_async(self, selection: windows_foundation.Rect, placement: windows_ui_popups.Placement, /) -> windows_foundation.IAsyncOperation[DeviceInformation]: ...
    def set_display_status(self, device: typing.Optional[DeviceInformation], status: str, options: DevicePickerDisplayStatusOptions, /) -> None: ...
    @typing.overload
    def show(self, selection: windows_foundation.Rect, /) -> None: ...
    @typing.overload
    def show(self, selection: windows_foundation.Rect, placement: windows_ui_popups.Placement, /) -> None: ...
    def add_device_picker_dismissed(self, handler: windows_foundation.TypedEventHandler[DevicePicker, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_device_picker_dismissed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_device_selected(self, handler: windows_foundation.TypedEventHandler[DevicePicker, DeviceSelectedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_device_selected(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_disconnect_button_clicked(self, handler: windows_foundation.TypedEventHandler[DevicePicker, DeviceDisconnectButtonClickedEventArgs], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_disconnect_button_clicked(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def appearance(self) -> typing.Optional[DevicePickerAppearance]: ...
    @_property
    def filter(self) -> typing.Optional[DevicePickerFilter]: ...
    @_property
    def requested_properties(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class DevicePickerAppearance(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePickerAppearance: ...
    @_property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...
    @_property
    def selected_foreground_color(self) -> windows_ui.Color: ...
    @selected_foreground_color.setter
    def selected_foreground_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def selected_background_color(self) -> windows_ui.Color: ...
    @selected_background_color.setter
    def selected_background_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def selected_accent_color(self) -> windows_ui.Color: ...
    @selected_accent_color.setter
    def selected_accent_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def foreground_color(self) -> windows_ui.Color: ...
    @foreground_color.setter
    def foreground_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def background_color(self) -> windows_ui.Color: ...
    @background_color.setter
    def background_color(self, value: windows_ui.Color) -> None: ...
    @_property
    def accent_color(self) -> windows_ui.Color: ...
    @accent_color.setter
    def accent_color(self, value: windows_ui.Color) -> None: ...

@typing.final
class DevicePickerFilter(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DevicePickerFilter: ...
    @_property
    def supported_device_classes(self) -> typing.Optional[windows_foundation_collections.IVector[DeviceClass]]: ...
    @_property
    def supported_device_selectors(self) -> typing.Optional[windows_foundation_collections.IVector[str]]: ...

@typing.final
class DeviceSelectedEventArgs(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceSelectedEventArgs: ...
    @_property
    def selected_device(self) -> typing.Optional[DeviceInformation]: ...

@typing.final
class DeviceThumbnail(winrt.system.Object):
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args) -> None: ...
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceThumbnail: ...
    def clone_stream(self) -> typing.Optional[windows_storage_streams.IRandomAccessStream]: ...
    def close(self) -> None: ...
    def flush_async(self) -> windows_foundation.IAsyncOperation[bool]: ...
    def get_input_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[windows_storage_streams.IInputStream]: ...
    def get_output_stream_at(self, position: winrt.system.UInt64, /) -> typing.Optional[windows_storage_streams.IOutputStream]: ...
    def read_async(self, buffer: typing.Optional[windows_storage_streams.IBuffer], count: winrt.system.UInt32, options: windows_storage_streams.InputStreamOptions, /) -> windows_foundation.IAsyncOperationWithProgress[windows_storage_streams.IBuffer, winrt.system.UInt32]: ...
    def seek(self, position: winrt.system.UInt64, /) -> None: ...
    def write_async(self, buffer: typing.Optional[windows_storage_streams.IBuffer], /) -> windows_foundation.IAsyncOperationWithProgress[winrt.system.UInt32, winrt.system.UInt32]: ...
    @_property
    def content_type(self) -> str: ...
    @_property
    def size(self) -> winrt.system.UInt64: ...
    @size.setter
    def size(self, value: winrt.system.UInt64) -> None: ...
    @_property
    def can_read(self) -> bool: ...
    @_property
    def can_write(self) -> bool: ...
    @_property
    def position(self) -> winrt.system.UInt64: ...

@typing.final
class DeviceUnpairingResult(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceUnpairingResult: ...
    @_property
    def status(self) -> DeviceUnpairingResultStatus: ...

@typing.final
class DeviceWatcher(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcher: ...
    def get_background_trigger(self, requested_event_kinds: typing.Iterable[DeviceWatcherEventKind], /) -> typing.Optional[windows_applicationmodel_background.DeviceWatcherTrigger]: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_added(self, handler: windows_foundation.TypedEventHandler[DeviceWatcher, DeviceInformation], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_added(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_enumeration_completed(self, handler: windows_foundation.TypedEventHandler[DeviceWatcher, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_enumeration_completed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_removed(self, handler: windows_foundation.TypedEventHandler[DeviceWatcher, DeviceInformationUpdate], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_removed(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_stopped(self, handler: windows_foundation.TypedEventHandler[DeviceWatcher, winrt.system.Object], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_stopped(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    def add_updated(self, handler: windows_foundation.TypedEventHandler[DeviceWatcher, DeviceInformationUpdate], /) -> windows_foundation.EventRegistrationToken: ...
    def remove_updated(self, token: windows_foundation.EventRegistrationToken, /) -> None: ...
    @_property
    def status(self) -> DeviceWatcherStatus: ...

@typing.final
class DeviceWatcherEvent(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcherEvent: ...
    @_property
    def device_information(self) -> typing.Optional[DeviceInformation]: ...
    @_property
    def device_information_update(self) -> typing.Optional[DeviceInformationUpdate]: ...
    @_property
    def kind(self) -> DeviceWatcherEventKind: ...

@typing.final
class DeviceWatcherTriggerDetails(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> DeviceWatcherTriggerDetails: ...
    @_property
    def device_watcher_events(self) -> typing.Optional[windows_foundation_collections.IVectorView[DeviceWatcherEvent]]: ...

@typing.final
class EnclosureLocation(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> EnclosureLocation: ...
    @_property
    def in_dock(self) -> bool: ...
    @_property
    def in_lid(self) -> bool: ...
    @_property
    def panel(self) -> Panel: ...
    @_property
    def rotation_angle_in_degrees_clockwise(self) -> winrt.system.UInt32: ...

@typing.final
class IDevicePairingSettings(winrt.system.Object):
    @staticmethod
    def _from(obj: winrt.system.Object, /) -> IDevicePairingSettings: ...
