import psutil as psu
from main import Main


class Disk(Main):
    info = {}
    template = '_' * 25 + '\n'

    def get(self):
        self.info.update(Active_time=psu.disk_usage('/').percent)

    def _prepare(self):
        for key, val in self.info.items():
            self.template += str(key).replace('_', ' ') + ': ' + str(val) + '%\n'
            self.template += '_' * 25 + '\n'


if __name__ == '__main__':
    a = Disk()
    a.get()
    a.show()
