'''
Main class for Lucid Technical Assessment, from which everything will be executed.

@author: Pedro
'''
from lucid.challenge.io import InputReader, OutputWriter
from lucid.challenge.processors import NextRunProcessor

import sys

if __name__ == '__main__':
    
    # Read argument
    current_hour = int(sys.argv[1].split(':')[0]) 
    current_minute = int(sys.argv[1].split(':')[1]) 
    
    # Read user input
    reader = InputReader()
    tasks = reader.read(sys.stdin)
    
    # Process each task to calculate the next run
    writer = OutputWriter()
    processor = NextRunProcessor(current_hour, current_minute)
    for task in tasks:
        writer.write(sys.stdout, processor.calculate_next_run(task))
