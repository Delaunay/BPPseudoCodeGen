
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Equipment.Rifle.Audio.Play_EQ_Rifle_Fire import Play_EQ_Rifle_Fire
from Script.FactoryGame import WasUnEquipped
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetAnimInstance
from Script.FactoryGame import PlayReloadEffects
from Script.FactoryGame import IsLocalInstigator
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RifleReloadMontage import RifleReloadMontage
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Equipment.Machinegun.Equip_Machinegun import ExecuteUbergraph_Equip_Machinegun.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGWeaponInstantFire
from Game.FactoryGame.Equipment.Rifle.Particle.RifleMuzzleFlash import RifleMuzzleFlash
from Script.UMG import GetUserWidgetObject
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.Machinegun.Equip_Machinegun import ExecuteUbergraph_Equip_Machinegun.K2Node_CustomEvent_showHUD
from Script.UMG import UserWidget
from Game.FactoryGame.Equipment.RebarGun.Particle.Hit import Hit
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.Machinegun.Widget_Machinegun import Widget_Machinegun
from Game.FactoryGame.Equipment.Rifle.Audio.Play_EQ_Rifle_Reload import Play_EQ_Rifle_Reload
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RiflePrimayMontage import RiflePrimayMontage
from Game.FactoryGame.Equipment.Machinegun.Equip_Machinegun import ExecuteUbergraph_Equip_Machinegun
from Script.Engine import SkeletalMeshComponent

class Equip_Machinegun(FGWeaponInstantFire):
    Fire: FMulticastScriptDelegate
    mLockAngle: float
    mInstantHitDamage = 4
    mWeaponTraceLength = 8500
    mMagSize = 100
    mAmmunitionClass = NewObject[Desc_CartridgeStandard]()
    mDamageTypeClass = NewObject[DamageType_Machinegun]()
    mReloadTime = 2
    mFireRate = 0.10000000149011612
    mAttachmentClass = NewObject[Attach_Machinegun]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Rifle
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_Machinegun(689)
    

    def PlayReloadEffects(self):
        self.ExecuteUbergraph_Equip_Machinegun(523)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_Machinegun.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Machinegun(865)
    

    def SwitchHUD(self, ShowHUD: bool):
        ExecuteUbergraph_Equip_Machinegun.K2Node_CustomEvent_showHUD = ShowHUD #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Machinegun(866)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_Machinegun(882)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Machinegun(902)
    

    def PlayFireEffect(self):
        self.ExecuteUbergraph_Equip_Machinegun(1358)
    

    def ExecuteUbergraph_Equip_Machinegun(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ReceiveBeginPlay()
        ReturnValue: Ptr[UserWidget] = self.mAmmo.GetUserWidgetObject()
        Machinegun: Ptr[Widget_Machinegun] = Cast[Widget_Machinegun](ReturnValue)
        bSuccess: bool = Machinegun
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Machinegun.mNailGun = self
        goto(ExecutionFlow.Pop())
        # Label 176
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue_0.GetMesh1P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_2.Montage_Play(RifleReloadMontage, 2, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 353
        ReturnValue_0 = self.GetInstigatorCharacter()
        ReturnValue_1 = ReturnValue_0.GetMesh1P()
        ReturnValue_2 = ReturnValue_1.GetAnimInstance()
        ReturnValue_4: bool = ReturnValue_2.Montage_IsPlaying(RifleReloadMontage)
        if not ReturnValue_4:
            goto('L176')
        goto(ExecutionFlow.Pop())
        self.PlayReloadEffects()
        ExecutionFlow.Push("L543")
        goto('L353')
        # Label 543
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Rifle_Reload, self, True)
        goto(ExecutionFlow.Pop())
        # Label 597
        ReturnValue_6: bool = self.IsLocalInstigator()
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.SwitchHUD(False)
        goto(ExecutionFlow.Pop())
        # Label 643
        ReturnValue1: bool = self.IsLocalInstigator()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        self.SwitchHUD(True)
        goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 694
        ReturnValue_7: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(RifleMuzzleFlash, self.Machinegun, "muzzleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_Rifle_Fire, self, True)
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        # Label 867
        self.WasUnEquipped()
        goto('L597')
        goto('L867')
        # Label 887
        self.WasEquipped()
        goto('L643')
        goto('L887')
        # Label 907
        ExecutionFlow.Push("L1082")
        ReturnValue1_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_2: Ptr[SkeletalMeshComponent] = ReturnValue1_1.GetMesh1P()
        ReturnValue1_3: Ptr[AnimInstance] = ReturnValue1_2.GetAnimInstance()
        ReturnValue1_4: bool = ReturnValue1_3.Montage_IsPlaying(RiflePrimayMontage)
        if not ReturnValue1_4:
            goto('L1181')
        goto(ExecutionFlow.Pop())
        # Label 1082
        ReturnValue_8: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, Hit, Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        goto('L694')
        # Label 1181
        ReturnValue1_1 = self.GetInstigatorCharacter()
        ReturnValue1_2 = ReturnValue1_1.GetMesh1P()
        ReturnValue1_3 = ReturnValue1_2.GetAnimInstance()
        ReturnValue1_5: float = ReturnValue1_3.Montage_Play(RiflePrimayMontage, 4, 0, 0, True)
        goto(ExecutionFlow.Pop())
        goto('L907')
    

    def Fire__DelegateSignature(self):
        pass
    
