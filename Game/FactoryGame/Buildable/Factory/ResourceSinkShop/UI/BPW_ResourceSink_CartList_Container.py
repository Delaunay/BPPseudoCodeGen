
from codegen.ue4_stub import *

from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_CartList_Container import ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_NewAmount
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_CartList_Container import ExecuteUbergraph_BPW_ResourceSink_CartList_Container
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_CartItem_Struct import ResourceSinkShop_CartItem_Struct
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_CartList_Container import ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_mSchematic
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_CartList_Container import ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_Schematic
from Script.UMG import UserWidget

class BPW_ResourceSink_CartList_Container(UserWidget):
    AnimCantAfford: Ptr[WidgetAnimation]
    mCartItemStruct: List[ResourceSinkShop_CartItem_Struct]
    OnItemRemovedFromCart: FMulticastScriptDelegate
    OnBuyAllButtonClicked: FMulticastScriptDelegate
    mText: FText
    OnItemAmountChangedInCart: FMulticastScriptDelegate
    
    def PlayCantAffordAnim(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AnimCantAfford, 0, 1, 0, 1)
    

    def ChangeItemAmount(self, schematic: TSubclassOf[FGSchematic], NewAmount: int32):
        self.OnItemAmountChangedInCart.ProcessMulticastDelegate(schematic, NewAmount)
    

    def SetTotalCostText(self, mTotalCostText: FText):
        self.mText = mTotalCostText
        self.mTotalCostText.SetText(self.mText)
    

    def SetBuyButtonVisibility(self, mCartItemStruct: Ref[List[ResourceSinkShop_CartItem_Struct]]):
        
        ReturnValue: int32 = len(mCartItemStruct)
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L150')
        self.mShoppingCartButtonBox.SetVisibility(0)
        # End
        # Label 150
        self.mShoppingCartButtonBox.SetVisibility(1)
    

    def UpdateCartList(self, mCartItemStruct: Ref[List[ResourceSinkShop_CartItem_Struct]]):
        self.mCartItemStruct = mCartItemStruct
        
        self.mCartList.GenerateCartList(Ref[self.mCartItemStruct])
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSink_CartList_Container(47)
    

    def BndEvt__mCartList_K2Node_ComponentBoundEvent_0_OnItemRemovedFromCart__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_mSchematic = mSchematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_CartList_Container(75)
    

    def BndEvt__mBuyAllButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSink_CartList_Container(108)
    

    def BndEvt__mCartList_K2Node_ComponentBoundEvent_2_OnItemAmountChanged__DelegateSignature(self, schematic: TSubclassOf[FGSchematic], NewAmount: int32):
        ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_Schematic = schematic #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_ResourceSink_CartList_Container.K2Node_ComponentBoundEvent_NewAmount = NewAmount #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_CartList_Container(10)
    

    def ExecuteUbergraph_BPW_ResourceSink_CartList_Container(self):
        self.ChangeItemAmount(Schematic, NewAmount)
        # End
        
        self.UpdateCartList(Ref[self.mCartItemStruct])
        # End
        self.OnItemRemovedFromCart.ProcessMulticastDelegate(mSchematic)
        # End
        self.OnBuyAllButtonClicked.ProcessMulticastDelegate()
    

    def OnItemAmountChangedInCart__DelegateSignature(self, schematic: TSubclassOf[FGSchematic], amount: int32):
        pass
    

    def OnBuyAllButtonClicked__DelegateSignature(self):
        pass
    

    def OnItemRemovedFromCart__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        pass
    
