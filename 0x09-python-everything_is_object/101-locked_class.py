#!/usr/bin/python3
class LockedClass:
    first_name = ''

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError("object has no attribute '{}'".format(name))
