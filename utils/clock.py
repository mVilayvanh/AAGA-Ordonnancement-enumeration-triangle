import time

class Clock:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        if self.end_time is not None:
            self.end_time = None

    def stop(self):
        self.end_time = time.time()

    def elapsed(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Clock has not been started and stopped properly.")
        return self.end_time - self.start_time
    
    def reset(self):
        self.start_time = None
        self.end_time = None