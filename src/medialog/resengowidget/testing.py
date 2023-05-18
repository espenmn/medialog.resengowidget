# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.resengowidget


class MedialogResengowidgetLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.resengowidget)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.resengowidget:default')


MEDIALOG_RESENGOWIDGET_FIXTURE = MedialogResengowidgetLayer()


MEDIALOG_RESENGOWIDGET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_RESENGOWIDGET_FIXTURE,),
    name='MedialogResengowidgetLayer:IntegrationTesting',
)


MEDIALOG_RESENGOWIDGET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_RESENGOWIDGET_FIXTURE,),
    name='MedialogResengowidgetLayer:FunctionalTesting',
)


MEDIALOG_RESENGOWIDGET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_RESENGOWIDGET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogResengowidgetLayer:AcceptanceTesting',
)
