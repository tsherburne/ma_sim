from types import MethodType

overrides = {
    'zip:bark': '_bark'}

def _bark(self):
    print (self.name + ": WoOoOoF!!")

def override_init(instances):
    for key, override_method_name in overrides.items():
        instance_name_to_override, method_name_to_override = key.split(':')
        instance_to_override = instances[instance_name_to_override]
        override_method = globals()[override_method_name]

        setattr(instance_to_override, method_name_to_override,
                                      MethodType(override_method, instance_to_override))