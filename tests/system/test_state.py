from pytest import raises as pytest_raises

from entelequia.system.implementation import SystemStarted, SystemStopped

from .conftest import AttrsMockSystem


def test_create_system_stopped(attrs_mock_system: AttrsMockSystem):
    state = SystemStopped(attrs_mock_system)

    assert state.system == attrs_mock_system
    assert not (state.is_started())
    assert state.is_stopped()

    assert state.start_up() is None
    with pytest_raises(AssertionError) as exception:
        state.shut_down()
    assert (
        str(exception.value) == f"{attrs_mock_system.name} is already stopped."
    )


def test_create_system_started(attrs_mock_system: AttrsMockSystem):
    state = SystemStarted(attrs_mock_system)

    assert state.system == attrs_mock_system
    assert state.is_started()
    assert not (state.is_stopped())

    with pytest_raises(AssertionError) as exception:
        state.start_up()
    assert (
        str(exception.value) == f"{attrs_mock_system.name} is already started."
    )
    assert state.shut_down() is None
