# SecretStorage module for Python
# Access passwords using the SecretService DBus API
# Author: Dmitry Shachnev, 2013
# License: BSD

"""This file provides quick access to all SecretStorage API. Please
refer to documentation of individual modules for API details.

It also provides some functions for compatibility with older
SecretStorage releases. Those functions are not recommended for use
in new software."""

from jeepney.integrate.blocking import connect_and_authenticate
from secretstorage.collection import Collection, create_collection, \
 get_all_collections, get_default_collection, get_any_collection, \
 get_collection_by_alias, search_items
from secretstorage.item import Item
from secretstorage.defines import DBUS_NOT_SUPPORTED, DBUS_EXEC_FAILED, \
 DBUS_NO_REPLY, DBUS_ACCESS_DENIED
from secretstorage.exceptions import SecretStorageException, \
 SecretServiceNotAvailableException, LockedException, \
 ItemNotFoundException

__version_tuple__ = (2, 3, 1)
__version__ = '.'.join(map(str, __version_tuple__))

def dbus_init(*args, **kwargs):
	return connect_and_authenticate()
