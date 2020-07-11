
from codegen.ue4_stub import *

from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.Engine import EqualEqual_IgnoreCase_TextText
from Script.Engine import K2_SetText
from Script.Engine import TextIsEmpty
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Buildable.Factory.TrainStation.UI.TrainStation import TrainStation
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Script.Engine import FormatArgumentData
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import UpdateRepresentation
from Script.Engine import Conv_StringToText
from Script.Engine import BooleanOR
from Game.FactoryGame.Buildable.Factory.Train.Station.Build_TrainStation import ExecuteUbergraph_Build_TrainStation.K2Node_Event_EndPlayReason
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.Engine import Format
from Game.FactoryGame.Buildable.Factory.Train.Station.Build_TrainStation import ExecuteUbergraph_Build_TrainStation.K2Node_Event_newColor
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import GetStationIdentifier
from Script.Engine import K2_GetActorLocation
from Script.Engine import ReceiveEndPlay
from Script.FactoryGame import GetStationName
from Game.FactoryGame.Buildable.Factory.Train.Station.Build_TrainStation import ExecuteUbergraph_Build_TrainStation
from Script.FactoryGame import RemoveRepresentationOfActor
from Script.FactoryGame import FGBuildableRailroadStation
from Script.FactoryGame import FGTrainStationIdentifier

class Build_TrainStation(FGBuildableRailroadStation):
    mMapText: FText = NSLOCTEXT("", "E439462347F68AA5CE470D91CE7735E6", "Train Station")
    mPlatformConnections = [{'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection0', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': 800, 'Y': 0, 'Z': 0}, 'RelativeRotation': {'Pitch': 0, 'Yaw': 180, 'Roll': 0}, 'Mobility': 0}, {'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection1', 'mPlatformConnectionStatus': 'ETrainPlatformConnectionType::ETPC_In', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': -800, 'Y': 0, 'Z': 0}, 'Mobility': 0}]
    mPlatformConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection0', RelativeLocation={'X': 800, 'Y': 0, 'Z': 0}, RelativeRotation={'Pitch': 0, 'Yaw': 180, 'Roll': 0})
    mPlatformConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection1', RelativeLocation={'X': -800, 'Y': 0, 'Z': 0}, mPlatformConnectionStatus='ETrainPlatformConnectionType::ETPC_In')
    mPowerConsumption = 50
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[Holo_TrainStation]()
    mDisplayName = NSLOCTEXT("", "16502BCC4D2CF4A772732E82C5D0744A", "Train Station")
    mDescription = NSLOCTEXT("", "45F1134A4FACC5A5FFA98D85DD102EFE", "Locomotives can be set to drive to and stop at the Train Station.\r\nYou can connect power to the train station to power up the trains on the railway as well as transport the power to other stations.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_TrainStationNew]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

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
        ReturnValue1: Ptr[FGTrainStationIdentifier] = self.GetStationIdentifier()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L462')
        ReturnValue_0: Ptr[FGTrainStationIdentifier] = self.GetStationIdentifier()
        localStationIdentifier = ReturnValue_0
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText("Train Station")
        ReturnValue_2: FText = localStationIdentifier.GetStationName()
        
        ReturnValue_3: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[ReturnValue_2])
        
        ReturnValue_4: bool = Default__KismetTextLibrary.EqualEqual_IgnoreCase_TextText(Ref[ReturnValue_2], Ref[ReturnValue_1])
        ReturnValue_5: bool = BooleanOR(ReturnValue_3, ReturnValue_4)
        if not ReturnValue_5:
            goto('L557')
        ReturnValue_6: FText = self.mMapText
        goto('L1146')
        # Label 462
        ReturnValue_6 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 482, 'Value': 'Invalid Train Station Identifier'}"
        goto('L1146')
        # Label 557
        ReturnValue1_0: FText = localStationIdentifier.GetStationName()
        FormatArgumentData.ArgumentName = "B"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue1_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mMapText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_7: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1063, 'Value': '{A}: {B}'}", Array)
        ReturnValue_6 = ReturnValue_7
    

    def GetActorRepresentationTexture(self):
        ReturnValue = TrainStation
    

    def GetActorRepresentationType(self):
        ReturnValue = 11
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

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
            goto('L144')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_2: bool = ReturnValue_1
        goto('L155')
        # Label 144
        ReturnValue_2 = False
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        # Label 10
        self.mMapText = newText
        ReturnValue = self.mMapText
    

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
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_Build_TrainStation.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TrainStation(39)
    

    def OnNameChanged(self):
        self.ExecuteUbergraph_Build_TrainStation(44)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_TrainStation(430)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Build_TrainStation.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TrainStation(469)
    

    def ExecuteUbergraph_Build_TrainStation(self):
        # Label 10
        ReturnValue: bool = self.UpdateRepresentation()
        # End
        # End
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 64, 'Value': 'Train Station'}"
        ReturnValue_0: Ptr[FGTrainStationIdentifier] = self.GetStationIdentifier()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        ReturnValue_2: FText = ReturnValue_0.GetStationName()
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: Variable,
            True: ReturnValue_2
        }
        
        switch.get(Variable_0, None) = None
        self.Name.K2_SetText(Ref[switch.get(Variable_0, None)])
        
        switch_0 = {
            False: Variable,
            True: ReturnValue_2
        }
        
        switch_0.get(Variable_0, None) = None
        self.Name_back.K2_SetText(Ref[switch_0.get(Variable_0, None)])
        goto('L10')
        self.ReceiveBeginPlay()
        ReturnValue_3: bool = self.AddAsRepresentation()
        # End
        self.ReceiveEndPlay(EndPlayReason)
        ReturnValue_4: bool = self.RemoveAsRepresentation()
    
