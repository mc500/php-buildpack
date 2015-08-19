import os.path
import logging
import shutil

_log = logging.getLogger('phalcon2')

# Extension Methods
# step1
def configure(ctx):
    pass

# step5
def preprocess_commands(ctx):
    return ()

# step4
def service_commands(ctx):
    return {}

# step3
def service_environment(ctx):
    return {}

# step2
def compile(install):
    _log.info("compile")
    try:
        _log.info("check if it exists")
        #
        if os.path.exists('/app/htdocs/phalcon.so'):
            _log.info("copy")
            shutil.copy2('/app/htdocs/phalcon.so', '/app/php/phalcon.so')

        _log.info("done")
    except Exception:
        self._log.exception("Error installing NewRelic! "
                            "NewRelic will not be available.")
    return 0