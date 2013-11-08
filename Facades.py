import sublime, sublime_plugin, os.path

class FacadesCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        self.required_facade = kwargs.get('facade')
        self.window = sublime.active_window()
        self.root_folder = self.window.folders()[0] + "/"
        self.laravel_root = "vendor/laravel/framework/src/Illuminate/"
        self.facades = {
            'App': 'Foundation/Application.php',
            'Artisan': 'Foundation/Artisan.php',
            'Auth': 'Auth/AuthManager.php',
            'Blade': 'View/Compilers/BladeCompiler.php',
            'Cache': 'Cache/CacheManager.php',
            'Config': 'Config/Repository.php',
            'Cookie': 'Cookie/CookieJar.php',
            'Crypt': 'Encryption/Encrypter.php',
            'DB': 'Database/DatabaseManager.php',
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
            'Queue': 'Queue/QueueManager.php',
            'Redirect': 'Routing/Redirector.php',
            'Redis': 'Redis/Database.php',
            'Request': 'Http/Request.php',
            'Response': 'Support/Facades/Response.php',
            'Route': 'Routing/Router.php',
            'Schema': 'Database/Schema/Builder.php',
            'Session': 'Session/SessionManager.php',
            'SSH': 'Remote/RemoteManager.php',
            'URL': 'Routing/UrlGenerator.php',
            'Validator': 'Validation/Factory.php',
            'View': 'View/Environment.php'
        }

        self.file_to_open = os.path.join(self.root_folder, self.laravel_root, self.facades[self.required_facade])
        try:
            self.window.open_file(self.file_to_open)
        except IndexError:
            sublime.status_message("Please open a Laravel project.")
