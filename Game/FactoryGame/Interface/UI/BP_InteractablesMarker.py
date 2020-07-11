
from codegen.ue4_stub import *

from Script.FactoryGame import FGInteractableMarker

class BP_InteractablesMarker(FGInteractableMarker):
    mIconWidget = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, DrawSize={'X': 64, 'Y': 64}, ObjectClass='/Script/UMG.WidgetComponent', ObjectFlags=2883617, ObjectName='Icon', RelativeLocation={'X': 0, 'Y': 0, 'Z': 100}, Space='EWidgetSpace::Screen', WidgetClass='/Game/FactoryGame/Interface/UI/InGame/Widget_WorldInteractable.Widget_WorldInteractable_C')
    mSplineMesh = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, Mobility=2, ObjectClass='/Script/Engine.SplineMeshComponent', ObjectFlags=2883617, ObjectName='SplineMesh', OverrideMaterials=[{'$AssetPath': '/Game/FactoryGame/Interface/UI/Material/MarkerLine.MarkerLine'}], RelativeScale3D={'X': 1, 'Y': 0.05000000074505806, 'Z': 1}, SplineParams={'StartPos': {'X': 0, 'Y': 0, 'Z': 0}, 'StartTangent': {'X': 100, 'Y': 0, 'Z': 0}, 'StartScale': {'X': 1, 'Y': 1}, 'StartRoll': 0, 'StartOffset': {'X': 0, 'Y': 0}, 'EndPos': {'X': 0, 'Y': 0, 'Z': 100}, 'EndTangent': {'X': 100, 'Y': 0, 'Z': 0}, 'EndScale': {'X': 1, 'Y': 1}, 'EndRoll': 0, 'EndOffset': {'X': 0, 'Y': 0}}, StaticMesh={'$AssetPath': '/Engine/BasicShapes/Plane.Plane'})
    mDesiredScreenRadius = 0.07999999821186066
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
