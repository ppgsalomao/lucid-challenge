'''
Processors

@author: Pedro
'''

from .models import ScheduledTaskNextRun

class NextRunProcessor(object):
    
    def calculate_next_run(self, task):
        """
        Calculates when the task will be executed next.
        Returns the minute and hour of execution and the day offset, with
        0 to today and 1 to tomorrow.
        
        task: ScheduledTask

        returns: ScheduledTaskNextRun
        """
        return ScheduledTaskNextRun(task, 0, 0, 0)