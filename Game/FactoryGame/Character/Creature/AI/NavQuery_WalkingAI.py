
from codegen.ue4_stub import *

from Script.NavigationSystem import NavigationQueryFilter

class NavQuery_WalkingAI(NavigationQueryFilter):
    Areas = [{'AreaClass': '/Script/NavigationSystem.NavArea_Null', 'TravelCostOverride': 1, 'EnteringCostOverride': 0, 'bIsExcluded': True, 'bOverrideTravelCost': False, 'bOverrideEnteringCost': False}, {'AreaClass': '/Script/NavigationSystem.NavArea_Default', 'TravelCostOverride': 1, 'EnteringCostOverride': 0, 'bIsExcluded': False, 'bOverrideTravelCost': False, 'bOverrideEnteringCost': False}, {'AreaClass': '/Script/FactoryGame.FGNavArea_Water', 'TravelCostOverride': 1, 'EnteringCostOverride': 0, 'bIsExcluded': True, 'bOverrideTravelCost': False, 'bOverrideEnteringCost': False}]
    
