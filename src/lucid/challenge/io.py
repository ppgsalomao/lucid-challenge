'''
IO Manupulation module

@author: Pedro
'''
from .models import ScheduledTask
import re

class InputReader(object):
    '''
    Reads and validates user input, converting it to model classes
    '''

    def read(self, stream):
        """
        Reads the stream provided and converts each line to a ScheduledTask
        
        stream: stream
        
        returns: [ScheduledTask]        
        """
        tasks = []

        for line in stream:
            line = line.rstrip()
            
            line_format = "([0-9]{1,2}|\*)+ ([0-9]{1,2}|\*)+ (.*)"
            line_search = re.search(line_format, line)
            
            if line_search:
                minute = line_search.group(1)
                if minute == "*":
                    minute = -1
                else:
                    minute = int(minute)

                hour = line_search.group(2)
                if hour == "*":
                    hour = -1
                else:
                    hour = int(hour)
                    
                command = line_search.group(3)
                tasks.append(ScheduledTask(minute, hour, command))
            
            # Break on empty lines.
            if not line:
                break
        
        return tasks

class OutputWriter(object):
    '''
    Writes to the provided stream the output as described in the Test.
    '''
    
    def write(self, stream, nextRun):
        """
        Writes the ScheduledTaskNextRun in the correct format
        """
        day_offset_str = "today" if nextRun.day_offset == 0 else "tomorrow"
        stream.write("%d:%02d %s - %s\n\r" % (nextRun.hour, 
                                              nextRun.minute, 
                                              day_offset_str, 
                                              nextRun.task.command))