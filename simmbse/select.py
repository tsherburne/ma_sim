import simpy
import logging
from .structure_item import StructureItem
from .num_spec import NumSpec, Choice


class Select(StructureItem):
    """
    Select is a call StructureItem that randomly (or per Branch selection probability)
    executes one of the contained CallStructure items.
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Select, self).__init__(env, logger,
                                     construct_id, systemModel, structureItem)
        self.structureType = "Select"

    def simulate(self):
        """
        Setup the Simpy simulation for a Select structure
        """

        self.log_start()

        # determine random choice of contained items
        choice = NumSpec(Choice(len(self.structureItems))).getValue()
        # execute random choice
        yield self.env.process(self.structureItems[choice].simulate())

        self.log_end()
