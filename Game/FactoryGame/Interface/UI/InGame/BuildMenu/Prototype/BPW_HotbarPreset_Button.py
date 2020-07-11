
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import CopyPresetHotbarToCurrentHotbar
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HotbarPreset_Button import ExecuteUbergraph_BPW_HotbarPreset_Button.K2Node_CustomEvent_ButtonIndex
from Script.Engine import Conv_ByteToInt
from Script.SlateCore import Margin
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HotbarPreset_Button import ExecuteUbergraph_BPW_HotbarPreset_Button
from Script.FactoryGame import PresetHotbar
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.CoreUObject import Box2D
from Script.Engine import SetArrayPropertyByName
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_GenericRightClickMenu import BPW_GenericRightClickMenu
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Interface.UI.InGame.-Shared.StandardButton_Struct import StandardButton_Struct
from Script.CoreUObject import LinearColor

class BPW_HotbarPreset_Button(UserWidget):
    mFGPlayerController: Ptr[FGPlayerController]
    mIndex: int32
    mPresetHotbar: PresetHotbar
    OnMenuItemClicked: FMulticastScriptDelegate
    OnHotbarPresetHovered: FMulticastScriptDelegate
    OnHotbarPresetUnhovered: FMulticastScriptDelegate
    
    def Cleanup(self):
        self.OnMenuItemClicked.Clear()
        # Label 10
        self.OnHotbarPresetHovered.Clear()
        self.OnHotbarPresetUnhovered.Clear()
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(29)
    

    def BndEvt__BPW_BuildMenuButton_Base_K2Node_ComponentBoundEvent_0_OnMenuOpened__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(410)
    

    def BndEvt__BPW_BuildMenuButton_Base_K2Node_ComponentBoundEvent_1_OnButtonClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(1747)
    

    def OnMenuItem(self, ButtonIndex: int32):
        ExecuteUbergraph_BPW_HotbarPreset_Button.K2Node_CustomEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(1793)
    

    def BndEvt__BPW_BuildMenuButton_Base_K2Node_ComponentBoundEvent_2_OnButtonHovered__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(1835)
    

    def BndEvt__BPW_BuildMenuButton_Base_K2Node_ComponentBoundEvent_3_OnButtonUnhovered__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(1868)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_HotbarPreset_Button(1892)
    

    def ExecuteUbergraph_BPW_HotbarPreset_Button(self):
        # Label 10
        self.Cleanup()
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        self.mFGPlayerController = Controller
        self.BPW_BuildMenuButton_Base.SetName(self.mPresetHotbar.PresetName)
        ReturnValue_0: int32 = Conv_ByteToInt(self.mPresetHotbar.IconIndex)
        
        self.mPresetHotbar.Hotbar.HotbarShortcuts = None
        Item = None
        Item = self.mPresetHotbar.Hotbar.HotbarShortcuts[ReturnValue_0]
        ReturnValue_1: Ptr[Texture2D] = Item.GetDisplayImage()
        self.BPW_BuildMenuButton_Base.SetIcon(ReturnValue_1)
        # End
        ReturnValue_2: Ptr[BPW_GenericRightClickMenu] = Default__WidgetBlueprintLibrary.Create(self, BPW_GenericRightClickMenu, None)
        Struct.Text_4_E8EE19824CB6399AF427C8B677E5F49E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 492, 'Value': 'Change Name or Icon'}"
        Struct.IconBrush_6_6BF4D8794D306ACEE50EA8B1767667C2 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        Struct.IconHeight_10_2FCF433D46FC80760CD5018CA8C45619 = 0
        Struct1.Text_4_E8EE19824CB6399AF427C8B677E5F49E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 847, 'Value': 'Overwrite with Current Hotbar'}"
        Struct1.IconBrush_6_6BF4D8794D306ACEE50EA8B1767667C2 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        Struct1.IconHeight_10_2FCF433D46FC80760CD5018CA8C45619 = 0
        Struct2.Text_4_E8EE19824CB6399AF427C8B677E5F49E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1212, 'Value': 'Remove Preset'}"
        Struct2.IconBrush_6_6BF4D8794D306ACEE50EA8B1767667C2 = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        Struct2.IconHeight_10_2FCF433D46FC80760CD5018CA8C45619 = 0
        Array: List[StandardButton_Struct] = [Struct, Struct1, Struct2]
        
        Default__KismetArrayLibrary.SetArrayPropertyByName(ReturnValue_2, "mButtons", Ref[Array])
        self.BPW_BuildMenuButton_Base.SetMenuContentWidget(ReturnValue_2)
        OutputDelegate.BindUFunction(self, OnMenuItem)
        ReturnValue_2.OnMenuButtonClicked.AddUnique(OutputDelegate)
        # End
        self.mFGPlayerController.CopyPresetHotbarToCurrentHotbar(self.mIndex)
        # End
        self.OnMenuItemClicked.ProcessMulticastDelegate(self.mIndex, ButtonIndex)
        # End
        self.OnHotbarPresetHovered.ProcessMulticastDelegate(self.mIndex)
        # End
        self.OnHotbarPresetUnhovered.ProcessMulticastDelegate()
        # End
        goto('L10')
    

    def OnHotbarPresetUnhovered__DelegateSignature(self):
        pass
    

    def OnHotbarPresetHovered__DelegateSignature(self, index: int32):
        pass
    

    def OnMenuItemClicked__DelegateSignature(self, HotbarPresetIndex: int32, MenuItemIndex: int32):
        pass
    
