import simpy
import logging
from .structure_item import StructureItem


class Loop(StructureItem):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Loop, self).__init__(env, logger,
                                   construct_id, systemModel, structureItem)
        self.structureType = "Loop"

    def execute(self):
        pass