from djsupervisor.autoreloaders.base import AutoReloader


class PollingAutoReloader(AutoReloader):

    def run(self):
        mtimes = {}
	while True:
            if self._code_has_changed(self._live_dirs,mtimes):
	    #  Fork a subprocess to make the restart call.
	    #  Otherwise supervisord might kill us and cancel the restart!
                if os.fork() == 0:
                    self._command.handle("restart",*self._reload_progs,**self._options)
                return 0
	    time.sleep(1)


    def _code_has_changed(self,live_dirs,mtimes):
        """Check whether code under the given directories has changed.

        This is a simple check based on file mtime.  New or deleted files
        don't count as code changes.
        """
        for filepath in self._command._find_live_code_files(live_dirs):
            try:
                stat = os.stat(filepath)
            except EnvironmentError:
                continue
            if filepath not in mtimes:
                mtimes[filepath] = stat.st_mtime
            else:
                if mtimes[filepath] != stat.st_mtime:
                    return True

