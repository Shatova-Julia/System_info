import psutil as psu


class Disk:
    @staticmethod
    def get_disk():
        return psu.disk_usage('/').percent

    @staticmethod
    def show_disk():
        print("Диск: {0}%".format(psu.disk_usage('/').percent))


if __name__ == '__main__':
    a = Disk()
    a.show_disk()
    b = a.get_disk()
    print(b)
