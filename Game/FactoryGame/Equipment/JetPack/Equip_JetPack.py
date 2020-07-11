
from codegen.ue4_stub import *

from Script.Engine import GetGameTimeInSeconds
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterMovementComponent
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Deactivate import Play_EQ_JetPack_Deactivate
from Script.Engine import FClamp
from Script.FactoryGame import FGCharacterPlayer
from Script.AkAudio import SetActorRTPCValue
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import IsEquipped
from Script.Engine import GetInstigator
from Script.Engine import ReceiveBeginPlay
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import ExecuteUbergraph_Equip_JetPack.K2Node_CustomEvent_delta1
from Script.Engine import ReceiveTick
from Script.FactoryGame import CanAffordUse
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import Equip_JetPack
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import ExecuteUbergraph_Equip_JetPack.K2Node_CustomEvent_Delta
from Script.CoreUObject import Vector
from Script.FactoryGame import FGJetPack
from Script.FactoryGame import ChargeForUse
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import ExecuteUbergraph_Equip_JetPack.K2Node_Event_DeltaSeconds
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import ExecuteUbergraph_Equip_JetPack
from Script.Engine import Actor
from Game.FactoryGame.Equipment.JetPack.Audio.Play_EQ_JetPack_Activate import Play_EQ_JetPack_Activate
from Script.Engine import GetOwner
from Script.AkAudio import AkComponent
from Script.FactoryGame import IsAliveAndWell

class Equip_JetPack(FGJetPack):
    mThrustPower: float = 4000
    mVelocityZExtreme: float = 350
    mVelocityZExtremesDamper: float = 0.8999999761581421
    mJumpBeforeThrustTime: float = 0.30000001192092896
    mMaxFuel: float = 1
    mCurrentFuel: float = 1
    mFuelRegenRate: float = 0.5
    mFuelConsumeRate: float = 0.20000000298023224
    mThrustCooldown: float = 0.4000000059604645
    mFuelWorth: float = 0.5
    mPaidForFuel: float
    mThrustAirControl: float = 0.30000001192092896
    mDefaultAirControl: float
    mRTPCInterval: float
    mAttachmentClass = NewObject[Attach_JetPack]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mEquipmentWidget = NewObject[Widget_JetPack]()
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_Fuel.Desc_Fuel_C', 'amount': 1}]
    mBackAnimation = EBackEquipment::BE_Jetpack
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    AutoReceiveInput = 1
    
    def GetMaxFuel(self):
        ReturnValue = self.mMaxFuel
    

    def GetCurrentFuel(self):
        ReturnValue = self.mCurrentFuel
    

    def GetNewVelocityWhenThrusting(self):
        DeltaSeconds = Delta
        ReturnValue1: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_0: Vector = ReturnValue1.GetVelocity()
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue1_0)
        ReturnValue: bool = GreaterEqual_FloatFloat(Z1, self.mVelocityZExtreme)
        if not ReturnValue:
            goto('L439')
        ReturnValue_0: float = 1 - self.mVelocityZExtremesDamper
        ReturnValue4: float = self.mThrustPower * ReturnValue_0
        ReturnValue5: float = DeltaSeconds * ReturnValue4
        NewZ = ReturnValue5
        # Label 360
        ReturnValue_1: Vector = Vector(0, 0, NewZ)
        ReturnValue_2: Vector = ReturnValue_1
        goto('L897')
        # Label 439
        ReturnValue_3: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_4: Vector = ReturnValue_3.GetVelocity()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_4)
        ReturnValue1_1: float = self.mVelocityZExtreme * -1
        ReturnValue_5: bool = Z <= ReturnValue1_1
        if not ReturnValue_5:
            goto('L819')
        ReturnValue_6: float = 1 + self.mVelocityZExtremesDamper
        ReturnValue2: float = self.mThrustPower * ReturnValue_6
        ReturnValue3: float = DeltaSeconds * ReturnValue2
        NewZ = ReturnValue3
        goto('L360')
        # Label 819
        ReturnValue_7: float = self.mThrustPower * DeltaSeconds
        NewZ = ReturnValue_7
        goto('L360')
    

    def CanThrust(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: bool = ReturnValue.IsAliveAndWell()
        if not ReturnValue_0:
            goto('L606')
        ReturnValue = self.GetInstigatorCharacter()
        Component: Ptr[FGCharacterMovementComponent] = Cast[FGCharacterMovementComponent](ReturnValue.CharacterMovement)
        bSuccess: bool = Component
        if not bSuccess:
            goto('L622')
        ReturnValue_1: float = Default__KismetSystemLibrary.GetGameTimeInSeconds(self)
        ReturnValue_2: bool = self.mThrustCooldown <= 0
        ReturnValue_3: bool = self.mCurrentFuel > 0
        ReturnValue_4: bool = Component.IsFalling()
        ReturnValue_5: float = ReturnValue_1 - Component.mLastJumpTimeStamp
        ReturnValue_6: bool = GreaterEqual_FloatFloat(ReturnValue_5, self.mJumpBeforeThrustTime)
        ReturnValue_7: bool = ReturnValue_6 and ReturnValue_4
        ReturnValue1: bool = ReturnValue_7 and ReturnValue_3
        ReturnValue2: bool = ReturnValue1 and ReturnValue_2
        ReturnValue_8: bool = ReturnValue2
        goto('L633')
        # Label 606
        ReturnValue_8 = False
        goto('L633')
        # Label 622
        ReturnValue_8 = False
    

    def OnStartThrusting(self):
        self.ExecuteUbergraph_Equip_JetPack(2906)
    

    def OnStopThrusting(self):
        self.ExecuteUbergraph_Equip_JetPack(2901)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_JetPack.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_JetPack(10)
    

    def ConsumeFuel(self, Delta: float):
        ExecuteUbergraph_Equip_JetPack.K2Node_CustomEvent_delta1 = Delta #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_JetPack(1174)
    

    def RegenerateFuel(self, Delta: float):
        ExecuteUbergraph_Equip_JetPack.K2Node_CustomEvent_Delta = Delta #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_JetPack(588)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_JetPack(1798)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_JetPack(1969)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_JetPack(2896)
    

    def ExecuteUbergraph_Equip_JetPack(self):
        self.ReceiveTick(DeltaSeconds)
        ReturnValue: bool = self.IsEquipped()
        if not ReturnValue:
            goto('L2911')
        ReturnValue2: float = self.mRTPCInterval + DeltaSeconds
        self.mRTPCInterval = ReturnValue2
        ReturnValue1: bool = self.mRTPCInterval > 0.10000000149011612
        if not ReturnValue1:
            goto('L267')
        Default__AkGameplayStatics.SetActorRTPCValue("FG_Tools_JetPack_Fuel", self.mCurrentFuel, 0, self)
        self.mRTPCInterval = 0
        # Label 267
        ReturnValue2_0: float = self.mThrustCooldown - DeltaSeconds
        self.mThrustCooldown = ReturnValue2_0
        if not self.mIsThrusting:
            goto('L382')
        self.ConsumeFuel(DeltaSeconds)
        # End
        # Label 382
        ReturnValue_0: bool = self.mCurrentFuel <= self.mMaxFuel
        ReturnValue_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_2: bool = ReturnValue_1.CharacterMovement.IsMovingOnGround()
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_0
        if not ReturnValue_3:
            goto('L2911')
        self.RegenerateFuel(DeltaSeconds)
        # End
        ReturnValue_4: bool = self.mPaidForFuel > 0
        # Label 622
        if not ReturnValue_4:
            goto('L1018')
        # Label 636
        ReturnValue2_1: float = self.mMaxFuel * self.mFuelRegenRate
        ReturnValue3: float = Delta * ReturnValue2_1
        ReturnValue1_0: float = self.mPaidForFuel - ReturnValue3
        self.mPaidForFuel = ReturnValue1_0
        ReturnValue2_1 = self.mMaxFuel * self.mFuelRegenRate
        ReturnValue3 = Delta * ReturnValue2_1
        ReturnValue_5: float = self.mCurrentFuel + ReturnValue3
        ReturnValue1_1: float = FClamp(ReturnValue_5, 0, 1)
        self.mCurrentFuel = ReturnValue1_1
        # End
        # Label 1018
        ReturnValue_6: bool = self.CanAffordUse()
        if not ReturnValue_6:
            goto('L2911')
        ReturnValue_7: bool = self.HasAuthority()
        if not ReturnValue_7:
            goto('L636')
        self.ChargeForUse()
        ReturnValue1_2: float = self.mPaidForFuel + self.mFuelWorth
        self.mPaidForFuel = ReturnValue1_2
        goto('L636')
        ReturnValue_8: float = self.mMaxFuel * self.mFuelConsumeRate
        ReturnValue1_3: float = delta1 * ReturnValue_8
        ReturnValue_9: float = self.mCurrentFuel - ReturnValue1_3
        ReturnValue_10: bool = ReturnValue_9 <= 0
        if not ReturnValue_10:
            goto('L1409')
        self.mThrustCooldown = Equip_JetPack.ClassDefaultObject.mThrustCooldown
        # Label 1409
        ReturnValue_8 = self.mMaxFuel * self.mFuelConsumeRate
        ReturnValue1_3 = delta1 * ReturnValue_8
        ReturnValue_9 = self.mCurrentFuel - ReturnValue1_3
        ReturnValue_11: float = FClamp(ReturnValue_9, 0, 1)
        self.mCurrentFuel = ReturnValue_11
        # End
        # Label 1626
        ReturnValue_12: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Deactivate, ReturnValue_12, True)
        # End
        # Label 1712
        ReturnValue_12 = self.GetInstigator()
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Activate, ReturnValue_12, True)
        # End
        self.ReceiveBeginPlay()
        ReturnValue_14: Ptr[Actor] = self.GetOwner()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_14)
        bSuccess: bool = Player
        self.mDefaultAirControl = Player.CharacterMovement.AirControl
        # End
        ReturnValue1_5: Ptr[Actor] = self.GetOwner()
        ReturnValue_15: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_5)
        if not ReturnValue_15:
            goto('L2911')
        ReturnValue1_5 = self.GetOwner()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_5)
        bSuccess1: bool = Player1
        if not bSuccess1:
            goto('L2911')
        ReturnValue1_5 = self.GetOwner()
        Player1 = Cast[FGCharacterPlayer](ReturnValue1_5)
        bSuccess1 = Player1
        self.mDefaultAirControl = Player1.CharacterMovement.AirControl
        ReturnValue1_5 = self.GetOwner()
        Player1 = Cast[FGCharacterPlayer](ReturnValue1_5)
        bSuccess1 = Player1
        Player1.CharacterMovement.AirControl = self.mThrustAirControl
        # End
        # Label 2470
        ReturnValue2_2: Ptr[Actor] = self.GetOwner()
        ReturnValue1_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_2)
        if not ReturnValue1_6:
            goto('L2810')
        ReturnValue2_2 = self.GetOwner()
        Player2: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue2_2)
        bSuccess2: bool = Player2
        if not bSuccess2:
            goto('L2911')
        ReturnValue2_2 = self.GetOwner()
        Player2 = Cast[FGCharacterPlayer](ReturnValue2_2)
        bSuccess2 = Player2
        Player2.CharacterMovement.AirControl = self.mDefaultAirControl
        # Label 2810
        ReturnValue1_7: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_JetPack_Deactivate, ReturnValue1_7, True)
        # End
        goto('L2470')
        goto('L1626')
        goto('L1712')
    
