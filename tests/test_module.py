from attrs import define, field
from pytest import raises as pytest_raises

from entelequia.system.module import Module
from entelequia.system.system import GenericSystem
from entelequia.system.system_interface import GenericSystemInterface


class MockSystem(GenericSystem):
    pass

class MockSystemInterface(GenericSystemInterface):
    accessor: str = "mock_system"

mock_system = MockSystem()
mock_interface = MockSystemInterface()


def test_module_wrong_creation():
    @define
    class WrongModule(Module):
        system: MockSystem
        interface: MockSystemInterface

    with pytest_raises(AssertionError):
        WrongModule(system=mock_system, interface=mock_interface)

def test_module_right_creation():
    @define
    class OkModule(Module):
        system: MockSystem
        interface: MockSystemInterface
        mock_system: MockSystem = field(init=False)

    module = OkModule(system=mock_system, interface=mock_interface)
    assert module.system == mock_system
    assert module.interface == mock_interface
    assert module.mock_system == mock_system
