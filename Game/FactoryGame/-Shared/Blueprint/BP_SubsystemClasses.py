
from codegen.ue4_stub import *

from Script.FactoryGame import FGSubsystemClasses

class BP_SubsystemClasses(FGSubsystemClasses):
    mStorySubsystemClass = NewObject[BP_StorySubsystem]()
    mTimeSubsystemClass = NewObject[BP_TimeOfDaySubsystem]()
    mRailroadSubsystemClass = NewObject[BP_RailroadSubsystem]()
    mCircuitSubsystemClass = NewObject[BP_CircuitSubsystem]()
    mSchematicManagerClass = NewObject[BP_SchematicManager]()
    mGamePhaseManagerClass = NewObject[BP_GamePhaseManager]()
    mResearchManagerClass = NewObject[BP_ResearchManager]()
    mTutorialIntroManagerClass = NewObject[BP_TutorialIntroManager]()
    mRadioactivitySubsystemClass = NewObject[BP_RadioactiveSubsystem]()
    mChatManagerClass = NewObject[BP_ChatManager]()
    mCentralStorageSubsystemClass = NewObject[FGCentralStorageSubsystem]()
    mMapManagerClass = NewObject[FGMapManager]()
    mBuildableSubsystemClass = NewObject[BP_BuildableSubsystem]()
    mFoliageRemovalSubsystemClass = NewObject[FGFoliageRemovalSubsystem]()
    mProximitySubsystemClass = NewObject[BP_ProximitySubsystem]()
    mUnlockSubsystem = NewObject[BP_UnlockSubsystem]()
    mResourceSinkSubsystemClass = NewObject[FGResourceSinkSubsystem]()
    mAdminInterfaceClass = NewObject[FGAdminInterface]()
    mItemRegrowSubsystemClass = NewObject[FGItemRegrowSubsystem]()
    
