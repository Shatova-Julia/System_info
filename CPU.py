import psutil as psu
from main import Main


class Cpu(Main):
    info = {}
    template = '_' * 25 + '\n'

    def get(self):
        self.info.update(Count=psu.cpu_count())
        self.info.update(Persent=psu.cpu_percent(interval=1))
        return self.info

    def _prepare(self):
        for key, val in self.info.items():
            self.template += str(key) + ': ' + str(val) + ('%\n' if str(key) == 'Persent' else '\n')
            self.template += '_' * 25 + '\n'


if __name__ == '__main__':
    a = Cpu()
    a.get()
    a.show()


