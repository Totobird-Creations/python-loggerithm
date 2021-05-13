from coloured import ColourFg, ColourBg, Style, Reset
import loggerithm
from loggerithm import handlers
logger = loggerithm.new()



logger.newmethod(
    'info',                            # This is the name of the method that will identify it
    level = 10,                        # By default will be 0
    label = 'INFO',                    # This is what is written on screen when you log a message with this method
    fmt = (ColourFg.cyan, Style.faint) # A tuple of `coloured` formatting functions (pip install coloured)
)

logger.LOG(logger.INFO, 'My awesome logging message.')
#          |            |> The message to log
#          |> The logging method id in all capitals



# The above by itself will not do anything. There needs to be a logging target handler
# There are 3 default target handlers:
# - loggerithm.handlers.STDOUT                    : Will dump to standard out
# - loggerithm.handlers.STDERR                    : Will dump to standard error
# - loggerithm.handlers.FILE(directory, filename) : Will dump to a file
logger.newtarget(
    handlers.STDOUT, # The logging handler
    level = 10,      # The logging level of the target
# The format of the target. Comes with several parameters:
# - t_?     : Replace the question mark with a strftime parameter
# - time    : Displays datetime.datetime.now()
# - method  : Displays the method's label
# - message : Displays the message
    fmt = '[{time}] [{method}] : {message}'
)

# You can also create your own target handler
def mytargethandler(line: str):
    print('My custom target handlers says... ' + line)
logger.newtarget(
    mytargethandler,
    level = 5,
    fmt = '{message}, {method}'
)

# You can also call the logging method to log a message
logger.INFO('My even more awesome logging message.')



# Logging levels
logger.INFO.setlevel(25) # Changes the logging level of a method
logger.setlevel(10)      # Changes the logging level of the logger
