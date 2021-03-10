import simpy
import logging
from .structure_item import StructureItem


class Select(StructureItem):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Select, self).__init__(env, logger,
                                     construct_id, systemModel, structureItem)
        self.structureType = "Select"

    def execute(self):
        pass