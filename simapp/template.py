import simpy
import logging
from simmbse import Function

class Template(Function):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Template, self).__init__(env, logger,
                                       construct_id, systemModel, structureItem)
        print("Template init....")

    def begin(self):
        print("Template begin override....")

    def exit(self):
        print("Template exit override....")

    def end(self):
        print("Template end override....")