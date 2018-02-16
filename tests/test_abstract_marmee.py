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


class TestMarmee(object):
    """docstring for testing marmee."""

    cls = AbstractMarmee

    def test_is_marmee(self):
        assert self.cls().is_marmee

    def test_name(self):
        with pytest.raises(NotImplementedError):
            assert self.cls().name
