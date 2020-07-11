
from codegen.ue4_stub import *

from Script.FactoryGame import FGPipelineHologram

class Holo_PipeHyper(FGPipelineHologram):
    mDefaultPipelineSupportRecipe = NewObject[Recipe_PipeHyperSupport]()
    mBendRadius = 300
    mBendRadius2D = 199
    mMinBendRadius = 75
    mMaxLength = 100
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='mSplineComponent', SplineCurves={'Position': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Rotation': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Scale': {'Points': [], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'ReparamTable': {'Points': [{'InVal': 0, 'OutVal': -1, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}], 'bIsLooped': False, 'LoopKeyOffset': 0}})
    mSplineData = [{'Location': {'X': 0, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 1, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 1, 'Y': 0, 'Z': 0}}, {'Location': {'X': 0, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 1, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 1, 'Y': 0, 'Z': 0}}]
    mMaxPlacementFloorAngle = 35
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad', '/Script/FactoryGame.FGBuildable']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
