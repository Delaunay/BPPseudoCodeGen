
from codegen.ue4_stub import *

from Script.FactoryGame import FGGamePhaseManager
from Script.Engine import Delay
from Script.FactoryGame import EGamePhase
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_CustomEvent_tradingPost
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MouseEvent1
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import GameStateBase
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGTutorialIntroManager
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Script.FactoryGame import GetIsTutorialCompleted
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_RecipePreview import Widget_TradingPost_RecipePreview
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicList import Widget_SchematicList
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import BooleanOR
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MyGeometry
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_CustomEvent_TierNumber
from Script.FactoryGame import GetGamePhase
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.Engine import GreaterEqual_ByteByte
from Script.FactoryGame import GetGamePhaseForTechTier
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton
from Script.Engine import GetGameState
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MouseEvent
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.SlateCore import SlateColor
from Script.FactoryGame import Default__FGTutorialIntroManager
from Script.CoreUObject import LinearColor

class Widget_TradingPost_TierButton(UserWidget):
    anim_Locked: Ptr[WidgetAnimation]
    mTierNum: int32
    mSchematicList: Ptr[Widget_SchematicList]
    mRecipePreview: Ptr[Widget_TradingPost_RecipePreview]
    mTradingPost: Ptr[Widget_TradingPost]
    IsFullyResearched: bool
    
    def SetLockedText(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L963')
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(State)
        ReturnValue_1: uint8 = ReturnValue_0.GetGamePhaseForTechTier(self.mTierNum)
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_1, 0)
        if not CmpSuccess:
            goto('L462')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_1, 1)
        if not CmpSuccess:
            goto('L587')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_1, 2)
        if not CmpSuccess:
            goto('L681')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_1, 3)
        if not CmpSuccess:
            goto('L775')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_1, 5)
        if not CmpSuccess:
            goto('L869')
        # End
        # Label 462
        LockedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 482, 'Value': 'Complete\r\nThe Hub'}"
        # Label 537
        self.LockText.SetText(LockedText)
        # End
        # Label 587
        LockedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 607, 'Value': 'Complete Space Elevator Phase 1'}"
        goto('L537')
        # Label 681
        LockedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 701, 'Value': 'Complete Space Elevator Phase 2'}"
        goto('L537')
        # Label 775
        LockedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 795, 'Value': 'Complete Space Elevator Phase 3'}"
        goto('L537')
        # Label 869
        LockedText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 889, 'Value': 'Complete Space Elevator Phase 5'}"
        goto('L537')
    

    def GetTierNumVisibility(self):
        if not self.IsFullyResearched:
            goto('L39')
        ReturnValue = 2
        goto('L59')
        # Label 39
        ReturnValue = 0
    

    def GetCheckVisibility(self):
        if not self.IsFullyResearched:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 2
    

    def isSelectable(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L587')
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(State)
        ReturnValue_1: uint8 = ReturnValue_0.GetGamePhase()
        ReturnValue_2: uint8 = ReturnValue_0.GetGamePhaseForTechTier(self.mTierNum)
        ReturnValue_3: bool = GreaterEqual_ByteByte(ReturnValue_1, ReturnValue_2)
        if not ReturnValue_3:
            goto('L603')
        ReturnValue_4: bool = self.mTierNum > 0
        ReturnValue1: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(State)
        ReturnValue_5: bool = ReturnValue1.GetIsTutorialCompleted()
        ReturnValue_6: bool = Not_PreBool(ReturnValue_5)
        ReturnValue_7: bool = ReturnValue_6 and ReturnValue_4
        ReturnValue1_0: bool = Not_PreBool(ReturnValue_7)
        if not ReturnValue1_0:
            goto('L603')
        isSelectable = True
        # End
        # Label 587
        isSelectable = False
        # End
        # Label 603
        isSelectable = False
    

    def GetWidgetClickable(self):
        
        isSelectable = None
        self.isSelectable(Ref[isSelectable])
        if not isSelectable:
            goto('L62')
        ReturnValue = 0
        goto('L82')
        # Label 62
        ReturnValue = 3
    

    def GetTextHoverColor(self):
        ReturnValue: bool = EqualEqual_IntInt(self.mTierNum, self.mTradingPost.mActiveTier)
        if not ReturnValue:
            goto('L161')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 74
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: SlateColor = TextWhite
        goto('L347')
        
        isSelectable = None
        # Label 161
        self.isSelectable(Ref[isSelectable])
        ReturnValue_1: bool = Not_PreBool(isSelectable)
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, self.IsFullyResearched)
        if not ReturnValue_2:
            goto('L74')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Text
    

    def GetButtonColor(self):
        
        isSelectable = None
        self.isSelectable(Ref[isSelectable])
        if not isSelectable:
            goto('L302')
        ReturnValue: bool = EqualEqual_IntInt(self.mTierNum, self.mTradingPost.mActiveTier)
        if not ReturnValue:
            goto('L462')
        
        isSelectable2 = None
        self.isSelectable(Ref[isSelectable2])
        ReturnValue1: bool = Not_PreBool(isSelectable2)
        ReturnValue1_0: bool = BooleanOR(ReturnValue1, self.IsFullyResearched)
        if not ReturnValue1_0:
            goto('L938')
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text1], Ref[Graphics1])
        ReturnValue_0: LinearColor = Graphics1
        goto('L1020')
        # Label 302
        LinearColor.R = 1
        LinearColor.G = 1
        LinearColor.B = 1
        LinearColor.A = 0
        ReturnValue_0 = LinearColor
        goto('L1020')
        # Label 462
        ReturnValue_1: bool = self.IsHovered()
        if not ReturnValue_1:
            goto('L778')
        
        isSelectable1 = None
        self.isSelectable(Ref[isSelectable1])
        ReturnValue_2: bool = Not_PreBool(isSelectable1)
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, self.IsFullyResearched)
        if not ReturnValue_3:
            goto('L691')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
        goto('L1020')
        
        Text = None
        Graphics = None
        # Label 691
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
        goto('L1020')
        # Label 778
        LinearColor1.R = 1
        LinearColor1.G = 1
        LinearColor1.B = 1
        LinearColor1.A = 0
        ReturnValue_0 = LinearColor1
        goto('L1020')
        
        Orange = None
        OrangeText = None
        # Label 938
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0 = Orange
    

    def UpdateTier(self):
        self.mTradingPost.SetTierAndDeafultSchematic(self.mTierNum)
    

    def BndEvt__Button_2_K2Node_ComponentBoundEvent_70_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_TierButton(909)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost_TierButton(947)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_TierButton(1072)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_TierButton(1139)
    

    def SetTierNumber(self, TierNumber: int32, Tradingpost: Ptr[Widget_TradingPost]):
        ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_CustomEvent_TierNumber = TierNumber #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPost_TierButton.K2Node_CustomEvent_tradingPost = Tradingpost #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_TierButton(15)
    

    def ExecuteUbergraph_Widget_TradingPost_TierButton(self):
        goto(ComputedJump("EntryPoint"))
        self.mTierNum = TierNumber
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(self.mTierNum, False, True, 1, 324)
        self.TierNumber.SetText(ReturnValue)
        self.mTradingPost = tradingPost
        self.mSchematicList = self.mTradingPost.mSchematicList
        self.mRecipePreview = self.mTradingPost.Widget_TradingPost_RecipePreview
        # Label 259
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mTradingPost.mCachedSchematicManager)
        if not ReturnValue_0:
            goto('L776')
        
        IsResearched = None
        self.mTradingPost.CheckIfTierIsFullyResearched(self.mTierNum, Ref[IsResearched])
        self.IsFullyResearched = IsResearched
        self.SetLockedText()
        Variable: uint8 = 2
        Variable1: uint8 = 0
        
        isSelectable1 = None
        self.isSelectable(Ref[isSelectable1])
        Variable_0: bool = isSelectable1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mLockedMessage.SetVisibility(switch.get(Variable_0, None))
        Variable2: uint8 = 0
        Variable3: uint8 = 2
        
        isSelectable2 = None
        self.isSelectable(Ref[isSelectable2])
        Variable1_0: bool = isSelectable2
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.TierButton.SetVisibility(switch_0.get(Variable1_0, None))
        # Label 775
        goto(ExecutionFlow.Pop())
        # Label 776
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 853, UUID = 476447631, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_TierButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L259')
        # Label 858
        self.UpdateTier()
        self.Widget_ButtonShine.PlayShineAnim()
        goto(ExecutionFlow.Pop())
        
        isSelectable = None
        self.isSelectable(Ref[isSelectable])
        if not isSelectable:
           goto(ExecutionFlow.Pop())
        goto('L858')
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.anim_Locked, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 994
        self.LockText.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        # Label 1033
        self.LockText.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        
        isSelectable3 = None
        self.isSelectable(Ref[isSelectable3])
        ReturnValue_2: bool = Not_PreBool(isSelectable3)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        goto('L1033')
        goto('L994')
    
