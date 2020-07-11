
from codegen.ue4_stub import *

from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetEquipmentInSlot
from Script.FactoryGame import HasValidCurrentDetails
from Script.Engine import FFloor
from Script.FactoryGame import ScannableDetails
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.FactoryGame import GetInventory
from Script.FactoryGame import FGEquipment
from Script.Engine import IsValid
from Script.Engine import GetHUD
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import SetValue
from Script.FactoryGame import GetDriver
from Script.Engine import Divide_IntInt
from Script.FactoryGame import FGVehicle
from Script.FactoryGame import GetIsUsingGamepad
from Script.Engine import Default__GameplayStatics
from Script.Engine import GameModeBase
from Script.FactoryGame import GetNumItems
from Script.FactoryGame import GetNumItemsFromCentralStorage
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import FGPlayerControllerBase
from Script.CoreUObject import LinearColor
from Script.Engine import GetGameMode
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import FGObjectScanner
from Script.FactoryGame import SetHUDVisibility
from Script.FactoryGame import FGAdminInterface
from Script.FactoryGame import GetKeyNameForAction
from Script.FactoryGame import IsMainMenuGameMode
from Script.SlateCore import SlateColor
from Script.FactoryGame import GetCurrentDetails
from Script.FactoryGame import Default__FGCentralStorageSubsystem
from Script.FactoryGame import FGGameMode
from Script.Engine import BlueprintFunctionLibrary
from Script.UMG import GetValue
from Script.FactoryGame import FGCentralStorageSubsystem
from Script.FactoryGame import GetAdminInterface

class HUDHelpers(BlueprintFunctionLibrary):
    
    
    def GetKeyNameForActionSimple(self, Controller: Ptr[Controller], buttonName: FName, __WorldContext: Ptr[Object]):
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](Controller_0)
        bSuccess: bool = Controller
        ReturnValue: bool = Controller.GetIsUsingGamepad()
        ReturnValue_0: FText = Controller.GetKeyNameForAction(buttonName, ReturnValue)
        Button = ReturnValue_0
    

    def GetAdminInterface(self, PlayerController: Ptr[PlayerController], __WorldContext: Ptr[Object]):
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](PlayerController)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L145')
        ReturnValue: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        adminInterface = ReturnValue
        # End
        # Label 145
        adminInterface = None
    

    def HasValidAdminInterface(self, Controller: Ptr[PlayerController], __WorldContext: Ptr[Object]):
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](Controller)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L196')
        ReturnValue: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        Valid = ReturnValue_0
        # Label 191
        # End
        # Label 196
        Valid = False
    

    def IsInMainMenu(self, WorldContext: Ptr[Object], __WorldContext: Ptr[Object]):
        ReturnValue: Ptr[GameModeBase] = Default__GameplayStatics.GetGameMode(WorldContext)
        Mode: Ptr[FGGameMode] = Cast[FGGameMode](ReturnValue)
        bSuccess: bool = Mode
        if not bSuccess:
            goto('L191')
        ReturnValue_0: bool = Mode.IsMainMenuGameMode()
        IsInMainMenu = ReturnValue_0
    

    def GetFGGameUI(self, Controller: Ptr[Controller], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L261')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L261')
        ReturnValue_0: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        localGameUI = ReturnValue_0
        # Label 261
        gameUI = localGameUI
    

    def GetNumItemsFromCentralStorage(self, OwningPawn: Ptr[Pawn], mItemClass: TSubclassOf[FGItemDescriptor], __WorldContext: Ptr[Object]):
        ReturnValue: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(OwningPawn)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L258')
        ReturnValue = Default__FGCentralStorageSubsystem.Get(OwningPawn)
        ReturnValue_1: int32 = ReturnValue.GetNumItemsFromCentralStorage(mItemClass)
        NumItems = ReturnValue_1
        # End
        # Label 258
        NumItems = -1
    

    def GetNumItemsOwned(self, __WorldContext: Ptr[Object]):
        pass
    

    def GetFactoryGameLightBlue(self, __WorldContext: Ptr[Object]):
        GraphicsBlue = LinearColor(R = 0.10702300071716309, G = 0.4341540038585663, B = 0.5583410263061523, A = 1)
        TextBlue = SlateColor(SpecifiedColor = LinearColor(R = 0.10702300071716309, G = 0.4341540038585663, B = 0.5583410263061523, A = 1), ColorUseRule = 0)
        Graphics = GraphicsBlue
        text = TextBlue
    

    def GetFactoryGameLightGray(self, __WorldContext: Ptr[Object]):
        mText = SlateColor(SpecifiedColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1), ColorUseRule = 0)
        mGraphics = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1)
        text = mText
        Graphics = mGraphics
    

    def GetFactoryGameDarkGray(self, __WorldContext: Ptr[Object]):
        mGraphics = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        mText = SlateColor(SpecifiedColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1), ColorUseRule = 0)
        text = mText
        Graphics = mGraphics
    

    def SetSliderSteps(self, mSlider: Ptr[Slider], mSteps: int32, __WorldContext: Ptr[Object]):
        ReturnValue: float = mSlider.GetValue()
        ReturnValue_0: int32 = mSteps - 1
        ReturnValue_1: int32 = ReturnValue_0 * 100
        ReturnValue_2: float = Conv_IntToFloat(ReturnValue_0)
        ReturnValue_3: int32 = Divide_IntInt(ReturnValue_1, ReturnValue_0)
        ReturnValue_4: float = ReturnValue_1 * ReturnValue
        ReturnValue_5: int32 = FFloor(ReturnValue_4)
        ReturnValue1: int32 = Divide_IntInt(ReturnValue_5, ReturnValue_3)
        ReturnValue1_0: float = Conv_IntToFloat(ReturnValue1)
        ReturnValue_6: float = ReturnValue1_0 / ReturnValue_2
        mSlider.SetValue(ReturnValue_6)
    

    def GetScanningObjectName(self, OwningPawn: Ptr[Pawn], __WorldContext: Ptr[Object]):
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OwningPawn)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L349')
        ReturnValue: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        Scanner: Ptr[FGObjectScanner] = Cast[FGObjectScanner](ReturnValue)
        bSuccess1: bool = Scanner
        if not bSuccess1:
            goto('L369')
        ReturnValue_0: bool = Scanner.HasValidCurrentDetails()
        if not ReturnValue_0:
            goto('L349')
        # Label 258
        ReturnValue_1: ScannableDetails = Scanner.GetCurrentDetails()
        Object Name = ReturnValue_1.DisplayText
        # End
        # Label 349
        Object Name = 
    

    def ShowHideHUD(self, isMenuOpen: bool, OwningPawn: Ptr[Pawn], Controller: Ptr[Controller], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L270')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L270')
        ReturnValue_0: bool = Not_PreBool(isMenuOpen)
        AsFGHUD.SetHUDVisibility(ReturnValue_0)
    

    def GetNumItemsFromInventory(self, inventoryComponent: Ptr[FGInventoryComponent], mItemClass: TSubclassOf[FGItemDescriptor], __WorldContext: Ptr[Object]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(inventoryComponent)
        if not ReturnValue:
            goto('L156')
        ReturnValue_0: int32 = inventoryComponent.GetNumItems(mItemClass)
        NumItems = ReturnValue_0
        # End
        # Label 156
        NumItems = -1
    

    def GetFactoryGameOrange(self, __WorldContext: Ptr[Object]):
        SlateColor.SpecifiedColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        SlateColor.ColorUseRule = 0
        Orange = SlateColor.SpecifiedColor
        OrangeText = SlateColor
    

    def GetFactoryGameWhite(self, __WorldContext: Ptr[Object]):
        mTextWhite = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        mGraphicsWhite = LinearColor(R = 1, G = 1, B = 1, A = 1)
        TextWhite = mTextWhite
        GraphicsWhite = mGraphicsWhite
    

    def GetNumItemsFromPlayerInventory(self, OwningPawn: Ptr[Pawn], mItemClass: TSubclassOf[FGItemDescriptor], __WorldContext: Ptr[Object]):
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OwningPawn)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L212')
        ReturnValue: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_0: int32 = ReturnValue.GetNumItems(mItemClass)
        NumItems = ReturnValue_0
        # End
        # Label 212
        AsFGVehicle: Ptr[FGVehicle] = Cast[FGVehicle](OwningPawn)
        bSuccess: bool = AsFGVehicle
        if not bSuccess:
            goto('L466')
        ReturnValue_1: Ptr[FGCharacterPlayer] = AsFGVehicle.GetDriver()
        ReturnValue1: Ptr[FGInventoryComponent] = ReturnValue_1.GetInventory()
        ReturnValue1_0: int32 = ReturnValue1.GetNumItems(mItemClass)
        NumItems = ReturnValue1_0
        # End
        # Label 466
        NumItems = -1
    
