
from cc3d import CompuCellSetup
        

from SeperationSteppables import SeperationSteppable

CompuCellSetup.register_steppable(steppable=SeperationSteppable(frequency=1))


CompuCellSetup.run()
