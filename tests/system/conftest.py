import pytest
from typing import ClassVar
from attrs import define

from entelequia.system.implementation import SubsystemImplementation, SystemState


@define(repr=False)
class AttrsMockSystem(SubsystemImplementation):
    name: ClassVar[str] = "Attrs Mock System"

class AnnotatedMockSystem(SubsystemImplementation):
    name: str = "Annotated Mock System"

class ClassicMockSystem(SubsystemImplementation):
    name = "Classic Mock System"

@pytest.fixture
def attrs_mock_system() -> AttrsMockSystem:
    yield AttrsMockSystem()

@pytest.fixture
def annotated_mock_system() -> AnnotatedMockSystem:
    yield AnnotatedMockSystem()

@pytest.fixture
def classic_mock_system() -> ClassicMockSystem:
    yield ClassicMockSystem()
