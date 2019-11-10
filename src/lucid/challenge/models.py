'''
Lucid Challenge Models.

@author: Pedro
'''

class ScheduledTask(object):
    
    def __init__(self, minute, hour, command):
        '''
        Creates a new ScheduledTask
        
        minute: int
        hour: int
        command: str
        '''
        self.minute = minute
        self.hour = hour
        self.command = command