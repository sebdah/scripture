"""
Config methods
"""

import logger

def get_config_object(config, facility, severity):
    """
    Return the config object i.e
    
    'config': {
        'local0': {
            '*': {
                'handler': 'file',
                'formatter': 'default',
                'loglevel': 'info'
            }
        }
    }
    return ['config']['local0']['*']
    """
    if config['version'] != 0:
        logger.LOGGER.error('Parsing config version %s is not implemented' % config['version'])
        return False
        
    if facility in config['config']:
        if severity in config['config'][facility]:
            return config['config'][facility][severity]
        elif '*' in config['config'][facility]:
            return config['config'][facility]['*']
    
    return None
