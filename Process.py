import psutil as psu


class Process:

    @staticmethod
    def get_proc():
        pids = psu.pids()
        dict_1 = {}
        for pid in pids:
            if psu.pid_exists(pid):
                dict_1[pid] = [psu.Process(pid).name(),
                               psu.Process(pid).status(),
                               psu.Process(pid).memory_info().pagefile
                               ]
        return dict_1

    @staticmethod
    def show_proc():
        pids = psu.pids()
        print("|{:-<28}| {:-<28}| {:-<28}| {:-<28}|".format('', '', '', ''))
        print("|{:<28}| {:<28}| {:<28}| {:<28}|".format('PID',
                                                        'Process name',
                                                        'Status',
                                                        'Pagefile').upper())
        for pid in pids:
            if psu.pid_exists(pid):
                print("|{:-<28}| {:-<28}| {:-<28}| {:-<28}|".format('', '', '', ''))

                print("|{:<28}| {:<28}| {:<28}| {:<28}|".format(psu.Process(pid).pid,
                                                                psu.Process(pid).name(),
                                                                psu.Process(pid).status(),
                                                                psu.Process(pid).memory_info().pagefile))
        print("|{:-<28}| {:-<28}| {:-<28}| {:-<28}|".format('', '', '', ''))


if __name__ == '__main__':
    a = Process()
    print(a.get_proc())
    a.show_proc()
