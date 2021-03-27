class AtacException(Exception):
    pass


class Valid2:
    def __init__(self, serviceNava):
        self.__v = serviceNava

    def validate(self, atac):
        erori = []
        if self.__v.read1(atac.getIdNavaAtacata()) is None:
            erori.append("Nu exista aceasta nava atacata")
        if self.__v.read1(atac.getIdNavaAtacator()) is None:
            erori.append("Nu exista aceasta nava atacatoare")
        if atac.getIdNavaAtacata() == atac.getIdNavaAtacator():
            erori.append("Id urile celorr doua nave din atac trebuie sa fie diferite")
        try:
            p = int(atac.getPagube())
            if p < 0:
                raise ValueError
        except ValueError:
            erori.append("Pagubele trebuie sa reprezinte un numar intreg pozititv")
        if erori:
            raise AtacException(erori)
