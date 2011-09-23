from watchdog.events import PatternMatchingEventHandler                          

class CustomPatternMatchingEventHandler(PatternMatchingEventHandler):

    def __init__(self, command, reload_progs, options, 
                 patterns=None, ignore_patterns=None,
		 ignore_directories=False, case_sensitive=False):
	super(CustomPatternMatchingEventHandler, self).__init__()
	self._command = command 
	self._reload_progs = reload_progs
	self._patterns = patterns
	self._ignore_patterns = ignore_patterns
	self._ignore_directories = ignore_directories
	self._case_sensitive = case_sensitive            

    def on_any_event(self, event):
	#  Fork a subprocess to make the restart call.
	#  Otherwise supervisord might kill us and cancel the restart!
	if os.fork() == 0:
	    self._command.handle("restart",*self._reload_progs,**self._options)
    

