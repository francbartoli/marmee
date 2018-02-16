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
        with pytest.raises(NotImplementedError):
            assert self.cls().is_marmee

    def test_name(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().name

    def test_get_name(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().get_name()

    def test_inputs(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().inputs

    def test_set_inputs(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().set_inputs()

    def test_results(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().results

    def test_get_results(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().get_results()

    def test_filters(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().filters

    def test_set_filters(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().set_filters()
