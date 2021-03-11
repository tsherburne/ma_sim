import simpy

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
        """
        Delay message by
        """
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
