import psutil as psu


class Memory:
    @staticmethod
    def get_total_memory():
        return round(psu.virtual_memory().total / (1024 ** 3), 2)

    @staticmethod
    def get_used_memory():
        return round(psu.virtual_memory().used / (1024 ** 3), 2)

    @staticmethod
    def show_memory():
        tot_mem = round(psu.virtual_memory().total / (1024 ** 3), 2)
        use_mem = round(psu.virtual_memory().used / (1024 ** 3), 2)
        print(f'Объем ОЗУ: {tot_mem} Gb / Используется {use_mem} Gb')


if __name__ == '__main__':
    a = Memory()
    a.show_memory()
    b = a.get_total_memory()
    print(b)
    