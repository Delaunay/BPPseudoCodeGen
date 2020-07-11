
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Conv_StringToName
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_Animation
from Script.Engine import Texture
from Game.FactoryGame.Resource.Environment.Crystal.BP_Crystal import BP_Crystal
from Game.FactoryGame.Prototype.WAT.BP_WAT2 import BP_WAT2
from Script.Engine import Sin
from Script.FactoryGame import ScannableDetails
from Script.Engine import Conv_IntToFloat
from Script.FactoryGame import FGDropPod
from Game.FactoryGame.Resource.Environment.Berry.UI.Berry_64 import Berry_64
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import Equip_ObjectScanner
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GetTAU
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Prototype.WAT.UI.T_WAT1 import T_WAT1
from Game.FactoryGame.Equipment.ObjectScanner.Icons.Monsters_64 import Monsters_64
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenuItem import Widget_ObjectScannerMenuItem
from Game.FactoryGame.Resource.Environment.DesertShroom.UI.Mushroom_64 import Mushroom_64
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_MyGeometry
from Script.Engine import ClassIsChildOf
from Script.Engine import Cos
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_InDeltaTime
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import ExecuteUbergraph_Widget_ObjectScannerMenu
from Game.FactoryGame.World.Benefit.NutBush.BP_NutBush import BP_NutBush
from Script.UMG import Construct
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import Widget_RadialMenuButton
from Script.UMG import Widget
from Game.FactoryGame.Resource.Environment.Crystal.UI.PowerSlugGreen_64 import PowerSlugGreen_64
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Buildable.Vehicle.Vehicle_RadialMenu.Vehicle_Icon_Cancel import Vehicle_Icon_Cancel
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGEnemy
from Game.FactoryGame.World.Benefit.Mushroom.BP_Shroom_01 import BP_Shroom_01
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import BP_WAT1
from Game.FactoryGame.World.Benefit.BerryBush.BP_BerryBush import BP_BerryBush
from Game.FactoryGame.Equipment.ObjectScanner.Icons.CrashSite_64 import CrashSite_64
from Script.FactoryGame import GetAvailableObjectDetails
from Script.UMG import UMGSequencePlayer
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Resource.Environment.Nut.UI.Nut_64_new import Nut_64_new
from Game.FactoryGame.Prototype.WAT.UI.T_WAT2 import T_WAT2
from Script.Engine import IsValidClass
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_CustomEvent_scannedActorClass
from Script.FactoryGame import SetScannableEntry

class Widget_ObjectScannerMenu(FGInteractWidget):
    SceneEnter: Ptr[WidgetAnimation]
    mObjectScanner: Ptr[Equip_ObjectScanner]
    mTitle: FText = NSLOCTEXT("", "2C75340646DDF3CCBAA8D1AB59C7FE29", "Recording menu")
    mAllButtons: List[Ptr[Widget_ObjectScannerMenuItem]]
    mCircleRadius: float = 300
    mSensitivity: float = 0.10000000149011612
    mClampedMousePos: Vector2D = Namespace(X=0.5, Y=0.800000011920929)
    mCancelText: FText = NSLOCTEXT("", "4C2D66D14834105B565737A7DB28D00F", "Cancel")
    mActive: bool
    mHighlightPosition: Vector2D
    mBestItem: Ptr[Widget_ObjectScannerMenuItem]
    mBestAngle: float
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def GetScannableIcon(self, ScannableDetails: ScannableDetails):
        ReturnValue7: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_Crystal)
        if not ReturnValue7:
            goto('L85')
        Texture = PowerSlugGreen_64
        # End
        # Label 85
        ReturnValue6: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_WAT2)
        if not ReturnValue6:
            goto('L170')
        Texture = T_WAT2
        # End
        # Label 170
        ReturnValue5: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_WAT1)
        if not ReturnValue5:
            goto('L255')
        Texture = T_WAT1
        # End
        # Label 255
        ReturnValue4: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_BerryBush)
        if not ReturnValue4:
            goto('L340')
        Texture = Berry_64
        # End
        # Label 340
        ReturnValue3: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_Shroom_01)
        if not ReturnValue3:
            goto('L425')
        Texture = Mushroom_64
        # End
        # Label 425
        ReturnValue2: bool = ClassIsChildOf(ScannableDetails.ScannableClass, FGEnemy)
        if not ReturnValue2:
            goto('L510')
        Texture = Monsters_64
        # End
        # Label 510
        ReturnValue1: bool = ClassIsChildOf(ScannableDetails.ScannableClass, BP_NutBush)
        if not ReturnValue1:
            goto('L595')
        Texture = Nut_64_new
        # End
        # Label 595
        ReturnValue: bool = ClassIsChildOf(ScannableDetails.ScannableClass, FGDropPod)
        if not ReturnValue:
            goto('L675')
        Texture = CrashSite_64
    

    def Get_RingHighlighter_Visibility_0(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        Variable_0: bool = self.mActive
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetPositionInCircle(self, index: int32):
        ReturnValue: float = Conv_IntToFloat(index)
        
        Item = None
        Item = self.mAllButtons[index]
        # Label 96
        ReturnValue_0: float = ReturnValue + 0
        ReturnValue_1: float = GetTAU()
        
        ReturnValue_2: int32 = len(self.mAllButtons)
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_2)
        ReturnValue_3: float = ReturnValue_0 / ReturnValue1
        ReturnValue_4: float = ReturnValue_3 * ReturnValue_1
        ReturnValue_5: float = Cos(ReturnValue_4)
        ReturnValue_6: float = Sin(ReturnValue_4)
        ReturnValue_7: Vector2D = Vector2D(ReturnValue_5, ReturnValue_6)
        Item.mCirclePosition = ReturnValue_7
        ReturnValue = Conv_IntToFloat(index)
        ReturnValue_0 = ReturnValue + 0
        ReturnValue_1 = GetTAU()
        
        ReturnValue_2 = len(self.mAllButtons)
        ReturnValue1 = Conv_IntToFloat(ReturnValue_2)
        ReturnValue_3 = ReturnValue_0 / ReturnValue1
        ReturnValue_4 = ReturnValue_3 * ReturnValue_1
        ReturnValue_5 = Cos(ReturnValue_4)
        ReturnValue_6 = Sin(ReturnValue_4)
        ReturnValue1_0: float = ReturnValue_5 * self.mCircleRadius
        ReturnValue2: float = self.mCircleRadius * ReturnValue_6
        ReturnValue1_1: Vector2D = Vector2D(ReturnValue1_0, ReturnValue2)
        Translation = ReturnValue1_1
    

    def OnAnimationFinished(self):
        ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_Animation = Animation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ObjectScannerMenu(1869)
    

    def OnItemSelected(self, scannedActorClass: TSubclassOf[Actor]):
        ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_CustomEvent_scannedActorClass = scannedActorClass #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ObjectScannerMenu(253)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ObjectScannerMenu(422)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ObjectScannerMenu(1864)
    

    def Tick(self):
        ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ObjectScannerMenu.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ObjectScannerMenu(1929)
    

    def ExecuteUbergraph_Widget_ObjectScannerMenu(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        if not self.mActive:
           goto(ExecutionFlow.Pop())
        ReturnValue: bool = EqualEqual_IntInt(self.Widget_RadialMenu.SelectedInt, 0)
        if not ReturnValue:
            goto('L96')
        goto(ExecutionFlow.Pop())
        # Label 96
        ReturnValue1: List[ScannableDetails] = self.mObjectScanner.GetAvailableObjectDetails()
        ReturnValue_0: int32 = self.Widget_RadialMenu.SelectedInt - 1
        self.OnItemSelected(ReturnValue1[ReturnValue_0].ScannableClass)
        goto(ExecutionFlow.Pop())
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(scannedActorClass)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        self.mObjectScanner.SetScannableEntry(scannedActorClass)
        goto(ExecutionFlow.Pop())
        # Label 356
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2.SetIgnoreLookInput(False)
        goto('L15')
        goto('L356')
        # Label 427
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0.SetIgnoreLookInput(True)
        Variable: Const[FName] = "Cancel"
        
        self.Widget_RadialMenu.Buttons = None
        ReturnValue1_1: int32 = self.Widget_RadialMenu.Buttons.append(Variable)
        Variable_0: Const[Ptr[Texture]] = Vehicle_Icon_Cancel
        
        self.Widget_RadialMenu.mIconTextures = None
        ReturnValue2: int32 = self.Widget_RadialMenu.mIconTextures.append(Variable_0)
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        # Label 764
        ReturnValue_3: List[ScannableDetails] = self.mObjectScanner.GetAvailableObjectDetails()
        
        ReturnValue_4: int32 = len(ReturnValue_3)
        ReturnValue_5: bool = Variable_1 <= ReturnValue_4
        if not ReturnValue_5:
            goto('L1515')
        Variable_2 = Variable_1
        ExecutionFlow.Push("L1729")
        ReturnValue_3 = self.mObjectScanner.GetAvailableObjectDetails()
        
        Item = None
        Item = ReturnValue_3[Variable_2]
        
        Item.DisplayText = None
        ReturnValue_6: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Item.DisplayText])
        ReturnValue_7: FName = Default__KismetStringLibrary.Conv_StringToName(ReturnValue_6)
        
        self.Widget_RadialMenu.Buttons = None
        ReturnValue_8: int32 = self.Widget_RadialMenu.Buttons.append(ReturnValue_7)
        ReturnValue_3 = self.mObjectScanner.GetAvailableObjectDetails()
        
        Item = None
        Item = ReturnValue_3[Variable_2]
        
        Texture = None
        self.GetScannableIcon(Item, Ref[Texture])
        
        self.Widget_RadialMenu.mIconTextures = None
        Texture = None
        ReturnValue3: int32 = self.Widget_RadialMenu.mIconTextures.append(Texture)
        goto(ExecutionFlow.Pop())
        # Label 1515
        self.Widget_RadialMenu.Generate Radial Menu()
        ReturnValue_9: Ptr[Widget] = self.Widget_RadialMenu.mContent.GetChildAt(0)
        Button: Ptr[Widget_RadialMenuButton] = Cast[Widget_RadialMenuButton](ReturnValue_9)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.mMonochromeIcon = True
        goto(ExecutionFlow.Pop())
        # Label 1729
        ReturnValue_10: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_10
        goto('L764')
        # Label 1803
        self.Construct()
        ReturnValue_11: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SceneEnter, 0, 1, 0, 1)
        goto('L427')
        goto('L1803')
        ReturnValue_12: bool = EqualEqual_ObjectObject(self.SceneEnter, Animation)
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        self.mActive = True
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0.SetIgnoreLookInput(True)
        goto(ExecutionFlow.Pop())
    
