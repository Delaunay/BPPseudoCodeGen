
from codegen.ue4_stub import *

from Script.FactoryGame import ShowOutline
from Script.FactoryGame import CreateAndAddNewRepresentation
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter1
from Script.Engine import Controller
from Script.FactoryGame import FGPlayerController
from Game.FactoryGame.-Shared.Crate.Widget_Crate import Widget_Crate
from Script.Engine import HUD
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_itemClass
from Script.FactoryGame import Get
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_numRemoved
from Script.Engine import GetController
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_state2
from Script.FactoryGame import GetInventory
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import HideOutline
from Script.Engine import GetHUD
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_lootcrate import MapCompass_Icon_lootcrate
from Script.FactoryGame import OnUse
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_newColor
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_state1
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_EndPlayReason
from Script.CoreUObject import Vector
from Script.FactoryGame import FGActorRepresentationManager
from Script.FactoryGame import FGHUD
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter2
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_state
from Script.FactoryGame import IsEmpty
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_byCharacter
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate
from Game.FactoryGame.-Shared.Crate.BP_Crate import ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter
from Script.FactoryGame import FGCrate
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class BP_Crate(FGCrate):
    mIsShowingHud: bool
    mMapText: FText = NSLOCTEXT("", "6C35E75245AAC6E2EA4400B3345F2CB2", "Crate")
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        # Label 10
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_lootcrate
    

    def GetActorRepresentationType(self):
        ReturnValue = 2
    

    def GetActorShouldShowInCompass(self):
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
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def IsActorStatic(self):
        ReturnValue = True
    

    def RemoveAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L244')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L244')
        ReturnValue_0 = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_2: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_3: bool = False
        goto('L255')
        # Label 244
        ReturnValue_3 = False
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_Crate.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(133)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Crate.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(138)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Crate.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(186)
    

    def OnUse(self):
        ExecuteUbergraph_BP_Crate.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Crate.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(232)
    

    def SwitchHUD(self, byCharacter: Ptr[FGCharacterPlayer]):
        ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_byCharacter = byCharacter #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(481)
    

    def OnRequestReprecentMarker(self):
        self.ExecuteUbergraph_BP_Crate(774)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_Crate.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(803)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Crate(916)
    

    def checkForClearAndRemove(self, ItemClass: TSubclassOf[FGItemDescriptor], numRemoved: int32):
        ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_itemClass = ItemClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Crate.K2Node_CustomEvent_numRemoved = numRemoved #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Crate(921)
    

    def ExecuteUbergraph_BP_Crate(self):
        # Label 10
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L1035')
        OutputDelegate1.BindUFunction(self, checkForClearAndRemove)
        ReturnValue2: Ptr[FGInventoryComponent] = self.GetInventory()
        ReturnValue2.OnItemRemovedDelegate.AddUnique(OutputDelegate1)
        # End
        # End
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.StaticMesh_0, 252)
        # End
        Default__FGBlueprintFunctionLibrary.HideOutline(self.StaticMesh_0)
        # End
        
        state = None
        self.OnUse(byCharacter, Ref[state])
        ReturnValue_0: Ptr[FGInventoryComponent] = self.GetInventory()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L373')
        self.SwitchHUD(byCharacter)
        # End
        # Label 373
        Default__KismetSystemLibrary.PrintString(self, "No valid Inventory in Crate", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        ReturnValue_2: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1035')
        ReturnValue_3: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_3)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L1035')
        AsFGHUD.OpenInteractUI(Widget_Crate, self)
        # End
        ReturnValue_4: bool = self.AddAsRepresentation()
        # End
        ReturnValue_5: bool = self.RemoveAsRepresentation()
        OutputDelegate.BindUFunction(self, checkForClearAndRemove)
        ReturnValue3: Ptr[FGInventoryComponent] = self.GetInventory()
        ReturnValue3.OnItemRemovedDelegate.Remove(OutputDelegate)
        # End
        goto('L10')
        ReturnValue1: Ptr[FGInventoryComponent] = self.GetInventory()
        ReturnValue_6: bool = ReturnValue1.IsEmpty()
        if not ReturnValue_6:
            goto('L1035')
        ReturnValue1_0: bool = self.RemoveAsRepresentation()
        self.K2_DestroyActor()
    
