
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Texture
from Script.AkAudio import PostAkEvent
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Icon
from Script.UMG import GetChildIndex
from Script.UMG import GetChildrenCount
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.Engine import IsValid
from Script.Engine import NotEqual_TextText
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_AdditionalInfo
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_Event_IsDesignTime
from Script.Engine import BooleanOR
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_IconVisibility
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_DescVisibility
from Script.UMG import PanelWidget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.UMG import GetText
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Description
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Title
from Script.AkAudio import AkComponent
from Script.CoreUObject import LinearColor

class Widget_ListButton(UserWidget):
    mIsSelected: bool
    OnClicked: FMulticastScriptDelegate
    mIsDisabled: bool
    mIcon: Ptr[Texture]
    mTitle: FText = NSLOCTEXT("", "F6450FE64DDFFA651044DF9D15FD0D53", "Title")
    mDescription: FText
    descVisibility: uint8 = ESlateVisibility::Hidden
    iconVisibility: uint8 = ESlateVisibility::HitTestInvisible
    mAdditionalInfo: FText
    mListWidget: Ptr[PanelWidget]
    mParentWidget: Ptr[UserWidget]
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mIsDeselectable: bool
    
    def GetIconColor(self):
        if not self.mIsDisabled:
            goto('L71')
        ReturnValue = LinearColor(R = 1, G = 1, B = 1, A = 0.5)
        goto('L123')
        # Label 71
        ReturnValue = LinearColor(R = 1, G = 1, B = 1, A = 1)
    

    def ClearListSelection(self):
        ExecutionFlow.Push("L533")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue:
            goto('L415')
        LocalListWidget = self.mListWidget
        # Label 89
        Variable: int32 = 0
        # Label 112
        ReturnValue_0: int32 = LocalListWidget.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L459")
        ReturnValue_2: Ptr[Widget] = self.mListWidget.GetChildAt(Variable)
        Button: Ptr[Widget_ListButton] = Cast[Widget_ListButton](ReturnValue_2)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = NotEqual_ObjectObject(Button, self)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Button.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 415
        ReturnValue_4: Ptr[PanelWidget] = self.GetParent()
        LocalListWidget = ReturnValue_4
        goto('L89')
        # Label 459
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L112')
    

    def GetIndexInList(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: bool = NotEqual_ObjectObject(self.mListWidget, ReturnValue)
        if not ReturnValue_0:
            goto('L163')
        ReturnValue_1: int32 = self.mListWidget.GetChildIndex(self.mParentWidget)
        index = ReturnValue_1
        # End
        # Label 163
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue_2:
            goto('L311')
        ReturnValue1: int32 = self.mListWidget.GetChildIndex(self)
        index = ReturnValue1
        # End
        # Label 311
        index = 0
    

    def GetTextColor(self):
        if not self.mIsDisabled:
            goto('L101')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
        goto('L346')
        # Label 101
        ReturnValue_0: bool = self.IsHovered()
        ReturnValue_1: bool = BooleanOR(self.mIsSelected, ReturnValue_0)
        # Label 163
        if not ReturnValue_1:
            goto('L264')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue = TextWhite
        goto('L346')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 264
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue = TextWhite
    

    def GetButtonBackground(self):
        if not self.mIsDisabled:
            goto('L174')
        LinearColor.R = 0
        LinearColor.G = 0
        LinearColor.B = 0
        LinearColor.A = 0
        ReturnValue = LinearColor
        goto('L555')
        # Label 174
        if not self.mIsSelected:
            goto('L275')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        # Label 243
        ReturnValue = Orange
        goto('L555')
        # Label 275
        ReturnValue_0: bool = self.IsHovered()
        if not ReturnValue_0:
            goto('L400')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
        goto('L555')
        # Label 400
        LinearColor1.R = 0
        LinearColor1.G = 0
        LinearColor1.B = 0
        LinearColor1.A = 0
        ReturnValue = LinearColor1
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ListButton(25)
    

    def mSetDisabled(self):
        self.ExecuteUbergraph_Widget_ListButton(259)
    

    def mSetEnabled(self):
        self.ExecuteUbergraph_Widget_ListButton(291)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ListButton(323)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ListButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ListButton(465)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ListButton(995)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ListButton(1052)
    

    def SendClick(self):
        self.ExecuteUbergraph_Widget_ListButton(1057)
    

    def UpdateButton(self, Icon: Ptr[Texture], Title: FText, Description: FText, descVisibility: uint8, iconVisibility: uint8, AdditionalInfo: FText):
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Icon = Icon #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Title = Title #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_Description = Description #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_DescVisibility = descVisibility #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_IconVisibility = iconVisibility #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ListButton.K2Node_CustomEvent_AdditionalInfo = AdditionalInfo #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ListButton(1062)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ListButton(1812)
    

    def ExecuteUbergraph_Widget_ListButton(self):
        # Label 10
        self.OnUnhovered.Clear()
        # End
        
        index = None
        # Label 25
        self.GetIndexInList(Ref[index])
        self.OnClicked.ProcessMulticastDelegate(index, self)
        self.ClearListSelection()
        if not self.mIsDeselectable:
            goto('L243')
        ReturnValue: bool = Not_PreBool(self.mIsSelected)
        self.mIsSelected = ReturnValue
        # Label 153
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue_0, True)
        # End
        # Label 243
        self.mIsSelected = True
        goto('L153')
        self.SetVisibility(3)
        # Label 275
        self.mIsDisabled = True
        # End
        self.SetVisibility(0)
        self.mIsDisabled = False
        # End
        
        index1 = None
        self.GetIndexInList(Ref[index1])
        # Label 346
        self.OnHovered.ProcessMulticastDelegate(index1, self)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        # End
        self.UpdateButton(self.mIcon, self.mTitle, self.mDescription, self.descVisibility, self.iconVisibility, self.mAdditionalInfo)
        # Label 533
        # End
        # Label 538
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue_2:
            goto('L608')
        # End
        # Label 608
        ReturnValue_3: Ptr[PanelWidget] = self.GetParent()
        self.mListWidget = ReturnValue_3
        # End
        # Label 652
        self.TextSpacer.SetVisibility(0)
        # Label 690
        ReturnValue_4: FText = self.AdditionalInfoText.GetText()
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_6: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[ReturnValue_4], Ref[ReturnValue_5])
        if not ReturnValue_6:
            goto('L909')
        self.AdditionalInfoText.SetVisibility(0)
        # End
        # Label 909
        self.AdditionalInfoText.SetVisibility(1)
        # End
        # Label 952
        self.TextSpacer.SetVisibility(1)
        goto('L690')
        
        index2 = None
        self.GetIndexInList(Ref[index2])
        self.OnUnhovered.ProcessMulticastDelegate(index2, self)
        # End
        goto('L538')
        goto('L25')
        self.AdditionalInfoText.SetText(AdditionalInfo)
        self.mButtonText.SetText(Title)
        self.mNumCanProduceText.SetText(Description)
        self.mNumCanProduceText.SetVisibility(DescVisibility)
        SlateBrush.ImageSize = self.mItemImageBrush.Brush.ImageSize
        SlateBrush.Margin = self.mItemImageBrush.Brush.Margin
        SlateBrush.TintColor = self.mItemImageBrush.Brush.TintColor
        SlateBrush.ResourceObject = Icon
        SlateBrush.DrawAs = self.mItemImageBrush.Brush.DrawAs
        SlateBrush.Tiling = self.mItemImageBrush.Brush.Tiling
        SlateBrush.Mirroring = self.mItemImageBrush.Brush.Mirroring
        
        SlateBrush = None
        self.mItemImageBrush.SetBrush(Ref[SlateBrush])
        self.mItemImageBrush.SetVisibility(IconVisibility)
        ReturnValue_7: bool = EqualEqual_ByteByte(IconVisibility, 1)
        if not ReturnValue_7:
            goto('L952')
        goto('L652')
        self.OnClicked.Clear()
        self.OnHovered.Clear()
        goto('L10')
    

    def OnUnhovered__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        pass
    

    def OnHovered__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        pass
    

    def OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        pass
    
