
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Weapon import ExecuteUbergraph_Widget_HUDBox_Weapon
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Weapon import ExecuteUbergraph_Widget_HUDBox_Weapon.K2Node_Event_InDeltaTime
from Script.FactoryGame import GetMagSize
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Pawn
from Script.Engine import IsValid
from Script.FactoryGame import FGWeapon
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Weapon import ExecuteUbergraph_Widget_HUDBox_Weapon.K2Node_Event_MyGeometry
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.Engine import Conv_IntToText
from Script.FactoryGame import GetCurrentAmmo
from Script.Engine import Default__KismetTextLibrary

class Widget_HUDBox_Weapon(Widget_HUDBox_Equipment_Parent):
    mAmmoCurrentValue: int32
    mAmmoMaxValue: int32
    mAmmoClass: TSubclassOf[FGItemDescriptor]
    mWeapon: Ptr[FGWeapon]
    bHasScriptImplementedTick = True
    
    def UpdateAmmoSlot(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue, self.mAmmoClass, self, Ref[numItems])
        ReturnValue_0: bool = numItems > 0
        ItemAmount.ItemClass = self.mAmmoClass
        ItemAmount.amount = numItems
        self.AmmoSlot.Setup CostIcon(None, ItemAmount, None, 0, 0, True, False, ReturnValue_0)
    

    def UpdateContent(self):
        self.ExecuteUbergraph_Widget_HUDBox_Weapon(521)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_Weapon.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_Weapon.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_Weapon(526)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Weapon(648)
    

    def ExecuteUbergraph_Widget_HUDBox_Weapon(self):
        # Label 10
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mWeapon)
        if not ReturnValue:
            goto('L653')
        self.mAmmoClass = self.mWeapon.mAmmunitionClass
        self.UpdateAmmoSlot()
        ReturnValue_0: int32 = self.mWeapon.GetCurrentAmmo()
        self.mAmmoCurrentValue = ReturnValue_0
        ReturnValue_1: int32 = self.mWeapon.GetMagSize()
        self.mAmmoMaxValue = ReturnValue_1
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(self.mAmmoCurrentValue, False, True, 1, 324)
        self.mAmmoCurrent.SetText(ReturnValue_2)
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(self.mAmmoMaxValue, False, True, 1, 324)
        self.mAmmoMax.SetText(ReturnValue1)
        # End
        goto('L10')
        self.UpdateContent()
        # End
        # Label 545
        AsFGWeapon: Ptr[FGWeapon] = Cast[FGWeapon](self.mEquipment)
        bSuccess: bool = AsFGWeapon
        if not bSuccess:
            goto('L653')
        self.mWeapon = AsFGWeapon
        # End
        goto('L545')
    
