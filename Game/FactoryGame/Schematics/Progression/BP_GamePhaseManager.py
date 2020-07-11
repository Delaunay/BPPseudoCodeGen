
from codegen.ue4_stub import *

from Script.FactoryGame import FGGamePhaseManager

class BP_GamePhaseManager(FGGamePhaseManager):
    mGamePhaseTierInfo = [{'gamePhase': 0, 'LastTierOfPhase': 2, 'Name': 'NSLOCTEXT("", "F8CFBECE48E1B7269F9BD2A693AF0321", "Project Assembly: Establishing")', 'PhaseUnlockedMessage': '/Game/FactoryGame/Interface/UI/Message/GameplayBeat/SpaceElevatorPhases/Widget_Establishing.Widget_Establishing_C'}, {'gamePhase': 1, 'LastTierOfPhase': 4, 'Name': 'NSLOCTEXT("", "9AFBAEDC484A278F80E69288D7D8D6D3", "Project Assembly: Platform")', 'PhaseUnlockedMessage': '/Game/FactoryGame/Interface/UI/Message/GameplayBeat/SpaceElevatorPhases/Widget_Development.Widget_Development_C'}, {'gamePhase': 2, 'LastTierOfPhase': 6, 'Name': 'NSLOCTEXT("", "E3903EF040016F06322E8BB1CE6FFE9C", "Project Assembly: Framework")', 'PhaseUnlockedMessage': '/Game/FactoryGame/Interface/UI/Message/GameplayBeat/SpaceElevatorPhases/Widget_Expansion.Widget_Expansion_C'}, {'gamePhase': 3, 'LastTierOfPhase': 8, 'Name': 'NSLOCTEXT("", "B3C3889B4335F59B5FAEB7A94008B112", "Project Assembly: Systems")', 'PhaseUnlockedMessage': '/Game/FactoryGame/Interface/UI/Message/GameplayBeat/SpaceElevatorPhases/Widget_Retention.Widget_Retention_C'}]
    mGamePhaseCosts = [{'gamePhase': 1, 'Cost': [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_1.Desc_SpaceElevatorPart_1_C', 'amount': 50}]}, {'gamePhase': 2, 'Cost': [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_1.Desc_SpaceElevatorPart_1_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_2.Desc_SpaceElevatorPart_2_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_3.Desc_SpaceElevatorPart_3_C', 'amount': 100}]}, {'gamePhase': 3, 'Cost': [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_2.Desc_SpaceElevatorPart_2_C', 'amount': 2500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_4.Desc_SpaceElevatorPart_4_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_5.Desc_SpaceElevatorPart_5_C', 'amount': 100}]}]
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
