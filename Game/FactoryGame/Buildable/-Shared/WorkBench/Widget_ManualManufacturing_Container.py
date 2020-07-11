
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import Delay
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing_Container import ExecuteUbergraph_Widget_ManualManufacturing_Container
from Script.UMG import OverlaySlot
from Script.InputCore import Key
from Script.FactoryGame import FGBuildable
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetRenderTranslation
from Script.UMG import Unhandled
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.-Shared.WorkBench.Widget_ManualManufacturing_Container import ExecuteUbergraph_Widget_ManualManufacturing_Container.K2Node_ComponentBoundEvent_RelevantClasses
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Script.FactoryGame import Init
from Script.UMG import WidgetAnimation
from Script.Engine import GetKey
from Script.Engine import EqualEqual_KeyKey
from Script.FactoryGame import SetDesiredHorizontalAlignment
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import HasAnyChildren
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.BPI_GameUI import BPI_GameUI
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import Widget_ShoppingList
from Script.UMG import EventReply
from Script.UMG import AddChildToOverlay

class Widget_ManualManufacturing_Container(Widget_UseableBase):
    PulseAnim: Ptr[WidgetAnimation]
    ShakeAnim: Ptr[WidgetAnimation]
    mLoopingSmoke: bool
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 1
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def OnPreviewKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "SpaceBar"))
        if not ReturnValue_0:
            goto('L187')
        self.mManufacturingWidget.SpaceBarOverride()
        # Label 187
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def SetWindowAlignment(self):
        self.SetDesiredHorizontalAlignment(2)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        UI: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](gameUI)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L333')
        
        shoppingList = None
        GetInterfaceUObject(UI).GetShoppingList(Ref[shoppingList])
        # Label 216
        ReturnValue_0: bool = shoppingList.mShoppingListIngredientContainer.HasAnyChildren()
        if not ReturnValue_0:
            goto('L349')
        self.SetRenderTranslation(Vector2D(X = -128, Y = 0))
        # End
        # Label 333
        shoppingList: Ptr[Widget_ShoppingList] = None
        goto('L216')
        # Label 349
        self.SetRenderTranslation(Vector2D(X = 0, Y = 0))
    

    def UpdateHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def Cleanup(self):
        self.mManufacturingWidget.Cleanup()
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing_Container(244)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing_Container(269)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing_Container(431)
    

    def LoopSmoke(self):
        self.ExecuteUbergraph_Widget_ManualManufacturing_Container(567)
    

    def BndEvt__mManufacturingWidget_K2Node_ComponentBoundEvent_0_OnRelevantClassesUpdated__DelegateSignature(self, relevantClasses: Ref[List[TSubclassOf[FGItemDescriptor]]]):
        ExecuteUbergraph_Widget_ManualManufacturing_Container.K2Node_ComponentBoundEvent_RelevantClasses = relevantClasses #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManualManufacturing_Container(583)
    

    def ExecuteUbergraph_Widget_ManualManufacturing_Container(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L157")
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue)
        ReturnValue_1: Ptr[OverlaySlot] = self.SmokeContainer.AddChildToOverlay(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 157
        if not self.mLoopingSmoke:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 1.5, LatentActionInfo(Linkage = 15, UUID = -1535993134, ExecutionFunction = "ExecuteUbergraph_Widget_ManualManufacturing_Container", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Destruct()
        self.Cleanup()
        goto(ExecutionFlow.Pop())
        self.Init()
        self.mManufacturingWidget.mInteractObject = self.mInteractObject
        self.mManufacturingWidget.Init()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mManufacturingWidget)
        self.SetInventoryVisibility(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.UpdateHeaderText()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.mManufacturingWidget.Manufacturing_Container = self
        self.SetWindowAlignment()
        goto(ExecutionFlow.Pop())
        self.mLoopingSmoke = True
        goto('L157')
        
        RelevantClasses = None
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[RelevantClasses])
        goto(ExecutionFlow.Pop())
    
