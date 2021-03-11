import simpy
import logging
from .structure_item import StructureItem

class Branch(StructureItem):
    """
    A Branch is a call StructureItem that sequentially executes contained StructureItems
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Branch, self).__init__(env, logger,
                                     construct_id, systemModel, structureItem)
        self.structureType = "Branch"
        if structureItem['annotation'] is not None:
            self.name = structureItem['annotation']
        else:
            self.name = ""

    def simulate(self):
        """
        Setup the Simpy simulation for a Branch structure
        """

        self.log_start()

        for struct in self.structureItems:
            yield(self.env.process(struct.simulate()))

        self.log_end()
