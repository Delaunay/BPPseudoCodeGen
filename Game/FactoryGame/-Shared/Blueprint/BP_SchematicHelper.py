
from codegen.ue4_stub import *

from Script.FactoryGame import GetNumInventorySlotsToUnlock
from Script.FactoryGame import FGGamePhaseManager
from Script.FactoryGame import FGUnlockInventorySlot
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import EGamePhase
from Script.FactoryGame import GetRecipesToUnlock
from Script.Engine import Conv_ByteToInt
from Script.Engine import Not_PreBool
from Script.FactoryGame import Default__FGGamePhaseManager
from Game.FactoryGame.Unlocks.BPI_UnlockableInterface import BPI_UnlockableInterface
from Script.FactoryGame import Get
from Script.FactoryGame import GetType
from Script.FactoryGame import AreSchematicDependenciesMet
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGUnlockArmEquipmentSlot
from Script.FactoryGame import FGTutorialIntroManager
from Script.FactoryGame import FGUnlock
from Script.FactoryGame import FGUnlockRecipe
from Script.Engine import Array_Append
from Script.FactoryGame import GetUnlocks
from Script.FactoryGame import GetIsTutorialCompleted
from Script.Engine import BooleanOR
from Script.FactoryGame import GetGamePhaseForSchematic
from Script.FactoryGame import GetGamePhase
from Script.FactoryGame import ESchematicType
from Script.FactoryGame import Default__FGSchematic
from Script.FactoryGame import FGRecipe
from Script.Engine import BooleanNOR
from Script.FactoryGame import GetNumArmEquipmentSlotsToUnlock
from Script.Engine import Array_Clear
from Script.FactoryGame import Default__FGTutorialIntroManager
from Script.Engine import BlueprintFunctionLibrary

class BP_SchematicHelper(BlueprintFunctionLibrary):
    
    
    def DoSchematicHasUnlocks(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0 > 0
        if not ReturnValue_1:
            goto('L182')
        HasUnlocks = True
        # End
        # Label 182
        HasUnlocks = False
    

    def GetNumArmEquipmentSlotsUnlocked(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L676")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L570')
        Variable_0 = Variable
        ExecutionFlow.Push("L602")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Slot: Ptr[FGUnlockArmEquipmentSlot] = Cast[FGUnlockArmEquipmentSlot](Item)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: int32 = Slot.GetNumArmEquipmentSlotsToUnlock()
        # Label 496
        ReturnValue1: int32 = localNumSlots + ReturnValue_2
        localNumSlots = ReturnValue1
        goto(ExecutionFlow.Pop())
        # Label 570
        numSlots = localNumSlots
        # End
        # Label 602
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def GetNumInventorySlotsUnlocked(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L676")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L570')
        Variable_0 = Variable
        ExecutionFlow.Push("L602")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Slot: Ptr[FGUnlockInventorySlot] = Cast[FGUnlockInventorySlot](Item)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: int32 = Slot.GetNumInventorySlotsToUnlock()
        # Label 496
        ReturnValue1: int32 = localNumSlots + ReturnValue_2
        localNumSlots = ReturnValue1
        goto(ExecutionFlow.Pop())
        # Label 570
        numSlots = localNumSlots
        # End
        # Label 602
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def GetUnlocksHandSlots(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L552")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L462')
        Variable_0 = Variable
        ExecutionFlow.Push("L478")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Slot: Ptr[FGUnlockArmEquipmentSlot] = Cast[FGUnlockArmEquipmentSlot](Item)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Result = True
        # End
        # Label 462
        Result = False
        # End
        # Label 478
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        # Label 547
        goto('L51')
    

    def GetUnlocksInventorySlot(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L552")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L462')
        Variable_0 = Variable
        ExecutionFlow.Push("L478")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Slot: Ptr[FGUnlockInventorySlot] = Cast[FGUnlockInventorySlot](Item)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Result = True
        # End
        # Label 462
        Result = False
        # End
        # Label 478
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        # Label 547
        goto('L51')
    

    def GetRecipesFromSchematic(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L653")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L547')
        Variable_0 = Variable
        ExecutionFlow.Push("L579")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Recipe: Ptr[FGUnlockRecipe] = Cast[FGUnlockRecipe](Item)
        bSuccess: bool = Recipe
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: List[TSubclassOf[FGRecipe]] = Recipe.GetRecipesToUnlock()
        
        # Label 496
        Default__KismetArrayLibrary.Array_Append(Ref[localRecipes], Ref[ReturnValue_2])
        goto(ExecutionFlow.Pop())
        # Label 547
        recipes = localRecipes
        # End
        # Label 579
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def GetUnlockDataStructFromSchematic(self, schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L699")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(schematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L547')
        Variable_0 = Variable
        ExecutionFlow.Push("L579")
        ReturnValue = Default__FGSchematic.GetUnlocks(schematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Interface: TScriptInterface[BPI_UnlockableInterface] = QueryInterface[BPI_UnlockableInterface](Item)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L653')
        
        UnlockDataStruct = None
        GetInterfaceUObject(Interface).GetUnlockDataStruct(Ref[UnlockDataStruct])
        
        UnlockDataStruct = None
        # Label 496
        Default__KismetArrayLibrary.Array_Append(Ref[localUnlockDataStruct], Ref[UnlockDataStruct])
        goto(ExecutionFlow.Pop())
        # Label 547
        UnlockDataStruct = localUnlockDataStruct
        # End
        # Label 579
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
        
        # Label 653
        Default__KismetArrayLibrary.Array_Clear(Ref[UnlockDataStruct])
        goto('L496')
    

    def IsSchematicLockedInAnyWay(self, WolrdContext: Ptr[Object], schematic: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        
        IsSchematicPhaseLocked = None
        self.IsSchematicPhaseLocked(WolrdContext, schematic, WolrdContext, Ref[IsSchematicPhaseLocked])
        
        IsSchematicLockedByTutorial = None
        self.IsSchematicLockedByTutorial(WolrdContext, schematic, WolrdContext, Ref[IsSchematicLockedByTutorial])
        
        IsSchematicDependentLocked = None
        self.IsSchematicDependentLocked(WolrdContext, schematic, WolrdContext, Ref[IsSchematicDependentLocked])
        ReturnValue: bool = BooleanOR(IsSchematicPhaseLocked, IsSchematicDependentLocked)
        ReturnValue1: bool = BooleanOR(ReturnValue, IsSchematicLockedByTutorial)
        IsLocked = ReturnValue1
    

    def IsSchematicLockedByTutorial(self, WorldContext: Ptr[Object], SchematicClass: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ReturnValue: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(WorldContext)
        # Label 51
        ReturnValue_0: uint8 = Default__FGSchematic.GetType(SchematicClass)
        ReturnValue_1: bool = ReturnValue.GetIsTutorialCompleted()
        ReturnValue_2: bool = EqualEqual_ByteByte(ReturnValue_0, 2)
        ReturnValue_3: bool = BooleanNOR(ReturnValue_1, ReturnValue_2)
        IsSchematicLockedByTutorial = ReturnValue_3
    

    def IsSchematicDependentLocked(self, WorldContext: Ptr[Object], SchematicClass: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ReturnValue: bool = Default__FGSchematic.AreSchematicDependenciesMet(SchematicClass, WorldContext)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        IsSchematicDependentLocked = ReturnValue_0
    

    def IsSchematicPartOfTutorial(self, SchematicClass: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ReturnValue: uint8 = Default__FGSchematic.GetType(SchematicClass)
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 2)
        IsSchematicPartOfTutortial = ReturnValue_0
    

    def IsSchematicPhaseLocked(self, WorldContext: Ptr[Object], SchematicClass: TSubclassOf[FGSchematic], __WorldContext: Ptr[Object]):
        ReturnValue: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(WorldContext)
        # Label 51
        ReturnValue_0: uint8 = ReturnValue.GetGamePhase()
        ReturnValue_1: uint8 = ReturnValue.GetGamePhaseForSchematic(SchematicClass)
        ReturnValue_2: int32 = Conv_ByteToInt(ReturnValue_0)
        ReturnValue1: int32 = Conv_ByteToInt(ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2 <= ReturnValue1
        IsSchematicPhaseLocked = ReturnValue_3
    
