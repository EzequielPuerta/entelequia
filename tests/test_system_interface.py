from pytest import raises as pytest_raises

from entelequia.system.system_interface import GenericSystemInterface


def test_system_interface_wrong_creation():
    class WrongSystemInterface(GenericSystemInterface):
        pass

    with pytest_raises(TypeError):
        WrongSystemInterface()

def test_system_interface_right_creation():
    accessor_name = "ok_system"
    class OkSystemInterface(GenericSystemInterface):
        accessor: str = accessor_name

    interface = OkSystemInterface()
    assert isinstance(interface, OkSystemInterface)
    assert interface.accessor == accessor_name
