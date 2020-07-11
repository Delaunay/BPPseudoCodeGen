
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import OnCameraExitedWater
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Swim.Stop_P_Swim_UnderWater import Stop_P_Swim_UnderWater
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Swim.Play_P_Swim_UnderWater import Play_P_Swim_UnderWater
from Script.Engine import Pawn
from Script.FactoryGame import OnCameraEnteredWater
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Swim.Play_P_Swim_Water_Exit_Heavy import Play_P_Swim_Water_Exit_Heavy
from Script.FactoryGame import FGWaterAudio
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Swim.Play_P_Swim_Water_Impact_Heavy import Play_P_Swim_Water_Impact_Heavy

class FGWaterAudio(FGWaterAudio):
    mString: FString = Camera Exited:
    mImpactAudioMap = [{'MinImpactVelocity': 4000, 'ImpactEvent': {'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Swim/Play_P_Swim_Water_Impact_Light.Play_P_Swim_Water_Impact_Light'}}, {'MinImpactVelocity': 100000000, 'ImpactEvent': {'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Swim/Play_P_Swim_Water_Impact_Medium.Play_P_Swim_Water_Impact_Medium'}}, {'MinImpactVelocity': 9999999827968, 'ImpactEvent': {'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Swim/Play_P_Swim_Water_Impact_Heavy.Play_P_Swim_Water_Impact_Heavy'}}]
    
    def OnCameraExitedWater(self):
        self.OnCameraExitedWater(waterVolume, exitLocation, PC)
        ReturnValue: Ptr[Pawn] = PC.K2_GetPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_P_Swim_UnderWater, ReturnValue, True)
        ReturnValue = PC.K2_GetPawn()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_Swim_Water_Exit_Heavy, ReturnValue, True)
    

    def OnCameraEnteredWater(self):
        self.OnCameraEnteredWater(waterVolume, enterLocation, PC)
        ReturnValue: Ptr[Pawn] = PC.K2_GetPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_Swim_UnderWater, ReturnValue, True)
        ReturnValue = PC.K2_GetPawn()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_Swim_Water_Impact_Heavy, ReturnValue, True)
    
