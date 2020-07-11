
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__GameplayStatics
from Script.Engine import LatentActionInfo
from Script.UMG import UMGSequencePlayer
from Script.Engine import GameInstance
from Script.UMG import PlayAnimation
from Script.Engine import Delay
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.Menu.MainMenu.Widget_AlphaInfoScreen import ExecuteUbergraph_Widget_AlphaInfoScreen
from Script.FactoryGame import Default__FGVersionFunctionLibrary
from Script.Engine import GetGameInstance
from Script.FactoryGame import EGameVersion
from Script.UMG import GetEndTime
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetGameVersion
from Script.FactoryGame import FGGameInstance
from Script.FactoryGame import SetHasSeenAlphaInfoScreen
from Script.UMG import UserWidget

class Widget_AlphaInfoScreen(UserWidget):
    AlphaSpawnAnim: Ptr[WidgetAnimation]
    
    def GetExperimentalVisibility(self):
        Variable: FString = "EXPERIMENTAL BUILD INFO"
        Variable1: FString = "EARLY ACCESS INFO"
        ReturnValue1: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue1_0: bool = EqualEqual_ByteByte(ReturnValue1, 1)
        Variable_0: bool = ReturnValue1_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mHeader.SetTitle(switch.get(Variable_0, None))
        ReturnValue: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 1)
        if not ReturnValue_0:
            goto('L445')
        self.mExperimentalNewsTextBlock.SetVisibility(0)
        self.mNewsTextBlock.SetVisibility(1)
        # End
        # Label 445
        self.mExperimentalNewsTextBlock.SetVisibility(1)
        self.mNewsTextBlock.SetVisibility(0)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AlphaInfoScreen(196)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_AlphaInfoScreen(411)
    

    def ExecuteUbergraph_Widget_AlphaInfoScreen(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.GetExperimentalVisibility()
        goto(ExecutionFlow.Pop())
        self.RemoveFromParent()
        ReturnValue: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue)
        bSuccess: bool = Instance
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Instance.SetHasSeenAlphaInfoScreen(True)
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AlphaSpawnAnim, 0, 1, 1, 1)
        self.Widget_StandardButton.SetVisibility(3)
        ReturnValue_0: float = self.AlphaSpawnAnim.GetEndTime()
        Default__KismetSystemLibrary.Delay(self, ReturnValue_0, LatentActionInfo(Linkage = 30, UUID = -139454934, ExecutionFunction = "ExecuteUbergraph_Widget_AlphaInfoScreen", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AlphaSpawnAnim, 0, 1, 0, 1)
        goto('L15')
    
