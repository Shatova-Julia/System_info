import psutil as psu
from main import Main


class Process(Main):
    info = {}
    template = '\n'

    def get(self):
        pids = psu.pids()
        for pid in pids:
            if psu.pid_exists(pid):
                self.info[pid] = [psu.Process(pid).name(),
                                  psu.Process(pid).status(),
                                  psu.Process(pid).memory_info().pagefile
                                  ]

    def _prepare(self):
        self.template += '|{:-<28}| {:-<28}| {:-<28}| {:-<28}|'.format('', '', '', '') + '\n'
        self.template += '|{:<28}| {:<28}| {:<28}| {:<28}|'.format('PID',
                                                                   'Process name',
                                                                   'Status',
                                                                   'Pagefile').upper() + '\n'
        for pid, val in self.info.items():
            self.template += '|{:-<28}| {:-<28}| {:-<28}| {:-<28}|'.format('', '', '', '') + '\n'

            self.template += '|{:<28}| {:<28}| {:<28}| {:<28}|'.format(pid, val[0], val[1], val[2]) + '\n'
        self.template += '|{:-<28}| {:-<28}| {:-<28}| {:-<28}|'.format('', '', '', '') + '\n'


if __name__ == '__main__':
    a = Process()
    a.get()
    a.show()
