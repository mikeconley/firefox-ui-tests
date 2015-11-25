# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette_driver import Wait

import time

from firefox_puppeteer.testcases import FirefoxTestCase


class TestRestoreWindowsAfterRestart(FirefoxTestCase):

    def setUp(self):
        FirefoxTestCase.setUp(self)

        # Each list element represents a window of tabs loaded at
        # some testing URL
        self.test_windows = [
          # Window 1
          [self.marionette.absolute_url('layout/mozilla.html'),
           self.marionette.absolute_url('layout/mozilla_community.html')],

          # Window 2
          [self.marionette.absolute_url('layout/mozilla_governance.html'),
           self.marionette.absolute_url('layout/mozilla_grants.html')],

          # Window 3
          [self.marionette.absolute_url('layout/mozilla.html')],
        ]

        self.private_windows = [
          [self.marionette.absolute_url('layout/mozilla_mission.html'),
           self.marionette.absolute_url('layout/mozilla_organizations.html')],

          [self.marionette.absolute_url('layout/mozilla_projects.html'),
           self.marionette.absolute_url('layout/mozilla_mission.html')],
        ]

        # Set browser to restore previous session
        self.prefs.set_pref('browser.startup.page', 3)


    def tearDown(self):
        try:
            self.windows.close_all([self.browser.tabbar.tabs[0]])
        finally:
            FirefoxTestCase.tearDown(self)

    def test_with_variety(self):
        self.open_windows(self.test_windows)
        self.open_windows(self.private_windows, is_private=True)

        self.restart()

        windows = self.windows.all
        # We should have only restored the test_windows, and none of
        # the private_windows...
        self.assertEqual(len(windows), 3)

        for win in windows:
            print "Saw a window with %s tabs" % len(win.tabbar.tabs)
            for tab in win.tabbar.tabs:
                print "Got a tab"
                print "Saw a tab: %s" % tab.location

    def open_windows(self, urlLists, is_private=False):
        if (is_private):
            win = self.browser.open_browser(is_private=True)
            win.switch_to()
        else:
            win = self.browser

        self.open_tabs(win, urlLists[0])

        for urls in urlLists[1:]:
            print "Opening a new window"
            win = self.browser.open_browser(is_private=is_private)
            win.switch_to()
            self.open_tabs(win, urls)


    def open_tabs(self, win, urls):
        print "Opening %s for initial tab" % urls[0]
        # Send the initial tab to the first URL...
        with self.marionette.using_context('content'):
            self.marionette.navigate(urls[0])
        # If there are any remaining URLs for this window,
        # open some new tabs and navigate to them.
        for url in urls[1:]:
            print "Opening url: %s in new tab" % url
            newtab = win.tabbar.open_tab()
            with self.marionette.using_context('content'):
                self.marionette.navigate(url)
