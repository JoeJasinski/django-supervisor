from djsupervisor.autoreloaders.base import AutoReloader
from djsupervisor.autoreloaders.watchdog_handler import CustomPatternMatchingEventHandler
from watchdog.observers import Observer

class WatchdogAutoReloader(AutoReloader):

    def run(self):

	event_handler = CustomPatternMatchingEventHandler(command=self._command,
		reload_progs=self._reload_progs, options=self._options,
		patterns=['*.pyo', '*.pyc', '*.py'])
	observer = Observer()
	for path in self._live_dirs:
	    observer.schedule(event_handler, path=path, recursive=True)
	observer.start()

