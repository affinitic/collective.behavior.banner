# -*- coding: utf-8 -*-

from plone.registry import field
from plone.registry import Record
from plone.registry.interfaces import IRegistry
from Products.CMFPlone import PloneMessageFactory as _
from zope.component import getUtility


def upgrade_registry_for_banner_scale(context):
    key_id = 'collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.banner_scale'  # noqa: E501
    registry = getUtility(IRegistry)
    records = registry.records
    if key_id in records:
        return

    record = Record(
        field.Choice(
            title=_(u'Banner scale'),
            description=_(u'Scale at which banner images are displayed'),
            required=True,
            vocabulary='collective.behavior.banner.all_sizes',
            default='preview'),
        value='preview')
    records[key_id] = record


def upgrade_registry_for_slider_global(context):
    key_id = 'collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.slider_global'
    registry = getUtility(IRegistry)
    records = registry.records
    if key_id in records:
        return

    record = Record(
        field.Bool(
            title=_(u'Slider global'),
            description=_(u'Use global slider if there is one'),
            default=False,
        ),
    )
    records[key_id] = record
