# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Acquisition import aq_inner
from medialog.resengowidget import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implementer

import json
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
import six.moves.urllib.request, six.moves.urllib.error, six.moves.urllib.parse


class IResengoPortlet(IPortletDataProvider):
    language = schema.TextLine(
        title=_(u'Country code'),
        description=_(u'NL'),  # NOQA: E501
        required=True,
        default=u'NL'
    )

    companyId = schema.Int(
        title=_(u'Country code'),
        description=_(u'Resengo customer id'),  # NOQA: E501
        required=True,
        default=1755231
    )




@implementer(IResengoPortlet)
class Assignment(base.Assignment):
    schema = IResengoPortlet

    def __init__(self, language='NL', companyId=1755231):
        self.language = language
        self.companyId = companyId


class AddForm(base.AddForm):
    schema = IResengoPortlet
    form_fields = field.Fields(IResengoPortlet)
    label = _(u'Add Resengo widget')
    description = _(u'This portlet displays Resengo widget')

    def create(self, data):
        return Assignment(
            language=data.get('language', 'NL'),
            companyId=data.get('companyId ', 1755231),
        )


class EditForm(base.EditForm):
    schema = IResengoPortlet
    form_fields = field.Fields(IResengoPortlet)
    label = _(u'Edit Reengo widget')
    description = _(u'This portlet displays Resengo widget.')


class Renderer(base.Renderer):
    schema = IResengoPortlet
    _template = ViewPageTemplateFile('resengo.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)

    def render(self):
        return self._template()
        #return self.jscript()

    #@property
    #def available(self):
    #    '''Show the portlet only if there are elements and
    #    not an anonymous user.'''
    #    return self._data()



    #@memoize
    def jscript(self):
        #jscript =  '(function(){var k=function(a,c,d,b){if(a.getElementById(d)){if(b){var e=100;var f=function(){setTimeout(function(){e--;if(window.RESENGO_WIDGET_SCRIPT_LOADED)b();else if(0<e)f();else throw Error('resengo script failed to load');},100)};f()}}else{var g=a.getElementsByTagName(c)[0];a=a.createElement(c);a.id=d;a.src='https://static.resengo.com/ResengoWidget';b&&(a.onload=b);g.parentNode.insertBefore(a,g)}},h=function(){return #k(document,'script','resengo-flow-widget-script',function(){RESENGO_WIDGET({companyId:'{}',language:'{}}'})})};window.attachEvent?window.attachEvent('onload',h):window.addEventListener('load',h,!1)})();'''.format(
        #     self.data.companyId, self.data.language,
        #)
        jscript =  """(function(){var k=function(a,c,d,b){if(a.getElementById(d)){if(b){var e=100;var f=function(){setTimeout(function(){e--;if(window.RESENGO_WIDGET_SCRIPT_LOADED)b();else if(0<e)f();else throw Error('resengo script failed to load');},100)};f()}}else{var g=a.getElementsByTagName(c)[0];a=a.createElement(c);a.id=d;a.src='https://static.resengo.com/ResengoWidget';b&&(a.onload=b);g.parentNode.insertBefore(a,g)}},h=function(){return k(document,'script','resengo-flow-widget-script',function(){RESENGO_WIDGET({companyId:'""" +  str(self.data.companyId) + """',language:'""" + self.data.language + """'})})};window.attachEvent?window.attachEvent('onload',h):window.addEventListener('load',h,!1)})()"""

        return jscript
