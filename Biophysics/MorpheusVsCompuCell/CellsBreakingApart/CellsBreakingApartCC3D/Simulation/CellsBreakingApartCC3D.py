
from cc3d import CompuCellSetup
        

from CellsBreakingApartCC3DSteppables import CellsBreakingApartCC3DSteppable

CompuCellSetup.register_steppable(steppable=CellsBreakingApartCC3DSteppable(frequency=1))


CompuCellSetup.run()
