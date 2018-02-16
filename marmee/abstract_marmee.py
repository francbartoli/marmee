# -*- coding: utf-8 -*-

"""Marmee module."""


class AbstractMarmee(object):
    "docstring for AbstractMarmee"""

    @property
    def name(self):
        raise NotImplementedError  # abstract class

    @property
    def is_marmee(self):
        return True
