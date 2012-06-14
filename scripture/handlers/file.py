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
    
    # Check that the path exists
    if not os.path.exists(config['path']):
        print 'Path %s does not exist' % config['path']
        return False
    
    
    # Open the file handler
    try:
        file_handle = open(u'%s/%s' % (config['path'], config['filename']), 'a')
    except IOError as err:
        print "I/O error({0}): {1}".format(err.errno, err.strerror)
    
    # Write the message to the file
    file_handle.write(u'%s\n' % message)
    
    # Close the file handle
    file_handle.close()
    
    return True