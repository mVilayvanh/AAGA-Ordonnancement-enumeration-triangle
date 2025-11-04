import time

class Clock:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.stamp = list()

    def start(self):
        self.start_time = time.time()
        if self.end_time is not None:
            self.end_time = None

    def stop(self):
        self.end_time = time.time()
        self.stamp.append(self.end_time - self.start_time)

    def elapsed(self):
        if self.start_time is None:
            raise ValueError("Clock has not been started properly.")
        if self.end_time is None:
            self.stop()
        return self.stamp[-1]
    
    def get_stamps(self):
        return self.stamp

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.stamp = list()