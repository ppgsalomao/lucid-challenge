'''
Main class for Lucid Technical Assessment, from which everything will be executed.

@author: Pedro
'''
from lucid.challenge.io import InputReader, OutputWriter
from lucid.challenge.processors import NextRunProcessor

import sys

if __name__ == '__main__':
    
    # Read user input
    reader = InputReader()
    tasks = reader.read(sys.stdin)
    
    # Process each task to calculate the next run
    writer = OutputWriter()
    processor = NextRunProcessor()
    for task in tasks:
        writer.write(sys.stdout, processor.calculate_next_run(task))
