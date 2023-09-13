from pytest import raises as pytest_raises

from entelequia.system.implementation import SubsystemImplementation

from .conftest import AnnotatedMockSystem, AttrsMockSystem, ClassicMockSystem


def test_create_subsystem_without_name():
    class UnnamedSystem(SubsystemImplementation):
        pass

    with pytest_raises(TypeError) as exception:
        UnnamedSystem()
    error = "Can't instantiate abstract class {} with abstract method name"
    assert str(exception.value) == error.format(UnnamedSystem.__name__)


# Classic version
def test_create_simple_classic_subsystem():
    mock_system = ClassicMockSystem()
    assert isinstance(mock_system, ClassicMockSystem)
    assert mock_system.name == ClassicMockSystem.name


# Annotated version
def test_create_simple_annotated_subsystem():
    mock_system = AnnotatedMockSystem()
    assert isinstance(mock_system, AnnotatedMockSystem)
    assert mock_system.name == AnnotatedMockSystem.name


# Attrs version
def test_create_simple_attrs_subsystem():
    mock_system = AttrsMockSystem()
    assert isinstance(mock_system, AttrsMockSystem)
    assert mock_system.name == AttrsMockSystem.name


def test_new_subsystems_should_be_stopped(
    classic_mock_system: ClassicMockSystem,
    annotated_mock_system: AnnotatedMockSystem,
    attrs_mock_system: AttrsMockSystem,
):
    for mock_system in [
        classic_mock_system,
        annotated_mock_system,
        attrs_mock_system,
    ]:
        assert mock_system.is_stopped()
        assert not (mock_system.is_started())


def test_start_up_subsystem(
    classic_mock_system: ClassicMockSystem,
    annotated_mock_system: AnnotatedMockSystem,
    attrs_mock_system: AttrsMockSystem,
):
    for mock_system in [
        classic_mock_system,
        annotated_mock_system,
        attrs_mock_system,
    ]:
        assert mock_system.is_stopped()
        mock_system.start_up()
        assert mock_system.is_started()


def test_shut_down_subsystem(
    classic_mock_system: ClassicMockSystem,
    annotated_mock_system: AnnotatedMockSystem,
    attrs_mock_system: AttrsMockSystem,
):
    for mock_system in [
        classic_mock_system,
        annotated_mock_system,
        attrs_mock_system,
    ]:
        assert mock_system.is_stopped()
        mock_system.start_up()
        assert mock_system.is_started()
        mock_system.shut_down()
        assert mock_system.is_stopped()


def test_shut_down_already_stopped_subsystem(
    classic_mock_system: ClassicMockSystem,
    annotated_mock_system: AnnotatedMockSystem,
    attrs_mock_system: AttrsMockSystem,
):
    for mock_system in [
        classic_mock_system,
        annotated_mock_system,
        attrs_mock_system,
    ]:
        assert mock_system.is_stopped()
        with pytest_raises(AssertionError) as exception:
            mock_system.shut_down()
        assert (
            str(exception.value) == f"{mock_system.name} is already stopped."
        )


def test_start_up_already_started_subsystem(
    classic_mock_system: ClassicMockSystem,
    annotated_mock_system: AnnotatedMockSystem,
    attrs_mock_system: AttrsMockSystem,
):
    for mock_system in [
        classic_mock_system,
        annotated_mock_system,
        attrs_mock_system,
    ]:
        mock_system.start_up()
        assert mock_system.is_started()
        with pytest_raises(AssertionError) as exception:
            mock_system.start_up()
        assert (
            str(exception.value) == f"{mock_system.name} is already started."
        )
