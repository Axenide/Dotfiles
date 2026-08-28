// ==UserScript==
// @name         Live Pywal CSS Reloader
// @namespace    fx-autoconfig
// @description  Automatically reloads the Pywal CSS theme when it changes
// @version      1.0
// @onlyonce
// ==/UserScript==

(function() {
    const file = Cc["@mozilla.org/file/local;1"]
        .createInstance(Ci.nsIFile);

    const homeDir = Services.dirsvc
        .get("Home", Ci.nsIFile)
        .path;

    file.initWithPath(
        homeDir + "/.cache/ambxst/pywalzen.css"
    );

    if (!file.exists()) {
        console.error("[Pywal] CSS file not found:", file.path);
        return;
    }

    const ios = Cc["@mozilla.org/network/io-service;1"]
        .getService(Ci.nsIIOService);

    const cssURL = ios.newFileURI(file);

    const styleSheetService =
        Cc["@mozilla.org/content/style-sheet-service;1"]
            .getService(Ci.nsIStyleSheetService);

    function reloadCSS() {
        try {
            if (styleSheetService.sheetRegistered(
                cssURL,
                styleSheetService.USER_SHEET
            )) {
                styleSheetService.unregisterSheet(
                    cssURL,
                    styleSheetService.USER_SHEET
                );
            }

            styleSheetService.loadAndRegisterSheet(
                cssURL,
                styleSheetService.USER_SHEET
            );

            console.log("[Pywal] CSS reloaded:", file.path);
        } catch (error) {
            console.error("[Pywal] Failed to reload CSS:", error);
        }
    }

    // Initial load
    reloadCSS();

    // Watch for changes
    let lastModified = file.lastModifiedTime;

    setInterval(() => {
        if (!file.exists())
            return;

        const modified = file.lastModifiedTime;

        if (modified !== lastModified) {
            lastModified = modified;
            reloadCSS();
        }
    }, 1000);
})();
