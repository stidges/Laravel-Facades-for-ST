import sublime, sublime_plugin, os.path

facades = {
    'App': 'Foundation/Application.php',
    'Artisan': 'Foundation/Artisan.php',
    'Auth': 'Auth/Guard.php',
    'Blade': 'View/Compilers/BladeCompiler.php',
    'Cache': 'Cache/Repository.php',
    'Config': 'Config/Repository.php',
    'Cookie': 'Cookie/CookieJar.php',
    'Crypt': 'Encryption/Encrypter.php',
    'DB': 'Database/Connection.php',
    'Event': 'Events/Dispatcher.php',
    'File': 'Filesystem/Filesystem.php',
    'Form': 'Html/FormBuilder.php',
    'Hash': 'Hashing/BcryptHasher.php',
    'HTML': 'Html/HtmlBuilder.php',
    'Input': 'Http/Request.php',
    'Lang': 'Translation/Translator.php',
    'Log': 'Log/Writer.php',
    'Mail': 'Mail/Mailer.php',
    'Paginator': 'Pagination/Environment.php',
    'Password': 'Auth/Reminders/PasswordBroker.php',
    'Queue': 'Queue/SyncQueue.php',
    'Redirect': 'Routing/Redirector.php',
    'Redis': 'Redis/Database.php',
    'Request': 'Http/Request.php',
    'Response': 'Support/Facades/Response.php',
    'Route': 'Routing/Router.php',
    'Schema': 'Database/Schema/Builder.php',
    'Session': 'Session/Store.php',
    'SSH': 'Remote/Connection.php',
    'URL': 'Routing/UrlGenerator.php',
    'Validator': 'Validation/Factory.php',
    'View': 'View/Environment.php'
}

def _open_facade_file(window, file):
    root_folder = window.folders()[0] + "/"
    laravel_root = "vendor/laravel/framework/src/Illuminate/"
    path = os.path.join(root_folder, laravel_root, file)

    if(os.path.exists(path)):
        window.open_file(path)
    else:
        sublime.status_message("Facade class not found.")

class FacadesCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        self.required_facade = kwargs.get('facade')
        self.window = sublime.active_window()
        self.filename = facades[self.required_facade]
        _open_facade_file(self.window, self.filename)

class InlineFacadesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.window = sublime.active_window()
        self.pos = self.view.sel()[0].begin()
        self.boundary = self.view.word(self.pos)
        self.word = self.view.substr(self.boundary)

        self.found = False
        for self.facade in facades:
            if self.facade.lower() == self.word.lower():
                _open_facade_file(self.window, facades[self.facade])
                self.found = True
                break

        if self.found == False:
            sublime.status_message("Facade '%s' not found" % (self.word))
