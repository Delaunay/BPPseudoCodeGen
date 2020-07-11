
from codegen.ue4_stub import *

from Script.UMG import SetSize
from Script.Engine import SetTextPropertyByName
from Script.Engine import Texture
from Script.UMG import CanvasPanelSlot
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildIndex
from Script.UMG import GetChildrenCount
from Script.Engine import Conv_IntToFloat
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Assets.Shared.default_tab_icon import default_tab_icon
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetAnchors
from Game.FactoryGame.Interface.UI.InGame.-Shared.ImageAndText import ImageAndText
from Game.FactoryGame.Interface.UI.Assets.Shared.0_White import 0_White
from Script.Engine import BreakVector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs import Widget_SlidingTabs
from Script.Engine import BooleanOR
from Script.Engine import SetBoolPropertyByName
from Script.UMG import Widget
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_TabsContainer import ExecuteUbergraph_Widget_TabsContainer
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.UMG import SetPosition
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_TabsContainer import ExecuteUbergraph_Widget_TabsContainer.K2Node_Event_IsDesignTime
from Script.UMG import AddChildToCanvas
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs_Button import Widget_SlidingTabs_Button
from Script.UMG import SetZOrder

class Widget_TabsContainer(UserWidget):
    mSlidingTabsWidget: Ptr[Widget_SlidingTabs]
    mButtons: List[ImageAndText] = [{'Texture_4_7082C106445A08AB1E68E496718E5427': {'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/0_White.0_White'}, 'Text_5_FD671CE446AF05CA543E228C049AB0F9': 'NSLOCTEXT("", "EACD098A45022B7B8C0099B62CC18EF3", "Title")'}, {'Text_5_FD671CE446AF05CA543E228C049AB0F9': 'NSLOCTEXT("", "9E3B6C7441A9154F109279AA8C57D29D", "Cool")'}, {'Text_5_FD671CE446AF05CA543E228C049AB0F9': 'NSLOCTEXT("", "5F238D2A44615A6EAE8A0EA1DD346EA8", "Sweet")'}, {'Text_5_FD671CE446AF05CA543E228C049AB0F9': 'NSLOCTEXT("", "742364874793B18830F398AD22DF14B2", "Awesome")'}]
    mButtonSize: Vector2D = Namespace(X=220, Y=36)
    OnButtonHovered: FMulticastScriptDelegate
    OnButtonUnhovered: FMulticastScriptDelegate
    OnButtonClicked: FMulticastScriptDelegate
    mOverrideButtonFunctions: bool
    OnNoTabsGenerated: FMulticastScriptDelegate
    OnTabsGenerated: FMulticastScriptDelegate
    
    def SetActiveButton(self, ActiveButton: Ptr[Widget_SlidingTabs_Button]):
        ExecutionFlow.Push("L466")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L392")
        ReturnValue_1: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        Button: Ptr[Widget_SlidingTabs_Button] = Cast[Widget_SlidingTabs_Button](ReturnValue_1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = self.mContainer.GetChildAt(Variable)
        ReturnValue_2: bool = EqualEqual_ObjectObject(ReturnValue_1, ActiveButton)
        Button.SetActive(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 392
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L28')
    

    def IfButtonClicked(self, Instigator: Ptr[Widget_SlidingTabs_Button]):
        if not self.mOverrideButtonFunctions:
            goto('L37')
        self.SetActiveButton(Instigator)
        # Label 37
        ReturnValue: int32 = self.mContainer.GetChildIndex(Instigator)
        self.OnButtonClicked.ProcessMulticastDelegate(ReturnValue)
    

    def IfButtonUnhovered(self, Insitagor: Ptr[Widget_SlidingTabs_Button]):
        self.OnButtonUnhovered.ProcessMulticastDelegate(Insitagor.IsActive)
    

    def IfButtonHovered(self, Instigator: Ptr[Widget_SlidingTabs_Button]):
        self.OnButtonHovered.ProcessMulticastDelegate(Instigator.IsActive)
    

    def GenerateButtons(self):
        ExecutionFlow.Push("L2735")
        Variable: int32 = 0
        # Label 28
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget)
        ReturnValue: bool = BooleanOR(ReturnValue1, self.mOverrideButtonFunctions)
        Variable1: bool = ReturnValue
        
        ReturnValue_0: int32 = len(self.mButtons)
        ReturnValue_1: int32 = ReturnValue_0 - 1
        
        switch = {
            False: Variable,
            True: ReturnValue_1
        }
        LocalLastIndex = switch.get(Variable1, None)
        Variable1_0: int32 = 0
        # Label 331
        Variable = 0
        ReturnValue1 = Default__KismetSystemLibrary.IsValid(self.mSlidingTabsWidget)
        ReturnValue = BooleanOR(ReturnValue1, self.mOverrideButtonFunctions)
        Variable1 = ReturnValue
        
        ReturnValue_0 = len(self.mButtons)
        ReturnValue_1 = ReturnValue_0 - 1
        
        switch_0 = {
            False: Variable,
            True: ReturnValue_1
        }
        ReturnValue_2: bool = Variable1_0 <= switch_0.get(Variable1, None)
        if not ReturnValue_2:
            goto('L2573')
        ExecutionFlow.Push("L2661")
        LocalIndex = Variable1_0
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_SlidingTabs_Button] = Default__WidgetBlueprintLibrary.Create(self, Widget_SlidingTabs_Button, ReturnValue_3)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mSlidingTabsWidget", self.mSlidingTabsWidget)
        Variable_0: Ptr[Texture] = default_tab_icon
        
        Item = None
        Item = self.mButtons[Variable1_0]
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(Item.Texture_4_7082C106445A08AB1E68E496718E5427)
        Variable_1: bool = ReturnValue_5
        
        switch_1 = {
            False: Variable_0,
            True: Item.Texture_4_7082C106445A08AB1E68E496718E5427
        }
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mIcon", switch_1.get(Variable_1, None))
        
        Item = None
        Item = self.mButtons[Variable1_0]
        
        Item.Text_5_FD671CE446AF05CA543E228C049AB0F9 = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_4, "mTitle", Ref[Item.Text_5_FD671CE446AF05CA543E228C049AB0F9])
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_4, "mTargetIndex", LocalIndex)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_4, "mOverrideButtonFunction", self.mOverrideButtonFunctions)
        ReturnValue_6: Ptr[CanvasPanelSlot] = self.mContainer.AddChildToCanvas(ReturnValue_4)
        ReturnValue1_0: bool = LocalLastIndex > 0
        Variable3: bool = ReturnValue1_0
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mButtonSize, Ref[X1], Ref[Y1])
        ReturnValue1_1: Vector2D = Vector2D(0, Y1)
        
        switch_2 = {
            False: ReturnValue1_1,
            True: self.mButtonSize
        }
        ReturnValue_6.SetSize(switch_2.get(Variable3, None))
        
        X = None
        Y = None
        BreakVector2D(self.mButtonSize, Ref[X], Ref[Y])
        ReturnValue_7: float = Conv_IntToFloat(LocalIndex)
        ReturnValue_8: float = X * ReturnValue_7
        ReturnValue_9: Vector2D = Vector2D(ReturnValue_8, 0)
        ReturnValue_6.SetPosition(ReturnValue_9)
        ReturnValue_10: int32 = LocalIndex * -1
        ReturnValue_6.SetZOrder(ReturnValue_10)
        Variable_2: Vector2D = Vector2D(X = 0, Y = 0)
        Variable1_1: Vector2D = Vector2D(X = 1, Y = 0)
        ReturnValue2: bool = LocalLastIndex > 0
        Variable2: bool = ReturnValue2
        Anchors.Minimum = Vector2D(X = 0, Y = 0)
        
        switch_3 = {
            False: Variable1_1,
            True: Variable_2
        }
        Anchors.Maximum = switch_3.get(Variable2, None)
        ReturnValue_6.SetAnchors(Anchors)
        OutputDelegate2.BindUFunction(self, IfButtonHovered)
        ReturnValue_4.OnHovered.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, IfButtonUnhovered)
        ReturnValue_4.OnUnhovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, IfButtonClicked)
        ReturnValue_4.OnClicked.AddUnique(OutputDelegate)
        ReturnValue3: bool = LocalLastIndex > 0
        ReturnValue_11: bool = Not_PreBool(ReturnValue3)
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        ReturnValue_4.SetBackgroundVisibility(False)
        ReturnValue_4.SetVisibility(3)
        goto(ExecutionFlow.Pop())
        # Label 2573
        ReturnValue_12: bool = LocalLastIndex > 0
        if not ReturnValue_12:
            goto('L2641')
        self.OnTabsGenerated.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 2641
        self.OnNoTabsGenerated.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 2661
        ReturnValue_13: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue_13
        goto('L331')
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_TabsContainer.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TabsContainer(589)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_TabsContainer(939)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TabsContainer(944)
    

    def ExecuteUbergraph_Widget_TabsContainer(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L243")
        ReturnValue1: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        Button1: Ptr[Widget_SlidingTabs_Button] = Cast[Widget_SlidingTabs_Button](ReturnValue1)
        bSuccess1: bool = Button1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Button1.OnHovered.Clear()
        Button1.OnUnhovered.Clear()
        Button1.OnClicked.Clear()
        goto(ExecutionFlow.Pop())
        # Label 243
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        # Label 312
        ReturnValue_0: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 415
        ReturnValue_2: Ptr[Widget] = self.mContainer.GetChildAt(0)
        Button: Ptr[Widget_SlidingTabs_Button] = Cast[Widget_SlidingTabs_Button](ReturnValue_2)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.SetActiveButton(Button)
        goto(ExecutionFlow.Pop())
        # Label 561
        Variable = 0
        goto('L312')
        self.Init()
        goto(ExecutionFlow.Pop())
        # Label 604
        self.mContainer.ClearChildren()
        
        ReturnValue_3: int32 = len(self.mButtons)
        ReturnValue_4: bool = ReturnValue_3 > 1
        if not ReturnValue_4:
            goto('L766')
        # Label 747
        self.GenerateButtons()
        goto('L415')
        # Label 766
        ImageAndText.Texture_4_7082C106445A08AB1E68E496718E5427 = 0_White
        ImageAndText.Text_5_FD671CE446AF05CA543E228C049AB0F9 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 823, 'Value': 'Title'}"
        
        ImageAndText = None
        ReturnValue_5: int32 = self.mButtons.append(ImageAndText)
        goto('L747')
        goto('L604')
        goto('L561')
    

    def OnTabsGenerated__DelegateSignature(self):
        pass
    

    def OnNoTabsGenerated__DelegateSignature(self):
        pass
    

    def OnButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        pass
    

    def OnButtonUnhovered__DelegateSignature(self, IsActiveButton: bool):
        pass
    

    def OnButtonHovered__DelegateSignature(self, IsActiveButton: bool):
        pass
    
