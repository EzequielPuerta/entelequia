from attrs import define

from entelequia.system.system import GenericSystem
from entelequia.system.system_interface import GenericSystemInterface


@define
class Module:
    system: GenericSystem
    interface: GenericSystemInterface
