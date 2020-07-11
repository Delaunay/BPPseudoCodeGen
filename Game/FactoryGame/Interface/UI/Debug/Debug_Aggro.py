
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Script.Engine import Default__GameplayStatics
from Script.UMG import UserWidget
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GetController
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroEntry import Widget_AggroEntry
from Script.Engine import Controller
from Script.Engine import GetAllActorsOfClass
from Script.FactoryGame import FGEnemy
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import WrapBoxSlot
from Game.FactoryGame.Interface.UI.Debug.Debug_Aggro import ExecuteUbergraph_Debug_Aggro
from Script.UMG import AddChildToWrapBox
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class Debug_Aggro(UserWidget):
    
    
    def Construct(self):
        self.ExecuteUbergraph_Debug_Aggro(638)
    

    def ExecuteUbergraph_Debug_Aggro(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L374")
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_AggroEntry] = Default__WidgetBlueprintLibrary.Create(self, Widget_AggroEntry, ReturnValue)
        
        OutActors = None
        Item = None
        Item = OutActors[Variable]
        ReturnValue_1: Ptr[Controller] = Item.GetController()
        Controller: Ptr[BP_EnemyController] = Cast[BP_EnemyController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0.AIController = Controller
        ReturnValue_2: Ptr[WrapBoxSlot] = self.mBox.AddChildToWrapBox(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 374
        ReturnValue_3: int32 = Variable + 1
        Variable: int32 = ReturnValue_3
        
        OutActors = None
        # Label 443
        ReturnValue_4: int32 = len(OutActors)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L15')
        # Label 582
        Variable = 0
        goto('L443')
        # Label 610
        Variable = 0
        goto('L582')
        OutActors: List[Ptr[FGEnemy]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, FGEnemy, Ref[OutActors])
        goto('L610')
    
