
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.UMG import ESlateVisibility
from Script.UMG import SetWidthOverride
from Script.UMG import SetHeightOverride
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HobarPreset_Editor_SmallIcon import ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HobarPreset_Editor_SmallIcon import ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon.K2Node_Event_IsDesignTime

class BPW_HobarPreset_Editor_SmallIcon(UserWidget):
    mIcon: Ptr[Texture]
    mIndex: int32
    mIsSelected: bool
    OnSmallIconClicked: FMulticastScriptDelegate
    mSmallIcon: bool
    mBigSize: float = 128
    mSmallSize: float = 70
    
    def mSetIsSelected(self, mIsSelected: bool):
        self.mIsSelected = mIsSelected
        Variable: uint8 = 3
        Variable1: uint8 = 2
        Variable_0: bool = self.mIsSelected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mSelected.SetVisibility(switch.get(Variable_0, None))
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon(10)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon(698)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon(731)
    

    def ExecuteUbergraph_BPW_HobarPreset_Editor_SmallIcon(self):
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
        Variable: bool = self.mSmallIcon
        
        switch = {
            False: self.mBigSize,
            True: self.mSmallSize
        }
        self.mSizeBox.SetWidthOverride(switch.get(Variable, None))
        Variable = self.mSmallIcon
        
        switch_0 = {
            False: self.mBigSize,
            True: self.mSmallSize
        }
        self.mSizeBox.SetHeightOverride(switch_0.get(Variable, None))
        # End
        self.OnSmallIconClicked.ProcessMulticastDelegate(self.mIndex)
        # End
        self.OnSmallIconClicked.Clear()
    

    def OnSmallIconClicked__DelegateSignature(self, index: int32):
        pass
    
