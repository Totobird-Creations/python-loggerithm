from pathlib import Path

import sys
sys.path.insert(0, '../')
import loggerithm



# When creating a logger object, pass a pathlib.Path object to load a TOML file. View `LOGGERITHMCFG.toml`
logger = loggerithm.new(loadfromconfig=Path('./LOGGERITHMCFG.toml'))
print(logger) # This logger object has 7 methods, 1 target and has it's level set to 10

logger.TRACE    ('This is a trace message') # Trace does not show up because traces' level is lower than the targets' level and the loggers' level
logger.DEBUG    ('This is a debug message')
logger.INFO     ('This is an info message')
logger.SUCCESS  ('The logging object has be succesfully been loaded from a configure file!')
logger.WARNING  ('This is a warning message')
logger.ERROR    ('This is an error message')
logger.CRITICAL ('This is a critical message!!!!!')
