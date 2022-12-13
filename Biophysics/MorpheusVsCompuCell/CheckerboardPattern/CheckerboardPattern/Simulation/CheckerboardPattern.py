
from cc3d import CompuCellSetup
        

from CheckerboardPatternSteppables import CheckerboardPatternSteppable

CompuCellSetup.register_steppable(steppable=CheckerboardPatternSteppable(frequency=1))


CompuCellSetup.run()
