
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_GasMask import ExecuteUbergraph_Widget_HUDBox_GasMask
from Game.FactoryGame.Resource.Parts.IodineInfusedFilter.Desc_HazmatFilter import Desc_HazmatFilter
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Resource.Parts.Filter.Desc_Filter import Desc_Filter
from Game.FactoryGame.Equipment.GasMask.Equip_GasMask import Equip_GasMask
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Equipment.HazmatSuit.Equip_HazmatSuit import Equip_HazmatSuit
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_GasMask import ExecuteUbergraph_Widget_HUDBox_GasMask.K2Node_Event_InDeltaTime
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_GasMask import ExecuteUbergraph_Widget_HUDBox_GasMask.K2Node_Event_MyGeometry
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent

class Widget_HUDBox_GasMask(Widget_HUDBox_Equipment_Parent):
    mFuelClass: TSubclassOf[FGItemDescriptor] = NewObject[Desc_Biofuel]()
    mGasMask: Ptr[Equip_GasMask]
    mHazmatSuit: Ptr[Equip_HazmatSuit]
    bHasScriptImplementedTick = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_GasMask(203)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_GasMask.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_GasMask.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_GasMask(428)
    

    def ExecuteUbergraph_Widget_HUDBox_GasMask(self):
        # Label 10
        self.mFuelClass = Desc_HazmatFilter
        # End
        # Label 34
        Variable: bool = False
        if not Variable1:
            goto('L64')
        # End
        # Label 64
        Variable1: bool = True
        self.mHudBoxParent.StartWarningSign()
        # End
        # Label 116
        Variable1 = False
        self.mHudBoxParent.StopWarningSign()
        # End
        # Label 168
        if not Variable:
            goto('L187')
        # End
        # Label 187
        Variable = True
        goto('L116')
        Mask: Ptr[Equip_GasMask] = Cast[Equip_GasMask](self.mEquipment)
        bSuccess: bool = Mask
        if not bSuccess:
            goto('L325')
        self.mGasMask = Mask
        self.mFuelClass = Desc_Filter
        # End
        # Label 325
        Suit: Ptr[Equip_HazmatSuit] = Cast[Equip_HazmatSuit](self.mEquipment)
        bSuccess1: bool = Suit
        if not bSuccess1:
            goto('L1191')
        self.mHazmatSuit = Suit
        goto('L10')
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mGasMask)
        if not ReturnValue:
            goto('L1033')
        ReturnValue_0: float = self.mGasMask.mCountdown / self.mGasMask.mFilterDuration
        self.Widget_ProgressBar.mProgressBar.SetPercent(ReturnValue_0)
        # Label 646
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_1, self.mFuelClass, self, Ref[numItems])
        ItemAmount.ItemClass = self.mFuelClass
        ItemAmount.amount = numItems
        ReturnValue1: bool = numItems > 0
        self.FuelSlot.Setup CostIcon(None, ItemAmount, None, 0, 0, False, False, ReturnValue1)
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_1, self.mFuelClass, self, Ref[numItems])
        ReturnValue_2: bool = numItems > 0
        if not ReturnValue_2:
            goto('L34')
        goto('L168')
        # Label 1033
        ReturnValue1_0: float = self.mHazmatSuit.mCountdown / self.mHazmatSuit.mFilterDuration
        self.Widget_ProgressBar.mProgressBar.SetPercent(ReturnValue1_0)
        goto('L646')
    
