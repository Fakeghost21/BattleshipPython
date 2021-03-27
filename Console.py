from Domain.NaveSpatiale import *
from Domain.Atac import *
from Domain.navaValidator import *
from Domain.atacValidator import *
from Service.navaService import *
from Service.atacService import *


class Console:

    def __init__(self, navaService, atacServiice):
        self.__nava_service = navaService
        self.__atac_service = atacServiice

    def __show_menu(self):
        print('1. Adaugare nava.')
        print("a1. Afisare nava")
        print('2. Adaugare atac')
        print("a2. Afisare atac")
        print('3. Adaugare id atac si se scade din curent hit points al navei atacate')
        print("4. Stergerea tuturor recenzilor care contin cel putin un cuvant interzis")
        print("5. Undo la stergerea recenzilor care contin cel putin un cuvant interzis")
        print('x. Exit')

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Optiune")
            if op == "1":
                self.__handle_addNava()
            elif op == "2":
                self.__handle_addAtac()
            elif op == "3":
                self.__atac_service.atac(theId=input("Id ul atacului: "))
            elif op == "a1":
                self.__show_list(self.__nava_service.read1())
            elif op == "a2":
                self.__show_list2(self.__atac_service.read1())
            elif op == "4":
                self.__show_list(self.__atac_service.ordonare())
            elif op == "5":
                self.__atac_service.batalii()
            elif op == "x":
                break

    def __handle_addNava(self):
        try:
            id = input('ID-ul: ')
            tip = input('Tip: ')
            maxHitPoints = input('Max hit points: ')
            c = Nave(id, tip, maxHitPoints, maxHitPoints)
            self.__nava_service.create1(c)
            print('Nava a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)
        except NavaException as e:
            print(e)

    def __handle_addAtac(self):
        try:
            id = input('ID-ul: ')
            idNavaAtacator = input('Id nava atacator: ')
            idNavaAtacata = input('Id nava atacata: ')
            pagube = input("Pagube")
            r = Atac(id, idNavaAtacator, idNavaAtacata, pagube)
            self.__atac_service.create1(r)
            print('Atacul a fost adaugat!')
        except AtacException as e:
            print(e)
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __show_list(self, objects):
        for obj in objects:
            print(obj)

    def __show_list2(self, objects):
        for obj in objects:
            c = self.__nava_service.read1(obj.getIdNavaAtacator())
            c2 = self.__nava_service.read1(obj.getIdNavaAtacata())
            print(c.getTip(), c2.getTip(), obj, sep=" - ")
