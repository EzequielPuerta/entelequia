from attrs import define, field

from entelequia.system.module import Module
from entelequia.modules.time.system import TimeSystem
from entelequia.modules.time.interface import TimeSystemInterface


@define(order=True, frozen=True)
class TimeModule(Module):
    system: TimeSystem
    interface: TimeSystemInterface


module = TimeModule(system=TimeSystem(), interface=TimeSystemInterface())
