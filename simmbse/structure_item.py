import simpy
import logging


"""
type StructureItem {
  id: ID!
  type: StructureType
  # optional annotation for a Branch
  annotation: String
  # reference UUID / Name / Num for: Function, Exit / ExitCondition (Exit), Replicate (DomainSet) types
  referenceID: String
  referenceName: String
  referenceNum: String
  structure: [StructureItem]
}
"""


class StructureItem:
    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 construct_id: str, systemModel: dict, structureItem: dict):

        from .branch import Branch
        from .function import Function
        #from .exit import Exit, ExitCondition
        from .loop import Loop #, LoopExit
        from .parallel import Parallel
        #from .replicate import Replicate
        from .select import Select

        self.env = env
        self.logger = logger
        self.construct_id = construct_id
        self.systemModel = systemModel
        self.structureItem = structureItem
        self.structureItems = list()
        self.structureType = "" # overidden by by subclass


        for num, struct in enumerate(self.structureItem['structure'], start=1):
            next_construct_id = self.construct_id + "." + str(num)
            if struct['type'] == "Branch":
                self.structureItems.append(Branch(self.env, self.logger,
                                                  next_construct_id, self.systemModel, struct))
            elif struct['type'] == "Function":
                self.structureItems.append(Function(self.env, self.logger,
                                                    next_construct_id, self.systemModel, struct))
            elif struct['type'] == "Loop":
                self.structureItems.append(Loop(self.env, self.logger,
                                                    next_construct_id, self.systemModel, struct))
            elif struct['type'] == "Parallel":
                self.structureItems.append(Parallel(self.env, self.logger,
                                                    next_construct_id, self.systemModel, struct))
            elif struct['type'] == "Select":
                self.structureItems.append(Select(self.env, self.logger,
                                                  next_construct_id, self.systemModel, struct))

    def __str__(self):
        stmt = ("\n" + "." * self.construct_id.count(".") +
                            "Struct: %s: %s" % (self.construct_id, self.structureType))

        for struct in self.structureItems:
            stmt += struct.__str__()

        return (stmt)

