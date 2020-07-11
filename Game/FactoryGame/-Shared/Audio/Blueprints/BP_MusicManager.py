
from codegen.ue4_stub import *

from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import ExecuteUbergraph_BP_MusicManager.K2Node_Event_worldSettings
from Script.Engine import GetClassDisplayName
from Script.Engine import Default__KismetSystemLibrary
from Script.AkAudio import SetSwitch
from Script.Engine import SelectFloat
from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import ExecuteUbergraph_BP_MusicManager.K2Node_Event_mapArea
from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import ExecuteUbergraph_BP_MusicManager.K2Node_Event_isNear
from Script.FactoryGame import GetZoneType
from Game.FactoryGame.-Shared.Audio.Music.Stop_Menu_Music import Stop_Menu_Music
from Script.FactoryGame import GetLevelStartedAkEvent
from Script.AkAudio import AkAudioEvent
from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import ExecuteUbergraph_BP_MusicManager
from Script.AkAudio import PostEvent
from Script.FactoryGame import Default__FGMapArea
from Game.FactoryGame.-Shared.Audio.Blueprints.BP_MusicManager import ExecuteUbergraph_BP_MusicManager.K2Node_Event_loadedWorld
from Game.FactoryGame.-Shared.Audio.Music.JannikReuterberg.Stop_Music import Stop_Music
from Script.AkAudio import SetRTPCValue
from Script.FactoryGame import FGWorldSettings
from Script.FactoryGame import FGMusicManager
from Script.FactoryGame import FGMapAreaZoneDescriptor

class BP_MusicManager(FGMusicManager):
    mUpdateInterval = 60
    mFactoryCloseDistance = 15000
    mMusicManagerClassName = Namespace(AssetPathName='/Game/FactoryGame/-Shared/Audio/Blueprints/BP_MusicManager.BP_MusicManager_C', SubPathString='')
    
    def Play(self):
        self.ExecuteUbergraph_BP_MusicManager(239)
    

    def Pause(self):
        self.ExecuteUbergraph_BP_MusicManager(244)
    

    def Stop(self):
        self.ExecuteUbergraph_BP_MusicManager(249)
    

    def NotifyPostLoadMap(self):
        ExecuteUbergraph_BP_MusicManager.K2Node_Event_loadedWorld = loadedWorld #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_MusicManager.K2Node_Event_worldSettings = WorldSettings #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MusicManager(372)
    

    def OnPlayerEnteredArea(self):
        ExecuteUbergraph_BP_MusicManager.K2Node_Event_mapArea = mapArea #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MusicManager(456)
    

    def OnPlayerNearBaseChanged(self):
        ExecuteUbergraph_BP_MusicManager.K2Node_Event_isNear = isNear #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MusicManager(621)
    

    def ExecuteUbergraph_BP_MusicManager(self):
        # Label 10
        ReturnValue: int32 = self.mAkObject.PostEvent(Stop_Menu_Music)
        ReturnValue_0: Ptr[AkAudioEvent] = Settings.GetLevelStartedAkEvent()
        ReturnValue4: int32 = self.mAkObject.PostEvent(ReturnValue_0)
        # End
        # Label 175
        ReturnValue1: int32 = self.mAkObject.PostEvent(Stop_Music)
        goto('L10')
        # End
        # End
        ReturnValue2: int32 = self.mAkObject.PostEvent(Stop_Music)
        ReturnValue3: int32 = self.mAkObject.PostEvent(Stop_Menu_Music)
        # End
        Settings: Ptr[FGWorldSettings] = Cast[FGWorldSettings](worldSettings)
        bSuccess: bool = Settings
        if not bSuccess:
            goto('L730')
        goto('L175')
        ReturnValue_1: TSubclassOf[FGMapAreaZoneDescriptor] = Default__FGMapArea.GetZoneType(mapArea)
        ReturnValue_2: FString = Default__KismetSystemLibrary.GetClassDisplayName(ReturnValue_1)
        self.mAkObject.SetSwitch("MapZone", ReturnValue_2)
        # End
        ReturnValue_3: float = SelectFloat(1, 0, isNear)
        self.mAkObject.SetRTPCValue("IsPlayerInBase", ReturnValue_3, 0)
    
