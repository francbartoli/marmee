======
marmee
======


.. image:: https://img.shields.io/pypi/v/marmee.svg
    :target: https://pypi.python.org/pypi/marmee

.. image:: https://img.shields.io/travis/francbartoli/marmee.svg
    :target: https://travis-ci.org/francbartoli/marmee

.. image:: https://readthedocs.org/projects/marmee/badge/?version=latest
    :target: https://marmee.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


.. image:: https://pyup.io/repos/github/francbartoli/marmee/shield.svg
    :target: https://pyup.io/repos/github/francbartoli/marmee/
    :alt: Updates


Execute safely Google Earth Engine algorithms through a tunnel like a marmot


* Free software: MIT license
* Documentation: https://marmee.readthedocs.io.


Features
--------

* TODO

STAC Parser
~~~~~~~~~~~

It can translate an object from GEE to a `STAC <https://github.com/radiantearth/stac-spec/>`_ schema representation.

.. code-block:: python

    from marmee.utils.parser import Stac
    imgAsset = 'projects/fao-wapor/L1_AET/L1_AET_0910'
    item = Stac(imgAsset).parse()
    print item.json

Which produces the JSON below as a STAC Item:

.. code-block:: json

    {
        "assets": {
            "L1_AET_0910": {
                "href": "L1_AET_0910",
                "name": "L1_AET_0910"
            }
        },
        "links": [
            {
                "href": "projects/fao-wapor/L1_AET",
                "rel": "ImageCollection",
                "hreflang": "EN"
            }
        ],
        "geometry": {
            "type": "LinearRing",
            "coordinates": [
                [
                    9.33536203029916,
                    40.00558427004632
                ],
                [
                    -1.7982352104060524,
                    40.0055842949407
                ],
                [
                    -14.416312088575413,
                    40.00558426248278
                ],
                [
                    -30.0062673066322,
                    40.00557958159156
                ],
                [
                    -30.0062673066322,
                    -40.00557958159156
                ],
                [
                    -17.756391286901717,
                    -40.0055842747424
                ],
                [
                    -4.396074577361316,
                    -40.00558421517503
                ],
                [
                    15.644400466056124,
                    -40.00558425647372
                ],
                [
                    32.3447962745126,
                    -40.005584280349574
                ],
                [
                    47.56071249632567,
                    -40.0055842595196
                ],
                [
                    65.00626724904829,
                    -40.00557956740052
                ],
                [
                    65.00626724904829,
                    40.00557956740052
                ],
                [
                    51.27191157635778,
                    40.00558426297113
                ],
                [
                    38.653834709547986,
                    40.00558426359986
                ],
                [
                    30.860316653195245,
                    40.00558428056272
                ],
                [
                    17.87111989480795,
                    40.00558425744303
                ],
                [
                    9.33536203029916,
                    40.00558427004632
                ]
            ]
        },
        "properties": {
            "provider": "",
            "ext_properties": {
                "system:index": "L1_AET_0910",
                "level": 1,
                "system:asset_size": 255491726,
                "area": "AfNE",
                "days_in_dk": 10,
                "id_no": "L1_AET_0910",
                "system:time_start": 1238544000000,
                "system:footprint": {
                    "type": "LinearRing",
                    "coordinates": [
                        [
                            9.33536203029916,
                            40.00558427004632
                        ],
                        [
                            -1.7982352104060524,
                            40.0055842949407
                        ],
                        [
                            -14.416312088575413,
                            40.00558426248278
                        ],
                        [
                            -30.0062673066322,
                            40.00557958159156
                        ],
                        [
                            -30.0062673066322,
                            -40.00557958159156
                        ],
                        [
                            -17.756391286901717,
                            -40.0055842747424
                        ],
                        [
                            -4.396074577361316,
                            -40.00558421517503
                        ],
                        [
                            15.644400466056124,
                            -40.00558425647372
                        ],
                        [
                            32.3447962745126,
                            -40.005584280349574
                        ],
                        [
                            47.56071249632567,
                            -40.0055842595196
                        ],
                        [
                            65.00626724904829,
                            -40.00557956740052
                        ],
                        [
                            65.00626724904829,
                            40.00557956740052
                        ],
                        [
                            51.27191157635778,
                            40.00558426297113
                        ],
                        [
                            38.653834709547986,
                            40.00558426359986
                        ],
                        [
                            30.860316653195245,
                            40.00558428056272
                        ],
                        [
                            17.87111989480795,
                            40.00558425744303
                        ],
                        [
                            9.33536203029916,
                            40.00558427004632
                        ]
                    ]
                }
            },
            "license": "",
            "datetime": "2009-04-01T00:00:00+00:00"
        },
        "bbox": [
            -30.0062673066322,
            -40.005584280349574,
            65.00626724904829,
            40.0055842949407
        ],
        "id": "projects/fao-wapor/L1_AET/L1_AET_0910"
    }

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
