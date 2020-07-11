
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import HasValidCurrentDetails
from Script.FactoryGame import WasEquipped
from Script.InputCore import Key
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.ObjectScanner.Animation.ObjectScannerCycleRight_01_Montage import ObjectScannerCycleRight_01_Montage
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import Montage_Stop
from Game.FactoryGame.Interface.UI.Material.Material_UI_ObjectScanner import Material_UI_ObjectScanner
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_ColorToLinearColor
from Script.Engine import Normal
from Script.Engine import Montage_Play
from Script.Engine import RetriggerableDelay
from Script.UMG import Create
from Script.FactoryGame import GetCurrentDetails
from Script.Engine import Montage_IsPlaying
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Equipment.ObjectScanner.Widget_ObjectScannerMenu import Widget_ObjectScannerMenu
from Script.Engine import K2_DrawText
from Script.Engine import SetVisibility
from Script.Engine import FClamp
from Script.Engine import Controller
from Script.Engine import CreateCanvasRenderTarget2D
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ObjectScannerEquip_01_Montage import ObjectScannerEquip_01_Montage
from Script.Engine import Pawn
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import SetLightColor
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key
from Game.FactoryGame.Equipment.ObjectScanner.Audio.Play_T_ObjectScanner_Static import Play_T_ObjectScanner_Static
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.ObjectScanner.Animation.ObjectScannerCycleLeft_01_Montage import ObjectScannerCycleLeft_01_Montage
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner.K2Node_Event_isObjectInRange
from Script.Engine import AnimMontage
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import GetInstigatorController
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import GetDistanceTo
from Script.Engine import GetOwner
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Script.AkAudio import PostAkEvent
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner.K2Node_Event_wasChange
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Conv_IntToFloat
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ObjectScannerCycleLeft_01_Montage import ObjectScannerCycleLeft_01_Montage
from Game.FactoryGame.Equipment.ObjectScanner.Audio.Stop_T_ObjectScanner_Static import Stop_T_ObjectScanner_Static
from Script.Engine import SetTextureParameterValue
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Equipment.ObjectScanner.Audio.Play_T_ObjectScanner import Play_T_ObjectScanner
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Equipment.ObjectScanner.Audio.Play_T_ObjectScanner_RotateTarget import Play_T_ObjectScanner_RotateTarget
from Game.FactoryGame.Interface.Font.DescriptionMaterialText import DescriptionMaterialText
from Script.Engine import Subtract_VectorVector
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ObjectScannerCycleRight_01_Montage import ObjectScannerCycleRight_01_Montage
from Script.Engine import Multiply_VectorVector
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key1
from Script.Engine import Conv_TextToString
from Script.Engine import SetScalarParameterValue
from Script.Engine import Lerp
from Script.Engine import Default__CanvasRenderTarget2D
from Script.FactoryGame import WasUnEquipped
from Script.FactoryGame import ScannableDetails
from Script.Engine import GetInstigator
from Script.Engine import CanvasRenderTarget2D
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetAnimInstance
from Script.Engine import GetCurrentActiveMontage
from Script.Engine import GreaterEqual_FloatFloat
from Script.FactoryGame import PlayBeep
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner
from Script.Engine import DegAtan2
from Script.CoreUObject import Vector
from Script.FactoryGame import FGObjectScanner
from Script.FactoryGame import CycleBackward
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.ObjectScanner.Equip_ObjectScanner import ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key2
from Script.Engine import AnimInstance
from Script.Engine import IsValidClass
from Script.Engine import K2_DrawTexture

class Equip_ObjectScanner(FGObjectScanner):
    mObjectScannerMenu: Ptr[Widget_ObjectScannerMenu]
    mAKLoopingSound: Ptr[AkComponent]
    mPlayingSound: bool
    mSoundAttachedTo: Ptr[Actor]
    mScreenMaterial: Ptr[MaterialInstanceDynamic]
    mScreenUpdateTimer: TimerHandle
    mScanlineLerpT: float = 1
    mScreenUpdateTime: float = 0.05000000074505806
    mNormalizedCloesnessToObject: float
    mObjectIsWithinRange: bool
    mTextTexture: Ptr[CanvasRenderTarget2D]
    mIsPlayingScannerStatic: Ptr[AkComponent]
    mBeepDelayMax = 3
    mBeepDelayMin = 0.10000000149011612
    mDetectionRange = 25000
    mUpdateClosestObjectTime = 2
    mObjectDetails = [{'ScannableClass': '/Game/FactoryGame/Resource/Environment/Crystal/BP_Crystal.BP_Crystal_C', 'DisplayText': 'NSLOCTEXT("", "86EC608140665F49DDDC7CAB3C24F13F", "Power Slugs")', 'ScannerLightColor': {'B': 177, 'G': 146, 'R': 0, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/PowerSlugs_RS/Research_PowerSlugs_3.Research_PowerSlugs_3_C'}, {'ScannableClass': '/Script/FactoryGame.FGEnemy', 'DisplayText': 'NSLOCTEXT("", "5B74A8BE4A1C9CD855BEFC811B4B3B25", "Enemies")', 'ScannerLightColor': {'B': 0, 'G': 101, 'R': 255, 'A': 0}, 'PreCacheAllOfType': False, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 10000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/AlienOrganisms_RS/Research_AOrganisms_2.Research_AOrganisms_2_C'}, {'ScannableClass': '/Game/FactoryGame/World/Benefit/DropPod/BP_DropPod.BP_DropPod_C', 'DisplayText': 'NSLOCTEXT("", "445D760D4B31F089FAB651BB8F5A483A", "Crash Sites")', 'ScannerLightColor': {'B': 0, 'G': 255, 'R': 25, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': True, 'NewDetectionRange': 10000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/Quartz_RS/Research_Quartz_4_1.Research_Quartz_4_1_C'}, {'ScannableClass': '/Game/FactoryGame/Prototype/WAT/BP_WAT1.BP_WAT1_C', 'DisplayText': 'NSLOCTEXT("", "F4D2653A4A5880AF210B01A5603FB563", "Somersloop")', 'ScannerLightColor': {'B': 39, 'G': 0, 'R': 218, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Story/Schematic_ObjectScanner_WAT1.Schematic_ObjectScanner_WAT1_C'}, {'ScannableClass': '/Game/FactoryGame/Prototype/WAT/BP_WAT2.BP_WAT2_C', 'DisplayText': 'NSLOCTEXT("", "B7981DAF4A4E916397EAE49AB80D441C", "Mercer Sphere")', 'ScannerLightColor': {'B': 255, 'G': 0, 'R': 170, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Story/Schematic_ObjectScanner_WAT2.Schematic_ObjectScanner_WAT2_C'}, {'ScannableClass': '/Game/FactoryGame/World/Benefit/BerryBush/BP_BerryBush.BP_BerryBush_C', 'DisplayText': 'NSLOCTEXT("", "ADD8E7C04B264BAFB77408BEF1094886", "Berry")', 'ScannerLightColor': {'B': 141, 'G': 0, 'R': 255, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/Nutrients_RS/Research_Nutrients_0.Research_Nutrients_0_C'}, {'ScannableClass': '/Game/FactoryGame/World/Benefit/NutBush/BP_NutBush.BP_NutBush_C', 'DisplayText': 'NSLOCTEXT("", "5427CF4542BC62E4F49D0BAD9B8BEFB0", "Nut")', 'ScannerLightColor': {'B': 0, 'G': 108, 'R': 186, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/Nutrients_RS/Research_Nutrients_1.Research_Nutrients_1_C'}, {'ScannableClass': '/Game/FactoryGame/World/Benefit/Mushroom/BP_Shroom_01.BP_Shroom_01_C', 'DisplayText': 'NSLOCTEXT("", "8FB555B946C751A2EA7A278D771C8161", "Mushroom")', 'ScannerLightColor': {'B': 208, 'G': 195, 'R': 255, 'A': 0}, 'PreCacheAllOfType': True, 'ShouldOverrideDetectionRange': False, 'NewDetectionRange': 1000, 'RequiredSchematic': '/Game/FactoryGame/Schematics/Research/Nutrients_RS/Research_Nutrients_2.Research_Nutrients_2_C'}]
    mAttachmentClass = NewObject[Attach_ObjectScanner]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mUnequipSound = Namespace(AssetPath='/Game/FactoryGame/Equipment/ObjectScanner/Audio/Stop_T_ObjectScanner_Static.Stop_T_ObjectScanner_Static')
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_ObjectScanner
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/ObjectScannerIdle_01.ObjectScannerIdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnUpdateTextMaterial(self, Canvas: Ptr[Canvas], Width: int32, Height: int32):
        LocalNoneText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'None'}"
        ReturnValue: float = Conv_IntToFloat(Height)
        ReturnValue1: float = Conv_IntToFloat(Width)
        ReturnValue_0: Vector2D = Vector2D(ReturnValue1, ReturnValue)
        Canvas.K2_DrawTexture(None, Vector2D(X = 0, Y = 0), ReturnValue_0, Vector2D(X = 0, Y = 0), Vector2D(X = 1, Y = 1), LinearColor(R = 1, G = 1, B = 1, A = 0), 2, 0, Vector2D(X = 0.5, Y = 0.5))
        ReturnValue_1: bool = self.HasValidCurrentDetails()
        if not ReturnValue_1:
            goto('L641')
        ReturnValue_2: ScannableDetails = self.GetCurrentDetails()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_2.ScannableClass)
        Variable: bool = ReturnValue_3
        
        switch = {
            False: LocalNoneText,
            True: ReturnValue_2.DisplayText
        }
        
        switch.get(Variable, None) = None
        ReturnValue_4: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[switch.get(Variable, None)])
        ObjectDisplayText = ReturnValue_4
        # Label 641
        ReturnValue1 = Conv_IntToFloat(Width)
        ReturnValue_5: float = ReturnValue1 / 2
        # Label 720
        ReturnValue1_0: Vector2D = Vector2D(ReturnValue_5, 7)
        Canvas.K2_DrawText(DescriptionMaterialText, ObjectDisplayText, ReturnValue1_0, Vector2D(X = 0.6000000238418579, Y = 0.6000000238418579), LinearColor(R = 1, G = 1, B = 1, A = 1), 0, LinearColor(R = 0, G = 0, B = 0, A = 1), Vector2D(X = 1, Y = 1), True, False, False, LinearColor(R = 0, G = 0, B = 0, A = 1))
    

    def SetupTextMaterial(self):
        ReturnValue: Ptr[CanvasRenderTarget2D] = Default__CanvasRenderTarget2D.CreateCanvasRenderTarget2D(self, CanvasRenderTarget2D, 256, 64)
        self.mTextTexture = ReturnValue
        OutputDelegate.BindUFunction(self, OnUpdateTextMaterial)
        self.mTextTexture.OnCanvasRenderTargetUpdate.AddUnique(OutputDelegate)
        self.mTextTexture.UpdateResource()
        self.mScreenMaterial.SetTextureParameterValue("text", self.mTextTexture)
    

    def GetAngleToClosestTarget(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mClosestObject)
        if not ReturnValue:
            goto('L1071')
        ReturnValue_0: Ptr[Actor] = self.GetOwner()
        ReturnValue_1: Vector = ReturnValue_0.GetActorForwardVector()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        ReturnValue_2: Vector = self.mClosestObject.K2_GetActorLocation()
        ReturnValue_3: float = DegAtan2(Y, X)
        ReturnValue_4: Vector = Multiply_VectorVector(ReturnValue_2, Vector(1, 1, 0))
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        ReturnValue1_0: Vector = ReturnValue1.K2_GetActorLocation()
        ReturnValue1_1: Vector = Multiply_VectorVector(ReturnValue1_0, Vector(1, 1, 0))
        ReturnValue_5: Vector = Subtract_VectorVector(ReturnValue_4, ReturnValue1_1)
        ReturnValue_6: Vector = Normal(ReturnValue_5, 9.999999747378752e-05)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_6)
        ReturnValue1_2: float = DegAtan2(Y1, X1)
        ReturnValue_7: float = ReturnValue1_2 - ReturnValue_3
        ReturnValue_8: bool = ReturnValue_7 <= 0
        ReturnValue_9: float = ReturnValue_7 + 360
        Variable1: bool = ReturnValue_8
        
        switch = {
            False: ReturnValue_7,
            True: ReturnValue_9
        }
        ReturnValue_10: bool = switch.get(Variable1, None) > 180
        
        switch_0 = {
            False: ReturnValue_7,
            True: ReturnValue_9
        }
        ReturnValue1_3: float = 360 - switch_0.get(Variable1, None)
        Variable: bool = ReturnValue_10
        
        switch_1 = {
            False: ReturnValue_7,
            True: ReturnValue_9
        }
        
        switch_2 = {
            False: switch_1.get(Variable1, None),
            True: ReturnValue1_3
        }
        ReturnValue_11: float = switch_2.get(Variable, None)
        goto('L1094')
        # Label 1071
        ReturnValue_11 = 0
    

    def InpActEvt_SecondaryFire_K2Node_InputActionEvent_2(self, Key: Key):
        ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key2 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_ObjectScanner(5686)
    

    def InpActEvt_PrimaryFire_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_ObjectScanner(2942)
    

    def InpActEvt_PrimaryFire_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_Equip_ObjectScanner.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_ObjectScanner(2910)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(50)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(2344)
    

    def Event BlinkLight(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(2974)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(3480)
    

    def Event Update Screen(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(3631)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Equip_ObjectScanner(5477)
    

    def UpdateScannerVisuals(self):
        ExecuteUbergraph_Equip_ObjectScanner.K2Node_Event_wasChange = wasChange #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_ObjectScanner(5651)
    

    def PlayBeep(self):
        ExecuteUbergraph_Equip_ObjectScanner.K2Node_Event_isObjectInRange = isObjectInRange #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_ObjectScanner(5691)
    

    def ExecuteUbergraph_Equip_ObjectScanner(self):
        goto(ComputedJump("EntryPoint"))
        self.PointLight.SetVisibility(False, False)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_0: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh1P()
        ReturnValue4: Ptr[AnimInstance] = ReturnValue2_0.GetAnimInstance()
        ReturnValue4_0: bool = ReturnValue4.Montage_IsPlaying(ObjectScannerEquip_01_Montage)
        if not ReturnValue4_0:
            goto('L230')
        goto(ExecutionFlow.Pop())
        # Label 230
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue4 = ReturnValue2_0.GetAnimInstance()
        ReturnValue4_1: float = ReturnValue4.Montage_Play(ObjectScannerEquip_01_Montage, 1, 0, 0, True)
        self.Event Update Screen()
        OutputDelegate.BindUFunction(self, Event Update Screen)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mScreenUpdateTime, True)
        self.mScreenUpdateTimer = ReturnValue
        goto(ExecutionFlow.Pop())
        # Label 540
        ExecutionFlow.Push("L943")
        ExecutionFlow.Push("L720")
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh1P()
        ReturnValue3: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue2_1: bool = ReturnValue3.Montage_IsPlaying(ObjectScannerCycleLeft_01_Montage)
        if not ReturnValue2_1:
            goto('L980')
        goto(ExecutionFlow.Pop())
        # Label 720
        ReturnValue1_1: Ptr[AnimInstance] = self.CrystalScanner_skl.GetAnimInstance()
        ReturnValue_0: bool = ReturnValue1_1.Montage_IsPlaying(ObjectScannerCycleLeft_01_Montage)
        if not ReturnValue_0:
            goto('L828')
        goto(ExecutionFlow.Pop())
        # Label 828
        ReturnValue1_1 = self.CrystalScanner_skl.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue1_1.Montage_Play(ObjectScannerCycleLeft_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 943
        self.mTextTexture.UpdateResource()
        goto(ExecutionFlow.Pop())
        # Label 980
        ReturnValue1 = self.GetInstigatorCharacter()
        ReturnValue1_0 = ReturnValue1.GetMesh1P()
        ReturnValue3 = ReturnValue1_0.GetAnimInstance()
        ReturnValue3_0: float = ReturnValue3.Montage_Play(ObjectScannerCycleLeft_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1157
        ExecutionFlow.Push("L1562")
        ReturnValue_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_2: Ptr[SkeletalMeshComponent] = ReturnValue_1.GetMesh1P()
        ReturnValue2_2: Ptr[AnimInstance] = ReturnValue_2.GetAnimInstance()
        ReturnValue3_1: bool = ReturnValue2_2.Montage_IsPlaying(ObjectScannerCycleRight_01_Montage)
        if not ReturnValue3_1:
            goto('L1332')
        goto(ExecutionFlow.Pop())
        # Label 1332
        ReturnValue_1 = self.GetInstigatorCharacter()
        ReturnValue_2 = ReturnValue_1.GetMesh1P()
        ReturnValue2_2 = ReturnValue_2.GetAnimInstance()
        ReturnValue2_3: float = ReturnValue2_2.Montage_Play(ObjectScannerCycleRight_01_Montage, 1, 0, 0, True)
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ObjectScanner_RotateTarget, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1562
        ReturnValue_4: Ptr[AnimInstance] = self.CrystalScanner_skl.GetAnimInstance()
        ReturnValue1_3: bool = ReturnValue_4.Montage_IsPlaying(ObjectScannerCycleRight_01_Montage)
        if not ReturnValue1_3:
            goto('L1670')
        goto(ExecutionFlow.Pop())
        # Label 1670
        ReturnValue_4 = self.CrystalScanner_skl.GetAnimInstance()
        ReturnValue_5: float = ReturnValue_4.Montage_Play(ObjectScannerCycleRight_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1785
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.mObjectScannerMenu)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue2_4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_5: Ptr[Controller] = ReturnValue2_4.GetInstigatorController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue2_5, self.mObjectScannerMenu, self)
        goto(ExecutionFlow.Pop())
        # Label 1964
        ReturnValue_7: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_8: Ptr[Controller] = ReturnValue_7.GetInstigatorController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_8)
        bSuccess: bool = Controller
        ReturnValue_9: Ptr[Widget_ObjectScannerMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_ObjectScannerMenu, Controller)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_9, "mObjectScanner", self)
        ReturnValue1_4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_5: Ptr[Controller] = ReturnValue1_4.GetInstigatorController()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue1_5, ReturnValue_9, self)
        self.mObjectScannerMenu = ReturnValue_9
        goto(ExecutionFlow.Pop())
        self.WasUnEquipped()
        ReturnValue3_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_3: Ptr[SkeletalMeshComponent] = ReturnValue3_2.GetMesh1P()
        ReturnValue5: Ptr[AnimInstance] = ReturnValue3_3.GetAnimInstance()
        ReturnValue_10: Ptr[AnimMontage] = ReturnValue5.GetCurrentActiveMontage()
        ReturnValue5.Montage_Stop(0, ReturnValue_10)
        ReturnValue7: bool = Default__KismetSystemLibrary.IsValid(self.mIsPlayingScannerStatic)
        if not ReturnValue7:
            goto('L2664')
        ReturnValue4_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_T_ObjectScanner_Static, self, True)
        
        # Label 2664
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mScreenUpdateTimer])
        ReturnValue1_6: bool = Default__KismetSystemLibrary.IsValid(self.mObjectScannerMenu)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        ReturnValue4_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_11: Ptr[Controller] = ReturnValue4_3.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue_11, self.mObjectScannerMenu, self)
        goto(ExecutionFlow.Pop())
        # Label 2885
        ReturnValue_12: bool = self.CycleBackward()
        goto('L1157')
        Variable: Key = Key
        goto('L1964')
        Variable = Key1
        goto('L1785')
        ReturnValue_13: float = self.GetAngleToClosestTarget()
        ReturnValue_14: bool = ReturnValue_13 <= 50
        self.PointLight.SetVisibility(ReturnValue_14, False)
        self.mScanlineLerpT = 0
        self.mScreenMaterial.SetScalarParameterValue("ScanLinesOpacity", 1)
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 1019784855, ExecutionFunction = "ExecuteUbergraph_Equip_ObjectScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3232
        self.Event BlinkLight()
        ReturnValue4_4: bool = Default__KismetSystemLibrary.IsValid(self.mClosestObject)
        ReturnValue3_4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_7: bool = ReturnValue4_4 and isObjectInRange
        Variable1: bool = ReturnValue1_7
        
        switch = {
            False: ReturnValue3_4,
            True: self.mClosestObject
        }
        ReturnValue1_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ObjectScanner, switch.get(Variable1, None), True)
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        ReturnValue_15: Ptr[MaterialInstanceDynamic] = self.CrystalScanner_skl.CreateDynamicMaterialInstance(2, Material_UI_ObjectScanner, "ScreenMaterial")
        self.mScreenMaterial = ReturnValue_15
        self.PointLight.SetVisibility(False, False)
        self.SetupTextMaterial()
        goto(ExecutionFlow.Pop())
        ReturnValue3_5: bool = Default__KismetSystemLibrary.IsValid(self.mScreenMaterial)
        if not ReturnValue3_5:
           goto(ExecutionFlow.Pop())
        ReturnValue2_6: bool = Default__KismetSystemLibrary.IsValid(self.mClosestObject)
        if not ReturnValue2_6:
            goto('L5399')
        ReturnValue_16: Ptr[Actor] = self.GetOwner()
        ReturnValue_17: float = self.mClosestObject.GetDistanceTo(ReturnValue_16)
        ReturnValue_18: float = ReturnValue_17 / self.mDetectionRange
        ReturnValue1_9: float = 1 - ReturnValue_18
        self.mNormalizedCloesnessToObject = ReturnValue1_9
        ReturnValue1_10: float = self.GetAngleToClosestTarget()
        ReturnValue_19: float = FClamp(ReturnValue1_10, 30, 70)
        ReturnValue_20: float = ReturnValue_19 - 30
        ReturnValue1_11: float = ReturnValue_20 / 40
        ReturnValue_21: float = Ease(1, 0, ReturnValue1_11, 7, 2, 2)
        ReturnValue_22: float = self.mNormalizedCloesnessToObject * ReturnValue_21
        self.mScreenMaterial.SetScalarParameterValue("Value", ReturnValue_22)
        # Label 4273
        ReturnValue2_7: float = self.mScreenUpdateTime / 0.30000001192092896
        ReturnValue_23: float = self.mScanlineLerpT + ReturnValue2_7
        self.mScanlineLerpT = ReturnValue_23
        ReturnValue_24: float = Lerp(0, 1, self.mScanlineLerpT)
        ReturnValue3_6: float = 1 - ReturnValue_24
        self.mScreenMaterial.SetScalarParameterValue("ScanLinesOpacity", ReturnValue3_6)
        ReturnValue_24 = Lerp(0, 1, self.mScanlineLerpT)
        ReturnValue2_8: float = 4 - ReturnValue_24
        ReturnValue_25: bool = ReturnValue_24 > 2
        Variable_0: bool = ReturnValue_25
        
        switch_0 = {
            False: ReturnValue_24,
            True: ReturnValue2_8
        }
        self.mScreenMaterial.SetScalarParameterValue("OutOfRangeOpacity", switch_0.get(Variable_0, None))
        ReturnValue_26: bool = self.mNormalizedCloesnessToObject <= 0
        self.mObjectIsWithinRange = ReturnValue_26
        Variable_1: float = 0
        Variable1_0: float = 1
        Variable2: bool = self.mObjectIsWithinRange
        
        switch_1 = {
            False: Variable_1,
            True: Variable1_0
        }
        self.mScreenMaterial.SetScalarParameterValue("ShowOutOfRangeWarning", switch_1.get(Variable2, None))
        ReturnValue_27: bool = GreaterEqual_FloatFloat(self.mScanlineLerpT, 4)
        ReturnValue_28: bool = self.mObjectIsWithinRange and ReturnValue_27
        if not ReturnValue_28:
            goto('L5097')
        self.mScanlineLerpT = 0
        goto(ExecutionFlow.Pop())
        # Label 5097
        ReturnValue1_12: bool = self.mNormalizedCloesnessToObject <= 0
        if not ReturnValue1_12:
            goto('L5284')
        ReturnValue5_0: bool = Default__KismetSystemLibrary.IsValid(self.mIsPlayingScannerStatic)
        if not ReturnValue5_0:
            goto('L5211')
        goto(ExecutionFlow.Pop())
        # Label 5211
        ReturnValue3_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ObjectScanner_Static, self, True)
        self.mIsPlayingScannerStatic = ReturnValue3_7
        goto(ExecutionFlow.Pop())
        # Label 5284
        ReturnValue6: bool = Default__KismetSystemLibrary.IsValid(self.mIsPlayingScannerStatic)
        if not ReturnValue6:
           goto(ExecutionFlow.Pop())
        ReturnValue2_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_T_ObjectScanner_Static, self, True)
        goto(ExecutionFlow.Pop())
        # Label 5399
        self.mNormalizedCloesnessToObject = 0
        self.mScreenMaterial.SetScalarParameterValue("Value", 0)
        goto('L4273')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mScreenUpdateTimer])
        goto(ExecutionFlow.Pop())
        # Label 5520
        ReturnValue_29: ScannableDetails = self.GetCurrentDetails()
        ReturnValue_30: LinearColor = Conv_ColorToLinearColor(ReturnValue_29.ScannerLightColor)
        self.PointLight.SetLightColor(ReturnValue_30, True)
        if not wasChange:
           goto(ExecutionFlow.Pop())
        goto('L540')
        ReturnValue_31: bool = self.HasValidCurrentDetails()
        if not ReturnValue_31:
           goto(ExecutionFlow.Pop())
        goto('L5520')
        goto('L2885')
        self.PlayBeep(isObjectInRange)
        goto('L3232')
    
