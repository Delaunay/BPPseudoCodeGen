
from codegen.ue4_stub import *

from Script.FactoryGame import GetTimeOfDayHours
from Script.Engine import SetScalarParameterValue
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import GetLightColor
from Script.Engine import SetOcclusionMaskDarkness
from Script.FactoryGame import GetColorCurveValue
from Script.Engine import SetVisibility
from Script.Engine import FClamp
from Script.Engine import Lerp
from Game.FactoryGame.World.Environment.DayNight.BP_Sky_Sphere import ExecuteUbergraph_BP_Sky_Sphere.K2Node_Event_settings
from Script.FactoryGame import FGSkySphere
from Script.Engine import DirectionalLightComponent
from Script.Engine import GreaterGreater_VectorRotator
from Script.Engine import MapRangeUnclamped
from Script.CoreUObject import Rotator
from Script.Engine import DirectionalLight
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import AtmosphericFog
from Script.Engine import SetLightColor
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.World.Environment.Sky.Material.SkyScape_Inst import SkyScape_Inst
from Script.Engine import SetIntensity
from Script.FactoryGame import GetNightPct
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SelectFloat
from Script.FactoryGame import Get
from Script.Engine import ReceiveTick
from Script.CoreUObject import Color
from Script.FactoryGame import GetDayPct
from Script.Engine import SetVectorParameterValue
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.Engine import Conv_LinearColorToColor
from Script.FactoryGame import FGTimeOfDaySubsystem
from Game.FactoryGame.World.Environment.Water.Material.MPC_Globals import MPC_Globals
from Script.Engine import BreakRotator
from Script.Engine import Default__KismetMaterialLibrary
from Script.Engine import K2_SetActorRotation
from Script.CoreUObject import Vector
from Game.FactoryGame.World.Environment.DayNight.FBrightnessAdjustment import FBrightnessAdjustment
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import ComposeRotators
from Script.Engine import Conv_VectorToLinearColor
from Script.Engine import RuntimeFloatCurve
from Script.Engine import K2_GetActorRotation
from Script.Engine import MakeRotator
from Script.Engine import SkyLight
from Script.Engine import LessLess_VectorRotator
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.World.Environment.DayNight.BP_Sky_Sphere import ExecuteUbergraph_BP_Sky_Sphere.K2Node_Event_DeltaSeconds
from Game.FactoryGame.World.Environment.DayNight.BP_Sky_Sphere import ExecuteUbergraph_BP_Sky_Sphere
from Script.FactoryGame import Default__FGTimeOfDaySubsystem
from Script.Engine import MakeRotFromX
from Script.Engine import Abs
from Script.Engine import GetForwardVector
from Script.Engine import SetSunMultiplier
from Script.Engine import SetOcclusionTint
from Script.Engine import PostProcessVolume
from Script.Engine import Conv_RotatorToVector
from Script.CoreUObject import LinearColor

class BP_Sky_Sphere(FGSkySphere):
    mSkyMaterial: Ptr[MaterialInstanceDynamic]
    mSunLight: Ptr[DirectionalLight]
    mSunHeight: float
    mHorizonFalloff: float = 3
    mOriginSunRotation: Rotator = Namespace(Pitch=0, Roll=25, Yaw=45)
    mSunRotationAxis: Rotator = Namespace(Pitch=55, Roll=0, Yaw=190)
    mSkyLight: Ptr[SkyLight]
    mMoonLight: Ptr[DirectionalLight]
    mOriginMoonRotation: Rotator = Namespace(Pitch=0, Roll=25, Yaw=45)
    mMoonRotationAxis: Rotator = Namespace(Pitch=55, Roll=0, Yaw=190)
    mSunRadius: float = 0.0003000000142492354
    mMoonRadius: float = 0.0006000000284984708
    mSunBrightnessAdjust: FBrightnessAdjustment = Namespace(LightIntensity_5_7DFA36F84BCB1C040E5D69B250CB0137=2.75, SkySphereDiscBrightness_6_E856AF074C7A0AFAA790FCA8730DAEF9=100)
    mMoonBrightnessAdjust: FBrightnessAdjustment = Namespace(LightIntensity_5_7DFA36F84BCB1C040E5D69B250CB0137=0.15000000596046448, SkySphereDiscBrightness_6_E856AF074C7A0AFAA790FCA8730DAEF9=75)
    mDominantLight: Ptr[DirectionalLight]
    mDiscRadius: float
    mAtmosphericFog: Ptr[AtmosphericFog]
    mGlobalPostProcess: Ptr[PostProcessVolume]
    Cubemap_Curve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0.20000000298023224, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 3, 'Value': 0.4000000059604645, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 19, 'Value': 0.4000000059604645, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 20, 'Value': 0.20000000298023224, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mSunLightColorCurve = Namespace(ColorCurves={'Keys': [{'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -1.004958152770996, 'Value': 0, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 3.871776580810547, 'Value': 0.7309452295303345, 'ArriveTangent': 0.0992596447467804, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.0992596447467804, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 4.389677047729492, 'Value': 0.5354695916175842, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 4.655557155609131, 'Value': 0.8931311368942261, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mSunIntensity = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 1}, ExternalCurve={'$Empty': True})
    mSkyLightIntensity = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 5}, ExternalCurve={'$Empty': True})
    mOcclusionTintColor = Namespace(ColorCurves={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 0}, ExternalCurve={'$Empty': True})
    mHorizonColorCurve = Namespace(ColorCurves={'Keys': [{'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.001622319221496582, 'Value': 0.06592988967895508, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.44048529863357544, 'Value': 0.4929298758506775, 'ArriveTangent': 0.09801075607538223, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.09801075607538223, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 9.759634017944336, 'Value': 1.022637963294983, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 23.694190979003906, 'Value': 2.227677345275879, 'ArriveTangent': 0.20059318840503693, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.20059318840503693, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 23.84693717956543, 'Value': 2.2253003120422363, 'ArriveTangent': -0.32994309067726135, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.32994309067726135, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 24.048465728759766, 'Value': 1.5925207138061523, 'ArriveTangent': -1.5067789554595947, 'ArriveTangentWeight': 0, 'LeaveTangent': -1.5067789554595947, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 24.119226455688477, 'Value': 1.8150205612182617, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mZenithColorCurve = Namespace(ColorCurves={'Keys': [{'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.950263261795044, 'Value': 0, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': -0.4036663770675659, 'Value': 0.07818662375211716, 'ArriveTangent': 0.2919608950614929, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.2919608950614929, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.0020411014556884766, 'Value': 0.20691198110580444, 'ArriveTangent': 0.23760980367660522, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.23760980367660522, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0.10753738880157471, 'Value': 0.19965365529060364, 'ArriveTangent': -0.1025567427277565, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.10255720466375351, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0.18279790878295898, 'Value': 0.09730611741542816, 'ArriveTangent': -0.8891769647598267, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.8891769647598267, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.30361711978912354, 'Value': 0.04399999603629112, 'ArriveTangent': -0.25935783982276917, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.25935783982276917, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.47006940841674805, 'Value': 0.02279999852180481, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mCloudColorCurve = Namespace(ColorCurves={'Keys': [{'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.7888109087944031, 'Value': 0.0539499968290329, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.48361289501190186, 'Value': 0.2150000035762787, 'ArriveTangent': 1.0704957246780396, 'ArriveTangentWeight': 0, 'LeaveTangent': 1.0704957246780396, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': -0.20398837327957153, 'Value': 0.6800000071525574, 'ArriveTangent': 0.8980071544647217, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.8980071544647217, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.16782963275909424, 'Value': 0.800000011920929, 'ArriveTangent': 0.29889050126075745, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.29889050126075745, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.36478185653686523, 'Value': 0.8500000238418579, 'ArriveTangent': 0.21860714256763458, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.21860714256763458, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0.8131626844406128, 'Value': 0.9410744309425354, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mCloudOpacity = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 1.2000000476837158}, ExternalCurve={'$Empty': True})
    mStarBrightness = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 0.20000000298023224}, ExternalCurve={'$Empty': True})
    mSkyLightColor = Namespace(ColorCurves={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 1}, ExternalCurve={'$Empty': True})
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0.25, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def SetLightAsDominant(self, Light: Ptr[DirectionalLight], newDominant: bool):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(Light)
        if not ReturnValue:
            goto('L129')
        # Label 65
        Light.LightComponent.SetVisibility(newDominant, False)
    

    def NewDominantLight(self, oldDominantLight: Ptr[DirectionalLight], NewDominantLight: Ptr[DirectionalLight]):
        ExecutionFlow.Push("L205")
        ExecutionFlow.Push("L65")
        ExecutionFlow.Push("L40")
        # Label 15
        self.SetLightAsDominant(oldDominantLight, False)
        goto(ExecutionFlow.Pop())
        # Label 40
        self.SetLightAsDominant(NewDominantLight, True)
        goto(ExecutionFlow.Pop())
        # Label 65
        self.mDominantLight = NewDominantLight
        ReturnValue: bool = EqualEqual_ObjectObject(self.mDominantLight, self.mSunLight)
        ReturnValue_0: float = SelectFloat(self.mSunRadius, self.mMoonRadius, ReturnValue)
        self.mDiscRadius = ReturnValue_0
        goto(ExecutionFlow.Pop())
    

    def CalculateDominantLight(self):
        ReturnValue: bool = GreaterEqual_FloatFloat(self.mSunLight.LightComponent.Intensity, self.mMoonLight.LightComponent.Intensity)
        Variable: bool = ReturnValue
        
        switch = {
            False: self.mMoonLight,
            True: self.mSunLight
        }
        newDominantLight: Ptr[DirectionalLight] = switch.get(Variable, None)
        ReturnValue_0: bool = NotEqual_ObjectObject(newDominantLight, self.mDominantLight)
        if not ReturnValue_0:
            goto('L292')
        self.NewDominantLight(self.mDominantLight, newDominantLight)
    

    def CalculateDiscBrightness(self, Light: Ptr[Light], brightnessAdjustment: FBrightnessAdjustment):
        ReturnValue: bool = Light.LightComponent.Intensity > 0
        if not ReturnValue:
            goto('L265')
        ReturnValue_0: float = brightnessAdjustment.LightIntensity_5_7DFA36F84BCB1C040E5D69B250CB0137 / Light.LightComponent.Intensity
        ReturnValue_1: float = FClamp(ReturnValue_0, 0, 1)
        intensityPct: float = ReturnValue_1
        # Label 265
        ReturnValue_2: float = brightnessAdjustment.SkySphereDiscBrightness_6_E856AF074C7A0AFAA790FCA8730DAEF9 * intensityPct
        discBrightness = ReturnValue_2
    

    def CalculateBrightness(self):
        
        discBrightness = None
        self.CalculateDiscBrightness(self.mMoonLight, self.mMoonBrightnessAdjust, Ref[discBrightness])
        
        discBrightness1 = None
        self.CalculateDiscBrightness(self.mSunLight, self.mSunBrightnessAdjust, Ref[discBrightness1])
        ReturnValue: bool = EqualEqual_ObjectObject(self.mDominantLight, self.mSunLight)
        Variable: bool = ReturnValue
        
        switch = {
            False: discBrightness,
            True: discBrightness1
        }
        # Label 139
        Brightness = switch.get(Variable, None)
    

    def CalculateLightRotation(self, OriginalRotation: Rotator, RotationAxis: Rotator, LightRotationCurve: RuntimeFloatCurve):
        ReturnValue: Vector = GetForwardVector(RotationAxis)
        ReturnValue_0: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_1: Vector = LessLess_VectorRotator(ReturnValue, OriginalRotation)
        ReturnValue_2: float = ReturnValue_0.GetTimeOfDayHours()
        
        ReturnValue_3: Rotator = MakeRotFromX(Ref[ReturnValue_1])
        
        ReturnValue_4: float = self.GetFloatCurveValue(ReturnValue_2, Ref[LightRotationCurve])
        ReturnValue_5: float = ReturnValue_4 * -1
        ReturnValue_6: Rotator = MakeRotator(0, ReturnValue_5, 0)
        ReturnValue_7: Rotator = ComposeRotators(ReturnValue_3, ReturnValue_6)
        ReturnValue1: Vector = GetForwardVector(ReturnValue_7)
        ReturnValue_8: Vector = GreaterGreater_VectorRotator(ReturnValue1, OriginalRotation)
        
        ReturnValue1_0: Rotator = MakeRotFromX(Ref[ReturnValue_8])
        NewRotation = ReturnValue1_0
    

    def UpdateGlobalParameters(self):
        ReturnValue: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_0: float = ReturnValue.GetDayPct()
        Default__KismetMaterialLibrary.SetScalarParameterValue(self, MPC_Globals, "DayPct", ReturnValue_0)
        ReturnValue = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_1: float = ReturnValue.GetNightPct()
        Default__KismetMaterialLibrary.SetScalarParameterValue(self, MPC_Globals, "NightPct", ReturnValue_1)
        ReturnValue_2: Rotator = self.mDominantLight.K2_GetActorRotation()
        ReturnValue_3: Vector = Conv_RotatorToVector(ReturnValue_2)
        ReturnValue_4: LinearColor = Conv_VectorToLinearColor(ReturnValue_3)
        
        Default__KismetMaterialLibrary.SetVectorParameterValue(self, MPC_Globals, "LightVector", Ref[ReturnValue_4])
        ReturnValue_5: LinearColor = self.mDominantLight.LightComponent.GetLightColor()
        
        Default__KismetMaterialLibrary.SetVectorParameterValue(self, MPC_Globals, "LightColor", Ref[ReturnValue_5])
    

    def UpdateCurvesFromTime(self):
        ExecutionFlow.Push("L1920")
        timeOfDay: float = 12
        ReturnValue: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_0: float = ReturnValue.GetTimeOfDayHours()
        timeOfDay = ReturnValue_0
        ExecutionFlow.Push("L1641")
        ExecutionFlow.Push("L1470")
        ExecutionFlow.Push("L1224")
        ExecutionFlow.Push("L518")
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        Component1: Ptr[DirectionalLightComponent] = Cast[DirectionalLightComponent](self.mSunLight.LightComponent)
        bSuccess1: bool = Component1
        if not bSuccess1:
            goto('L417')
        
        self.mSunLightShaftOcclusionCurve = None
        ReturnValue2: float = self.GetFloatCurveValue(timeOfDay, Ref[self.mSunLightShaftOcclusionCurve])
        Component1.SetOcclusionMaskDarkness(ReturnValue2)
        
        # Label 417
        ReturnValue5: float = self.GetFloatCurveValue(timeOfDay, Ref[self.mStarBrightness])
        self.mSkyMaterial.SetScalarParameterValue("Stars brightness", ReturnValue5)
        goto(ExecutionFlow.Pop())
        # Label 518
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mSkyLight)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue1_0: float = ReturnValue1.GetTimeOfDayHours()
        
        ReturnValue4_0: float = self.GetFloatCurveValue(ReturnValue1_0, Ref[self.mSkyLightIntensity])
        self.mSkyLight.LightComponent.SetIntensity(ReturnValue4_0)
        ReturnValue1 = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue1_0 = ReturnValue1.GetTimeOfDayHours()
        
        ReturnValue1_1: LinearColor = self.GetColorCurveValue(ReturnValue1_0, Ref[self.mSkyLightColor])
        self.mSkyLight.LightComponent.SetLightColor(ReturnValue1_1)
        ReturnValue1 = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue1_0 = ReturnValue1.GetTimeOfDayHours()
        
        ReturnValue_1: LinearColor = self.GetColorCurveValue(ReturnValue1_0, Ref[self.mOcclusionTintColor])
        ReturnValue_2: Color = Conv_LinearColorToColor(ReturnValue_1, True)
        
        self.mSkyLight.LightComponent.SetOcclusionTint(Ref[ReturnValue_2])
        goto(ExecutionFlow.Pop())
        # Label 1224
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mMoonLight)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        Component: Ptr[DirectionalLightComponent] = Cast[DirectionalLightComponent](self.mMoonLight.LightComponent)
        bSuccess: bool = Component
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        self.mMoonLightShaftOcclusionCurve = None
        ReturnValue1_2: float = self.GetFloatCurveValue(timeOfDay, Ref[self.mMoonLightShaftOcclusionCurve])
        Component.SetOcclusionMaskDarkness(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        # Label 1470
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValid(self.mAtmosphericFog)
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        
        self.mSunFogMultiplier = None
        ReturnValue3_0: float = self.GetFloatCurveValue(timeOfDay, Ref[self.mSunFogMultiplier])
        self.mAtmosphericFog.AtmosphericFogComponent.SetSunMultiplier(ReturnValue3_0)
        goto(ExecutionFlow.Pop())
        # Label 1641
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mGlobalPostProcess)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_4: float = self.GetFloatCurveValue(timeOfDay, Ref[self.Cubemap_Curve])
        self.mGlobalPostProcess.Settings.AmbientCubemapIntensity = ReturnValue_4
        self.mGlobalPostProcess.Settings.bOverride_AmbientCubemapIntensity = True
        self.mGlobalPostProcess.Settings = self.mGlobalPostProcess.Settings
        goto(ExecutionFlow.Pop())
    

    def UpdateLightRotation(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        if not ReturnValue1:
            goto('L334')
        
        NewRotation1 = None
        # Label 65
        self.CalculateLightRotation(self.mOriginSunRotation, self.mSunRotationAxis, self.mSunRotationPitch, Ref[NewRotation1])
        ReturnValue1_0: bool = self.mSunLight.K2_SetActorRotation(NewRotation1, False)
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mMoonLight)
        if not ReturnValue:
            goto('L334')
        
        NewRotation = None
        self.CalculateLightRotation(self.mOriginMoonRotation, self.mMoonRotationAxis, self.mMoonRotationPitch, Ref[NewRotation])
        ReturnValue_0: bool = self.mMoonLight.K2_SetActorRotation(NewRotation, False)
    

    def UpdateMaterialParameters(self):
        ReturnValue: Rotator = self.mSunLight.K2_GetActorRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_0: float = MapRangeUnclamped(Pitch, 0, -60, 0, 1)
        self.mSunHeight = ReturnValue_0
        
        brightness = None
        self.CalculateBrightness(Ref[brightness])
        self.mSkyMaterial.SetScalarParameterValue("SunAndMoonBrightness", brightness)
        self.mSkyMaterial.SetScalarParameterValue("SunAndMoonBrightness", brightness)
        self.mSkyMaterial.SetScalarParameterValue("SunAndMoonRadius", self.mDiscRadius)
        ReturnValue1: float = Abs(self.mSunHeight)
        ReturnValue_1: float = Lerp(3, 8, ReturnValue1)
        self.mSkyMaterial.SetScalarParameterValue("Horizon Falloff", ReturnValue_1)
        ReturnValue_2: bool = self.mSunHeight <= 0.5
        ReturnValue_3: float = Abs(self.mSunHeight)
        ReturnValue_4: float = SelectFloat(ReturnValue_3, 0, ReturnValue_2)
        self.mSkyMaterial.SetScalarParameterValue("Sun height", ReturnValue_4)
    

    def UserConstructionScript(self):
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.Sky_Sphere_mesh.CreateDynamicMaterialInstance(0, SkyScape_Inst, "None")
        self.mSkyMaterial = ReturnValue
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mMoonLight)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue1
        ReturnValue_2: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        ReturnValue1_0: bool = ReturnValue_1 and ReturnValue2
        if not ReturnValue1_0:
            goto('L392')
        self.UpdatePreview()
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_Sky_Sphere.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Sky_Sphere(947)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Sky_Sphere(210)
    

    def UpdatePreview(self):
        self.ExecuteUbergraph_BP_Sky_Sphere(139)
    

    def ApplySkySphereSettings(self):
        ExecuteUbergraph_BP_Sky_Sphere.K2Node_Event_settings = Settings #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Sky_Sphere(215)
    

    def ExecuteUbergraph_BP_Sky_Sphere(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ReceiveBeginPlay()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue: bool = self.mSunLight.K2_SetActorRotation(self.mOriginSunRotation, False)
        goto(ExecutionFlow.Pop())
        # Label 139
        self.UpdateLightRotation()
        self.UpdateCurvesFromTime()
        self.CalculateDominantLight()
        self.UpdateMaterialParameters()
        self.UpdateGlobalParameters()
        goto(ExecutionFlow.Pop())
        goto('L15')
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mSkyMaterial)
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        self.mSkyMaterial.SetVectorParameterValue("Horizon color", settings.HorizonColor)
        self.mSkyMaterial.SetVectorParameterValue("Zenith Color", settings.ZenithColor)
        self.mSkyMaterial.SetVectorParameterValue("Cloud_Color", settings.CloudColor)
        self.mSkyMaterial.SetScalarParameterValue("Cloudiness", settings.CloudOpacity)
        ExecutionFlow.Push("L740")
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        self.mSunLight.LightComponent.SetLightColor(settings.SunLightColor, True)
        self.mSunLight.LightComponent.SetIntensity(settings.SunIntensity)
        goto(ExecutionFlow.Pop())
        # Label 740
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.mMoonLight)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        self.mMoonLight.LightComponent.SetLightColor(settings.MoonLightColor, True)
        self.mMoonLight.LightComponent.SetIntensity(settings.MoonIntensity)
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mSunLight)
        ReturnValue_1: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        ReturnValue6: bool = Default__KismetSystemLibrary.IsValid(self.mMoonLight)
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue6
        ReturnValue1_0: bool = ReturnValue_2 and ReturnValue5
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        goto('L139')
    
