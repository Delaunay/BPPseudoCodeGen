
from codegen.ue4_stub import *

from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetEquipmentInSlot
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import Pawn
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGNobeliskDetonator
from Script.Engine import PlayerController
from Script.FactoryGame import GetNormalizedCollectionProgress
from Game.FactoryGame.Character.Player.Widget_PlayerHUD import ExecuteUbergraph_Widget_PlayerHUD
from Script.Engine import K2_GetPawn
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetDisabledInputGate
from Script.FactoryGame import FGEquipment
from Script.FactoryGame import DisabledInputGate
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.UMG import StopAnimation
from Script.Engine import GetHUD
from Script.FactoryGame import GetReviveProgress
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGGameUserSettings
from Script.FactoryGame import GetChargePct
from Script.FactoryGame import SubscribeToDynamicOptionUpdate
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import SetMouseCursorWidget
from Script.Engine import CurveFloat
from Script.FactoryGame import Default__FGGameUserSettings
from Script.FactoryGame import GetIsUsingGamepad
from Script.Engine import BooleanOR
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.UMG import WidgetAnimation
from Script.Engine import MakeLiteralText
from Script.FactoryGame import FGHUD
from Script.FactoryGame import UnsubscribeToAllDynamicOptionUpdate
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import EqualEqual_TextText
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import SetShowCrossHair
from Script.UMG import Create
from Script.UMG import IsAnimationPlaying
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_DefaultCursor import Widget_DefaultCursor
from Script.FactoryGame import GetFloatOptionValue
from Script.UMG import SetRenderOpacity
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import Widget_BuildMenu
from Script.Engine import GetFloatValue

class Widget_PlayerHUD(UserWidget):
    ReveiveBeat: Ptr[WidgetAnimation]
    PulseText: Ptr[WidgetAnimation]
    mReviveCruve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/ReviveCurve.ReviveCurve')
    
    def GetNobeliskBarVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue: float = self.GetNobeliskBarPercent()
        ReturnValue_0: bool = ReturnValue > 0.10000000149011612
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
    

    def GetNobeliskBarPercent(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L417')
        ReturnValue_0: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        Detonator: Ptr[FGNobeliskDetonator] = Cast[FGNobeliskDetonator](ReturnValue_0)
        bSuccess1: bool = Detonator
        if not bSuccess1:
            goto('L499')
        ReturnValue_1: float = Detonator.GetChargePct()
        self.mNobeliskProgressbar.mProgressBar.SetPercent(ReturnValue_1)
        ReturnValue_1 = Detonator.GetChargePct()
        ReturnValue_2: float = ReturnValue_1
        # Label 412
        goto('L499')
        # Label 417
        self.mNobeliskProgressbar.mProgressBar.SetPercent(0)
        ReturnValue_2 = 0
    

    def Get_mCollectBar_Percent(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L570')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L570')
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(Player.mPickupToCollect)
        if not ReturnValue1:
            goto('L488')
        ReturnValue_2: float = Player.mPickupToCollect.GetNormalizedCollectionProgress()
        self.mPickupBar.mProgressBar.SetPercent(ReturnValue_2)
        ReturnValue_3: float = ReturnValue_2
        goto('L570')
        # Label 488
        self.mPickupBar.mProgressBar.SetPercent(0)
        ReturnValue_3 = 0
    

    def Get_CollectBarContainer_Visibility(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L346')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L346')
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(Player.mPickupToCollect)
        if not ReturnValue1:
            goto('L346')
        ReturnValue_2: uint8 = 3
        goto('L366')
        # Label 346
        ReturnValue_2 = 2
    

    def OnToggleInteractUI(self, IsOpen: bool, InteractWidgetClass: TSubclassOf[UserWidget]):
        Menu: TSubclassOf[Widget_BuildMenu] = ClassCast[Widget_BuildMenu](InteractWidgetClass)
        bSuccess: bool = Menu
        if not bSuccess:
            goto('L79')
        # Label 79
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess_0: bool = Controller
        if not bSuccess_0:
            goto('L530')
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(Menu)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = IsOpen and ReturnValue_1
        # Label 300
        ReturnValue_3: DisabledInputGate = Controller.GetDisabledInputGate()
        ReturnValue_4: bool = BooleanOR(IsOpen, ReturnValue_3.mHotbar)
        ReturnValue1: bool = BooleanOR(ReturnValue_4, ReturnValue_2)
        if not ReturnValue1:
            goto('L492')
        self.Widget_HotbarContainer.SetVisibility(2)
        # End
        # Label 492
        self.Widget_HotbarContainer.SetVisibility(0)
    

    def OnToggleInventory(self, IsOpen: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L295')
        ReturnValue_0: DisabledInputGate = Controller.GetDisabledInputGate()
        ReturnValue_1: bool = BooleanOR(IsOpen, ReturnValue_0.mHotbar)
        if not ReturnValue_1:
            goto('L257')
        self.Widget_HotbarContainer.SetVisibility(2)
        # End
        # Label 257
        self.Widget_HotbarContainer.SetVisibility(0)
    

    def SetImageVisibility(self, Value: bool, Image: Ptr[Image]):
        if not Value:
            goto('L57')
        Image.SetVisibility(0)
        # End
        # Label 57
        Image.SetVisibility(2)
    

    def OnDisabledInputGateChanged(self, NewValue: DisabledInputGate):
        ExecutionFlow.Push("L821")
        ExecutionFlow.Push("L691")
        ExecutionFlow.Push("L598")
        # Label 15
        ExecutionFlow.Push("L505")
        ExecutionFlow.Push("L412")
        ExecutionFlow.Push("L319")
        ExecutionFlow.Push("L226")
        ExecutionFlow.Push("L133")
        ReturnValue7: bool = Not_PreBool(NewValue.mBuildGun)
        self.SetImageVisibility(ReturnValue7, self.Widget_KeyShortcuts.mBuildGun)
        goto(ExecutionFlow.Pop())
        # Label 133
        ReturnValue6: bool = Not_PreBool(NewValue.mDismantle)
        self.SetImageVisibility(ReturnValue6, self.Widget_KeyShortcuts.mDismantle)
        goto(ExecutionFlow.Pop())
        # Label 226
        ReturnValue5: bool = Not_PreBool(NewValue.mFlashLight)
        self.SetImageVisibility(ReturnValue5, self.Widget_KeyShortcuts.mFlashLight)
        goto(ExecutionFlow.Pop())
        # Label 319
        ReturnValue4: bool = Not_PreBool(NewValue.mResourceScanner)
        self.SetImageVisibility(ReturnValue4, self.Widget_KeyShortcuts.mResourceScanner)
        goto(ExecutionFlow.Pop())
        # Label 412
        ReturnValue3: bool = Not_PreBool(NewValue.mOpenCodex)
        self.SetImageVisibility(ReturnValue3, self.Widget_KeyShortcuts.mCodex)
        goto(ExecutionFlow.Pop())
        # Label 505
        ReturnValue2: bool = Not_PreBool(NewValue.mInventory)
        self.SetImageVisibility(ReturnValue2, self.Widget_KeyShortcuts.mInventory)
        goto(ExecutionFlow.Pop())
        # Label 598
        ReturnValue1: bool = Not_PreBool(NewValue.mToggleMap)
        self.SetImageVisibility(ReturnValue1, self.Widget_KeyShortcuts.mMinimap)
        goto(ExecutionFlow.Pop())
        # Label 691
        ReturnValue: bool = Not_PreBool(NewValue.mHotbar)
        if not ReturnValue:
            goto('L782')
        self.Widget_HotbarContainer.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        # Label 782
        self.Widget_HotbarContainer.SetVisibility(2)
        goto(ExecutionFlow.Pop())
    

    def GetVisibility_0(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L280')
        Variable: uint8 = 2
        Variable1: uint8 = 4
        ReturnValue_0: bool = Controller.GetIsUsingGamepad()
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
        goto('L300')
        # Label 280
        ReturnValue_1 = 4
    

    def Get_mInputLockedTExt_Visibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L256')
        Variable: uint8 = 0
        Variable1: uint8 = 2
        Variable_0: bool = Player.mWaitingForPlayerState
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
        goto('L276')
        # Label 256
        ReturnValue_0 = 2
    

    def GetScannerDetailsVisibility(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        Name = None
        Default__HUDHelpers.GetScanningObjectName(ReturnValue, self, Ref[Name])
        Variable: uint8 = 1
        Variable1: uint8 = 4
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText()
        
        Name = None
        ReturnValue_1: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[Name], Ref[ReturnValue_0])
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_2: uint8 = switch.get(Variable_0, None)
    

    def Get_mReviveProgressBar_Visibility(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L389')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L389')
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(Player.mPlayerToRevive)
        if not ReturnValue1:
            goto('L389')
        ReturnValue_2: bool = self.IsAnimationPlaying(self.ReveiveBeat)
        if not ReturnValue_2:
            goto('L433')
        # Label 364
        ReturnValue_3: uint8 = 3
        goto('L484')
        # Label 389
        self.StopAnimation(self.ReveiveBeat)
        ReturnValue_3 = 2
        goto('L484')
        # Label 433
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ReveiveBeat, 0, 1, 0, 1)
        goto('L364')
    

    def Get_mReviveProgressBar_Percent(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L701')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L701')
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(Player.mPlayerToRevive)
        if not ReturnValue1:
            goto('L619')
        ReturnValue_2: float = Player.mPlayerToRevive.GetReviveProgress()
        ReturnValue_3: float = self.mReviveCruve.GetFloatValue(ReturnValue_2)
        self.mReviveBar.mProgressBar.SetPercent(ReturnValue_3)
        ReturnValue_2 = Player.mPlayerToRevive.GetReviveProgress()
        ReturnValue_4: float = ReturnValue_2
        goto('L701')
        # Label 619
        self.mReviveBar.mProgressBar.SetPercent(0)
        ReturnValue_4 = 0
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayerHUD(957)
    

    def PlayRadiationAnimation(self):
        self.ExecuteUbergraph_Widget_PlayerHUD(30)
    

    def StopRadiationAnimation(self):
        self.ExecuteUbergraph_Widget_PlayerHUD(91)
    

    def EventUpdateQuickslotBackgroundOpacity(self):
        self.ExecuteUbergraph_Widget_PlayerHUD(1099)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PlayerHUD(1254)
    

    def ExecuteUbergraph_Widget_PlayerHUD(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.EventUpdateQuickslotBackgroundOpacity()
        goto(ExecutionFlow.Pop())
        self.Widget_PlayerHealthBar.mRadiationDamageBox.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        self.Widget_PlayerHealthBar.mRadiationDamageBox.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 152
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PulseText, 0, 0, 0, 1)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnDisabledInputGateChanged)
        Controller.mDisabledInputGateChanged.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 362
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_DefaultCursor] = Default__WidgetBlueprintLibrary.Create(self, Widget_DefaultCursor, ReturnValue1)
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1.SetMouseCursorWidget(1, ReturnValue_1)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, OnToggleInventory)
        Controller1.OnToggleInventory.AddUnique(OutputDelegate1)
        OutputDelegate3.BindUFunction(self, OnToggleInteractUI)
        Controller1.OnToggleInteractionUI.AddUnique(OutputDelegate3)
        ReturnValue_2: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_2)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(AsFGHUD)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        AsFGHUD.SetShowCrossHair(True)
        goto('L152')
        ExecutionFlow.Push("L967")
        goto('L362')
        # Label 967
        ReturnValue_4: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        OutputDelegate2.BindUFunction(self, EventUpdateQuickslotBackgroundOpacity)
        
        OutputDelegate2 = None
        ReturnValue_4.SubscribeToDynamicOptionUpdate("FG.CompassBGOpacity", Ref[OutputDelegate2])
        goto('L15')
        ReturnValue1_0: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_5: float = ReturnValue1_0.GetFloatOptionValue("FG.CompassBGOpacity")
        self.mVisorBackground.SetRenderOpacity(ReturnValue_5)
        goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue2_0.UnsubscribeToAllDynamicOptionUpdate(self)
        goto(ExecutionFlow.Pop())
    
