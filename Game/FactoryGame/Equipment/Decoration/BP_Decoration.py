
from codegen.ue4_stub import *

from Script.FactoryGame import MakeInventoryStack
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Controller
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import SetWorldScale3D
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import AddStacks
from Script.FactoryGame import Default__FGDecorationDescriptor
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetGroundMeshScale
from Script.Engine import GetController
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Equipment.Decoration.BP_Decoration import ExecuteUbergraph_BP_Decoration.K2Node_Event_byCharacter
from Script.FactoryGame import GetInventory
from Script.Engine import TimerHandle
from Script.CoreUObject import Object
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Equipment.Decoration.BP_Decoration import ExecuteUbergraph_BP_Decoration
from Script.FactoryGame import HasEnoughSpaceForStacks
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import MakeInventoryItem
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.FactoryGame import FGDecorationActor
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import FGUseState_Valid
from Script.Engine import IsValidClass
from Script.FactoryGame import UpdateUseState
from Script.FactoryGame import GetGroundMesh
from Game.FactoryGame.Equipment.Decoration.BP_Decoration import ExecuteUbergraph_BP_Decoration.K2Node_Event_state
from Script.Engine import StaticMesh
from Script.FactoryGame import InventoryStack

class BP_Decoration(FGDecorationActor):
    mSetupTimer: TimerHandle
    bReplicates = True
    
    def GatherDependencies(self):
        dependentObjects: List[Ptr[Object]] = List[ObjectProperty /Game/FactoryGame/Equipment/Decoration/BP_Decoration.BP_Decoration_C:GatherDependencies.out_dependentObjects.out_dependentObjects]([])
    

    def NeedTransform(self):
        ReturnValue = True
    

    def ShouldSave(self):
        ReturnValue = True
    

    def GetLookAtDecription(self):
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 374, 'Value': 'Press [{BUTTON}] to pick up'}", Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def IsUseable(self):
        ReturnValue = True
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(FGUseState_Valid, Ref[useState])
    

    def PickUp(self, inUser: Ptr[FGCharacterPlayer]):
        ReturnValue: Ptr[FGInventoryComponent] = inUser.GetInventory()
        localInventory = ReturnValue
        ReturnValue_0: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(self.mDecorationDescriptor)
        ReturnValue_1: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue_0)
        Array: List[InventoryStack] = [ReturnValue_1]
        returnStack = Array
        
        ReturnValue_2: bool = localInventory.HasEnoughSpaceForStacks(Ref[returnStack])
        if not ReturnValue_2:
            goto('L351')
        
        localInventory.AddStacks(Ref[returnStack])
        self.K2_DestroyActor()
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Decoration(119)
    

    def OnUse(self):
        ExecuteUbergraph_BP_Decoration.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Decoration.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Decoration(249)
    

    def SetupActor(self):
        self.ExecuteUbergraph_BP_Decoration(530)
    

    def ExecuteUbergraph_BP_Decoration(self):
        
        # Label 10
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mSetupTimer])
        # End
        # Label 57
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L535')
        self.PickUp(byCharacter)
        # End
        self.ReceiveBeginPlay()
        OutputDelegate.BindUFunction(self, SetupActor)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mSetupTimer = ReturnValue_0
        # End
        goto('L57')
        # Label 254
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(self.mDecorationDescriptor)
        if not ReturnValue_1:
            goto('L535')
        ReturnValue_2: Ptr[StaticMesh] = Default__FGDecorationDescriptor.GetGroundMesh(self.mDecorationDescriptor)
        ReturnValue_3: bool = self.StaticMesh.SetStaticMesh(ReturnValue_2)
        ReturnValue_4: Vector = Default__FGDecorationDescriptor.GetGroundMeshScale(self.mDecorationDescriptor)
        self.StaticMesh.SetWorldScale3D(ReturnValue_4)
        goto('L10')
        goto('L254')
    
