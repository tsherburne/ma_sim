import simpy
import logging
from .structure_item import StructureItem


class Parallel(StructureItem):
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        super(Parallel, self).__init__(env, logger,
                                       construct_id, systemModel, structureItem)
        self.structureType = "Parallel"

    def simulate(self):
        self.log_start()
        parallel_items = []
        for struct in self.structureItems:
            parallel_items.append(self.env.process(struct.simulate()))

        for item in parallel_items:
            yield item

        self.log_end()
