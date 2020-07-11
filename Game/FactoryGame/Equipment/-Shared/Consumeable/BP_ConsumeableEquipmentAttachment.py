
from codegen.ue4_stub import *

from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetTPOverrideMesh
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ConsumablesEquip_01_Montage import ConsumablesEquip_01_Montage
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipmentAttachment import ExecuteUbergraph_BP_ConsumeableEquipmentAttachment.K2Node_Event_useLocation
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.Eat_01_Montage import Eat_01_Montage
from Script.FactoryGame import OnAttach
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponentEquipment
from Script.FactoryGame import IsFirstPerson
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipmentAttachment import ExecuteUbergraph_BP_ConsumeableEquipmentAttachment.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGEquipmentAttachment
from Script.FactoryGame import GetActiveIndex
from Script.CoreUObject import Vector
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.-Shared.Consumeable.BP_ConsumeableEquipmentAttachment import ExecuteUbergraph_BP_ConsumeableEquipmentAttachment
from Script.FactoryGame import Default__FGConsumableDescriptor
from Script.FactoryGame import GetStackFromIndex
from Script.FactoryGame import GetAttachedTo
from Script.Engine import Montage_IsPlaying
from Script.FactoryGame import GetEquipmentSlot
from Script.FactoryGame import BreakInventoryItem
from Script.FactoryGame import FGConsumableDescriptor
from Script.Engine import IsValidClass
from Script.Engine import AnimInstance
from Script.Engine import SkeletalMeshComponent
from Script.Engine import StaticMesh
from Script.FactoryGame import PlayUseEffect

class BP_ConsumeableEquipmentAttachment(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def GetHandsItem(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L480')
        ReturnValue = self.GetAttachedTo()
        ReturnValue_1: Ptr[FGInventoryComponentEquipment] = ReturnValue.GetEquipmentSlot(1)
        ReturnValue_2: int32 = ReturnValue_1.GetActiveIndex()
        
        stack = None
        ReturnValue_3: bool = ReturnValue_1.GetStackFromIndex(ReturnValue_2, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        Descriptor: TSubclassOf[FGConsumableDescriptor] = ClassCast[FGConsumableDescriptor](itemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L480')
        Item = Descriptor
        # End
        # Label 480
        Item = None
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_ConsumeableEquipmentAttachment.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ConsumeableEquipmentAttachment(10)
    

    def PlayUseEffect(self):
        ExecuteUbergraph_BP_ConsumeableEquipmentAttachment.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ConsumeableEquipmentAttachment(421)
    

    def OnAttach(self):
        self.ExecuteUbergraph_BP_ConsumeableEquipmentAttachment(884)
    

    def ExecuteUbergraph_BP_ConsumeableEquipmentAttachment(self):
        
        item = None
        self.GetHandsItem(Ref[item])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(item)
        if not ReturnValue:
            goto('L1333')
        
        item = None
        self.GetHandsItem(Ref[item])
        ReturnValue_0: Ptr[StaticMesh] = Default__FGConsumableDescriptor.GetTPOverrideMesh(item)
        ReturnValue_1: bool = self.StaticMesh.SetStaticMesh(ReturnValue_0)
        
        item = None
        self.GetHandsItem(Ref[item])
        ReturnValue_2: Vector = Vector(item.ClassDefaultObject.mCustomHandsMeshScale, item.ClassDefaultObject.mCustomHandsMeshScale, item.ClassDefaultObject.mCustomHandsMeshScale)
        self.StaticMesh.SetRelativeScale3D(ReturnValue_2)
        # End
        self.PlayUseEffect(useLocation)
        ReturnValue_3: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_4: bool = ReturnValue_3.IsFirstPerson()
        if not ReturnValue_4:
            goto('L521')
        # End
        # Label 521
        ReturnValue_3 = self.GetAttachedTo()
        ReturnValue_5: Ptr[SkeletalMeshComponent] = ReturnValue_3.GetMesh3P()
        ReturnValue_6: Ptr[AnimInstance] = ReturnValue_5.GetAnimInstance()
        ReturnValue_7: bool = ReturnValue_6.Montage_IsPlaying(Eat_01_Montage)
        if not ReturnValue_7:
            goto('L699')
        # End
        # Label 699
        ReturnValue_3 = self.GetAttachedTo()
        ReturnValue_5 = ReturnValue_3.GetMesh3P()
        ReturnValue_6 = ReturnValue_5.GetAnimInstance()
        ReturnValue_8: float = ReturnValue_6.Montage_Play(Eat_01_Montage, 1, 0, 0, True)
        # End
        self.OnAttach()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: bool = ReturnValue1.IsFirstPerson()
        if not ReturnValue1_0:
            goto('L975')
        # End
        # Label 975
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_1: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh3P()
        ReturnValue1_2: Ptr[AnimInstance] = ReturnValue1_1.GetAnimInstance()
        ReturnValue1_3: bool = ReturnValue1_2.Montage_IsPlaying(ConsumablesEquip_01_Montage)
        if not ReturnValue1_3:
            goto('L1153')
        # End
        # Label 1153
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_1 = ReturnValue1.GetMesh3P()
        ReturnValue1_2 = ReturnValue1_1.GetAnimInstance()
        ReturnValue1_4: float = ReturnValue1_2.Montage_Play(ConsumablesEquip_01_Montage, 1, 0, 0, True)
    
