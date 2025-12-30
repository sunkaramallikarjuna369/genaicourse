# Day 30: Docker Compose
class Service:
    def __init__(self, name):
        self.name = name
        self.status = 'stopped'
    def start(self):
        self.status = 'running'
s = Service('web')
s.start()
assert s.status == 'running'
