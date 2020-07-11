
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.FactoryGame import FGColorGun
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import SetObjectPropertyByName
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.UMG import SlotAsOverlaySlot
from Script.FactoryGame import GetSecondaryColorForSlot
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetHorizontalAlignment
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ColorGun import ExecuteUbergraph_Widget_HUDBox_ColorGun
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetPrimaryColorForSlot
from Script.FactoryGame import GetCurrentAmmo
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Weapon import Widget_HUDBox_Weapon
from Script.UMG import SetBrushTintColor
from Script.UMG import Create
from Script.FactoryGame import GetColorSlotIndex
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.CoreUObject import LinearColor

class Widget_HUDBox_ColorGun(Widget_HUDBox_Equipment_Parent):
    mColorGun: Ptr[FGColorGun]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_ColorGun(1305)
    

    def UpdateColors(self):
        self.ExecuteUbergraph_Widget_HUDBox_ColorGun(1310)
    

    def ExecuteUbergraph_Widget_HUDBox_ColorGun(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 92, UUID = -2080854293, ExecutionFunction = "ExecuteUbergraph_Widget_HUDBox_ColorGun", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 92
        Gun: Ptr[FGColorGun] = Cast[FGColorGun](self.mEquipment)
        bSuccess: bool = Gun
        if not bSuccess:
            goto('L15')
        self.mColorGun = Gun
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_HUDBox_Weapon] = Default__WidgetBlueprintLibrary.Create(self, Widget_HUDBox_Weapon, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mEquipment", self.mEquipment)
        ReturnValue_1: Ptr[PanelSlot] = self.mAmmoContainer.AddChild(ReturnValue_0)
        ReturnValue_2: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(ReturnValue_0)
        ReturnValue_2.SetHorizontalAlignment(0)
        OutputDelegate.BindUFunction(self, UpdateColors)
        ReturnValue_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        goto(ExecutionFlow.Pop())
        # Label 563
        Variable: bool = False
        self.mHudBoxParent.StopWarningSign()
        goto(ExecutionFlow.Pop())
        # Label 611
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mColorGun)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: uint8 = self.mColorGun.GetColorSlotIndex()
        ReturnValue_6: LinearColor = self.mColorGun.GetPrimaryColorForSlot(ReturnValue_5)
        SlateColor.SpecifiedColor = ReturnValue_6
        SlateColor.ColorUseRule = 0
        self.mColorA.SetBrushTintColor(SlateColor)
        ReturnValue1: uint8 = self.mColorGun.GetColorSlotIndex()
        ReturnValue_7: LinearColor = self.mColorGun.GetSecondaryColorForSlot(ReturnValue1)
        SlateColor1.SpecifiedColor = ReturnValue_7
        SlateColor1.ColorUseRule = 0
        self.mColorB.SetBrushTintColor(SlateColor1)
        ReturnValue_8: int32 = self.mColorGun.GetCurrentAmmo()
        ReturnValue_9: bool = ReturnValue_8 > 0
        if not ReturnValue_9:
            goto('L1215')
        if not Variable1:
            goto('L1289')
        goto(ExecutionFlow.Pop())
        # Label 1215
        Variable1: bool = False
        if not Variable:
            goto('L1241')
        goto(ExecutionFlow.Pop())
        # Label 1241
        Variable = True
        self.mHudBoxParent.StartWarningSign()
        goto(ExecutionFlow.Pop())
        # Label 1289
        Variable1 = True
        goto('L563')
        goto('L92')
        goto('L611')
    
