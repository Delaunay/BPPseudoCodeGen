
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Consumable import Widget_HUDBox_Consumable
from Script.Engine import Texture2D
from Script.FactoryGame import FGSuitBase
from Script.Engine import Delay
from Script.FactoryGame import FGColorGun
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetEquipmentInSlot
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetVisibility
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.FactoryGame import FGChainsaw
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment import ExecuteUbergraph_Widget_HUDBox_Equipment
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment import ExecuteUbergraph_Widget_HUDBox_Equipment.K2Node_Event_InDeltaTime
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.FactoryGame import FGConsumableEquipment
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment import ExecuteUbergraph_Widget_HUDBox_Equipment.K2Node_Event_MyGeometry
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Fuel import Widget_HUDBox_Fuel
from Script.FactoryGame import FGGasMask
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBOX_Jetpack import Widget_HUDBox_Jetpack
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGEquipment
from Script.Engine import TimerHandle
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_GasMask import Widget_HUDBox_GasMask
from Script.FactoryGame import GetActiveIndex
from Script.FactoryGame import FGJetPack
from Script.Engine import Format
from Script.FactoryGame import FGWeapon
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ObjectScanner import Widget_HUDBox_ObjectScanner
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import FGObjectScanner
from Script.UMG import UserWidget
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import FGResourceMiner
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Weapon import Widget_HUDBox_Weapon
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGBuildGun
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import GetSizeLinear
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_ColorGun import Widget_HUDBox_ColorGun
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.FactoryGame import GetEquipmentSlot
from Script.FactoryGame import GetActiveEquipmentItem
from Script.Engine import IsValidClass
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import EEquipmentSlot

class Widget_HUDBox_Equipment(UserWidget):
    mCachedInventoryComponent: Ptr[FGInventoryComponent]
    mEquipmentSlot: uint8
    mAmmoClass: TSubclassOf[FGItemDescriptor]
    mAmmoCurrentValue: int32
    mAmmoMaxValue: int32
    mEquipment: Ptr[FGEquipment]
    mCharPlayer: Ptr[FGCharacterPlayer]
    mContentWidgetClass: TSubclassOf[Widget_HUDBox_Equipment_Parent]
    UpdateSlotTimerHandle: TimerHandle
    mActiveIndex: int32
    mToolbeltSize: int32
    
    def SetEquipmentSlotText(self):
        ReturnValue: Ptr[FGInventoryComponentEquipment] = self.mCharPlayer.GetEquipmentSlot(1)
        ReturnValue_0: int32 = ReturnValue.GetActiveIndex()
        ReturnValue1: Ptr[FGInventoryComponentEquipment] = self.mCharPlayer.GetEquipmentSlot(1)
        ReturnValue_1: int32 = ReturnValue_0 + 1
        ReturnValue_2: int32 = ReturnValue1.GetSizeLinear()
        FormatArgumentData.ArgumentName = "Active"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_1
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Total"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue_2
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 689, 'Value': '{Active}/{Total}'}", Array)
        self.Widget_EquipmentSlotDot.mEquipmentSlotText.SetText(ReturnValue_3)
    

    def GetEquipmentSlotVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue: bool = EqualEqual_ByteByte(self.mEquipmentSlot, 1)
        ReturnValue_0: Ptr[FGInventoryComponentEquipment] = self.mCharPlayer.GetEquipmentSlot(1)
        ReturnValue_1: int32 = ReturnValue_0.GetSizeLinear()
        ReturnValue_2: bool = ReturnValue_1 > 1
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue
        # Label 237
        Variable_0: bool = ReturnValue_3
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Widget_EquipmentSlotDot.SetVisibility(switch.get(Variable_0, None))
    

    def SetContentWidgetClass(self):
        AsFGWeapon: Ptr[FGWeapon] = Cast[FGWeapon](self.mEquipment)
        bSuccess7: bool = AsFGWeapon
        if not bSuccess7:
            goto('L269')
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(AsFGWeapon.mAmmunitionClass)
        if not ReturnValue:
            goto('L922')
        Gun: Ptr[FGColorGun] = Cast[FGColorGun](self.mEquipment)
        bSuccess4: bool = Gun
        if not bSuccess4:
            goto('L903')
        self.mContentWidgetClass = Widget_HUDBox_ColorGun
        # End
        # Label 269
        Equipment: Ptr[FGConsumableEquipment] = Cast[FGConsumableEquipment](self.mEquipment)
        bSuccess5: bool = Equipment
        if not bSuccess5:
            goto('L372')
        self.mContentWidgetClass = Widget_HUDBox_Consumable
        # End
        # Label 372
        Pack: Ptr[FGJetPack] = Cast[FGJetPack](self.mEquipment)
        bSuccess6: bool = Pack
        if not bSuccess6:
            goto('L475')
        self.mContentWidgetClass = Widget_HUDBox_Jetpack
        # End
        # Label 475
        AsFGChainsaw: Ptr[FGChainsaw] = Cast[FGChainsaw](self.mEquipment)
        bSuccess3: bool = AsFGChainsaw
        if not bSuccess3:
            goto('L578')
        self.mContentWidgetClass = Widget_HUDBox_Fuel
        # End
        # Label 578
        Mask: Ptr[FGGasMask] = Cast[FGGasMask](self.mEquipment)
        bSuccess1: bool = Mask
        if not bSuccess1:
            goto('L681')
        self.mContentWidgetClass = Widget_HUDBox_GasMask
        # End
        # Label 681
        Base: Ptr[FGSuitBase] = Cast[FGSuitBase](self.mEquipment)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L784')
        self.mContentWidgetClass = Widget_HUDBox_GasMask
        # End
        # Label 784
        Scanner: Ptr[FGObjectScanner] = Cast[FGObjectScanner](self.mEquipment)
        bSuccess2: bool = Scanner
        if not bSuccess2:
            goto('L887')
        self.mContentWidgetClass = Widget_HUDBox_ObjectScanner
        # End
        # Label 887
        self.mContentWidgetClass = None
        # End
        # Label 903
        self.mContentWidgetClass = Widget_HUDBox_Weapon
    

    def GetEquipmentInSlot(self):
        ReturnValue: Ptr[FGEquipment] = self.mCharPlayer.GetEquipmentInSlot(self.mEquipmentSlot)
        equipment = ReturnValue
    

    def UpdateTitle(self):
        
        Class1 = None
        self.GetEquipmentItemClass(Ref[Class1])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(Class1)
        if not ReturnValue:
            goto('L237')
        
        Class = None
        self.GetEquipmentItemClass(Ref[Class])
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(Class)
        self.Widget_HUDBox.mTitleObject.SetText(ReturnValue_0)
    

    def UpdateIcon(self):
        
        Class = None
        self.GetEquipmentItemClass(Ref[Class])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(Class)
        if not ReturnValue:
            goto('L791')
        
        Class1 = None
        self.GetEquipmentItemClass(Ref[Class1])
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Class1)
        SlateBrush.ImageSize = self.Widget_HUDBox.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.Widget_HUDBox.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.Widget_HUDBox.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = self.Widget_HUDBox.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_HUDBox.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_HUDBox.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_HUDBox.mIconObject.SetBrush(Ref[SlateBrush])
    

    def GetEquipmentItemClass(self):
        ReturnValue: InventoryItem = self.mCharPlayer.GetActiveEquipmentItem(self.mEquipmentSlot)
        
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[ReturnValue], Ref[itemClass], Ref[itemState])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(itemClass)
        if not ReturnValue_0:
            goto('L325')
        ReturnValue = self.mCharPlayer.GetActiveEquipmentItem(self.mEquipmentSlot)
        
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[ReturnValue], Ref[itemClass], Ref[itemState])
        Class = itemClass
        # End
        # Label 325
        Class = None
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Equipment(1862)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_Equipment.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_Equipment.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_Equipment(1867)
    

    def HideWidget(self):
        self.ExecuteUbergraph_Widget_HUDBox_Equipment(1886)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Equipment(1961)
    

    def ExecuteUbergraph_Widget_HUDBox_Equipment(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.SetEquipmentSlotText()
        
        Equipment = None
        self.GetEquipmentInSlot(Ref[Equipment])
        ReturnValue: bool = NotEqual_ObjectObject(Equipment, self.mEquipment)
        if not ReturnValue:
            goto('L207')
        
        Equipment2 = None
        self.GetEquipmentInSlot(Ref[Equipment2])
        Gun: Ptr[FGBuildGun] = Cast[FGBuildGun](Equipment2)
        bSuccess2: bool = Gun
        if not bSuccess2:
            goto('L626')
        goto(ExecutionFlow.Pop())
        # Label 207
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mEquipment)
        if not ReturnValue_0:
            goto('L351')
        Gun1: Ptr[FGBuildGun] = Cast[FGBuildGun](self.mEquipment)
        bSuccess4: bool = Gun1
        if not bSuccess4:
            goto('L1337')
        # Label 351
        ReturnValue_1: bool = self.Widget_HUDBox.IsAnimationPlaying(self.Widget_HUDBox.RemoveAnim)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        ReturnValue_3: uint8 = self.mHUDBoxOverlay.GetVisibility()
        ReturnValue_4: bool = EqualEqual_ByteByte(ReturnValue_3, 1)
        ReturnValue1: bool = Not_PreBool(ReturnValue_4)
        ReturnValue_5: bool = ReturnValue1 and ReturnValue_2
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        self.HideWidget()
        goto(ExecutionFlow.Pop())
        
        Equipment2 = None
        # Label 626
        self.GetEquipmentInSlot(Ref[Equipment2])
        Miner: Ptr[FGResourceMiner] = Cast[FGResourceMiner](Equipment2)
        bSuccess1: bool = Miner
        if not bSuccess1:
            goto('L729')
        goto(ExecutionFlow.Pop())
        # Label 729
        self.Widget_HUDBox.StopWarningSign()
        
        Equipment1 = None
        self.GetEquipmentInSlot(Ref[Equipment1])
        self.mEquipment = Equipment1
        self.mHUDBoxOverlay.SetVisibility(0)
        ReturnValue_6: Ptr[UMGSequencePlayer] = self.Widget_HUDBox.PlayAnimation(self.Widget_HUDBox.SpawnAnim, 0, 1, 0, 1)
        self.mWContent.ClearChildren()
        self.UpdateIcon()
        self.UpdateTitle()
        self.SetContentWidgetClass()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValidClass(self.mContentWidgetClass)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[Widget_HUDBox_Equipment_Parent] = Default__WidgetBlueprintLibrary.Create(self, self.mContentWidgetClass, ReturnValue_8)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_9, "mEquipment", self.mEquipment)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_9, "mHudBoxParent", self.Widget_HUDBox)
        ReturnValue_10: Ptr[PanelSlot] = self.mWContent.AddChild(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 1337
        Miner1: Ptr[FGResourceMiner] = Cast[FGResourceMiner](self.mEquipment)
        bSuccess3: bool = Miner1
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        goto('L351')
        # Label 1417
        ReturnValue_11: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_11)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1785')
        self.mCharPlayer = Player
        ReturnValue_12: Ptr[FGInventoryComponentEquipment] = self.mCharPlayer.GetEquipmentSlot(self.mEquipmentSlot)
        self.mCachedInventoryComponent = ReturnValue_12
        Variable: uint8 = 1
        Variable1: uint8 = 3
        ReturnValue1_0: bool = EqualEqual_ByteByte(self.mEquipmentSlot, 1)
        Variable_0: bool = ReturnValue1_0
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.Widget_EquipmentSlotDot.SetVisibility(switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        # Label 1785
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1417, UUID = 2041022721, ExecutionFunction = "ExecuteUbergraph_Widget_HUDBox_Equipment", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L1417')
        self.GetEquipmentSlotVisibility()
        goto('L15')
        self.mHUDBoxOverlay.SetVisibility(1)
        self.mWContent.ClearChildren()
        goto(ExecutionFlow.Pop())
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateSlotTimerHandle])
        goto(ExecutionFlow.Pop())
    
