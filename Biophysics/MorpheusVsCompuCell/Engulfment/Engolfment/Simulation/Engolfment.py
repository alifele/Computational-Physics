
from cc3d import CompuCellSetup
        

from EngolfmentSteppables import EngolfmentSteppable

CompuCellSetup.register_steppable(steppable=EngolfmentSteppable(frequency=1))


CompuCellSetup.run()
