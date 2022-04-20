import psutil as psu
from main import Main


class Memory(Main):
    info = {}
    template = '_' * 30 + '\n'

    def get(self):
        self.info.update(Virtual_memory_total=round(psu.virtual_memory().total / (1024 ** 3), 2))
        self.info.update(Virtual_memory_used=round(psu.virtual_memory().used / (1024 ** 3), 2))
        self.info.update(Swap_memory_total=round(psu.swap_memory().total / (1024 ** 3), 2))
        self.info.update(Swap_memory_used=round(psu.swap_memory().used / (1024 ** 3), 2))

    def _prepare(self):
        for key, val in self.info.items():
            self.template += str(key).replace('_', ' ') + ': ' + str(val) + 'Gb\n'
            self.template += '_' * 30 + '\n'


if __name__ == '__main__':
    a = Memory()
    a.get()
    a.show()
