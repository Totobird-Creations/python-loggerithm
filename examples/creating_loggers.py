import loggerithm



# This will return a logger object
logger = loggerithm.new()
print(logger)
# This is equivalent to doing
logger = loggerithm.Logger()
print(logger)
# You can also create a logger object inside of loggerithm
loggerithm.new('logger')
print(loggerithm.logger)
