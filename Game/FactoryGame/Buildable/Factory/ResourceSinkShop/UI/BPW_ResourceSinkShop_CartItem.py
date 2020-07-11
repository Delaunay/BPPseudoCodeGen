
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.FactoryGame import GetCost
from Script.FactoryGame import GetItemIcon
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import SetText
from Script.FactoryGame import IsRepeatPurchasesAllowed
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_CartItem_Struct import ResourceSinkShop_CartItem_Struct
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartItem import ExecuteUbergraph_BPW_ResourceSinkShop_CartItem
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToInt
from Script.Engine import IsNumeric
from Script.Engine import Format
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import NotEqual_ByteByte
from Script.UMG import UserWidget
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartItem import ExecuteUbergraph_BPW_ResourceSinkShop_CartItem.K2Node_ComponentBoundEvent_CommitMethod
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CartItem import ExecuteUbergraph_BPW_ResourceSinkShop_CartItem.K2Node_ComponentBoundEvent_Text
from Script.SlateCore import SlateBrush
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetSchematicDisplayName

class BPW_ResourceSinkShop_CartItem(UserWidget):
    mCartItem: ResourceSinkShop_CartItem_Struct
    OnRemoveButtonClicked: FMulticastScriptDelegate
    OnItemAmountChanged: FMulticastScriptDelegate
    
    def ChangeItemAmount(self, mNewAmount: int32):
        ReturnValue: bool = mNewAmount <= 1
        if not ReturnValue:
            goto('L90')
        self.OnRemoveButtonClicked.ProcessMulticastDelegate(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        # End
        # Label 90
        self.OnItemAmountChanged.ProcessMulticastDelegate(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668, mNewAmount)
    

    def UpdateCartItem(self, mCartItem: ResourceSinkShop_CartItem_Struct):
        self.mCartItem = mCartItem
        ReturnValue: SlateBrush = Default__FGSchematic.GetItemIcon(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        
        self.mIcon.SetBrush(Ref[ReturnValue])
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(self.mCartItem.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798, False, True, 1, 324)
        self.mInputNumberToAdd.SetText(ReturnValue1)
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        self.mItemName.SetText(ReturnValue_0)
        ReturnValue_1: List[ItemAmount] = Default__FGSchematic.GetCost(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        
        Item = None
        Item = ReturnValue_1[0]
        ReturnValue_2: int32 = self.mCartItem.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 * Item.amount
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_2, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "amount"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 896, 'Value': 'x{amount}'}", Array)
        self.mItemCost.SetText(ReturnValue_4)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(10)
    

    def BndEvt__mTrashButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(193)
    

    def BndEvt__mRemoveFromCart_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(235)
    

    def BndEvt__mAddToCart_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(314)
    

    def BndEvt__mInputNumberToAdd_K2Node_ComponentBoundEvent_3_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_BPW_ResourceSinkShop_CartItem.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_ResourceSinkShop_CartItem.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(393)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_CartItem(self):
        self.UpdateCartItem(self.mCartItem)
        ReturnValue: bool = Default__FGSchematic.IsRepeatPurchasesAllowed(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        if not ReturnValue:
            goto('L150')
        self.mAddRemoveContainer.SetVisibility(0)
        # End
        # Label 150
        self.mAddRemoveContainer.SetVisibility(2)
        # End
        self.OnRemoveButtonClicked.ProcessMulticastDelegate(self.mCartItem.mSchematic_2_F254EA0E48CE5A1D4DAD3296BA94D668)
        # End
        ReturnValue_0: int32 = self.mCartItem.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 - 1
        self.ChangeItemAmount(ReturnValue_0)
        # End
        ReturnValue_1: int32 = self.mCartItem.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798 + 1
        self.ChangeItemAmount(ReturnValue_1)
        # End
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 0)
        if not CmpSuccess:
            goto('L578')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L704')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 2)
        if not CmpSuccess:
            goto('L578')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 3)
        if not CmpSuccess:
            goto('L578')
        # End
        # Label 578
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(self.mCartItem.mCartItemAmount_6_93629BD24F75478DFED5F086C5732798, False, True, 1, 324)
        self.mInputNumberToAdd.SetText(ReturnValue1)
        # End
        
        Text = None
        # Label 704
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_3: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_2)
        ReturnValue_4: bool = Default__KismetStringLibrary.IsNumeric(ReturnValue_2)
        ReturnValue_5: bool = ReturnValue_3 > 0
        ReturnValue_6: bool = ReturnValue_4 and ReturnValue_5
        if not ReturnValue_6:
            goto('L578')
        
        Text = None
        ReturnValue_2 = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_3 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_2)
        self.ChangeItemAmount(ReturnValue_3)
        
        Text = None
        ReturnValue_2 = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_3 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_2)
        ReturnValue_7: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_3, False, True, 1, 324)
        self.mInputNumberToAdd.SetText(ReturnValue_7)
    

    def OnItemAmountChanged__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic], mNewAmount: int32):
        pass
    

    def OnRemoveButtonClicked__DelegateSignature(self, mSchematic: TSubclassOf[FGSchematic]):
        pass
    
