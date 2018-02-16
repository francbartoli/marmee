# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty

"""Marmee module."""


class AbstractMarmee(object):
    """Give docstring for AbstractMarmee."""

    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        """Give the name."""
        raise NotImplementedError  # abstract

    @abstractmethod
    def get_name(self):
        """Set the method that should give the name."""
        raise NotImplementedError  # abstract

    @abstractproperty
    def is_marmee(self):
        """Give if it is the implementation."""
        raise NotImplementedError  # abstract

    @abstractproperty
    def inputs(self):
        """Give the inputs of a calculation at certain point."""
        raise NotImplementedError  # abstract

    @abstractmethod
    def set_inputs(self):
        """Set the method that should place the inputs."""
        raise NotImplementedError  # abstract

    @abstractproperty
    def results(self):
        """Give the results of a calculation at certain point."""
        raise NotImplementedError  # abstract

    @abstractmethod
    def get_results(self):
        """Set the method that should give the results."""
        raise NotImplementedError  # abstract

    @abstractproperty
    def filters(self):
        """Give the filters of a calculation at certain point."""
        raise NotImplementedError  # abstract

    @abstractmethod
    def set_filters(self):
        """Set the method that should place the filters."""
        raise NotImplementedError  # abstract
