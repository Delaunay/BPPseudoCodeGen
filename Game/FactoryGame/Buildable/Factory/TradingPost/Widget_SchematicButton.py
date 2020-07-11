
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FGGamePhaseManager
from Script.FactoryGame import GetActiveSchematic
from Script.FactoryGame import EGamePhase
from Script.Engine import Pawn
from Script.FactoryGame import GetItemIcon
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.SlateCore import Margin
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import GameStateBase
from Script.FactoryGame import GetSchematicCategory
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetCategoryIcon
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicList import Widget_SchematicList
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.FactoryGame import GetGamePhaseForSchematic
from Script.FactoryGame import FGButtonWidget
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import GetGamePhase
from Script.FactoryGame import FGSchematic
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import GreaterEqual_ByteByte
from Script.FactoryGame import Default__FGSchematicCategory
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import IsSchematicPurchased
from Script.FactoryGame import CanSetAsActiveSchematic
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicButton import ExecuteUbergraph_Widget_SchematicButton
from Script.FactoryGame import FGSchematicCategory
from Script.UMG import SetRenderOpacity
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import GetSchematicDisplayName
from Script.CoreUObject import LinearColor

class Widget_SchematicButton(FGButtonWidget):
    mSchematicClass: TSubclassOf[FGSchematic]
    mUnlockedText: FText = NSLOCTEXT("", "55FDDDA0412BA0D98CE81AB1F5012101", "unlocked")
    mActiveText: FText = NSLOCTEXT("", "91E23AF841B372CF8C38B0AE4C5264AB", "CURRENT MILESTONE")
    mIconTexture: Ptr[Object]
    mSchematicList: Ptr[Widget_SchematicList]
    mTradingPostWidget: Ptr[Widget_TradingPost]
    mIsSchematicPhaseLocked: bool
    mIsSchematicDependentLocked: bool
    mIsSchematicLockedByTutorial: bool
    bIsFocusable = True
    
    def GetResearchTextVisibility(self):
        
        IsActive = None
        self.IsActiveSchematic(Ref[IsActive])
        if not IsActive:
            goto('L62')
        ReturnValue = 0
        goto('L82')
        # Label 62
        ReturnValue = 1
    

    def GetLockedLockVisibility(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicLockedByTutorial)
        if not ReturnValue:
            goto('L77')
        ReturnValue_0: uint8 = 3
        goto('L97')
        # Label 77
        ReturnValue_0 = 2
    

    def GetLockedIconVisibility(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicLockedByTutorial)
        if not ReturnValue:
            goto('L77')
        ReturnValue_0: uint8 = 2
        goto('L97')
        # Label 77
        ReturnValue_0 = 3
    

    def GetIsButtonClickable(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue1: bool = BooleanOR(ReturnValue, self.mIsSchematicLockedByTutorial)
        ReturnValue_0: bool = Not_PreBool(ReturnValue1)
        if not ReturnValue_0:
            goto('L206')
        ReturnValue_1: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue_1:
            goto('L231')
        # Label 206
        ReturnValue_2: uint8 = 3
        # Label 226
        goto('L251')
        # Label 231
        ReturnValue_2 = 0
    

    def GetButtonIsEnabled(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue1: bool = BooleanOR(ReturnValue, self.mIsSchematicLockedByTutorial)
        ReturnValue_0: bool = Not_PreBool(ReturnValue1)
        ReturnValue_1: bool = ReturnValue_0
    

    def GetSchematicEnabledInPhase(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L460')
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(State)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L476')
        ReturnValue_0 = Default__FGGamePhaseManager.Get(State)
        ReturnValue_2: uint8 = ReturnValue_0.GetGamePhase()
        ReturnValue_3: uint8 = ReturnValue_0.GetGamePhaseForSchematic(self.mSchematicClass)
        ReturnValue_4: bool = GreaterEqual_ByteByte(ReturnValue_2, ReturnValue_3)
        ReturnValue_5: bool = ReturnValue_4
        goto('L487')
        # Label 460
        ReturnValue_5 = True
        goto('L487')
        # Label 476
        ReturnValue_5 = True
    

    def IsActivateButtonEnabled(self):
        ReturnValue: bool = self.mSchematicList.mSchematicManager.CanSetAsActiveSchematic(self.mSchematicClass)
        ReturnValue_0: bool = ReturnValue
    

    def GetActivateButtonVisibility(self):
        
        IsActive = None
        self.IsActiveSchematic(Ref[IsActive])
        ReturnValue: bool = Not_PreBool(IsActive)
        ReturnValue_0: bool = EqualEqual_ClassClass(self.mTradingPostWidget.mSelectedSchematic, self.mSchematicClass)
        # Label 112
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
            goto('L189')
        ReturnValue_2: uint8 = 0
        goto('L209')
        # Label 189
        ReturnValue_2 = 2
    

    def GetSelectedSchematicFeedback(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSchematicList.mSchematicManager)
        if not ReturnValue:
            goto('L1237')
        ReturnValue_0: bool = EqualEqual_ClassClass(self.mSchematicList.mTradingPostWidget.mSelectedSchematic, self.mSchematicClass)
        if not ReturnValue_0:
            goto('L508')
        self.mButtonBG.SetRenderOpacity(1)
        ReturnValue1: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        # Label 293
        ReturnValue_1: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue1_0: bool = BooleanOR(ReturnValue_1, self.mIsSchematicLockedByTutorial)
        ReturnValue2: bool = BooleanOR(ReturnValue1_0, ReturnValue1)
        if not ReturnValue2:
            goto('L1068')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        # Label 476
        ReturnValue_2: LinearColor = Graphics
        goto('L1237')
        # Label 508
        ReturnValue_3: bool = self.IsHovered()
        if not ReturnValue_3:
            goto('L871')
        self.mButtonBG.SetRenderOpacity(1)
        ReturnValue_4: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        ReturnValue3: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue4: bool = BooleanOR(ReturnValue3, self.mIsSchematicLockedByTutorial)
        ReturnValue5: bool = BooleanOR(ReturnValue4, ReturnValue_4)
        # Label 770
        if not ReturnValue5:
            goto('L1155')
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text1], Ref[Graphics1])
        ReturnValue_2 = Graphics1
        goto('L1237')
        # Label 871
        self.mButtonBG.SetRenderOpacity(0)
        LinearColor.R = 0.20000000298023224
        LinearColor.G = 0.20000000298023224
        LinearColor.B = 0.20000000298023224
        LinearColor.A = 1
        ReturnValue_2 = LinearColor
        goto('L1237')
        
        Orange = None
        OrangeText = None
        # Label 1068
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_2 = Orange
        goto('L1237')
        
        Text = None
        Graphics = None
        # Label 1155
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_2 = Graphics
    

    def IsActiveSchematic(self):
        ReturnValue: TSubclassOf[FGSchematic] = self.mSchematicList.mSchematicManager.GetActiveSchematic()
        ReturnValue_0: bool = EqualEqual_ClassClass(ReturnValue, self.mSchematicClass)
        IsActive = ReturnValue_0
    

    def GetCategoryIconColor(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue1: bool = BooleanOR(ReturnValue, self.mIsSchematicLockedByTutorial)
        ReturnValue_0: bool = Not_PreBool(ReturnValue1)
        if not ReturnValue_0:
            goto('L293')
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mSchematicList.mSchematicManager)
        if not ReturnValue_1:
            goto('L770')
        # Label 206
        ReturnValue_2: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue_2:
            goto('L380')
        
        Text = None
        Graphics = None
        # Label 293
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_3: LinearColor = Graphics
        goto('L770')
        # Label 380
        ReturnValue_4: bool = self.IsHovered()
        if not ReturnValue_4:
            goto('L505')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        ReturnValue_3 = GraphicsWhite1
        goto('L770')
        # Label 505
        ReturnValue_5: bool = EqualEqual_ClassClass(self.mSchematicList.mTradingPostWidget.mSelectedSchematic, self.mSchematicClass)
        if not ReturnValue_5:
            goto('L688')
        
        TextWhite2 = None
        GraphicsWhite2 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite2], Ref[GraphicsWhite2])
        ReturnValue_3 = GraphicsWhite2
        goto('L770')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 688
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_3 = GraphicsWhite
    

    def GetSchematicActivatedBorderVisibility(self):
        
        IsActive = None
        self.IsActiveSchematic(Ref[IsActive])
        if not IsActive:
            goto('L62')
        ReturnValue = 3
        goto('L82')
        # Label 62
        ReturnValue = 2
    

    def GetSchematicBoughtTextColor(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPhaseLocked, self.mIsSchematicDependentLocked)
        ReturnValue1: bool = BooleanOR(ReturnValue, self.mIsSchematicLockedByTutorial)
        ReturnValue_0: bool = Not_PreBool(ReturnValue1)
        if not ReturnValue_0:
            goto('L293')
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mSchematicList.mSchematicManager)
        if not ReturnValue_1:
            goto('L380')
        # Label 206
        ReturnValue_2: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue_2:
            goto('L476')
        
        Text = None
        Graphics = None
        # Label 293
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_3: SlateColor = Text
        goto('L688')
        # Label 380
        ReturnValue_4: bool = EqualEqual_ClassClass(self.mSchematicList.mTradingPostWidget.mSelectedSchematic, self.mSchematicClass)
        if not ReturnValue_4:
            goto('L563')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        # Label 476
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        ReturnValue_3 = TextWhite1
        goto('L688')
        # Label 563
        ReturnValue_5: bool = self.IsHovered()
        if not ReturnValue_5:
            goto('L606')
        goto('L476')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 606
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_3 = TextWhite
    

    def GetSchematicBoughtBorderColor(self):
        ReturnValue: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: LinearColor = LinearColor(R = 0.009310999885201454, G = 0.02352900058031082, B = 0.023295000195503235, A = 1)
        goto('L226')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 144
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = GraphicsWhite
    

    def GetSchematicBoughtContentColor(self):
        ReturnValue: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: LinearColor = LinearColor(R = 0.5840790271759033, G = 0.9130989909172058, B = 0.9046609997749329, A = 1)
        goto('L226')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 144
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = GraphicsWhite
    

    def GetSchematicBoughtColorFeedback(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(None)
        if not ReturnValue1:
            goto('L493')
        ReturnValue: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue:
            goto('L201')
        # Label 144
        ReturnValue_0: LinearColor = LinearColor(R = 0.009310999885201454, G = 0.02352900058031082, B = 0.023295000195503235, A = 0.3499999940395355)
        goto('L493')
        # Label 201
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mSchematicList.mTradingPostWidget)
        if not ReturnValue_1:
            goto('L493')
        ReturnValue_2: bool = EqualEqual_ClassClass(self.mSchematicList.mTradingPostWidget.mSelectedSchematic, self.mSchematicClass)
        if not ReturnValue_2:
            goto('L441')
        ReturnValue_0 = LinearColor(R = 0, G = 0.10640200227499008, B = 0.25, A = 1)
        goto('L493')
        # Label 441
        ReturnValue_0 = LinearColor(R = 0.009310999885201454, G = 0.02352900058031082, B = 0.023295000195503235, A = 1)
    

    def GetCategoryIcon(self):
        SlateBrush.ImageSize = Vector2D(X = 32, Y = 32)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        # Label 112
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        # Label 189
        SlateBrush.ResourceObject = None
        # Label 209
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        ReturnValue1: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSchematicClass)
        ReturnValue: bool = EqualEqual_ObjectObject(SlateBrush.ResourceObject, ReturnValue1.ResourceObject)
        if not ReturnValue:
            goto('L1025')
        ReturnValue_0: TSubclassOf[FGSchematicCategory] = Default__FGSchematic.GetSchematicCategory(self.mSchematicClass)
        # Label 476
        ReturnValue_1: SlateBrush = Default__FGSchematicCategory.GetCategoryIcon(ReturnValue_0)
        self.mIconTexture = ReturnValue_1.ResourceObject
        # Label 563
        SlateBrush1.ImageSize = self.CategoryIcon.Brush.ImageSize
        SlateBrush1.Margin = self.CategoryIcon.Brush.Margin
        SlateBrush1.TintColor = self.CategoryIcon.Brush.TintColor
        SlateBrush1.ResourceObject = self.mIconTexture
        SlateBrush1.DrawAs = self.CategoryIcon.Brush.DrawAs
        SlateBrush1.Tiling = self.CategoryIcon.Brush.Tiling
        SlateBrush1.Mirroring = self.CategoryIcon.Brush.Mirroring
        ReturnValue_2: SlateBrush = SlateBrush1
        goto('L1117')
        # Label 1025
        ReturnValue_3: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSchematicClass)
        self.mIconTexture = ReturnValue_3.ResourceObject
        goto('L563')
    

    def GetSchematicBoughtCheckImageFeedback(self):
        ReturnValue: bool = self.mSchematicList.mSchematicManager.IsSchematicPurchased(self.mSchematicClass)
        if not ReturnValue:
            goto('L112')
        ReturnValue_0: uint8 = 0
        goto('L132')
        # Label 112
        ReturnValue_0 = 2
    

    def GetActivatedText(self):
        
        IsActive = None
        self.IsActiveSchematic(Ref[IsActive])
        if not IsActive:
            goto('L69')
        ReturnValue = self.mActiveText
        goto('L89')
        # Label 69
        ReturnValue = 
    

    def GetSchematicName(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mSchematicClass)
        if not ReturnValue:
            goto('L156')
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.mSchematicClass)
        ReturnValue_1: FText = ReturnValue_0
        goto('L176')
        # Label 156
        ReturnValue_1 = 
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_102_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SchematicButton(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SchematicButton(199)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_68_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SchematicButton(611)
    

    def ExecuteUbergraph_Widget_SchematicButton(self):
        self.mSchematicList.mTradingPostWidget.OnSchematicClicked(self.mSchematicClass)
        # Label 77
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        # Label 97
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue, True)
        self.Widget_ButtonShine.PlayShineAnim()
        # End
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsSchematicPhaseLocked = None
        Default__BP_SchematicHelper.IsSchematicPhaseLocked(ReturnValue2, self.mSchematicClass, self, Ref[IsSchematicPhaseLocked])
        self.mIsSchematicPhaseLocked = IsSchematicPhaseLocked
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsSchematicDependentLocked = None
        Default__BP_SchematicHelper.IsSchematicDependentLocked(ReturnValue1, self.mSchematicClass, self, Ref[IsSchematicDependentLocked])
        self.mIsSchematicDependentLocked = IsSchematicDependentLocked
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsSchematicLockedByTutorial = None
        Default__BP_SchematicHelper.IsSchematicLockedByTutorial(ReturnValue_1, self.mSchematicClass, self, Ref[IsSchematicLockedByTutorial])
        self.mIsSchematicLockedByTutorial = IsSchematicLockedByTutorial
        # End
        # Label 525
        ReturnValue1_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue1_0, True)
        # Label 606
        # End
        goto('L525')
    
