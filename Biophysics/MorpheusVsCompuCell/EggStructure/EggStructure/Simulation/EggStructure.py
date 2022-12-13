
from cc3d import CompuCellSetup
        

from EggStructureSteppables import EggStructureSteppable

CompuCellSetup.register_steppable(steppable=EggStructureSteppable(frequency=1))


CompuCellSetup.run()
