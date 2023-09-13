from __future__ import annotations
from flask import Flask

from entelequia.system.module import Module
from entelequia.system.system_interface import GenericSystemInterface
from entelequia.system.system import GenericSystem

class Entelequia(Flask):

    def __init__(self, *args, modules: set[Module], **kwargs):
        self.modules: dict[str, Module] = {module.interface.accessor : module for module in modules}
        for accessor, module in self.modules.items():
            setattr(self, accessor, module.system)
        super().__init__(*args, **kwargs)

    def register_module(self, module: Module) -> None:
        self.modules[module.interface.accessor] = module

    def implements(self, interface: GenericSystemInterface) -> GenericSystem:
        return self.__system_named(
            interface.accessor,
            not_found=SystemError(f"No System implements '{interface.__name__}'."))

    def __system_named(self,
                     system_name: str,
                     not_found: Exception = SystemError('No System called by the requested name.')) -> GenericSystem:
        try:
            return self.modules[system_name].system
        except KeyError:
            raise not_found
