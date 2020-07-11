
from codegen.ue4_stub import *

from Script.UMG import GetSize
from Script.UMG import SetSize
from Script.Engine import K2_IsTimerActiveHandle
from Game.FactoryGame.Interface.UI.Menu.Widget_AreaSelection_Button import ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_IsDesignTime
from Script.Engine import SetScalarParameterValue
from Script.AkAudio import PostAkEvent
from Script.Engine import Conv_TextToString
from Script.Engine import NotEqual_BoolBool
from Script.UMG import CanvasPanelSlot
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetEndTime
from Script.UMG import SetPadding
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import SlotAsOverlaySlot
from Script.Engine import Not_PreBool
from Script.UMG import GetEffectMaterial
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Ease
from Game.FactoryGame.Interface.UI.Menu.Widget_AreaSelection_Button import ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_MyGeometry
from Script.Engine import PlayerController
from Script.Engine import SelectFloat
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import GetWorldDeltaSeconds
from Script.Engine import EqualEqual_StriStri
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetHeightOverride
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BreakVector2D
from Game.FactoryGame.Interface.UI.Menu.Widget_AreaSelection_Button import ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_InDeltaTime
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import EGameVersion
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Menu.Widget_AreaSelection_Button import ExecuteUbergraph_Widget_AreaSelection_Button
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.UMG import IsAnimationPlaying
from Script.CoreUObject import Vector2D
from Script.FactoryGame import Default__FGVersionFunctionLibrary
from Script.AkAudio import AkComponent
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.Menu.StartingLocationsDataStruct import StartingLocationsDataStruct
from Script.FactoryGame import GetGameVersion
from Script.UMG import GetAnimationCurrentTime
from Script.UMG import SetZOrder

class Widget_AreaSelection_Button(UserWidget):
    LockedHover: Ptr[WidgetAnimation]
    IsHoveredAnim: Ptr[WidgetAnimation]
    mIsLocked: bool
    mIsSelected: bool
    mStartingLocs: StartingLocationsDataStruct
    OnClicked: FMulticastScriptDelegate
    mLerpT: float
    mLerpDuration: float = 0.25
    mLerpUpdateTime: float = 0.009999999776482582
    mLerpTimerHandle: TimerHandle
    mIsGrowing: bool = True
    mWidth: float = 400
    mHoverWidthIncrease: float = 80
    mSpacing: float
    mIsLerping: bool
    
    def SetExperimentalLabelVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 1)
        ReturnValue_1: bool = Default__KismetStringLibrary.EqualEqual_StriStri(self.mStartingLocs.StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96, "?startloc=DuneDesert")
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mExperimentalBuildLabel.SetVisibility(switch.get(Variable_0, None))
    

    def SkipSizeLerp(self, isGrowing: bool):
        ReturnValue: bool = Default__KismetSystemLibrary.K2_IsTimerActiveHandle(self, self.mLerpTimerHandle)
        if not ReturnValue:
            goto('L71')
        # End
        # Label 71
        self.StartSizeLerp(isGrowing)
        self.mLerpT = 1
    

    def StartSizeLerp(self, Growing: bool):
        ReturnValue: bool = NotEqual_BoolBool(Growing, self.mIsGrowing)
        if not ReturnValue:
            goto('L156')
        ReturnValue_0: float = 1 - self.mLerpT
        self.mLerpT = ReturnValue_0
        self.mIsGrowing = Growing
        # Label 140
        self.mIsLerping = True
        # End
        # Label 156
        self.mLerpT = 0
        goto('L140')
    

    def SetBorderTint(self, Color: SlateColor):
        self.mNameBG.SetColorAndOpacity(Color.SpecifiedColor)
        self.mBorder.SetColorAndOpacity(Color.SpecifiedColor)
    

    def DeselectAnim(self):
        ReturnValue: bool = self.IsAnimationPlaying(self.IsHoveredAnim)
        if not ReturnValue:
            goto('L231')
        ReturnValue_0: float = self.IsHoveredAnim.GetEndTime()
        ReturnValue_1: float = self.GetAnimationCurrentTime(self.IsHoveredAnim)
        ReturnValue_2: float = ReturnValue_0 - ReturnValue_1
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IsHoveredAnim, ReturnValue_2, 1, 1, 1)
        # End
        # Label 231
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IsHoveredAnim, 0, 1, 1, 1)
    

    def SelectAnim(self):
        ReturnValue: bool = self.IsAnimationPlaying(self.IsHoveredAnim)
        if not ReturnValue:
            goto('L135')
        ReturnValue_0: float = self.GetAnimationCurrentTime(self.IsHoveredAnim)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IsHoveredAnim, ReturnValue_0, 1, 0, 1)
        # End
        # Label 135
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IsHoveredAnim, 0, 1, 0, 1)
    

    def SetSelected(self, isSelected: bool):
        LocalIsSelected = isSelected
        if not LocalIsSelected:
            goto('L152')
        self.SkipSizeLerp(True)
        ReturnValue1: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue1.SetZOrder(3)
        # Label 128
        self.mIsSelected = LocalIsSelected
        # End
        # Label 152
        if not self.mIsSelected:
            goto('L266')
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue.SetZOrder(0)
        self.StartSizeLerp(False)
        goto('L128')
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AreaSelection_Button(444)
    

    def LerpSize(self):
        self.ExecuteUbergraph_Widget_AreaSelection_Button(1229)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AreaSelection_Button(2656)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_AreaSelection_Button(2661)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AreaSelection_Button(3950)
    

    def Tick(self):
        ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_AreaSelection_Button.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AreaSelection_Button(3955)
    

    def ExecuteUbergraph_Widget_AreaSelection_Button(self):
        # Label 10
        self.SetExperimentalLabelVisibility()
        if not self.mIsLocked:
            goto('L135')
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.RetainerBox_0.GetEffectMaterial()
        ReturnValue.SetScalarParameterValue("amount", 0.8999999761581421)
        # End
        # Label 135
        ReturnValue = self.RetainerBox_0.GetEffectMaterial()
        ReturnValue.SetScalarParameterValue("amount", 0)
        # End
        # Label 232
        ReturnValue_0: bool = Not_PreBool(self.mIsLocked)
        if not ReturnValue_0:
            goto('L3983')
        self.Widget_ButtonShine.PlayShineAnim()
        self.SetSelected(True)
        self.OnClicked.ProcessMulticastDelegate(self.mStartingLocs)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue1, True)
        # End
        ReturnValue2: bool = Not_PreBool(self.mIsLocked)
        if not ReturnValue2:
            goto('L777')
        Variable: int32 = 2
        Variable1: int32 = 0
        ReturnValue2_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        Variable_0: bool = self.mIsSelected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_0.SetZOrder(switch.get(Variable_0, None))
        if not self.mIsSelected:
            goto('L828')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.SetBorderTint(Text)
        # End
        # Label 777
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LockedHover, 0, 1, 1, 1)
        # End
        # Label 828
        self.StartSizeLerp(False)
        # End
        # Label 848
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue_1, True)
        self.StartSizeLerp(True)
        
        Orange = None
        OrangeText = None
        # Label 948
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.SetBorderTint(OrangeText)
        # End
        # Label 1031
        if not self.mIsSelected:
            goto('L848')
        goto('L948')
        # Label 1050
        ReturnValue1_2: bool = Not_PreBool(self.mIsLocked)
        if not ReturnValue1_2:
            goto('L1178')
        ReturnValue1_3: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue1_3.SetZOrder(3)
        goto('L1031')
        # Label 1178
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LockedHover, 0, 1, 0, 1)
        # End
        ReturnValue_4: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_5: float = ReturnValue_4 / self.mLerpDuration
        ReturnValue3: float = self.mLerpT + ReturnValue_5
        self.mLerpT = ReturnValue3
        ReturnValue_6: float = SelectFloat(620, 700, self.mIsGrowing)
        ReturnValue1_4: float = SelectFloat(700, 620, self.mIsGrowing)
        ReturnValue_7: float = Ease(ReturnValue_6, ReturnValue1_4, self.mLerpT, 7, 2, 2)
        self.mButtonSize.SetHeightOverride(ReturnValue_7)
        ReturnValue_8: float = self.mWidth + self.mHoverWidthIncrease
        ReturnValue1_5: float = self.mWidth + self.mHoverWidthIncrease
        ReturnValue4: float = SelectFloat(self.mWidth, ReturnValue_8, self.mIsGrowing)
        ReturnValue5: float = SelectFloat(ReturnValue1_5, self.mWidth, self.mIsGrowing)
        ReturnValue2_1: float = Ease(ReturnValue4, ReturnValue5, self.mLerpT, 7, 2, 2)
        self.mButtonSize.SetWidthOverride(ReturnValue2_1)
        ReturnValue2_2: float = SelectFloat(0, 1, self.mIsGrowing)
        ReturnValue3_0: float = SelectFloat(1, 0, self.mIsGrowing)
        ReturnValue1_6: float = Ease(ReturnValue2_2, ReturnValue3_0, self.mLerpT, 7, 2, 2)
        self.mBorder.SetRenderOpacity(ReturnValue1_6)
        self.mTitleContainer.SetRenderOpacity(ReturnValue1_6)
        self.mDescriptionContainer.SetRenderOpacity(ReturnValue1_6)
        ReturnValue_9: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mButtonSize)
        ReturnValue6: float = SelectFloat(self.mSpacing, 0, self.mIsGrowing)
        ReturnValue7: float = SelectFloat(0, self.mSpacing, self.mIsGrowing)
        ReturnValue3_1: float = Ease(ReturnValue6, ReturnValue7, self.mLerpT, 7, 2, 2)
        Margin1.Left = ReturnValue3_1
        Margin1.Top = 0
        Margin1.Right = ReturnValue3_1
        Margin1.Bottom = 0
        ReturnValue_9.SetPadding(Margin1)
        ReturnValue_10: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_10:
            goto('L3983')
        self.mIsLerping = False
        # End
        goto('L1050')
        goto('L232')
        # Label 2666
        self.mButtonSize.SetWidthOverride(self.mWidth)
        ReturnValue1_7: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mButtonSize)
        Margin.Left = self.mSpacing
        Margin.Top = 0
        Margin.Right = self.mSpacing
        Margin.Bottom = 0
        ReturnValue1_7.SetPadding(Margin)
        ReturnValue_11: float = self.mSpacing * 2
        ReturnValue2_3: float = self.mWidth + ReturnValue_11
        ReturnValue_12: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mScaleBox)
        ReturnValue_13: Vector2D = ReturnValue_12.GetSize()
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_13, Ref[X], Ref[Y])
        ReturnValue_14: Vector2D = Vector2D(ReturnValue2_3, Y)
        ReturnValue_12.SetSize(ReturnValue_14)
        
        self.mStartingLocs.Name_15_B24B9E3F4D2123245CD4C3AC88089645 = None
        ReturnValue_15: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mStartingLocs.Name_15_B24B9E3F4D2123245CD4C3AC88089645])
        self.mAreaNameTextObject.SetTitle(ReturnValue_15)
        self.mDescriptionTextObject.SetText(self.mStartingLocs.Description_16_FC7E65A7491E131F357F18A1353545CB)
        SlateBrush.ImageSize = self.mLevelScreenshotObject.Brush.ImageSize
        SlateBrush.Margin = self.mLevelScreenshotObject.Brush.Margin
        SlateBrush.TintColor = self.mLevelScreenshotObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mStartingLocs.Image_17_BEFE2AB0455E5D921A998EB9F17BDDC1
        SlateBrush.DrawAs = self.mLevelScreenshotObject.Brush.DrawAs
        SlateBrush.Tiling = self.mLevelScreenshotObject.Brush.Tiling
        SlateBrush.Mirroring = self.mLevelScreenshotObject.Brush.Mirroring
        
        SlateBrush = None
        self.mLevelScreenshotObject.SetBrush(Ref[SlateBrush])
        goto('L10')
        # Label 3904
        self.mDescriptionSizebox.SetWidthOverride(self.mWidth)
        goto('L2666')
        goto('L3904')
        if not self.mIsLerping:
            goto('L3983')
        self.LerpSize()
    

    def OnClicked__DelegateSignature(self, StartingLoc: StartingLocationsDataStruct):
        pass
    
