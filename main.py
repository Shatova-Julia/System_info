import Process
import CPU
import Memory
import Swap
import Disk


def show_statistic():
    CPU.Cpu().show_cpu()
    print('_' * 50)
    Memory.Memory().show_memory()
    print('_' * 50)
    Swap.Swap().show_swap()
    print('_' * 50)
    Disk.Disk().show_disk()
    Process.Process().show_proc()


if __name__ == '__main__':
    show_statistic()
