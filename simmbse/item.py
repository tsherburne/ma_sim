import simpy
import logging


class Item:
    """
    Items represent flows within and between functions.
    An item is an input to or an output from a function.
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 systemModel: dict, item: dict):

        self.name = item['identity']['name']
        self.id = item['identity']['id']
        self.size = item['attributes']['size']
        self.type = "Item"

    def set_payload(self):
        pass

    def get_payload(self):
        pass


class ControlAction(Item):
    """
    A controller may provide control actions to control some process and
    to enforce constraints on the behavior of the controlled process.
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 systemModel: dict, item: dict):

        super(ControlAction, self).__init__(env, logger, systemModel, item)

        self.type = "ControlAction"


class Feedback(Item):
    """
    Process models may be updated in part by feedback used to observe the controlled process.
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 systemModel: dict, item: dict):

        super(Feedback, self).__init__(env, logger, systemModel, item)

        self.type = "Feedback"


class Context(Item):
    """
    The set of process model variables and values.
    """

    def __init__(self, env: simpy.Environment, logger: logging.Logger,
                 systemModel: dict, item: dict):

        super(Context, self).__init__(env, logger, systemModel, item)

        self.type = "Context"
