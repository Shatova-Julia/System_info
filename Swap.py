import psutil as psu


class Swap:
    @staticmethod
    def get_total_swap():
        return round(psu.swap_memory().total / (1024**3), 2)

    @staticmethod
    def get_used_swap():
        return round(psu.swap_memory().used / (1024**3), 2)

    @staticmethod
    def show_swap():
        tot_swp = round(psu.swap_memory().total / (1024**3), 2)
        use_swp = round(psu.swap_memory().used / (1024**3), 2)
        print(f'Объем Swap: {tot_swp} Gb / Используется {use_swp} Gb')


if __name__ == '__main__':
    a = Swap()
    a.show_swap()
    b = a.get_total_swap()
    print(b)
