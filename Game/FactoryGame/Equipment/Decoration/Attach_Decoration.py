
from codegen.ue4_stub import *

from Script.FactoryGame import GetStackFromIndex
from Game.FactoryGame.Equipment.Decoration.Attach_Decoration import ExecuteUbergraph_Attach_Decoration
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import GetActiveIndex
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import OnAttach
from Script.FactoryGame import Default__FGDecorationDescriptor
from Script.FactoryGame import FGDecorationDescriptor
from Script.FactoryGame import GetEquipmentSlot
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.FactoryGame import GetMesh1P
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.Engine import StaticMesh
from Script.FactoryGame import FGEquipmentAttachment

class Attach_Decoration(FGEquipmentAttachment):
    mCachedDescriptorClass: TSubclassOf[FGDecorationDescriptor]
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def CacheDescriptor(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[FGInventoryComponentEquipment] = ReturnValue.GetEquipmentSlot(1)
        ReturnValue_1: int32 = ReturnValue_0.GetActiveIndex()
        
        stack = None
        ReturnValue_2: bool = ReturnValue_0.GetStackFromIndex(ReturnValue_1, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        Descriptor: TSubclassOf[FGDecorationDescriptor] = ClassCast[FGDecorationDescriptor](itemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L390')
        self.mCachedDescriptorClass = Descriptor
    

    def OnAttach(self):
        self.ExecuteUbergraph_Attach_Decoration(145)
    

    def ExecuteUbergraph_Attach_Decoration(self):
        # Label 10
        self.OnAttach()
        self.CacheDescriptor()
        ReturnValue: Ptr[StaticMesh] = Default__FGDecorationDescriptor.GetMesh1P(self.mCachedDescriptorClass)
        ReturnValue_0: bool = self.StaticMesh.SetStaticMesh(ReturnValue)
        # End
        goto('L10')
    
