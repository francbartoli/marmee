# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import ValidationError
from pystac.models.item import Item
from pystac.models.asset import Asset
from pystac.models.link import Link
from pystac.models.collection import Collection
from pystac.models.properties import Properties
from ee import EEException, data, Image, ImageCollection
import pendulum
import dask
from dask.delayed import delayed
import json
import os

TOKEN_TYPE = [
    ('Image', 'Item'),
    ('ImageCollection', 'Collection')
]


class Stac(object):
    def __init__(self, gee):
        self.gee = gee

    @property
    def type(self):
        if TOKEN_TYPE[0][0] == self._get_info(
        ).get('type'):
            return TOKEN_TYPE[0][1]
        elif TOKEN_TYPE[1][0] == self._get_info(
        ).get('type'):
            return TOKEN_TYPE[1][1]

    def parse(self):
        """Parse an asset from Earth Engine to STAC item

        Raises:
            ValueError -- If asset is an ImageCollection

        Returns:
            Item -- STAC feature of the Google Earth Engine Asset
            Collection -- STAC collection of the Google Earth Engine Asset
        """

        if self.type == TOKEN_TYPE[0][1]:
            try:
                return Item(
                    item_id=self._link(None, None)[1],
                    links=self._link(None, None)[0],
                    assets=self._asset(None),
                    properties=self._properties(None)[0],
                    geometry=self._properties(None)[2]
                )
            except ValidationError as e:
                raise
        elif self.type == TOKEN_TYPE[1][1]:
            try:
                # parallelize item computation
                items = [self._features_iterator(
                    feature['id'],
                    self._link(feature, data.ASSET_TYPE_IMAGE_COLL)[0],
                    self._asset(
                        feature['properties']['system:index']
                    ),
                    self._properties(feature)[0],
                    self._properties(feature)[2]
                ) for feature in self._get_full_info()['features']]
                res_list = dask.compute(items)[0]

                return Collection(
                    features=res_list
                )
            except ValidationError as e:
                raise
        else:
            raise TypeError("Unrecognized Stac type found.")

    def _get_info(self):
        return data.getInfo(self.gee)

    def _get_full_info(self):
        if self.type in TOKEN_TYPE[0][1]:
            return data.getValue(
                {'json': Image(self.gee).serialize()}
            )
        elif self.type in TOKEN_TYPE[1][1]:
            return data.getValue(
                {'json': ImageCollection(self.gee).serialize()}
            )

    def _properties(self, gson):
        if not gson:
            gson = self._get_info()
        if 'properties' in gson.keys():
            extprops = gson.get('properties')
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

    def _asset(self, gson):
        if not gson:
            gson = self._properties(None)[1]
        href = name = gson
        try:
            asset = Asset(href=href, name=name)
            return {asset.name: asset.dict}
        except ValidationError as e:
            raise

    def _link(self, gson, rel_asset):
        lang = "EN"
        linktype = ""
        if not gson:
            gson = self._get_info()
        if 'id' in gson:
            ident = gson.get('id')
            href = os.path.dirname(ident)
            if not rel_asset:
                if data.getInfo(
                    href
                ).get('type') in data.ASSET_TYPE_IMAGE_COLL:
                    rel = data.ASSET_TYPE_IMAGE_COLL
                elif data.getInfo(
                    href
                ).get('type') in data.ASSET_TYPE_FOLDER:
                    rel = data.ASSET_TYPE_FOLDER
            else:
                rel = rel_asset
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

    @delayed
    def _features_iterator(ft_id, link, asset, props, geom):

        return Item(
            item_id=ft_id,
            links=link,
            assets=asset,
            properties=props,
            geometry=geom
        )
