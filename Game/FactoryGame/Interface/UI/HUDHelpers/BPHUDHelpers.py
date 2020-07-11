
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ParseIntoArray
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GetObjectClass
from Script.Engine import GetHUD
from Script.Engine import Replace
from Script.Engine import ClassIsChildOf
from Script.Engine import Contains
from Script.FactoryGame import FGInteractWidget
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import GetInteractWidgetStack
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import SetHUDVisibility
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import BlueprintFunctionLibrary
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class BPHUDHelpers(BlueprintFunctionLibrary):
    
    
    def DoesTextContainSearchWords(self, Input: FString, SearchFor: FString, Ignore Punctuation: bool, __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L725")
        ReturnValue: List[FString] = Default__KismetStringLibrary.ParseIntoArray(SearchFor, " ", True)
        LocalSearchWords = ReturnValue
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 141
        ReturnValue_0: int32 = len(LocalSearchWords)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L624')
        Variable_0 = Variable
        ExecutionFlow.Push("L640")
        
        Item = None
        Item = LocalSearchWords[Variable_0]
        ReturnValue_2: FString = Default__KismetStringLibrary.Replace(Input, ".", "", 1)
        ReturnValue_3: bool = Default__KismetStringLibrary.Contains(ReturnValue_2, Item, False, False)
        ReturnValue_4: bool = Ignore Punctuation and ReturnValue_3
        ReturnValue1: bool = Default__KismetStringLibrary.Contains(Input, Item, False, False)
        ReturnValue_5: bool = BooleanOR(ReturnValue1, ReturnValue_4)
        if not ReturnValue_5:
            goto('L714')
        goto(ExecutionFlow.Pop())
        # Label 624
        ReturnValue_6: bool = True
        goto('L725')
        # Label 640
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L141')
        # Label 714
        ReturnValue_6 = False
    

    def GetDefaultRCO(self, Controller: Ptr[PlayerController], __WorldContext: Ptr[Object]):
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L154')
        ReturnValue: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        RCO = ReturnValue
        # End
        # Label 154
        Default__KismetSystemLibrary.PrintString(None, "Error: Failed to get default remote call object", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
        RCO = None
    

    def FindWidgetOfClass(self, Windget: TSubclassOf[FGInteractWidget], Target: Ptr[FGGameUI], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L675")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGInteractWidget]] = Target.GetInteractWidgetStack()
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L585')
        Variable_0 = Variable
        ExecutionFlow.Push("L601")
        ReturnValue = Target.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue[Variable_0]
        ReturnValue_2: TSubclassOf[FGInteractWidget] = Default__GameplayStatics.GetObjectClass(Item)
        ReturnValue_3: bool = ClassIsChildOf(ReturnValue_2, Windget)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue = Target.GetInteractWidgetStack()
        
        Item = None
        Item = ReturnValue[Variable_0]
        Widget = Item
        # End
        # Label 585
        Widget = None
        # End
        # Label 601
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def GetFGHud(self, Controller: Ptr[Controller], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L235')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L224')
        AsFGHUD_0: Ptr[FGHUD] = AsFGHUD
        # End
        # Label 224
        AsFGHUD_0 = None
    

    def ShowHideHUD(self, isMenuOpen: bool, OwningPawn: Ptr[Pawn], Controller: Ptr[Controller], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L270')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L270')
        ReturnValue_0: bool = Not_PreBool(isMenuOpen)
        AsFGHUD.SetHUDVisibility(ReturnValue_0)
    

    def PopStackWidget(self, instigatingController: Ptr[Controller], Stack Widget: Ptr[FGInteractWidget], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](instigatingController)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L297')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L297')
        ReturnValue_0: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_1: bool = ReturnValue_0.PopWidget(Stack Widget)
    

    def PushStackWidget(self, instigatingController: Ptr[Controller], stackWidget: Ptr[FGInteractWidget], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](instigatingController)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L287')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L287')
        ReturnValue_0: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_0.PushWidget(stackWidget)
    
