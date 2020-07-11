
from codegen.ue4_stub import *

from Script.FactoryGame import FGPipelineHologram
from Script.FactoryGame import EHologramSplinePathMode

class Holo_Pipeline(FGPipelineHologram):
    mSupportedSplineModes: List[uint8] = ['EHologramSplinePathMode::HSPM_AUTO', 'EHologramSplinePathMode::HSPM_AUTO_2D', 'EHologramSplinePathMode::HSPM_HORZ_TO_VERT']
    mDefaultPipelineSupportRecipe = NewObject[Recipe_PipeSupport]()
    mBendRadius = 100
    mBendRadius2D = 199
    mMinBendRadius = 75
    mMaxLength = 50
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='mSplineComponent', SplineCurves={'Position': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Rotation': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Scale': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'ReparamTable': {'Points': [{'InVal': 0, 'OutVal': -1, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}], 'bIsLooped': False, 'LoopKeyOffset': 0}})
    mSplineData = [{'Location': {'X': 0, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 1, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 1, 'Y': 0, 'Z': 0}}, {'Location': {'X': 0, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 1, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 1, 'Y': 0, 'Z': 0}}]
    mMaxPlacementFloorAngle = 35
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad', '/Script/FactoryGame.FGBuildable']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetSupportedSplineModes(self):
        splineModes: List[uint8] = self.mSupportedSplineModes
    
