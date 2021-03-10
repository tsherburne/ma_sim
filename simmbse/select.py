import simpy
import logging
from .structure_item import StructureItem
from .num_spec import NumSpec, Choice


class Select(StructureItem):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Select, self).__init__(env, logger,
                                     construct_id, systemModel, structureItem)
        self.structureType = "Select"

    def simulate(self):
        self.log_start()
        choice = NumSpec(Choice(len(self.structureItems))).getValue()
        yield self.env.process(self.structureItems[choice].simulate())
        self.log_end()
