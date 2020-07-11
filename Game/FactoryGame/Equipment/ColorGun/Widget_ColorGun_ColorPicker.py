
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Slot import Widget_ColorPicker_Slot
from Script.UMG import OverlaySlot
from Script.Engine import Conv_ByteToInt
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import GetSecondaryColorForSlot
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.UMG import SetHorizontalAlignment
from Script.Engine import IsValid
from Game.FactoryGame.Equipment.ColorGun.Equip_ColorGun import Equip_ColorGun
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot1
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot2
from Script.Engine import EqualEqual_IntInt
from Script.FactoryGame import GetPrimaryColorForSlot
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_PrimaryColor
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_EditPreset import Widget_ColorPicker_EditPreset
from Script.Engine import Conv_IntToByte
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Script.FactoryGame import SetPrimaryColorForSlot
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_SecondaryColor
from Script.UMG import Create
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGun_ColorPicker import ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot3
from Script.CoreUObject import Vector2D
from Script.FactoryGame import GetNumColorSlotsExposedToPlayers
from Script.FactoryGame import GetColorSlotIndex
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import SetColorSlot
from Script.FactoryGame import SetSecondaryColorForSlot
from Script.UMG import AddChildToOverlay
from Script.CoreUObject import LinearColor

class Widget_ColorGun_ColorPicker(UserWidget):
    mColorGun: Ptr[Equip_ColorGun]
    mSlotSizes: Vector2D = Namespace(X=90, Y=90)
    mSelectedSlot: Ptr[Widget_ColorPicker_Slot]
    OnAccept: FMulticastScriptDelegate
    OnCancel: FMulticastScriptDelegate
    SelectedIndex: int32
    
    def CompressValue(self, Value: float, MinValue: float):
        ReturnValue: float = 1 - MinValue
        ReturnValue_0: float = Value * ReturnValue
        ReturnValue_1: float = ReturnValue_0 + MinValue
        Out Value = ReturnValue_1
    

    def ConvertColorToPreviewColor(self, InputColor: LinearColor, MinValue: float):
        LocalMinValue = MinValue
        
        Value = None
        self.CompressValue(InputColor.B, LocalMinValue, Ref[Value])
        
        Value1 = None
        self.CompressValue(InputColor.G, LocalMinValue, Ref[Value1])
        
        Value2 = None
        self.CompressValue(InputColor.R, LocalMinValue, Ref[Value2])
        LinearColor.R = Value2
        LinearColor.G = Value1
        LinearColor.B = Value
        LinearColor.A = 1
        OutputColor = LinearColor
    

    def UpdatePreview(self):
        ReturnValue: uint8 = Conv_IntToByte(self.SelectedIndex)
        ReturnValue_0: LinearColor = self.mColorGun.GetPrimaryColorForSlot(ReturnValue)
        ReturnValue_1: LinearColor = self.mColorGun.GetSecondaryColorForSlot(ReturnValue)
        
        OutputColor = None
        self.ConvertColorToPreviewColor(ReturnValue_0, 0.009999999776482582, Ref[OutputColor])
        
        OutputColor1 = None
        self.ConvertColorToPreviewColor(ReturnValue_1, 0.009999999776482582, Ref[OutputColor1])
        self.Widget_ColorPicker_Preview.SetColors(OutputColor, OutputColor1)
    

    def SetupSlots(self):
        ExecutionFlow.Push("L1288")
        self.mColorGrid.ClearChildren()
        Variable: int32 = 0
        # Label 64
        ReturnValue: uint8 = self.mColorGun.GetNumColorSlotsExposedToPlayers()
        ReturnValue_0: int32 = Conv_ByteToInt(ReturnValue)
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1214")
        LocalIndex = Variable
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_ColorPicker_Slot] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorPicker_Slot, ReturnValue_3)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_4, "mSize", Ref[self.mSlotSizes])
        ReturnValue1: uint8 = Conv_IntToByte(LocalIndex)
        ReturnValue_5: LinearColor = self.mColorGun.GetPrimaryColorForSlot(ReturnValue1)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_4, "mPrimaryColor", Ref[ReturnValue_5])
        ReturnValue_6: uint8 = Conv_IntToByte(LocalIndex)
        ReturnValue_7: LinearColor = self.mColorGun.GetSecondaryColorForSlot(ReturnValue_6)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_4, "mSecondaryColor", Ref[ReturnValue_7])
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_4, "mIndex", LocalIndex)
        ReturnValue_8: Ptr[PanelSlot] = self.mColorGrid.AddChild(ReturnValue_4)
        OutputDelegate3.BindUFunction(self, OnSlotClicked)
        ReturnValue_4.OnClicked.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnSlotHovered)
        ReturnValue_4.OnHovered.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnSlotUnhovered)
        ReturnValue_4.OnUnhovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnSlotEditClicked)
        ReturnValue_4.OnEditClicked.AddUnique(OutputDelegate)
        ReturnValue_9: bool = EqualEqual_IntInt(LocalIndex, self.SelectedIndex)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        self.mSelectedSlot = ReturnValue_4
        self.mSelectedSlot.SetIsSelected(True)
        goto(ExecutionFlow.Pop())
        # Label 1214
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L64')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(315)
    

    def OnSlotClicked(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot3 = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(320)
    

    def OnSlotHovered(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot2 = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(525)
    

    def OnSlotUnhovered(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot1 = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(526)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(527)
    

    def BndEvt__mCancel_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(625)
    

    def OnSlotEditClicked(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_Slot = Slot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(645)
    

    def OnUpdatePreset(self, PrimaryColor: LinearColor, SecondaryColor: LinearColor):
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_PrimaryColor = PrimaryColor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ColorGun_ColorPicker.K2Node_CustomEvent_SecondaryColor = SecondaryColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGun_ColorPicker(1084)
    

    def ExecuteUbergraph_Widget_ColorGun_ColorPicker(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.UpdatePreview()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorGun)
        if not ReturnValue:
            goto('L238')
        ReturnValue_0: uint8 = self.mColorGun.GetColorSlotIndex()
        ReturnValue_1: int32 = Conv_ByteToInt(ReturnValue_0)
        self.SelectedIndex = ReturnValue_1
        self.SetupSlots()
        self.UpdatePreview()
        goto(ExecutionFlow.Pop())
        # Label 238
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.20000000298023224, LatentActionInfo(Linkage = 30, UUID = -96541862, ExecutionFunction = "ExecuteUbergraph_Widget_ColorGun_ColorPicker", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L30')
        ReturnValue_2: bool = NotEqual_ObjectObject(Slot3, self.mSelectedSlot)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        self.mSelectedSlot.SetIsSelected(False)
        self.mSelectedSlot = Slot3
        self.mSelectedSlot.SetIsSelected(True)
        self.SelectedIndex = self.mSelectedSlot.mIndex
        self.UpdatePreview()
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        ReturnValue_3: uint8 = Conv_IntToByte(self.SelectedIndex)
        self.mColorGun.SetColorSlot(ReturnValue_3)
        self.OnAccept.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        self.OnCancel.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_ColorPicker_EditPreset] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorPicker_EditPreset, ReturnValue_4)
        
        Slot.mPrimaryColor = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_5, "mPrimaryColor", Ref[Slot.mPrimaryColor])
        
        Slot.mSecondaryColor = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_5, "mSecondaryColor", Ref[Slot.mSecondaryColor])
        ReturnValue_6: Ptr[OverlaySlot] = self.mEditPresetContainer.AddChildToOverlay(ReturnValue_5)
        ReturnValue_6.SetHorizontalAlignment(0)
        ReturnValue_6.SetVerticalAlignment(0)
        OutputDelegate.BindUFunction(self, OnUpdatePreset)
        ReturnValue_5.OnAccept.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        ReturnValue1: uint8 = Conv_IntToByte(self.SelectedIndex)
        self.mColorGun.SetPrimaryColorForSlot(ReturnValue1, PrimaryColor)
        ReturnValue2: uint8 = Conv_IntToByte(self.SelectedIndex)
        self.mColorGun.SetSecondaryColorForSlot(ReturnValue2, SecondaryColor)
        self.mSelectedSlot.UpdateColors(PrimaryColor, SecondaryColor)
        goto('L15')
    

    def OnCancel__DelegateSignature(self):
        pass
    

    def OnAccept__DelegateSignature(self):
        pass
    
