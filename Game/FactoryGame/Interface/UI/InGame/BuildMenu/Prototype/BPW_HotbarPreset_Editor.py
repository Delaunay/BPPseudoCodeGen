
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import FGPlayerController
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HobarPreset_Editor_SmallIcon import BPW_HobarPreset_Editor_SmallIcon
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HotbarPreset_Editor import ExecuteUbergraph_BPW_HotbarPreset_Editor.K2Node_ComponentBoundEvent_Text
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Array_Identical
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HotbarPreset_Editor import ExecuteUbergraph_BPW_HotbarPreset_Editor
from Script.FactoryGame import GetNumPresetHotbars
from Script.UMG import Widget
from Script.FactoryGame import FGHotbarShortcut
from Script.Engine import SetIntPropertyByName
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import GetPresetHotbar

class BPW_HotbarPreset_Editor(UserWidget):
    OpenAnim: Ptr[WidgetAnimation]
    OnPresetUpdated: FMulticastScriptDelegate
    mPresetIndex: int32
    mName: FText
    mIconIndex: int32
    mShortcuts: List[Ptr[FGHotbarShortcut]]
    
    def GetShouldOverwriteBar(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        ReturnValue_0: int32 = Controller.GetNumPresetHotbars()
        ReturnValue_1: bool = self.mPresetIndex <= ReturnValue_0
        if not ReturnValue_1:
            goto('L461')
        ReturnValue = self.GetOwningPlayer()
        Controller = Cast[FGPlayerController](ReturnValue)
        bSuccess = Controller
        
        presetHotbar = None
        Controller.GetPresetHotbar(self.mPresetIndex, Ref[presetHotbar])
        
        presetHotbar.Hotbar.HotbarShortcuts = None
        ReturnValue_2: bool = Default__KismetArrayLibrary.Array_Identical(Ref[presetHotbar.Hotbar.HotbarShortcuts], Ref[self.mShortcuts])
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3
        goto('L472')
        # Label 461
        ReturnValue_4 = False
    

    def OnSmallIconClicked(self, index: int32):
        ExecutionFlow.Push("L460")
        self.SetIconIndex(index)
        Variable: int32 = 0
        # Label 51
        ReturnValue: int32 = self.mSmallIconsContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L386")
        ReturnValue_1: Ptr[Widget] = self.mSmallIconsContainer.GetChildAt(Variable)
        Icon: Ptr[BPW_HobarPreset_Editor_SmallIcon] = Cast[BPW_HobarPreset_Editor_SmallIcon](ReturnValue_1)
        bSuccess: bool = Icon
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = EqualEqual_IntInt(Icon.mIndex, self.mIconIndex)
        Icon.mSetIsSelected(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 386
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def GenerateSmallIcons(self):
        ExecutionFlow.Push("L996")
        self.mSmallIconsContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 87
        ReturnValue: int32 = len(self.mShortcuts)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L922")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        
        Item = None
        Item = self.mShortcuts[Variable_0]
        ReturnValue_2: bool = Item.IsValidShortcut(Controller)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[BPW_HobarPreset_Editor_SmallIcon] = Default__WidgetBlueprintLibrary.Create(self, BPW_HobarPreset_Editor_SmallIcon, None)
        
        Item = None
        Item = self.mShortcuts[Variable_0]
        ReturnValue_4: Ptr[Texture2D] = Item.GetDisplayImage()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mIcon", ReturnValue_4)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_3, "mIndex", Variable_0)
        ReturnValue_5: Ptr[PanelSlot] = self.mSmallIconsContainer.AddChild(ReturnValue_3)
        ReturnValue_6: bool = EqualEqual_IntInt(Variable_0, self.mIconIndex)
        ReturnValue_3.mSetIsSelected(ReturnValue_6)
        OutputDelegate.BindUFunction(self, OnSmallIconClicked)
        ReturnValue_3.OnSmallIconClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 922
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L87')
    

    def SetIconIndex(self, mIconIndex: int32):
        self.mIconIndex = mIconIndex
        
        Item = None
        Item = self.mShortcuts[self.mIconIndex]
        ReturnValue: Ptr[Texture2D] = Item.GetDisplayImage()
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
    

    def SetName(self, mName: FText):
        self.mName = mName
        self.mNameTextObject.SetText(self.mName)
    

    def OnOpen(self, Name: FText, IconIndex: int32, mPresetIndex: int32, mShortcuts: Ref[List[Ptr[FGHotbarShortcut]]]):
        self.mPresetIndex = mPresetIndex
        self.mShortcuts = mShortcuts
        self.SetVisibility(0)
        self.SetName(Name)
        self.SetIconIndex(IconIndex)
        self.GenerateSmallIcons()
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OpenAnim, 0, 1, 0, 1)
    

    def BndEvt__mEditPresetCanel_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Editor(31)
    

    def BndEvt__mEditPresetAccept_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Editor(36)
    

    def BndEvt__mNameTextObject_K2Node_ComponentBoundEvent_2_OnEditableTextChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_BPW_HotbarPreset_Editor.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_HotbarPreset_Editor(136)
    

    def BndEvt__mWindow_K2Node_ComponentBoundEvent_3_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Editor(10)
    

    def ExecuteUbergraph_BPW_HotbarPreset_Editor(self):
        # Label 10
        self.SetVisibility(1)
        # End
        goto('L10')
        ReturnValue: bool = self.GetShouldOverwriteBar()
        self.OnPresetUpdated.ProcessMulticastDelegate(self.mName, self.mIconIndex, self.mPresetIndex, ReturnValue)
        self.SetVisibility(1)
        # End
        self.mName = Text
    

    def OnPresetUpdated__DelegateSignature(self, Name: FText, IconIndex: int32, PresetIndex: int32, ShouldOverwrite: bool):
        pass
    
