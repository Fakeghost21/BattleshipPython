from UI.Console import *
from Repository.GenericRepository import *
from Service.navaService import *
from Service.atacService import *


def main():
    repoNave = GenericFileRepository("Nave.txt")
    repoAtac = GenericFileRepository("Atac.txt")
    ValidatorNave = Verif()
    serviceNava = ServiceNava(repoNave, ValidatorNave)
    validatorAtac = Valid2(serviceNava)
    serviceAtac = ServiceAtac(repoAtac, validatorAtac, repoNave)
    dr = Console(serviceNava, serviceAtac)
    dr.run_console()


main()
