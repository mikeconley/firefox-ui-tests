# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

default_prefs = {
    'app.update.auto': False,
    'app.update.enabled': False,
    'browser.dom.window.dump.enabled': True,
    'browser.newtab.url': 'about:blank',
    'browser.newtabpage.enabled': False,
    'browser.safebrowsing.enabled': False,
    'browser.safebrowsing.malware.enabled': False,
    'browser.search.update': False,
    'browser.sessionstore.resume_from_crash': False,
    'browser.shell.checkDefaultBrowser': False,
    'browser.startup.page': 0,
    'browser.tabs.animate': False,
    'browser.tabs.remote.autostart': False,
    'browser.tabs.warnOnClose': False,
    'browser.tabs.warnOnOpen': False,
    'browser.uitour.enabled': False,
    'browser.warnOnQuit': False,
    'datareporting.healthreport.service.enabled': False,
    'datareporting.healthreport.uploadEnabled': False,
    'datareporting.healthreport.documentServerURI': "http://%(server)s/healthreport/",
    'datareporting.healthreport.about.reportUrl': "http://%(server)s/abouthealthreport/",
    'datareporting.policy.dataSubmissionEnabled': False,
    'datareporting.policy.dataSubmissionPolicyAccepted': False,
    'dom.ipc.reportProcessHangs': False,
    'dom.report_all_js_exceptions': True,
    'extensions.enabledScopes': 5,
    'extensions.autoDisableScopes': 10,
    'extensions.getAddons.cache.enabled': False,
    'extensions.installDistroAddons': False,
    'extensions.logging.enabled': True,
    'extensions.showMismatchUI': False,
    'extensions.update.enabled': False,
    'extensions.update.notifyUser': False,
    'focusmanager.testmode': True,
    'geo.provider.testing': True,
    'javascript.options.showInConsole': True,
    'security.notification_enable_delay': 0,
    'signon.rememberSignons': False,
    'startup.homepage_welcome_url': 'about:blank',
    'toolkit.startup.max_resumed_crashes': -1,
    'toolkit.telemetry.enabled': False,
}