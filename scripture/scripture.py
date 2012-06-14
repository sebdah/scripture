"""
Basic scripture operations
"""

import config
import handlers
import definitions

import datetime

def logger(ch, method, properties, msg, configuration):
    """
    Write the message to a given backend
    """
    # Set up some configuration
    facility    = get_facility(method.routing_key)
    severity    = get_severity(method.routing_key)
    
    # Get the config object
    config_object = config.get_config_object(configuration, facility, severity)
    if not config_object:
        return False

    # Check if the severity is high enough
    if definitions.LOG_LEVELS[severity.upper()] < definitions.LOG_LEVELS[config_object['loglevel'].upper()]:
        return None

    message = format(   msg,
                        configuration['formatters'][config_object['formatter']],
                        facility = facility,
                        severity = severity)
    
    for handler in config_object['handlers']:
        if handler == 'file':
            handlers.file.log(message, config = configuration['handlers']['file'])
        
    print " [x] Received %r" % (message,)

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
