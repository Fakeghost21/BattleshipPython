from Domain.NaveSpatiale import *
from Service.navaService import *
from Repository.GenericRepository import *
import unittest


class NavaException(Exception):
    pass


class Verif:
    def validate(self, nava):
        erori = []
        if nava.getTip() == "":
            erori.append("Tipul trebuie sa fie nenul.")
        try:
            p = int(nava.getMaxHitPoints())
            if p != abs(p):
                raise ValueError
        except ValueError:
            erori.append("Punctele maxime acumulate trebuie sa reprezinte un numar intreg nenul")
        if erori:
            raise NavaException(erori)


def test():
    validator = Verif()
    n1 = Nave(theId="eg22eea", tip="", maxHitPoints="123456", curentHitPoints="123456")
    repo = GenericFileRepository("NaveTeste.txt")
    service = ServiceNava(repo, validator)
    try:
        service.create1(n1)
    except NavaException:
        pass
    n2 = Nave(theId="eg22eea", tip="fewfwefe", maxHitPoints="-123456", curentHitPoints="123456")
    try:
        service.create1(n2)
    except NavaException:
        pass
    n3 = Nave(theId="eg22eea", tip="", maxHitPoints="-123456", curentHitPoints="123456")
    try:
        service.create1(n3)
    except NavaException:
        pass
    assert len(service.read1()) == 0
    n4 = Nave(theId="eg22eea", tip="fhsgcvha", maxHitPoints="123456", curentHitPoints="123456")
    try:
        service.create1(n4)
    except NavaException:
        pass
    assert len(service.read1()) == 1
    n4 = Nave(theId="eg22eea", tip="hjbjhb", maxHitPoints="1234578", curentHitPoints="1234578")
    try:
        service.create1(n4)
    except ValueError:
        pass
    assert len(service.read1()) == 1


test()
