from collections.abc import Generator
from typing import ClassVar

import pytest
from attrs import define

from entelequia.system.implementation import SubsystemImplementation


@define(repr=False)
class AttrsMockSystem(SubsystemImplementation):
    name: ClassVar[str] = "Attrs Mock System"


class AnnotatedMockSystem(SubsystemImplementation):
    name: str = "Annotated Mock System"


class ClassicMockSystem(SubsystemImplementation):
    name = "Classic Mock System"


@pytest.fixture
def attrs_mock_system() -> Generator[AttrsMockSystem, None, None]:
    yield AttrsMockSystem()


@pytest.fixture
def annotated_mock_system() -> Generator[AnnotatedMockSystem, None, None]:
    yield AnnotatedMockSystem()


@pytest.fixture
def classic_mock_system() -> Generator[ClassicMockSystem, None, None]:
    yield ClassicMockSystem()
