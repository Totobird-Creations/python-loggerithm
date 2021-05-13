import toml

import loggerithm
import loggerithm.handlers



def test_version():
    VERSION = toml.load('pyproject.toml')['tool']['poetry']['version']
    assert(loggerithm.__version__ == VERSION)



def test_subclass():
    loggerithm.LoggerMethod
    loggerithm.LoggerTarget
    loggerithm.Logger
    loggerithm.new
    loggerithm.handlers.STDOUT
    loggerithm.handlers.STDERR
    loggerithm.handlers.FILE
