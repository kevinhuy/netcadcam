# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from typing import Optional, Set
from ipaddress import IPv4Address

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from netcad.vlan import vlan_profile as vp
from netcad.vlan.vlan_profile import VlanProfile
from .interface_profile import InterfaceVirtual, InterfaceProfile

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------

__all__ = [
    "InterfaceL3",
    "InterfaceVlan",
    "InterfaceIsLoopback",
    "InterfaceIsManagement",
    "InterfaceIsInVRF",
]

# -----------------------------------------------------------------------------
#
#                        Interface Profiles for VLANs
#
# -----------------------------------------------------------------------------


class InterfaceL3(InterfaceProfile):
    def __init__(self, if_ipaddr: Optional[IPv4Address] = None, **params):
        super(InterfaceL3, self).__init__(**params)
        self.if_ipaddr = if_ipaddr


class InterfaceIsManagement(InterfaceL3):
    """
    An interface that is only used for out of band management
    """

    is_mgmt_only = True


class InterfaceIsLoopback(InterfaceVirtual, InterfaceL3):
    """
    A loopback interface is a virtual IP address
    """

    is_loopback = True


class InterfaceIsInVRF(InterfaceL3):
    is_in_vrf = True
    vrf: Optional[str] = "management"


class InterfaceVlan(InterfaceVirtual, InterfaceL3):
    """
    InterfaceVlan is used to declare IP addresses assigned to VLANs.  Also
    referred to an SVI.
    """

    vlan: VlanProfile

    def vlans_used(self) -> Set[vp.VlanProfile]:
        return {self.vlan}
