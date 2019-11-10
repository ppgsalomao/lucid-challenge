'''
Lucid Challenge Models.

@author: Pedro
'''

class ScheduledTask(object):
    
    def __init__(self, minute, hour, command):
        self.minute = minute
        self.hour = hour
        self.command = command
        
    def __str__(self):
        return "SheduledTask(minute=%d, hour=%d, command='%s')" \
            % (self.minute, self.hour, self.command)
            
            
class ScheduledTaskNextRun(object):
    
    def __init__(self, task, hour, minute, day_offset):
        self.task = task
        self.hour = hour
        self.minute = minute
        self.day_offset = day_offset

    def __str__(self):
        day_offset_str = "today" if self.day_offset == 0 else "tomorrow"
        return "%d:%02d %s - %s" % (self.hour, self.minute, day_offset_str,
                                    self.task.command)