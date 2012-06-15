"""
Basic scripture operations
"""

import config
import handlers
import definitions
import logger

import datetime

def write_log(ch, method, properties, msg, configuration):
    """
    Write the message to a given backend
    """
    # Set up some configuration
    facility    = get_facility(method.routing_key)
    severity    = get_severity(method.routing_key)
    
    # Get the config object
    config_object = config.get_config_object(configuration, facility, severity)
    if config_object is None:
        logger.LOGGER.debug('No match of %s.%s in the configuration' % (facility, severity))
        return False
    elif config_object is False:
        logger.LOGGER.error('An error occurred when parsing the configuration')
        return False

    # Check if the severity is high enough
    if definitions.LOG_LEVELS[severity.upper()] < definitions.LOG_LEVELS[config_object['loglevel'].upper()]:
        logger.LOGGER.debug('Config level not high enough')
        return None

    # Format the message
    message = format(   msg,
                        configuration['formatters'][config_object['formatter']],
                        facility = facility,
                        severity = severity)
    
    # Print the message according to the handler
    for handler in config_object['handlers']:
        if configuration['handlers'][handler]['type'] == 'file_handler':
            handlers.file.log(message, config = configuration['handlers'][handler])
        
    logger.LOGGER.info("Recived %s.%s: %r" % (facility, severity, msg))

def format(message, format, facility = None, severity = None):
    """
    Return a formatted message
    """
    rtn_message = format
    rtn_message = rtn_message.replace('{{DATETIME_UTC}}', datetime.datetime.utcnow().isoformat())
    rtn_message = rtn_message.replace('{{MESSAGE}}', message)
    rtn_message = rtn_message.replace('{{FACILITY}}', facility)
    rtn_message = rtn_message.replace('{{SEVERITY}}', severity.upper())
    return rtn_message

def get_facility(routing_key):
    """
    Returns the facility given the routing key
    """
    return routing_key.split('.')[0]
    
def get_severity(routing_key):
    """
    Returns the severity given the routing key
    """
    return routing_key.split('.')[1]
