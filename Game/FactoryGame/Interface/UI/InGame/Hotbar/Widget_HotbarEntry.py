
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarEntry import ExecuteUbergraph_Widget_HotbarEntry.K2Node_CustomEvent_ShowNotification
from Script.Engine import Delay
from Script.FactoryGame import FGPlayerController
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Assets.Hotbar.hotbar_slot_empty import hotbar_slot_empty
from Script.Engine import Conv_IntToText
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BooleanOR
from Script.FactoryGame import Default__FGRecipeManager
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import FGHotbarShortcut
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Assets.Hotbar.hotbar_slot_default import hotbar_slot_default
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarEntry import ExecuteUbergraph_Widget_HotbarEntry
from Game.FactoryGame.Interface.UI.Assets.Hotbar.hotbar_slot_active import hotbar_slot_active
from Script.UMG import UMGSequencePlayer
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Script.FactoryGame import FGRecipeManager
from Game.FactoryGame.Interface.UI.InGame.Hotbar.Widget_HotbarContainer import Widget_HotbarContainer
from Game.FactoryGame.Interface.UI.Assets.Materials.127_Grey import 127_Grey
from Script.CoreUObject import LinearColor

class Widget_HotbarEntry(UserWidget):
    FocusAnimation: Ptr[WidgetAnimation]
    SpawnAnimation: Ptr[WidgetAnimation]
    mShortcut: Ptr[FGHotbarShortcut]
    mShortcutIndex: int32
    CachedIsValid: bool
    CachedIsActive: bool
    WasActive: bool
    LastShortcutTexture: Ptr[Texture]
    mHotbarContainer: Ptr[Widget_HotbarContainer]
    mShowNotification: bool
    padding = Namespace(Bottom=2, Left=4, Right=4, Top=2)
    
    def GetIconVisibility(self):
        if not self.CachedIsValid:
            goto('L39')
        ReturnValue = 3
        goto('L59')
        # Label 39
        ReturnValue = 2
    

    def GetSlotTextColor(self):
        mHotbarSlotTextActiveColor = SlateColor(SpecifiedColor = LinearColor(R = 0.05098000168800354, G = 0.05098000168800354, B = 0.05098000168800354, A = 1), ColorUseRule = 0)
        mHotbarSlotTextDefaultColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        if not self.CachedIsActive:
            goto('L182')
        ReturnValue = mHotbarSlotTextActiveColor
        goto('L209')
        # Label 182
        ReturnValue = mHotbarSlotTextDefaultColor
    

    def GetSlotBrush(self):
        mHotbarSlotDefault = hotbar_slot_default
        mHotbarSlotActive = hotbar_slot_active
        mHotbarSlotEmpty = hotbar_slot_empty
        if not self.CachedIsActive:
            goto('L533')
        SlateBrush2.ImageSize = self.mHotbarSlot.Brush.ImageSize
        SlateBrush2.Margin = self.mHotbarSlot.Brush.Margin
        SlateBrush2.TintColor = self.mHotbarSlot.Brush.TintColor
        SlateBrush2.ResourceObject = mHotbarSlotActive
        SlateBrush2.DrawAs = self.mHotbarSlot.Brush.DrawAs
        SlateBrush2.Tiling = self.mHotbarSlot.Brush.Tiling
        SlateBrush2.Mirroring = self.mHotbarSlot.Brush.Mirroring
        ReturnValue = SlateBrush2
        goto('L1466')
        # Label 533
        if not self.CachedIsValid:
            goto('L1009')
        SlateBrush.ImageSize = self.mHotbarSlot.Brush.ImageSize
        SlateBrush.Margin = self.mHotbarSlot.Brush.Margin
        SlateBrush.TintColor = self.mHotbarSlot.Brush.TintColor
        SlateBrush.ResourceObject = mHotbarSlotDefault
        SlateBrush.DrawAs = self.mHotbarSlot.Brush.DrawAs
        SlateBrush.Tiling = self.mHotbarSlot.Brush.Tiling
        SlateBrush.Mirroring = self.mHotbarSlot.Brush.Mirroring
        ReturnValue = SlateBrush
        goto('L1466')
        # Label 1009
        SlateBrush1.ImageSize = self.mHotbarSlot.Brush.ImageSize
        SlateBrush1.Margin = self.mHotbarSlot.Brush.Margin
        SlateBrush1.TintColor = self.mHotbarSlot.Brush.TintColor
        SlateBrush1.ResourceObject = mHotbarSlotEmpty
        SlateBrush1.DrawAs = self.mHotbarSlot.Brush.DrawAs
        SlateBrush1.Tiling = self.mHotbarSlot.Brush.Tiling
        SlateBrush1.Mirroring = self.mHotbarSlot.Brush.Mirroring
        ReturnValue = SlateBrush1
    

    def GetSlotText(self):
        ReturnValue: bool = BooleanOR(self.CachedIsActive, self.CachedIsValid)
        if not ReturnValue:
            goto('L197')
        ReturnValue_0: int32 = self.mShortcutIndex + 1
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        ReturnValue_2: FText = ReturnValue_1
        goto('L217')
        # Label 197
        ReturnValue_2 = 
    

    def GetIcon(self):
        if not self.CachedIsValid:
            goto('L517')
        ReturnValue: Ptr[Texture2D] = self.mShortcut.GetDisplayImage()
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        ReturnValue_0: SlateBrush = SlateBrush
    

    def OnHotbarUpdated(self, ShowNotification: bool):
        ExecuteUbergraph_Widget_HotbarEntry.K2Node_CustomEvent_ShowNotification = ShowNotification #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HotbarEntry(1407)
    

    def ExecuteUbergraph_Widget_HotbarEntry(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 39
        ReturnValue: Ptr[FGRecipeManager] = Default__FGRecipeManager.Get(ReturnValue2)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L934')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess1: bool = Controller1
        ReturnValue_1: bool = self.mShortcut.IsValidShortcut(Controller1)
        self.CachedIsValid = ReturnValue_1
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        ReturnValue_3: bool = self.mShortcut.IsActive(Controller)
        self.CachedIsActive = ReturnValue_3
        ReturnValue_4: SlateBrush = self.GetSlotBrush()
        
        self.mHotbarSlot.SetBrush(Ref[ReturnValue_4])
        ReturnValue_5: SlateBrush = self.GetIcon()
        
        self.mIcon.SetBrush(Ref[ReturnValue_5])
        ReturnValue_6: uint8 = self.GetIconVisibility()
        self.mIcon.SetVisibility(ReturnValue_6)
        ReturnValue_7: FText = self.GetSlotText()
        self.mNumberText.SetText(ReturnValue_7)
        ReturnValue_8: SlateColor = self.GetSlotTextColor()
        self.mNumberText.SetColorAndOpacity(ReturnValue_8)
        if not self.CachedIsActive:
            goto('L1011')
        ReturnValue_9: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FocusAnimation, 0, 1, 0, 1)
        self.WasActive = True
        goto(ExecutionFlow.Pop())
        # Label 934
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -312706902, ExecutionFunction = "ExecuteUbergraph_Widget_HotbarEntry", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1011
        if not self.WasActive:
            goto('L1083')
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FocusAnimation, 0, 1, 1, 1)
        self.WasActive = False
        goto(ExecutionFlow.Pop())
        # Label 1083
        if not self.CachedIsValid:
            goto('L1387')
        ReturnValue_10: Ptr[Texture2D] = self.mShortcut.GetDisplayImage()
        ReturnValue_11: bool = EqualEqual_ObjectObject(ReturnValue_10, self.LastShortcutTexture)
        ReturnValue_12: bool = Not_PreBool(ReturnValue_11)
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 0, 1)
        ReturnValue1_1: Ptr[Texture2D] = self.mShortcut.GetDisplayImage()
        self.LastShortcutTexture = ReturnValue1_1
        if not self.mShowNotification:
           goto(ExecutionFlow.Pop())
        self.mHotbarContainer.ShowNotification(self.mShortcutIndex)
        goto(ExecutionFlow.Pop())
        # Label 1387
        self.LastShortcutTexture = 127_Grey
        goto(ExecutionFlow.Pop())
        self.mShowNotification = ShowNotification
        goto('L15')
    
