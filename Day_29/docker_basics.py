# Day 29: Docker Basics
class DockerContainer:
    def __init__(self, name, image):
        self.name = name
        self.image = image
    def run(self):
        return f'Running {self.name} from {self.image}'
c = DockerContainer('myapp', 'python:3.9')
assert c.run() == 'Running myapp from python:3.9'
