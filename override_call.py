#!/usr/bin/python3
from override import Dog
from override_functions import override_init

zip = Dog("zip")
bob = Dog("bob")

instances = {
    "zip": zip,
    "bob": bob}

override_init(instances)

bob.run()
zip.run()

