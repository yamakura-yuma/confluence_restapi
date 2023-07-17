#!/usr/bin/python
# coding: utf-8

import os

class EnvReader:
    def get(self, name: str) -> str|None:
        return os.environ.get(name)
