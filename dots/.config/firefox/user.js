/*
┌─────────────────────────────────────┐
│                                     │
│     ░█░█░█▀▀░█▀▀░█▀▄░░░░▀▀█░█▀▀     │
│     ░█░█░▀▀█░█▀▀░█▀▄░░░░░░█░▀▀█     │
│     ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░▀▀░░▀▀▀     │
│                                     │
└─────────────────────────────────────┘

This will make Firefox use the userChrome.css and userContent.css files located in the chrome folder of your profile folder.
With the adition of Fastfox.js, Peskyfox.js and Smoothfox.js, you can use the following user.js file to make Firefox faster and smoother.
Hope you enjoy it!
- Axenide
*/

user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);

/*
┌───────────────────────────────────────┐
│░█▀▀░█▀█░█▀▀░▀█▀░█▀▀░█▀█░█░█░░░░▀▀█░█▀▀│
│░█▀▀░█▀█░▀▀█░░█░░█▀▀░█░█░▄▀▄░░░░░░█░▀▀█│
│░▀░░░▀░▀░▀▀▀░░▀░░▀░░░▀▀▀░▀░▀░▀░░▀▀░░▀▀▀│
└───────────────────────────────────────┘
*/
user_pref("nglayout.initialpaint.delay", 0); 
user_pref("nglayout.initialpaint.delay_in_oopif", 0); 
user_pref("content.notify.interval", 100000); 
user_pref("browser.startup.preXulSkeletonUI", false);
user_pref("layout.css.grid-template-masonry-value.enabled", true);
user_pref("dom.enable_web_task_scheduling", true);
user_pref("gfx.webrender.all", true); 
user_pref("gfx.webrender.precache-shaders", true);
user_pref("gfx.webrender.compositor", true);
user_pref("layers.gpu-process.enabled", true);
user_pref("media.hardware-video-decoding.enabled", true);
user_pref("gfx.canvas.accelerated", true); 
user_pref("gfx.canvas.accelerated.cache-items", 32768);
user_pref("gfx.canvas.accelerated.cache-size", 4096);
user_pref("gfx.content.skia-font-cache-size", 80);
user_pref("image.cache.size", 10485760);
user_pref("image.mem.decode_bytes_at_a_time", 131072); 
user_pref("image.mem.shared.unmap.min_expiration_ms", 120000); 
user_pref("media.memory_cache_max_size", 1048576); 
user_pref("media.memory_caches_combined_limit_kb", 2560000); 
user_pref("media.cache_readahead_limit", 9000); 
user_pref("media.cache_resume_threshold", 6000); 
user_pref("browser.cache.memory.max_entry_size", 153600); 
user_pref("network.buffer.cache.size", 262144); 
user_pref("network.buffer.cache.count", 128); 
user_pref("network.http.max-connections", 1800); 
user_pref("network.http.max-persistent-connections-per-server", 10); 
user_pref("network.ssl_tokens_cache_capacity", 32768); 

/*
┌───────────────────────────────────────────┐
│░█▀█░█▀▀░█▀▀░█░█░█░█░█▀▀░█▀█░█░█░░░░▀▀█░█▀▀│
│░█▀▀░█▀▀░▀▀█░█▀▄░░█░░█▀▀░█░█░▄▀▄░░░░░░█░▀▀█│
│░▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░░░▀▀▀░▀░▀░▀░░▀▀░░▀▀▀│
└───────────────────────────────────────────┘
*/
user_pref("layout.css.prefers-color-scheme.content-override", 2);
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);
user_pref("app.update.suppressPrompts", true);
user_pref("browser.compactmode.show", true);
user_pref("browser.privatebrowsing.vpnpromourl", "");
user_pref("extensions.getAddons.showPane", false); 
user_pref("extensions.htmlaboutaddons.recommendations.enabled", false);
user_pref("browser.shell.checkDefaultBrowser", false);
user_pref("browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons", false);
user_pref("browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features", false);
user_pref("browser.preferences.moreFromMozilla", false);
user_pref("browser.tabs.tabmanager.enabled", false);
user_pref("full-screen-api.transition-duration.enter", "0 0");
user_pref("full-screen-api.transition-duration.leave", "0 0");
user_pref("full-screen-api.warning.delay", -1);
user_pref("full-screen-api.warning.timeout", 0);
user_pref("browser.aboutwelcome.enabled", false); 
user_pref("findbar.highlightAll", true);
user_pref("middlemouse.contentLoadURL", false);
user_pref("browser.privatebrowsing.enable-new-indicator", false);
user_pref("browser.urlbar.suggest.engines", false);
user_pref("browser.urlbar.suggest.topsites", false);
user_pref("browser.urlbar.suggest.calculator", true);
user_pref("browser.urlbar.unitConversion.enabled", true);
user_pref("browser.newtabpage.activity-stream.feeds.topsites", false); 
user_pref("browser.newtabpage.activity-stream.feeds.section.topstories", false); 
user_pref("extensions.pocket.enabled", false);
user_pref("browser.download.useDownloadDir", false);
user_pref("browser.download.alwaysOpenPanel", false);
user_pref("browser.download.manager.addToRecentDocs", false);
user_pref("browser.download.always_ask_before_handling_new_types", true);
user_pref("browser.download.open_pdf_attachments_inline", true);
user_pref("browser.tabs.loadBookmarksInTabs", true);
user_pref("browser.bookmarks.openInTabClosesMenu", false);
user_pref("cookiebanners.service.mode", 2);
user_pref("cookiebanners.service.mode.privateBrowsing", 2);
user_pref("layout.css.has-selector.enabled", true);

/*
┌───────────────────────────────────────────────┐
│░█▀▀░█▄█░█▀█░█▀█░▀█▀░█░█░█▀▀░█▀█░█░█░░░░▀▀█░█▀▀│
│░▀▀█░█░█░█░█░█░█░░█░░█▀█░█▀▀░█░█░▄▀▄░░░░░░█░▀▀█│
│░▀▀▀░▀░▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀░░░▀▀▀░▀░▀░▀░░▀▀░░▀▀▀│
└───────────────────────────────────────────────┘
*/
user_pref("general.smoothScroll",                       true); 
user_pref("general.smoothScroll.msdPhysics.enabled",    true);
user_pref("general.smoothScroll.msdPhysics.continuousMotionMaxDeltaMS", 12);
user_pref("general.smoothScroll.msdPhysics.enabled",                    true);
user_pref("general.smoothScroll.msdPhysics.motionBeginSpringConstant",  600);
user_pref("general.smoothScroll.msdPhysics.regularSpringConstant",      650);
user_pref("general.smoothScroll.msdPhysics.slowdownMinDeltaMS",         25);
user_pref("general.smoothScroll.msdPhysics.slowdownMinDeltaRatio",      2.0);
user_pref("general.smoothScroll.msdPhysics.slowdownSpringConstant",     250);
user_pref("general.smoothScroll.currentVelocityWeighting",              1.0);
user_pref("general.smoothScroll.stopDecelerationWeighting",             1.0);
user_pref("mousewheel.default.delta_multiplier_y",                      100); 

/*
┌────────┐
│░█░█░▀█▀│
│░█░█░░█░│
│░▀▀▀░▀▀▀│
└────────┘
*/
user_pref("browser.uiCustomization.state", "{\"placements\":{\"widget-overflow-fixed-list\":[],\"unified-extensions-area\":[\"78272b6fa58f4a1abaac99321d503a20_proton_me-browser-action\",\"newtaboverride_agenedia_com-browser-action\",\"userchrome-toggle_joolee_nl-browser-action\",\"ublock0_raymondhill_net-browser-action\",\"_3c078156-979c-498b-8990-85f7987dd929_-browser-action\",\"jid1-zadieub7xozojw_jetpack-browser-action\",\"vimium-c_gdh1995_cn-browser-action\",\"_762f9885-5a13-4abd-9c77-433dcd38b8fd_-browser-action\",\"pywalfox_frewacom_org-browser-action\",\"user-agent-switcher_ninetailed_ninja-browser-action\",\"_testpilot-containers-browser-action\",\"jid1-kkzogwgsw3ao4q_jetpack-browser-action\",\"_46551ec9-40f0-4e47-8e18-8e5cf550cfb8_-browser-action\",\"tabcenter-reborn_ariasuni-browser-action\",\"firefoxcolor_mozilla_com-browser-action\",\"_4c421bb7-c1de-4dc6-80c7-ce8625e34d24_-browser-action\",\"side-view_mozilla_org-browser-action\",\"_12cf650b-1822-40aa-bff0-996df6948878_-browser-action\"],\"nav-bar\":[\"back-button\",\"forward-button\",\"home-button\",\"urlbar-container\",\"save-to-pocket-button\",\"downloads-button\",\"unified-extensions-button\"],\"toolbar-menubar\":[\"menubar-items\"],\"TabsToolbar\":[\"tabbrowser-tabs\",\"alltabs-button\"],\"PersonalToolbar\":[\"personal-bookmarks\"]},\"seen\":[\"save-to-pocket-button\",\"developer-button\",\"userchrome-toggle_joolee_nl-browser-action\",\"_3c078156-979c-498b-8990-85f7987dd929_-browser-action\",\"jid1-zadieub7xozojw_jetpack-browser-action\",\"_762f9885-5a13-4abd-9c77-433dcd38b8fd_-browser-action\",\"user-agent-switcher_ninetailed_ninja-browser-action\",\"vimium-c_gdh1995_cn-browser-action\",\"_testpilot-containers-browser-action\",\"ublock0_raymondhill_net-browser-action\",\"jid1-kkzogwgsw3ao4q_jetpack-browser-action\",\"_46551ec9-40f0-4e47-8e18-8e5cf550cfb8_-browser-action\",\"tabcenter-reborn_ariasuni-browser-action\",\"firefoxcolor_mozilla_com-browser-action\",\"newtaboverride_agenedia_com-browser-action\",\"_4c421bb7-c1de-4dc6-80c7-ce8625e34d24_-browser-action\",\"side-view_mozilla_org-browser-action\",\"pywalfox_frewacom_org-browser-action\",\"78272b6fa58f4a1abaac99321d503a20_proton_me-browser-action\",\"_12cf650b-1822-40aa-bff0-996df6948878_-browser-action\"],\"dirtyAreaCache\":[\"nav-bar\",\"PersonalToolbar\",\"toolbar-menubar\",\"TabsToolbar\",\"unified-extensions-area\"],\"currentVersion\":20,\"newElementCount\":30}");

user_pref("animatedFox.centeredTabs", true);
user_pref("animatedFox.centeredUrl", true);
user_pref("animatedFox.hideSingleTab", true);
user_pref("animatedFox.roundedCorners", true);
user_pref("animatedFox.showTabCloseButton", true);
