import psutil as psu


class Cpu:
    @staticmethod
    def get_cpu():
        return psu.cpu_percent(1, 1)

    @staticmethod
    def show_cpu():
        for i, n_cpu in enumerate(psu.cpu_percent(1, 1)):
            print("Процессор: {0}      Нагрузка: {1}%".format(i + 1, n_cpu))


if __name__ == '__main__':
    a = Cpu()
    a.show_cpu()
    b = a.get_cpu()
    print(b)
