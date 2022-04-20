from abc import abstractmethod


class Main:
    template = ''

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def _prepare(self):
        pass

    def show(self):
        self._prepare()
        print(self.template)
