
from cc3d import CompuCellSetup
        

from DispersalSteppables import DispersalSteppable

CompuCellSetup.register_steppable(steppable=DispersalSteppable(frequency=1))


CompuCellSetup.run()
