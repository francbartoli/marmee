# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import ValidationError
from pystac.models.item import Item
from pystac.models.asset import Asset
from pystac.models.link import Link
from pystac.models.properties import Properties
from ee import EEException, data
import pendulum
import json
import os

TOKEN_TYPE = [
    ('Image', 'Item'),
    ('ImageCollection', 'ItemCollection')
]


class Stac(object):
    def __init__(self, gee):
        self.gee = gee

    @property
    def type(self):
        if TOKEN_TYPE[0][0] in self._get_info(
        ).get('type'):
            return TOKEN_TYPE[0][1]
        elif TOKEN_TYPE[1][0] in self._get_info(
        ).get('type'):
            return TOKEN_TYPE[1][1]

    def parse(self):
        """Parse an asset from Earth Engine to STAC item

        Raises:
            ValueError -- If asset is an ImageCollection

        Returns:
            Item -- STAC feature of the Google Earth Engine Asset
        """

        if self.type == TOKEN_TYPE[0][1]:
            try:
                return Item(
                    item_id=self._link()[1],
                    links=self._link()[0],
                    assets=self._asset(),
                    properties=self._properties()[0],
                    geometry=self._properties()[2]
                )
            except ValidationError as e:
                raise
        else:
            raise ValueError("Not implemented yet")

    def _get_info(self):
        return data.getInfo(self.gee)

    def _properties(self):
        if 'properties' in self._get_info().keys():
            extprops = self._get_info().get('properties')
            provider = license = dtime = index = ""
            footprint = {}
            for key in extprops.keys():
                if isinstance(json.dumps(extprops[key]), str):
                    if key == "provider":
                        provider = extprops[key]
                    if key == "license":
                        license = extprops[key]
                    if key == "system:time_start":
                        dtime = pendulum.from_timestamp(
                            extprops[key] / 1000
                        ).to_rfc3339_string()
                    if dtime and key == "system:time_end":
                        dtime = dtime + "/" + pendulum.from_timestamp(
                            extprops[key] / 1000
                        ).to_rfc3339_string()
                    if key == "system:index":
                        index = extprops[key]
                if isinstance(extprops[key], dict):
                    if key == "system:footprint":
                        footprint = extprops[key]
            try:
                prop = Properties(
                    datetime=dtime,
                    asset_license=license,
                    provider=provider,
                    ext_properties=extprops
                )
                return (prop, index, footprint,)
            except ValidationError as e:
                raise

    def _asset(self):
        href = name = self._properties()[1]
        try:
            asset = Asset(href=href, name=name)
            return {asset.name: asset.dict}
        except ValidationError as e:
            raise

    def _link(self):
        lang = "EN"
        linktype = ""
        if 'id' in self._get_info().keys():
            ident = self._get_info().get('id')
            href = os.path.dirname(ident)
            if data.getInfo(
                href
            ).get('type') in data.ASSET_TYPE_IMAGE_COLL:
                rel = data.ASSET_TYPE_IMAGE_COLL
            elif data.getInfo(
                href
            ).get('type') in data.ASSET_TYPE_FOLDER:
                rel = data.ASSET_TYPE_FOLDER
            try:
                return (
                    [Link(
                        href=href,
                        rel=rel,
                        hreflang=lang,
                        link_type=linktype
                    )],
                    ident,
                )
            except ValidationError as e:
                raise
        else:
            raise EEException("Asset has to be with unique id property")
