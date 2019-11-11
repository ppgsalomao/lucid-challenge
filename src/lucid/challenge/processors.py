'''
Processors

@author: Pedro
'''

from .models import ScheduledTaskNextRun
import datetime

class NextRunProcessor(object):
    
    def __init__(self, current_hour, current_minute):
        """
        Creates a new NextRun processor with current hour and minute
        """
        self.current_hour = current_hour
        self.current_minute = current_minute
        self.now = datetime.datetime.now()
        self.now = self.now.replace(hour=current_hour, 
                                    minute=current_minute, 
                                    second=0, 
                                    microsecond=0)
    
    def calculate_next_run(self, task):
        """
        Calculates when the task will be executed next.
        Returns the minute and hour of execution and the day offset, with
        0 to today and 1 to tomorrow.
        
        task: ScheduledTask

        returns: ScheduledTaskNextRun
        """
        day_offset = 0
        hour = task.hour
        minute = task.minute
        
        if task.hour >= 0 and task.minute >= 0:
            scheduled_time = self.now.replace(hour=task.hour, 
                                              minute=task.minute)
             
            if scheduled_time < self.now:
                day_offset = 1
        elif task.minute >= 0:
            hour = self.current_hour
            if task.minute < self.current_minute:
                hour = hour + 1
                if hour == 24:
                    hour = 0
                    day_offset = 1
        elif task.hour >= 0:
            minute = 0
            if task.hour < self.current_hour:
                day_offset = 1
            elif task.hour == self.current_hour:
                minute = self.current_minute
        else:
            hour = self.current_hour
            minute = self.current_minute
            
        return ScheduledTaskNextRun(task, hour, minute, day_offset)