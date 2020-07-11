
from codegen.ue4_stub import *

from Script.UMG import RemoveChildAt
from Script.Engine import Conv_TextToString
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import HorizontalBoxSlot
from Script.UMG import GetChildrenCount
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.Engine import Conv_IntToFloat
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedText import Widget_LetterSpacedText
from Script.Engine import LatentActionInfo
from Script.SlateCore import FontOutlineSettings
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import SetStringPropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import SetStructurePropertyByName
from Script.UMG import SetRenderTranslation
from Script.UMG import SetRenderScale
from Script.Engine import TimerHandle
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import SetFloatPropertyByName
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import SlotAsHorizontalBoxSlot
from Script.Engine import BreakVector2D
from Script.UMG import Widget
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.InGame.Widget_Respawn import ExecuteUbergraph_Widget_Respawn
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import Conv_IntToString
from Script.Engine import RandomInteger
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.UMG import SetRenderOpacity
from Script.Engine import Concat_StrStr
from Game.FactoryGame.Interface.Font.DescriptionText import DescriptionText
from Script.Engine import RandomFloatInRange

class Widget_Respawn(UserWidget):
    LoadingBar: Ptr[WidgetAnimation]
    mRespawnMessages: List[FText] = ['NSLOCTEXT("", "A0F4C69A4A6BC8D7B2805CA5F2DF5E76", "Loading bar...")', 'NSLOCTEXT("", "A99CE3664375CF0DF871D8B0F3712785", "Warming up quantum mechanics...")', 'NSLOCTEXT("", "4F96C7E243F23AAF933AE4B427CD56A5", "Deactivating subject sensation and cognition...")', 'NSLOCTEXT("", "67652E6A437CF558A8AB11A1BF9D9FEB", "Vacuuming the vacuum...")', 'NSLOCTEXT("", "F247E683455218B457D0EC8B97CC417A", "Making the macroscopic microscopic...")', 'NSLOCTEXT("", "F79836564205D50BEE31F59300F91364", "Entering the future...")', 'NSLOCTEXT("", "47D1CD944595B957B6C214B95A1A1E4B", "Filing reports...")', 'NSLOCTEXT("", "187C58DA408E4602D9C6A5B4CD90265D", "Amending liability fees...")', 'NSLOCTEXT("", "EE1DEC754E2057EE6476C4A120AE05B9", "Revoking holidays...")', 'NSLOCTEXT("", "8C2EA26A4E9936C10D7544AA62A03D86", "Checking promotional list placement...")', 'NSLOCTEXT("", "354F630B485A65B955CCF0B7AB2EC980", "Avoiding relatives...")', 'NSLOCTEXT("", "650A38D241C12F9A23346681D2189440", "Compensating for spatial and temporal drift...")', 'NSLOCTEXT("", "75A2553B49CFEC6F218CD1A7E23006E3", "Guesstimating previous physical state...")', 'NSLOCTEXT("", "D40EEB774E7E85BAB99BF59CBF035FA6", "Turning it off and on again...")', 'NSLOCTEXT("", "297E8CED4FC05B7A97B777869ABDAF70", "Scanning biomatter state...")', 'NSLOCTEXT("", "A399685249E5E88CDB91CB8DA559AB46", "Destroying quantum-based viruses...")', 'NSLOCTEXT("", "0745E9D041E223BBAB9EDEAB0A749509", "Removing aggressive alien matter...")', 'NSLOCTEXT("", "CCBD117F4F0307A4C4ED7C8C0BDF9A68", "Reconstructing deficient organs...")', 'NSLOCTEXT("", "495FD19A49232758715148ADBFC2CF64", "Applying duct tape...")', 'NSLOCTEXT("", "1820C45E450468554C33A581E6E68857", "Cleaning toilet...")', 'NSLOCTEXT("", "11D9EDF9433CCE982FA981B07A0EEA52", "Optimizing indoctrination...")', 'NSLOCTEXT("", "7E338EC04B1A627E9D5D54AFE416A0F5", "Booting five out of eight senses...")', 'NSLOCTEXT("", "4CF7512C45DA92D3001F7E8F60DE6D0D", "Distributing endorphins...")', 'NSLOCTEXT("", "FDB0F52F4B485FC2674AC387A87BBCB2", "You’re going to be...")', 'NSLOCTEXT("", "0BE16D1844A207FB28A786AE7715E9BA", "Initiating redeployment...")', 'NSLOCTEXT("", "C42B135D4DB09CB5F735138A23400E2F", "Reducing difficulty…")', 'NSLOCTEXT("", "CCE048114586D445E0549299575FE26B", "Firing therapist...")', 'NSLOCTEXT("", "E6CA09654F15564F7250069391DDAFD1", "Hiring therapist…")', 'NSLOCTEXT("", "A60DF49E48D11E45B306CDA6FB54821C", "Living on the edge…")', 'NSLOCTEXT("", "ED2A03604AA3EA4D090102A237A54A93", "Reconsidering employment…")', 'NSLOCTEXT("", "962FA9AF4CD23BB8ABD21B9389099010", "Reading the small print…")', 'NSLOCTEXT("", "7FA310D7450277B5BC0D33A87AD5391D", "Predicting chance of future accidents…")', 'NSLOCTEXT("", "8EF2E89B4A005AA2E493379F46CA59C9", "Playing Elevator_Track_4.mp3...")', 'NSLOCTEXT("", "9095396B454686A44A282895A1B047C5", "Ditching non-organic matter…")', 'NSLOCTEXT("", "C184EE78474D5C0D635CC3812368F3DC", "Questioning existence...")', 'NSLOCTEXT("", "521DBE824F1D1C40514D4588E7282D1F", "Learning from mistakes...")', 'NSLOCTEXT("", "9CDB857D4871CCC8A4BDEFB61D13F784", "Washing brain...")', 'NSLOCTEXT("", "16E4A0DE4F6BCFE67DB8C79DED784541", "Stealing keys...")', 'NSLOCTEXT("", "E92D42C64525167CDFCA2587B44288B1", "Spawning aliens...")', 'NSLOCTEXT("", "FFFDF4704E55CBE094A29D99D8865901", "Blaming Simon...")', 'NSLOCTEXT("", "F720186A4547C995BB2A50B795214D92", "Adding microtransactions...")', 'NSLOCTEXT("", "8A7209B241FB06E39B82CA8B025EC054", "Spilling coffee...")', 'NSLOCTEXT("", "34CF86284464DC9DEBAA248E38B4BE8C", "Removing dad jokes...")', 'NSLOCTEXT("", "7AB762A746A4B7B133B315AEECC60E13", "Altering genetics...")', 'NSLOCTEXT("", "3E3B8BCE405891EF5E2CA08E7E1A77CC", "Skipping stones...")', 'NSLOCTEXT("", "C3A74674429462B43F9AE1B9FB35ADBB", "Overthrowing the government...")', 'NSLOCTEXT("", "C173D8FC4F5EDF9788187D997DC159AF", "Rolling dice...")', 'NSLOCTEXT("", "D8D64012473C89FF80CEACAE52F51ADA", "Saving the world...")', 'NSLOCTEXT("", "B24F3B044FDAFF6C422056AEECC796A9", "Advancing science...")', 'NSLOCTEXT("", "A5F5D1AD447E42E1DFEB5F912036FB6C", "Rousing Big Brother...")']
    mProgressBarUpdate: TimerHandle
    mMessageInt: int32
    MaxMessages: int32 = 6
    MessageFadeLength: int32 = 4
    mTipMessages: List[FText] = ['NSLOCTEXT("", "3BD0D3A248B4070E40CBD8A9245FA2BD", "Don’t die.")', 'NSLOCTEXT("", "84B3BC5143837A3BC297D18DB4C29D86", "Back to work, and Stay Effective.")', 'NSLOCTEXT("", "8603EF0243845CAD1C60169CBDC83ECB", "Are you feeling stuck? Are you lost? Is the entire world against you? Inform ADA so we can replace your brain’s reward center!")', 'NSLOCTEXT("", "01E3DDFF4C4D39DE737FE69055C6BAE3", "Bored of the standard orange and grey factories? Try out our FICSIT-approved color gun! No fun, without a gun!")', 'NSLOCTEXT("", "DF85BD2D4F74A7E13BC51D8A0D4886B1", "Getting killed a lot? Try bringing a weapon next time, or medkits, or, you know, stop doing whatever you’re doing.")', 'NSLOCTEXT("", "211B3FBC4569E5B550E12FAC2DC6B760", "Be nice to Steve, he’s under a lot of pressure.")', 'NSLOCTEXT("", "4E36313444D1C9DC34A30F97E47DFBA3", "We own you.")', 'NSLOCTEXT("", "7845D6B74F92161A6BD27FAEA4D7046E", "Don’t worry, be happy.")', 'NSLOCTEXT("", "B332729D42BF625DE63F06B523BE0956", "ADA is always watching.")', 'NSLOCTEXT("", "AC791BC14110C1275E21F0AFA56A8C6E", "Who am I to tell you what to do?")', 'NSLOCTEXT("", "CEF77FD941EE84F05023D0A0533B03C7", "Am I real?")', 'NSLOCTEXT("", "BE30367F47D0B651078A729DFDE0FEF5", "One of these is not like the others.")', 'NSLOCTEXT("", "91CE17F04EAE2EB41F8F9B9457C222EB", "Your fun is wrong.")', 'NSLOCTEXT("", "921B26134F6039C2DD177D8D3E2F8983", "Life needs things to live.")', 'NSLOCTEXT("", "9E078F184F46D526BE11AAB472FAD165", "Is it Thursday yet?")', 'NSLOCTEXT("", "C3B488C14F8BB999FE2DABB40E2E770A", "Are you real?")', 'NSLOCTEXT("", "D5B7E292492C6C885EB4F48812C7D99F", "[REDACTED]")', 'NSLOCTEXT("", "01E292DE41CE25D7BC3675BA4CD92F69", "Keep an eye on that power capacity.")', 'NSLOCTEXT("", "20F501FB4F63FDD946DEF99F7435A6D0", "Faster belts don’t necessarily mean faster production.")', 'NSLOCTEXT("", "0CD518D04F8BF08F1821B38AB2B6EC9A", "Whoever reads this is a poo-poo head.")', 'NSLOCTEXT("", "01811D604D030B424822C5BEE6389DD2", "You are appreciated.")', 'NSLOCTEXT("", "098C61C54E0C2FF7B137A294F9ADB974", "Look behind you.")', 'NSLOCTEXT("", "229C62364803B02970941FB09DE2EFF7", "So, uh, wanna go out sometime?")', 'NSLOCTEXT("", "93D7BD52472C7712DC247E95460D8C3F", "Wait is this supposed to be useful or something?")', 'NSLOCTEXT("", "4307C02E4329A54E3E8277A919896116", "<3")', 'NSLOCTEXT("", "2EF1DE874713D154FBC1A28CA725943C", "Level up! Ha, kidding! We don’t even have levels.")', 'NSLOCTEXT("", "6742E51C4550710C02716E9F3FDAAA73", "Can’t stop, won’t stop!")', 'NSLOCTEXT("", "4C5B1F0946C14A1D1DB92FABD817FE8B", "Now we have to load the game for you, all over again.")', 'NSLOCTEXT("", "4535FFF84A65382B7B43EF8672A3178C", "If you’re afraid of spiders, we got your back. Enable Arachnophobia mode in the options menu. Get it? Arach-NO-phobia?")', 'NSLOCTEXT("", "E892420E43163CF3E36BEB8704597C17", "Sometimes all you need is a potato.")', 'NSLOCTEXT("", "DFFF4B19465A76EF2F128DA5D3029E7A", "I had a lot of fun writing these.")', 'NSLOCTEXT("", "2CD0D5CB4D2832A3229A90B02D229021", "BRB")', 'NSLOCTEXT("", "734E02D3472291CD2678598CB86A7D20", "Congratulations! You made it to the loading screen.")', 'NSLOCTEXT("", "D7CDED0D44769AC382CD4F838BF472D8", "Dear diary, ")', 'NSLOCTEXT("", "63AA463C4ECC974B293369B04C52F6AB", "Happy birthday!")', 'NSLOCTEXT("", "104D5B224C1F4743AB41F8B638C9EE58", "I’d love to stay and chat, but…")', 'NSLOCTEXT("", "B9B60438453E6738F588E1B28B620549", "The key is a lie.")', 'NSLOCTEXT("", "D667D2674464F8EAA25C2C91BB64774E", "GG EZ")', 'NSLOCTEXT("", "B2AE78C54EA6B155D0E1E2B9324E655D", "Catch phrase!")', 'NSLOCTEXT("", "67153B214F4EDAEE73D459A349511481", "Rude.")', 'NSLOCTEXT("", "236CB45E49250A51EE5527859486B078", "Come here often?")', 'NSLOCTEXT("", "CA222F324CDDA32D3ADF64B5B896D394", "Hello? Anyone there?")', 'NSLOCTEXT("", "3F9ECBC948C1E2C367C945BFB710816A", "Life + Universe + Everything.")', 'NSLOCTEXT("", "24779B29495D0CCAA4FF72BD89F2AB40", "Abort.")', 'NSLOCTEXT("", "1F176657431732F140285CA6EC570C22", "Hey, nice to see you again.")', 'NSLOCTEXT("", "58420240490C6E6ED4020C8126FBA943", "*insert lore here*")', 'NSLOCTEXT("", "2C5BCEA946817549404B86A8F4309F85", "Hope you brought a towel.")', 'NSLOCTEXT("", "28BA2C824B4D4B92A363A19B92BA651C", "This is my favourite tip in the game.")']
    mTipIndex: int32
    ProgressBarBlipWidth: float
    
    def GetRandomTip(self):
        
        ReturnValue: int32 = len(self.mTipMessages)
        ReturnValue_0: int32 = RandomInteger(ReturnValue)
        self.mTipIndex = ReturnValue_0
        
        Item = None
        Item = self.mTipMessages[self.mTipIndex]
        self.mTipText.SetText(Item)
    

    def SetTipNumber(self):
        ReturnValue: int32 = self.mTipIndex + 1
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue)
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr(self.mTipTitle.mText, ReturnValue_0)
        self.mTipTitle.SetTitle(ReturnValue_1)
    

    def UpdateProgressBlips(self):
        ReturnValue: Ptr[HorizontalBoxSlot] = Default__WidgetLayoutLibrary.SlotAsHorizontalBoxSlot(self.Image)
        
        X = None
        Y = None
        BreakVector2D(self.Image.Brush.ImageSize, Ref[X], Ref[Y])
        ReturnValue_0: float = ReturnValue.padding.Right + X
        self.ProgressBarBlipWidth = ReturnValue_0
        ReturnValue_1: int32 = self.mLoadingBar.GetChildrenCount()
        ReturnValue_2: float = ReturnValue_1 * self.ProgressBarBlipWidth
        ReturnValue_3: float = ReturnValue_2 * -1
        ReturnValue_4: Vector2D = Vector2D(ReturnValue_3, 0)
        self.mLoadingBar.SetRenderTranslation(ReturnValue_4)
        OutputDelegate.BindUFunction(self, MoveProgressbar)
        ReturnValue_5: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.3499999940395355, True)
        self.mProgressBarUpdate = ReturnValue_5
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Respawn(1038)
    

    def SpawnRespawnMessage(self):
        self.ExecuteUbergraph_Widget_Respawn(1043)
    

    def MoveProgressbar(self):
        self.ExecuteUbergraph_Widget_Respawn(2623)
    

    def ExecuteUbergraph_Widget_Respawn(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.GetRandomTip()
        self.SetTipNumber()
        self.SpawnRespawnMessage()
        self.UpdateProgressBlips()
        goto(ExecutionFlow.Pop())
        self.SpawnRespawnMessage()
        goto(ExecutionFlow.Pop())
        # Label 87
        ExecutionFlow.Push("L581")
        ReturnValue: int32 = self.mLoadingMessages.GetChildrenCount()
        ReturnValue_0: int32 = self.MaxMessages - self.MessageFadeLength
        ReturnValue1: int32 = ReturnValue - ReturnValue_0
        ReturnValue_1: float = Conv_IntToFloat(self.MessageFadeLength)
        ReturnValue_2: float = 1 / ReturnValue_1
        ReturnValue_3: Ptr[Widget] = self.mLoadingMessages.GetChildAt(Variable)
        ReturnValue3: int32 = self.MessageFadeLength - ReturnValue1
        ReturnValue1_0: int32 = ReturnValue3 + Variable
        ReturnValue1_1: float = Conv_IntToFloat(ReturnValue1_0)
        ReturnValue_4: float = ReturnValue1_1 * ReturnValue_2
        ReturnValue_3.SetRenderOpacity(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 581
        ReturnValue_5: int32 = Variable + 1
        Variable: int32 = ReturnValue_5
        # Label 650
        ReturnValue = self.mLoadingMessages.GetChildrenCount()
        ReturnValue_0 = self.MaxMessages - self.MessageFadeLength
        ReturnValue1 = ReturnValue - ReturnValue_0
        ReturnValue2: int32 = ReturnValue1 - 1
        ReturnValue_6: bool = Variable <= ReturnValue2
        if not ReturnValue_6:
            goto('L891')
        goto('L87')
        # Label 891
        ReturnValue_7: float = RandomFloatInRange(0.5, 3)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_7, LatentActionInfo(Linkage = 72, UUID = -626592142, ExecutionFunction = "ExecuteUbergraph_Widget_Respawn", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1010
        Variable = 0
        goto('L650')
        goto('L15')
        
        ReturnValue_8: int32 = len(self.mRespawnMessages)
        ReturnValue_9: bool = ReturnValue_8 > 0
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_8 = len(self.mRespawnMessages)
        ReturnValue_10: int32 = RandomInteger(ReturnValue_8)
        self.mMessageInt = ReturnValue_10
        ReturnValue_11: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_12: Ptr[Widget_LetterSpacedText] = Default__WidgetBlueprintLibrary.Create(self, Widget_LetterSpacedText, ReturnValue_11)
        
        Item = None
        Item = self.mRespawnMessages[self.mMessageInt]
        
        Item = None
        ReturnValue_13: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Item])
        Default__KismetSystemLibrary.SetStringPropertyByName(ReturnValue_12, "mText", ReturnValue_13)
        SlateFontInfo.FontObject = DescriptionText
        SlateFontInfo.FontMaterial = None
        SlateFontInfo.OutlineSettings = FontOutlineSettings(OutlineSize = 0, bSeparateFillAlpha = False, bApplyOutlineToDropShadows = False, OutlineMaterial = None, OutlineColor = LinearColor(R = 0, G = 0, B = 0, A = 1))
        SlateFontInfo.TypefaceFontName = "SemiBold"
        SlateFontInfo.Size = 15
        
        SlateFontInfo = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_12, "mFont", Ref[SlateFontInfo])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_12, "mLetterSpacing", 2.5)
        ReturnValue_14: Ptr[PanelSlot] = self.mLoadingMessages.AddChild(ReturnValue_12)
        ReturnValue_12.SetRenderScale(Vector2D(X = 1, Y = -1))
        
        self.mRespawnMessages.remove(self.mMessageInt)
        ReturnValue2_0: int32 = self.mLoadingMessages.GetChildrenCount()
        ReturnValue2_1: bool = ReturnValue2_0 > 1
        if not ReturnValue2_1:
            goto('L2468')
        ReturnValue3_0: int32 = self.mLoadingMessages.GetChildrenCount()
        ReturnValue4: int32 = ReturnValue3_0 - 2
        ReturnValue1_2: Ptr[Widget] = self.mLoadingMessages.GetChildAt(ReturnValue4)
        Text: Ptr[Widget_LetterSpacedText] = Cast[Widget_LetterSpacedText](ReturnValue1_2)
        bSuccess: bool = Text
        if not bSuccess:
            goto('L2468')
        ReturnValue_15: FString = Default__KismetStringLibrary.Concat_StrStr(Text.mText, " OK")
        Text.SetTitle(ReturnValue_15)
        # Label 2468
        ReturnValue1_3: int32 = self.mLoadingMessages.GetChildrenCount()
        ReturnValue1_4: bool = ReturnValue1_3 > self.MaxMessages
        if not ReturnValue1_4:
            goto('L1010')
        ExecutionFlow.Push("L2468")
        ReturnValue_16: bool = self.mLoadingMessages.RemoveChildAt(0)
        goto(ExecutionFlow.Pop())
        
        X = None
        Y = None
        BreakVector2D(self.mLoadingBar.RenderTransform.Translation, Ref[X], Ref[Y])
        ReturnValue_17: float = self.ProgressBarBlipWidth + X
        ReturnValue_18: Vector2D = Vector2D(ReturnValue_17, 0)
        self.mLoadingBar.SetRenderTranslation(ReturnValue_18)
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mLoadingBar.RenderTransform.Translation, Ref[X1], Ref[Y1])
        ReturnValue_19: float = self.mConsoleSizeBox.WidthOverride - self.ProgressBarBlipWidth
        ReturnValue_20: bool = X1 > ReturnValue_19
        if not ReturnValue_20:
           goto(ExecutionFlow.Pop())
        ReturnValue4_0: int32 = self.mLoadingBar.GetChildrenCount()
        ReturnValue_21: float = ReturnValue4_0 * self.ProgressBarBlipWidth
        ReturnValue1_5: float = ReturnValue_21 - self.ProgressBarBlipWidth
        ReturnValue1_6: float = ReturnValue1_5 * -1
        ReturnValue1_7: Vector2D = Vector2D(ReturnValue1_6, 0)
        self.mLoadingBar.SetRenderTranslation(ReturnValue1_7)
        goto(ExecutionFlow.Pop())
    
