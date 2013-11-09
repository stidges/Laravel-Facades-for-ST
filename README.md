# Laravel 4 Facades for Sublime Text

This [Sublime Text](http://www.sublimetext.com) package offers easy access to the Laravel 4 facades.

If you ever find yourself digging through the Laravel 4 source code in search of the code that is behind a Facade, look no further! This plugin provides easy access to all the Laravel 4 Facades through the Sublime Text Command Palette. You can access it by pressing `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (Mac) and typing 'Facade', and  you will get a list of all the available Facades.

You can also select (or set the cursor within) the Facade in your code, and press `Ctrl + Shift + F12` (`Cmd + Shift + F12` on OSX) to open the underlying Facade class.

**Note**: *Some of the Facades in this package are specific to Laravel 4.1, so they might not work for you*

## Installation ##

#### Package Control ####

Run `Package Control: Install Package` command, find and install `Laravel 4 Facades`.

#### Without Package Control (Not Recommended) ####

Clone this repository (or extract the downloaded ZIP file) to your Sublime Text packages folder. You can find your Packages folder by using the `Preferences > Browse Packages...` menu in Sublime Text.

### Updates ###

* v1.1.3 - Changed Cache and Session driver to point to Repository class instead of specific implementation. (November 8, 2013)
* v1.1.2 - Changed Manager classes to the default implementation (Thanks to [Bastian Hofmann](https://github.com/BastianHofmann) for pointing this out). (November 8, 2013)
* v1.1.1 - Added menu to `Preferences > Package Settings` to make customizing key bindings easier.
* v1.1.0 - Open Facade class under the current cursor. (November 7, 2013)
* v1.0.0 - Initial version. (November 7, 2013)


### Issues ###

Please let me know if you have any issues with this package, I would be glad to help out!
