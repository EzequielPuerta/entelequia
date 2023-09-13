from pytest import raises as pytest_raises

from entelequia.modules.time import module as time_module

def test_app_creation(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_wrong_system_accessor(app):
    with pytest_raises(SystemError):
        app.unknown_system

def test_app_modules_accessor(app):
    assert len(app.modules) == 1

def test_register_module(app_factory):
    app = app_factory(modules=set())
    assert len(app.modules) == 0

    with pytest_raises(SystemError):
        app.implements(type(time_module.interface))

    app.register_module(time_module)
    assert len(app.modules) == 1
    assert app.modules[time_module.interface.accessor] == time_module

def test_implements(app):
    assert isinstance(app.implements(type(time_module.interface)), type(time_module.system))

def test_method_accessor(app):
    time_system = getattr(app, time_module.interface.accessor)
    assert time_system == time_module.system


# def test_interface_not_implemented(app):
#     class MockSystemInterface(GenericSystemInterface):
#         accessor: str = "mock_system"

#     class
#     with pytest_raises(SystemError):
#         app.mock_system
