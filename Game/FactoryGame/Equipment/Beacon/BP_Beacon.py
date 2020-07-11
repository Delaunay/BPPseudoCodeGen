
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter
from Script.Engine import Texture2D
from Script.FactoryGame import ECompassViewDistance
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion2
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion1
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.Engine import Controller
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion2
from Script.FactoryGame import MakeInventoryStack
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_state
from Script.FactoryGame import HasEnoughSpaceForItem
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import GetController
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_player2
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Resource.Equipment.Beacon.BP_EquipmentDescriptorBeacon import BP_EquipmentDescriptorBeacon
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter2
from Script.FactoryGame import GetInventory
from Script.CoreUObject import Object
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_player1
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_state1
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion1
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import UpdateRepresentation
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion3
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion
from Script.Engine import GetPlayerController
from Script.FactoryGame import FGBeacon
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_state3
from Script.FactoryGame import MakeInventoryItem
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion3
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter1
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_newColor
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter3
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import Widget_Beacon
from Script.UMG import Create
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon
from Script.FactoryGame import FGUseState_Valid
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_state2
from Script.FactoryGame import UpdateUseState
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import ExecuteUbergraph_BP_Beacon.K2Node_Event_player
from Script.CoreUObject import LinearColor
from Script.FactoryGame import InventoryStack

class BP_Beacon(FGBeacon):
    mCompassTexture: Ptr[Texture2D] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Map/MapCompass_Icon_beacon.MapCompass_Icon_beacon')
    mCompassText: FText = NSLOCTEXT("", "75DA2B80464FD8F650B0AF9B4E3DAEA5", "Beacon")
    mWidget: Ptr[Widget_Beacon]
    mCompassColor: LinearColor = Namespace(A=1, B=0.09530699998140335, G=0.09530699998140335, R=0.09530699998140335)
    compassViewDistance: uint8 = ECompassViewDistance::CVD_Far
    bReplicates = True
    
    def ShouldSave(self):
        ReturnValue = True
    

    def GatherDependencies(self):
        Array: List[Ptr[Object]] = []
        dependentObjects: List[Ptr[Object]] = Array
    

    def NeedTransform(self):
        ReturnValue = False
    

    def GetLookAtDecription(self):
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        # Label 145
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 374, 'Value': 'Press [{BUTTON}] to configure Beacon'}", Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def IsUseable(self):
        ReturnValue = True
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(FGUseState_Valid, Ref[useState])
    

    def GetActorCompassViewDistance(self):
        ReturnValue = self.compassViewDistance
    

    def SetActorCompassViewDistance(self):
        self.FlushNetDormancy()
        # Label 10
        self.compassViewDistance = compassViewDistance
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L127')
        ReturnValue_0: bool = self.UpdateRepresentation()
        # Label 95
        ReturnValue_1: uint8 = self.compassViewDistance
        goto('L356')
        # Label 127
        ReturnValue_2: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L356')
        ReturnValue_3: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3.Server_SetActorCompassViewDistance(self, self.compassViewDistance)
        goto('L95')
    

    def SetActorRepresentationText(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L127')
        self.FlushNetDormancy()
        self.mCompassText = newText
        ReturnValue_0: bool = self.UpdateRepresentation()
        # Label 95
        ReturnValue_1: FText = self.mCompassText
        goto('L356')
        # Label 127
        ReturnValue_2: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L356')
        ReturnValue_3: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3.Server_SetActorRepresentationText(self, newText)
        goto('L95')
    

    def UpdateRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.UpdateRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        ReturnValue = self.mCompassColor
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mCompassText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = self.mCompassTexture
    

    def GetActorRepresentationType(self):
        ReturnValue = 1
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

    def RemoveAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_2: bool = ReturnValue_1
        goto('L155')
        # Label 144
        ReturnValue_2 = False
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def IsActorStatic(self):
        ReturnValue = True
    

    def AddAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.CreateAndAddNewRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def SetColor(self, NewColor: LinearColor):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L100')
        self.FlushNetDormancy()
        self.mCompassColor = NewColor
        ReturnValue_0: bool = self.UpdateRepresentation()
        # Label 95
        # End
        # Label 100
        ReturnValue_1: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L324')
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_SetActorRepresentationColor(self, NewColor)
    

    def CloseWidget(self, Controller: Ptr[Controller]):
        Default__BPHUDHelpers.PopStackWidget(Controller, self.mWidget, self)
        self.mWidget = None
    

    def PostLoadGame(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion3 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion3 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(559)
    

    def PostSaveGame(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion2 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion2 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(554)
    

    def PreLoadGame(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion1 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion1 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(549)
    

    def PreSaveGame(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_saveVersion = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_gameVersion = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(544)
    

    def OnUseStop(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter3 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_state3 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(29)
    

    def RegisterInteractingPlayer(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_player2 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(34)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(39)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(44)
    

    def UnregisterInteractingPlayer(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_player1 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(49)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Beacon(54)
    

    def OnUse(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Beacon.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(83)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(564)
    

    def PickUpBeacon(self):
        ExecuteUbergraph_BP_Beacon.K2Node_Event_player = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Beacon(592)
    

    def ExecuteUbergraph_BP_Beacon(self):
        # Label 10
        self.K2_DestroyActor()
        # End
        # End
        # End
        # End
        # End
        # End
        ReturnValue: bool = self.AddAsRepresentation()
        # End
        ReturnValue_0: bool = byCharacter.IsLocallyControlled()
        if not ReturnValue_0:
            goto('L1016')
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mWidget)
        if not ReturnValue_1:
            goto('L228')
        self.CloseWidget(None)
        # End
        # Label 228
        ReturnValue_2: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1016')
        ReturnValue_3: Ptr[Widget_Beacon] = Default__WidgetBlueprintLibrary.Create(self, Widget_Beacon, Controller)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mBeacon", self)
        Default__BPHUDHelpers.PushStackWidget(Controller, ReturnValue_3, self)
        self.mWidget = ReturnValue_3
        # End
        # End
        # End
        # End
        # End
        self.SetColor(newColor)
        # End
        ReturnValue_4: Ptr[FGInventoryComponent] = player.GetInventory()
        ReturnValue1: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_EquipmentDescriptorBeacon)
        
        ReturnValue_5: bool = ReturnValue_4.HasEnoughSpaceForItem(Ref[ReturnValue1])
        if not ReturnValue_5:
            goto('L1016')
        ReturnValue_6: bool = self.RemoveAsRepresentation()
        ReturnValue_4 = player.GetInventory()
        ReturnValue_7: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(BP_EquipmentDescriptorBeacon)
        ReturnValue_8: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue_7)
        
        ReturnValue_9: int32 = ReturnValue_4.AddStack(False, Ref[ReturnValue_8])
        goto('L10')
    
