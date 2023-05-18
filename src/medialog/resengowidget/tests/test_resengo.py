# -*- coding: utf-8 -*-
from medialog.resengowidget.testing import MEDIALOG_RESENGOWIDGET_FUNCTIONAL_TESTING
from medialog.resengowidget.testing import MEDIALOG_RESENGOWIDGET_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility

import unittest


class PortletIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_RESENGOWIDGET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_resengo_is_registered(self):
        portlet = getUtility(
            IPortletType,
            name='medialog.resengowidget.portlets.Resengo',
        )
        self.assertEqual(portlet.addview, 'medialog.resengowidget.portlets.Resengo')


class PortletFunctionalTest(unittest.TestCase):

    layer = MEDIALOG_RESENGOWIDGET_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
