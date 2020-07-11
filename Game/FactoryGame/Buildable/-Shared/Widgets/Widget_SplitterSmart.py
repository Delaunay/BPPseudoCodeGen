
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import Widget_SplitterProgrammable
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import Construct
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import Destruct
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import PreConstruct
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterSmart import ExecuteUbergraph_Widget_SplitterSmart.K2Node_Event_IsDesignTime
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterSmart import ExecuteUbergraph_Widget_SplitterSmart

class Widget_SplitterSmart(Widget_SplitterProgrammable):
    mCallCustomTickOnConstruct = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_SplitterSmart(25)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SplitterSmart(40)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SplitterSmart.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterSmart(45)
    

    def ExecuteUbergraph_Widget_SplitterSmart(self):
        # Label 10
        self.Destruct()
        # End
        self.Construct()
        # End
        goto('L10')
        self.PreConstruct(IsDesignTime)
    
