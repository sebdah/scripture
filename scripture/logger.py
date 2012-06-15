"""
Scripture logging implementation
"""

import sys
import logging
import logging.config

CONFIGURATION = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)-8s - %(name)-16s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'scripture': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

logging.config.dictConfig(CONFIGURATION)
LOGGER = logging.getLogger('scripture')
