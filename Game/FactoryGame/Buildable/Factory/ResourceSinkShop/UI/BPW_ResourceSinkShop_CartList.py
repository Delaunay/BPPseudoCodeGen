
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartItem import BPW_ResourceSinkShop_CartItem
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartList import ExecuteUbergraph_BPW_ResourceSinkShop_CartList
from Script.UMG import SetVerticalAlignment
from Script.UMG import AddChildToVerticalBox
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_CartItem_Struct import ResourceSinkShop_CartItem_Struct
from Script.UMG import UserWidget

class BPW_ResourceSinkShop_CartList(UserWidget):
    mCartItemStruct: List[ResourceSinkShop_CartItem_Struct]
    OnItemRemovedFromCart: FMulticastScriptDelegate
    OnItemAmountChanged: FMulticastScriptDelegate
    
    def UpdateEmptyCartFeedback(self):
        
        ReturnValue: int32 = len(self.mCartItemStruct)
        ReturnValue_0: bool = ReturnValue <= 0
        if not ReturnValue_0:
            goto('L150')
        self.mEmptyCartFeedback.SetVisibility(0)
        # End
        # Label 150
        self.mEmptyCartFeedback.SetVisibility(1)
    

    def ChangeItemAmount(self, schematic: TSubclassOf[FGSchematic], NewAmount: int32):
        self.OnItemAmountChanged.ProcessMulticastDelegate(schematic, NewAmount)
    

    def RemoveItemFromCart(self, mSchematic: TSubclassOf[FGSchematic]):
        self.OnItemRemovedFromCart.ProcessMulticastDelegate(mSchematic)
    

    def GenerateCartList(self, mCartItemStruct: Ref[List[ResourceSinkShop_CartItem_Struct]]):
        ExecutionFlow.Push("L748")
        self.mCartItemStruct = mCartItemStruct
        self.mCartItemVerticalBox.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 114
        ReturnValue: int32 = len(self.mCartItemStruct)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L674")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[BPW_ResourceSinkShop_CartItem] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSinkShop_CartItem, ReturnValue_1)
        
        Item = None
        Item = self.mCartItemStruct[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mCartItem", Ref[Item])
        ReturnValue_3: Ptr[VerticalBoxSlot] = self.mCartItemVerticalBox.AddChildToVerticalBox(ReturnValue_2)
        ReturnValue_3.SetVerticalAlignment(1)
        OutputDelegate1.BindUFunction(self, RemoveItemFromCart)
        ReturnValue_2.OnRemoveButtonClicked.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, ChangeItemAmount)
        ReturnValue_2.OnItemAmountChanged.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 674
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L114')
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartList(29)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartList(57)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_CartList(self):
        # Label 10
        self.UpdateEmptyCartFeedback()
        # End
        
        self.GenerateCartList(Ref[self.mCartItemStruct])
        goto('L10')
        self.OnItemRemovedFromCart.Clear()
    

    def OnItemAmountChanged__DelegateSignature(self, schematic: TSubclassOf[FGSchematic], NewAmount: int32):
        pass
    

    def OnItemRemovedFromCart__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        pass
    
