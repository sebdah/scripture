"""
Simple file handler
"""

import os.path

def log(message, config):
    """
    Log to file
    """
    # Verify the config
    mandatory_keys = ['path', 'filename']
    for key in mandatory_keys:
        if key not in config:
            print u'Missing config key %s' % key
            return False
    
    file_handle = open(u'%s/%s' % (config['path'], config['filename']), 'a')
    file_handle.write(u'%s\n' % message)
    file_handle.close()
    
    return True