from djsupervisor.autoreloaders.base import AutoReloader


class PollingAutoReloader(AutoReloader):

    def run(self):

	while True:
            if self._code_has_changed(self._live_dirs,mtimes):
	    #  Fork a subprocess to make the restart call.
	    #  Otherwise supervisord might kill us and cancel the restart!
                if os.fork() == 0:
                    self._command.handle("restart",*self._reload_progs,**self._options)
                return 0
	    time.sleep(1)

