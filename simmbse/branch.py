import simpy
import logging
from .structure_item import StructureItem


class Branch(StructureItem):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Branch, self).__init__(env, logger,
                                     construct_id, systemModel, structureItem)
        self.structureType = "Branch"

    def execute(self):
        pass
