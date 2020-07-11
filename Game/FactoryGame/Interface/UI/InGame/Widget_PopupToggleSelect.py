
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupToggleSelect import ExecuteUbergraph_Widget_PopupToggleSelect.K2Node_CustomEvent_ChildIndex
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupToggleSelect import ExecuteUbergraph_Widget_PopupToggleSelect.K2Node_Event_Instigator
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import Widget_PopupContentImageButton
from Script.Engine import BooleanOR
from Script.FactoryGame import FGPopupInstigatorInterface
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupToggleSelect import Widget_PopupToggleSelect
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGPopupWidgetContent
from Script.Engine import Array_IsValidIndex
from Script.Engine import GetObjectClass
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupToggleSelect import ExecuteUbergraph_Widget_PopupToggleSelect
from Script.Engine import IsValid
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.UMG import UserWidget

class Widget_PopupToggleSelect(FGPopupWidgetContent):
    mBody: FText
    mSelectedChild: int32 = -1
    mSelectionWidgets: List[Ptr[UserWidget]]
    
    def SetOptionalTextElements(self):
        self.mTitleText.SetText(Title)
    

    def GetShouldOkayBeEnabled(self):
        
        ReturnValue: int32 = len(self.mSelectionWidgets)
        
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_IsValidIndex(self.mSelectedChild, Ref[self.mSelectionWidgets])
        ReturnValue_1: bool = ReturnValue <= 0
        ReturnValue_2: bool = BooleanOR(ReturnValue_0, ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2
    

    def SetInstigatorAndInitialize(self):
        ExecuteUbergraph_Widget_PopupToggleSelect.K2Node_Event_Instigator = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PopupToggleSelect(793)
    

    def OnChildSelected(self, ChildIndex: int32):
        ExecuteUbergraph_Widget_PopupToggleSelect.K2Node_CustomEvent_ChildIndex = ChildIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PopupToggleSelect(817)
    

    def NotifyPopupConfirmed(self):
        self.ExecuteUbergraph_Widget_PopupToggleSelect(845)
    

    def NotifyPopupCanceled(self):
        self.ExecuteUbergraph_Widget_PopupToggleSelect(1080)
    

    def ExecuteUbergraph_Widget_PopupToggleSelect(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L329")
        
        Item = None
        Item = self.mSelectionWidgets[Variable]
        Button: Ptr[Widget_PopupContentImageButton] = Cast[Widget_PopupContentImageButton](Item)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnChildSelected)
        Button.NotifyPopupContentIndexSelect.AddUnique(OutputDelegate)
        
        Item = None
        Item = self.mSelectionWidgets[Variable]
        ReturnValue: Ptr[PanelSlot] = self.mSlot.AddChild(Item)
        goto(ExecutionFlow.Pop())
        # Label 329
        ReturnValue_0: int32 = Variable + 1
        Variable: int32 = ReturnValue_0
        
        # Label 398
        ReturnValue_1: int32 = len(self.mSelectionWidgets)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L15')
        # Label 537
        Variable = 0
        goto('L398')
        # Label 565
        Interface: TScriptInterface[FGPopupInstigatorInterface] = QueryInterface[FGPopupInstigatorInterface](self.mInstigator)
        bSuccess1: bool = Interface
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1: TSubclassOf[Widget_PopupToggleSelect] = Default__GameplayStatics.GetObjectClass(self)
        
        widgets = None
        GetInterfaceUObject(Interface).WidgetFactory(ReturnValue1, Ref[widgets])
        self.mSelectionWidgets = widgets
        Variable = 0
        goto('L537')
        self.mInstigator = Instigator
        goto('L565')
        self.mSelectedChild = ChildIndex
        goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mInstigator)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Interface1: TScriptInterface[FGPopupInstigatorInterface] = QueryInterface[FGPopupInstigatorInterface](self.mInstigator)
        bSuccess2: bool = Interface1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: TSubclassOf[Widget_PopupToggleSelect] = Default__GameplayStatics.GetObjectClass(self)
        GetInterfaceUObject(Interface1).NotifyPopupClosed(ReturnValue_4, self.mSelectedChild)
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
    
