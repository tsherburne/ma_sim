import simpy
DEF_FUNCTION_DURATION = 5
DEF_FUNCTION_TIMEOUT = 5
DEF_LINK_CAPACITY = 5
DEF_LINK_DELAY = 5

class Link:
    """
    A link is the physical implementation of an interface.
    """
    def __init__(self, env, capacity, delay):
        self.env = env
        self.delay = delay
        self.msg = simpy.Store(env)
        self.capacity = simpy.Container(env, capacity)

    def latency(self, value):
        yield self.env.timeout(self.delay)
        self.msg.put(value)

    def queue(self, value, size):
        # queue message based on link capacity and message size
        remaining = size
        while remaining > 0:
            if remaining > self.capacity.capacity:
                chunk = self.capacity.capacity
            else:
                chunk = remaining

            # handle contention of multiple senders
            self.capacity.put(chunk)
            # link: capacity of 1, transfers message of size 1 in 1 time unit
            yield self.env.timeout(chunk / self.capacity.capacity)
            self.capacity.get(chunk)

            remaining -= chunk

        self.env.process(self.latency(value))

    def put(self, value, size):
        self.env.process(self.queue(value, size))

    def get(self):
        return self.msg.get()

class Function:
    """
    A Function is a transformation that accepts one or more inputs (items)
    and transforms them into outputs (items).
    """
    def __init__(self, env, name, duration = DEF_FUNCTION_DURATION,
                                  timeout = DEF_FUNCTION_TIMEOUT, logger = None):
        self.env = env
        self.name = name
        self.duration = duration
        self.timeout = timeout
        self.logger = logger

    def execute(self):
        if self.logger is not None:
            self.logger.info('Execute Start: %s at: %d' % (self.name, self.env.now))
        self.begin()
        yield self.env.timeout(self.duration)
        self.exit()
        self.end()
        if self.logger is not None:
            self.logger.info('Execute End: %s at: %d' % (self.name, self.env.now))

    def begin(self):
        """
        Begin Logic is executed at the very beginning of function execution
        (after enablement and triggering but before resources are acquired).
        """
        return

    def exit(self):
        """
        Exit Logic determines which exit to use for a multi-exit function.
        If the exit logic is empty, the probabilities associated with the
        exits are used to choose the exit.
        """
        return

    def end(self):
        """
        End Logic is executed at the very end of function execution
        (after resources are produced and items are output).
        """
        return