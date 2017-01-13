#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_lib import constants

# The alias of the extension.
ALIAS = 'firewallrouterinsertion'

# Whether or not this extension is simply signaling behavior to the user
# or it actively modifies the attribute map.
IS_SHIM_EXTENSION = False

# Whether the extension is marking the adoption of standardattr model for
# legacy resources, or introducing new standardattr attributes. False or
# None if the standardattr model is adopted since the introduction of
# resource extension.
# If this is True, the alias for the extension should be prefixed with
# 'standard-attr-'.
IS_STANDARD_ATTR_EXTENSION = False

# The name of the extension.
NAME = 'FWaaS Router Insertion'

# The description of the extension.
DESCRIPTION = "Provides router insertion support for FWaaS version 1"

# A timestamp of when the extension was introduced.
UPDATED_TIMESTAMP = "2016-01-01T10:00:00-00:00"

# The name of the resource
RESOURCE_NAME = "firewall"

# The plural for the resource
COLLECTION_NAME = "firewalls"

RESOURCE_ATTRIBUTE_MAP = {
    COLLECTION_NAME: {
        'router_ids': {'allow_post': True, 'allow_put': True,
                       'validate': {'type:uuid_list': None},
                       'is_visible': True,
                       'default': constants.ATTR_NOT_SPECIFIED},
    }
}

# The subresource attribute map for the extension.  This extension has only
# top level resources, not child resources, so this is set to an empty dict.
SUB_RESOURCE_ATTRIBUTE_MAP = {
}

# The action map.
ACTION_MAP = {
}

# The list of required extensions.
REQUIRED_EXTENSIONS = [
]

# The list of optional extensions.
OPTIONAL_EXTENSIONS = [
]
