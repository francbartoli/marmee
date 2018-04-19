#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `marmee` package."""

import pytest
from marmee.abstract_marmee import AbstractMarmee


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


class TestAbstractMarmee(object):
    """docstring for testing marmee."""

    cls = AbstractMarmee

    def test_is_marmee(self):
        try:
            self.cls().is_marmee()
        except (NotImplementedError, TypeError):
            assert True

    def test_name(self):
        try:
            self.cls().name
        except (NotImplementedError, TypeError):
            assert True

    def test_get_name(self):
        try:
            self.cls().get_name()
        except (NotImplementedError, TypeError):
            assert True

    def test_inputs(self):
        try:
            self.cls().inputs
        except (NotImplementedError, TypeError):
            assert True

    def test_set_inputs(self):
        try:
            self.cls().set_inputs()
        except (NotImplementedError, TypeError):
            assert True

    def test_results(self):
        try:
            self.cls().outputs
        except (NotImplementedError, TypeError):
            assert True

    def test_get_results(self):
        try:
            self.cls().get_outputs()
        except (NotImplementedError, TypeError):
            assert True

    def test_filters(self):
        try:
            self.cls().filters
        except (NotImplementedError, TypeError):
            assert True

    def test_set_filters(self):
        try:
            self.cls().set_filters()
        except (NotImplementedError, TypeError):
            assert True
