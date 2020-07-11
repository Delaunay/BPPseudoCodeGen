
from codegen.ue4_stub import *

from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetItemName
from Script.Engine import TimerHandle
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetNumItems
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.InventoryAddNotification.Widget_ItemNotification import ExecuteUbergraph_Widget_ItemNotification

class Widget_ItemNotification(UserWidget):
    bleep: Ptr[WidgetAnimation]
    ConstructAnim: Ptr[WidgetAnimation]
    mItemClass: TSubclassOf[FGItemDescriptor]
    mNumItems: int32
    mInventory: Ptr[FGInventoryComponent]
    mPickupTimer: TimerHandle
    padding = Namespace(Bottom=4, Left=4, Right=4, Top=4)
    
    def GetTotalNumItemsInPlayerInventory(self):
        ReturnValue: int32 = self.mInventory.GetNumItems(self.mItemClass)
        FormatArgumentData.ArgumentName = "X"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 315, 'Value': '({X})'}", Array)
        self.mNumItemsInInventoryText.SetText(ReturnValue_0)
    

    def GetNumItemsPickedUp(self):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(self.mNumItems, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 330, 'Value': '+{A}'}", Array)
        self.mNumItemsPickedUpText.SetText(ReturnValue_0)
    

    def AddToNumItems(self, NumItems: int32):
        ReturnValue: int32 = NumItems + self.mNumItems
        self.mNumItems = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ItemNotification(350)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ItemNotification(355)
    

    def UpdatePickUpAmount(self):
        self.ExecuteUbergraph_Widget_ItemNotification(402)
    

    def ExecuteUbergraph_Widget_ItemNotification(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ConstructAnim, 0, 1, 0, 1)
        OutputDelegate.BindUFunction(self, UpdatePickUpAmount)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mPickupTimer = ReturnValue_0
        # End
        # Label 176
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemClass)
        if not ReturnValue_1:
            goto('L430')
        ReturnValue_2: FText = Default__FGItemDescriptor.GetItemName(self.mItemClass)
        self.mItemNameText.SetText(ReturnValue_2)
        goto('L10')
        goto('L176')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mPickupTimer])
        # End
        self.GetNumItemsPickedUp()
        self.GetTotalNumItemsInPlayerInventory()
    
