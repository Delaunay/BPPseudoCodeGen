
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import FinishSpawningActor
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_NewsText1
from Script.Engine import Split
from Script.UMG import AsyncTaskDownloadImage
from Script.Engine import TextIsEmpty
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.UMG import SetText
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_NewsText
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed.K2Node_Event_IsDesignTime
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import GetAllActorsOfClass
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_Texture1
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_Texture
from Script.Engine import Contains
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.UMG import DownloadImage
from Script.Engine import TextToUpper
from Script.Engine import Default__GameplayStatics
from Script.Engine import Texture2DDynamic
from Script.Engine import NotEqual_IgnoreCase_TextText
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import MakeLiteralText
from Script.Engine import LaunchURL
from Script.UMG import UserWidget
from Script.Engine import MakeTransform
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import FGNewsFeedActor
from Game.FactoryGame.Interface.UI.Menu.Widget_NewsFeed import ExecuteUbergraph_Widget_NewsFeed
from Script.UMG import Default__AsyncTaskDownloadImage
from Script.Engine import Concat_StrStr
from Script.CoreUObject import Transform

class Widget_NewsFeed(UserWidget):
    OnHover: Ptr[WidgetAnimation]
    mNewsFeedActor: Ptr[FGNewsFeedActor]
    mNewsTextBody: FText
    mNewsTextHeader: FText
    mIsExpanded: bool
    FoundNewsActor: bool
    mLinkURL: FString
    mHeaderURL: FString
    
    def GetStringFromTag(self, TagName: FString, SourceString: FString):
        ReturnValue: FString = Default__KismetStringLibrary.Concat_StrStr("</", TagName)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr("<", TagName)
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue, ">")
        ReturnValue3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1, ">")
        
        LeftS = None
        RightS = None
        ReturnValue_0: bool = Default__KismetStringLibrary.Split(SourceString, ReturnValue3, 1, 0, Ref[LeftS], Ref[RightS])
        
        LeftS1 = None
        RightS1 = None
        ReturnValue1_0: bool = Default__KismetStringLibrary.Split(RightS, ReturnValue2, 1, 0, Ref[LeftS1], Ref[RightS1])
        ReturnValue4: FString = Default__KismetStringLibrary.Concat_StrStr(LeftS, RightS1)
        ReturnValue_1: bool = ReturnValue1_0 and ReturnValue_0
        Variable: bool = ReturnValue_1
        OutString = LeftS1
        
        switch = {
            False: SourceString,
            True: ReturnValue4
        }
        OutSource = switch.get(Variable, None)
        success = ReturnValue_1
    

    def GetNewsHeaderText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mNewsFeedActor)
        if not ReturnValue:
            goto('L308')
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText()
        
        self.mNewsFeedActor.mNewFeedText = None
        ReturnValue_1: bool = Default__KismetTextLibrary.NotEqual_IgnoreCase_TextText(Ref[self.mNewsFeedActor.mNewFeedText], Ref[ReturnValue_0])
        if not ReturnValue_1:
            goto('L333')
        
        Header = None
        Body = None
        self.GetHeaderAndBody(self.mNewsFeedActor.mNewFeedText, Ref[Header], Ref[Body])
        ReturnValue_2: FText = Header
        goto('L360')
        # Label 308
        ReturnValue_2 = 
        goto('L360')
        # Label 333
        ReturnValue_2 = self.mNewsTextHeader
    

    def GetHeaderAndBody(self, InText: FText):
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[InText])
        
        LeftS = None
        RightS = None
        ReturnValue_0: bool = Default__KismetStringLibrary.Split(ReturnValue, "<title>", 1, 0, Ref[LeftS], Ref[RightS])
        
        LeftS1 = None
        RightS1 = None
        ReturnValue1: bool = Default__KismetStringLibrary.Split(RightS, "</title>", 1, 0, Ref[LeftS1], Ref[RightS1])
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(LeftS1)
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr(LeftS, RightS1)
        
        ReturnValue_3: FText = Default__KismetTextLibrary.TextToUpper(Ref[ReturnValue_1])
        
        LeftS2 = None
        RightS2 = None
        ReturnValue2: bool = Default__KismetStringLibrary.Split(ReturnValue_2, "<body>", 1, 0, Ref[LeftS2], Ref[RightS2])
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_StringToText(RightS2)
        Header = ReturnValue_3
        Body = ReturnValue1_0
    

    def GetNewsBodyText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mNewsFeedActor)
        if not ReturnValue:
            goto('L308')
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText()
        
        self.mNewsFeedActor.mNewFeedText = None
        ReturnValue_1: bool = Default__KismetTextLibrary.NotEqual_IgnoreCase_TextText(Ref[self.mNewsFeedActor.mNewFeedText], Ref[ReturnValue_0])
        if not ReturnValue_1:
            goto('L333')
        
        Header = None
        Body = None
        self.GetHeaderAndBody(self.mNewsFeedActor.mNewFeedText, Ref[Header], Ref[Body])
        ReturnValue_2: FText = Body
        goto('L360')
        # Label 308
        ReturnValue_2 = 
        goto('L360')
        # Label 333
        ReturnValue_2 = self.mNewsTextBody
    

    def OnFail_74A37E23495D65D8B1428F9D6302EA77(self, Texture: Ptr[Texture2DDynamic]):
        ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_Texture1 = Texture #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NewsFeed(4054)
    

    def OnSuccess_74A37E23495D65D8B1428F9D6302EA77(self, Texture: Ptr[Texture2DDynamic]):
        ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_Texture = Texture #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NewsFeed(1357)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_NewsFeed(874)
    

    def FindNewsFeedActor(self):
        self.ExecuteUbergraph_Widget_NewsFeed(1233)
    

    def OnNewsTextReceived(self, NewsText: FText):
        ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_NewsText1 = NewsText #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NewsFeed(1238)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_NewsFeed.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NewsFeed(1352)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_NewsFeed(1423)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_NewsFeed(1470)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_NewsFeed(1517)
    

    def ParseText(self, NewsText: FText):
        ExecuteUbergraph_Widget_NewsFeed.K2Node_CustomEvent_NewsText = NewsText #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_NewsFeed(1522)
    

    def BndEvt__Widget_FrontEnd_Button_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_NewsFeed(4012)
    

    def ExecuteUbergraph_Widget_NewsFeed(self):
        goto(ComputedJump("EntryPoint"))
        self.FindNewsFeedActor()
        goto(ExecutionFlow.Pop())
        # Label 30
        Default__KismetSystemLibrary.LaunchURL(self.mHeaderURL)
        goto(ExecutionFlow.Pop())
        # Label 72
        ExecutionFlow.Push("L167")
        
        OutActors = None
        Item = None
        Item = OutActors[Variable]
        self.mNewsFeedActor = Item
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 167
        ReturnValue: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue
        # Label 236
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        OutActors = None
        ReturnValue_1: int32 = len(OutActors)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L446')
        Variable = Variable_0
        goto('L72')
        # Label 446
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mNewsFeedActor)
        if not ReturnValue_4:
            goto('L674')
        self.FoundNewsActor = True
        
        self.mNewsFeedActor.mNewFeedText = None
        ReturnValue_5: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mNewsFeedActor.mNewFeedText])
        if not ReturnValue_5:
            goto('L766')
        OutputDelegate.BindUFunction(self, ParseText)
        self.mNewsFeedActor.mOnNewsReceived.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 674
        if not self.FoundNewsActor:
            goto('L689')
        goto(ExecutionFlow.Pop())
        # Label 689
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = 310361445, ExecutionFunction = "ExecuteUbergraph_Widget_NewsFeed", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 766
        self.ParseText(self.mNewsFeedActor.mNewFeedText)
        goto(ExecutionFlow.Pop())
        # Label 812
        Variable = False
        Variable_0 = 0
        Variable = 0
        goto('L236')
        # Label 874
        ReturnValue_6: Transform = MakeTransform(Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_7: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, FGNewsFeedActor, 0, None, Ref[ReturnValue_6])
        ReturnValue_6 = MakeTransform(Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_8: Ptr[FGNewsFeedActor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_7, Ref[ReturnValue_6])
        self.mNewsFeedActor = ReturnValue_8
        self.FindNewsFeedActor()
        goto(ExecutionFlow.Pop())
        # Label 1166
        OutActors: List[Ptr[FGNewsFeedActor]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, FGNewsFeedActor, Ref[OutActors])
        goto('L812')
        goto('L1166')
        self.mNewsTextHeader = 
        self.mNewsTextBody = 
        ReturnValue_9: FText = self.GetNewsBodyText()
        
        self.RichTextBlock_0.SetText(Ref[ReturnValue_9])
        goto(ExecutionFlow.Pop())
        goto('L874')
        Variable_1: Ptr[Texture2DDynamic] = Texture
        self.mNewsImage.SetBrushFromTextureDynamic(Variable_1, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        goto('L30')
        Variable1: FString = "https://www.satisfactorygame.com/"
        
        NewsText = None
        ReturnValue_11: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        
        OutString1 = None
        OutSource1 = None
        Success1 = None
        self.GetStringFromTag("headerURL", OutSource, Ref[OutString1], Ref[OutSource1], Ref[Success1])
        Variable3: bool = Success1
        
        switch = {
            False: Variable1,
            True: OutString1
        }
        self.mHeaderURL = switch.get(Variable3, None)
        Variable_2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1860, 'Value': 'Read More'}"
        
        NewsText = None
        ReturnValue_11 = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        
        OutString2 = None
        OutSource2 = None
        Success2 = None
        self.GetStringFromTag("linkName", OutSource, Ref[OutString2], Ref[OutSource2], Ref[Success2])
        Variable1_0: bool = Success2
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_StringToText(OutString2)
        
        switch_0 = {
            False: Variable_2,
            True: ReturnValue1_0
        }
        self.mLinkButton.SetTitle(switch_0.get(Variable1_0, None))
        Variable_3: FString = "https://www.satisfactorygame.com/"
        
        NewsText = None
        ReturnValue_11 = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        
        OutString2 = None
        OutSource2 = None
        Success2 = None
        self.GetStringFromTag("linkName", OutSource, Ref[OutString2], Ref[OutSource2], Ref[Success2])
        
        OutString3 = None
        OutSource3 = None
        Success3 = None
        self.GetStringFromTag("linkURL", OutSource2, Ref[OutString3], Ref[OutSource3], Ref[Success3])
        Variable2: bool = Success3
        
        switch_1 = {
            False: Variable_3,
            True: OutString3
        }
        self.mLinkURL = switch_1.get(Variable2, None)
        
        NewsText = None
        ReturnValue_11 = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        ReturnValue_12: bool = Default__KismetStringLibrary.Contains(OutString, "http", False, False)
        Variable_4: bool = ReturnValue_12
        ReturnValue_13: FString = Default__KismetStringLibrary.Concat_StrStr("http://ingamenews.satisfactorygame.com/SatisfactoryImages/", OutString)
        
        switch_2 = {
            False: ReturnValue_13,
            True: OutString
        }
        ReturnValue_14: Ptr[AsyncTaskDownloadImage] = Default__AsyncTaskDownloadImage.DownloadImage(switch_2.get(Variable_4, None))
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_14)
        if not ReturnValue1_1:
            goto('L3259')
        OutputDelegate1.BindUFunction(self, OnSuccess_74A37E23495D65D8B1428F9D6302EA77)
        ReturnValue_14.OnSuccess.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, OnFail_74A37E23495D65D8B1428F9D6302EA77)
        ReturnValue_14.OnFail.AddUnique(OutputDelegate2)
        ReturnValue_14.Activate()
        
        NewsText = None
        # Label 3259
        ReturnValue_11 = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        
        OutString2 = None
        OutSource2 = None
        Success2 = None
        self.GetStringFromTag("linkName", OutSource, Ref[OutString2], Ref[OutSource2], Ref[Success2])
        
        OutString3 = None
        OutSource3 = None
        Success3 = None
        self.GetStringFromTag("linkURL", OutSource2, Ref[OutString3], Ref[OutSource3], Ref[Success3])
        ReturnValue_15: FText = Default__KismetTextLibrary.Conv_StringToText(OutSource3)
        
        Header = None
        Body = None
        self.GetHeaderAndBody(ReturnValue_15, Ref[Header], Ref[Body])
        self.mHeadline.SetText(Header)
        
        NewsText = None
        ReturnValue_11 = Default__KismetTextLibrary.Conv_TextToString(Ref[NewsText])
        
        OutString = None
        OutSource = None
        Success = None
        self.GetStringFromTag("img", ReturnValue_11, Ref[OutString], Ref[OutSource], Ref[Success])
        
        OutString2 = None
        OutSource2 = None
        Success2 = None
        self.GetStringFromTag("linkName", OutSource, Ref[OutString2], Ref[OutSource2], Ref[Success2])
        
        OutString3 = None
        OutSource3 = None
        Success3 = None
        self.GetStringFromTag("linkURL", OutSource2, Ref[OutString3], Ref[OutSource3], Ref[Success3])
        ReturnValue_15 = Default__KismetTextLibrary.Conv_StringToText(OutSource3)
        
        Header = None
        Body = None
        self.GetHeaderAndBody(ReturnValue_15, Ref[Header], Ref[Body])
        
        Body = None
        self.RichTextBlock_0.SetText(Ref[Body])
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.LaunchURL(self.mLinkURL)
        goto(ExecutionFlow.Pop())
        Variable_1 = Texture1
        goto(ExecutionFlow.Pop())
    
