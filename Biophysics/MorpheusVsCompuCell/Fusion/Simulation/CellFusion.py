
from cc3d import CompuCellSetup
        

from CellFusionSteppables import CellFusionSteppable

CompuCellSetup.register_steppable(steppable=CellFusionSteppable(frequency=1))


CompuCellSetup.run()
