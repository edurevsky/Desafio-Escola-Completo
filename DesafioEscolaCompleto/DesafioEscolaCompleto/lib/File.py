class ArquivoNaoEncontrado(Exception):
    pass


class NaoETipoFile(Exception):
    pass


class File:

    def __init__(self, local):
        self.__local = local

    @property
    def local(self):
        return self.__local


class Reader:

    def __init__(self, arquivo: File):
        if type(arquivo) == File:
            self.__arquivo = arquivo
        else:
            raise NaoETipoFile

    @property
    def arquivo(self):
        return self.__arquivo

    def ler(self):
        try:
            with open(file=self.arquivo.local, mode="r", encoding="UTF-8") as arquivo:
                dados = arquivo.read()
                print(dados)
                return dados
            arquivo.close()
        except FileNotFoundError:
            raise ArquivoNaoEncontrado


class Writer:

    def __init__(self, arquivo: File):
        if type(arquivo) == File:
            self.__arquivo = arquivo
        else:
            raise NaoETipoFile

    @property
    def arquivo(self):
        return self.__arquivo

    def escrever(self, texto):
        try:
            with open(file=self.arquivo.local, mode="w", encoding="UTF-8") as arquivo:
                arquivo.write(texto)
            arquivo.close()
        except FileNotFoundError:
            raise ArquivoNaoEncontrado


class Appender:

    def __init__(self, arquivo: File):
        if type(arquivo) == File:
            self.__arquivo = arquivo

    @property
    def arquivo(self):
        return self.__arquivo

    def append(self, texto, newLine: bool):
        try:
            with open(file=self.arquivo.local, mode="a", encoding="UTF-8") as arquivo:
                arquivo.write(texto)
                if newLine:
                    arquivo.write("\n")
                arquivo.flush()
            arquivo.close()
        except FileNotFoundError:
            raise ArquivoNaoEncontrado