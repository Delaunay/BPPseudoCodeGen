
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture2D
from Script.Engine import Delay
from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetFreightInventory
from Script.Engine import Pawn
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon
from Script.FactoryGame import GetFreightCargoType
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_UpdateTime
from Script.Engine import PlayerController
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon.K2Node_ComponentBoundEvent_Alpha
from Script.FactoryGame import FGFreightWagon
from Script.FactoryGame import GetAmountConvertedByForm
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetItemName
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Conv_FloatToText
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon.K2Node_ComponentBoundEvent_DrainDuration
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.FactoryGame import EFreightCargoType
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Game.FactoryGame.Interface.UI.Audio.ItemTransfer.Play_UI_GrabAllDumpAll import Play_UI_GrabAllDumpAll
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_MyGeometry
from Script.FactoryGame import Init
from Script.FactoryGame import GetScaledFluidStackSize
from Script.Engine import NotEqual_ByteByte
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import GetFluidColorLinear
from Script.UMG import ScrollToStart
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import GetStackFromIndex
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_InDeltaTime
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import BreakInventoryItem
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.FactoryGame import RemoveAllFromIndex
from Script.CoreUObject import LinearColor

class Widget_FreightWagon(Widget_UseableBase):
    mFreightWagon: Ptr[FGFreightWagon]
    mInventoryComponent: Ptr[FGInventoryComponent]
    mFlushing: bool
    mMaxLiquidStorage: float
    mLastStorage: float
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCustomTickRate = 0.10000000149011612
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def SetFluidInfo(self, fluidDescriptor: TSubclassOf[FGItemDescriptor]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(fluidDescriptor)
        if not ReturnValue:
            goto('L738')
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(fluidDescriptor)
        self.mFluidName.SetText(ReturnValue_0)
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(fluidDescriptor)
        SlateBrush.ImageSize = self.mFluidIcon.Brush.ImageSize
        SlateBrush.Margin = self.mFluidIcon.Brush.Margin
        SlateBrush.TintColor = self.mFluidIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_1
        SlateBrush.DrawAs = self.mFluidIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mFluidIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mFluidIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mFluidIcon.SetBrush(Ref[SlateBrush])
        self.mFluidIcon.SetVisibility(0)
        # End
        # Label 738
        self.mFluidName.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 775, 'Value': 'None'}")
        self.mFluidIcon.SetVisibility(2)
    

    def SetFluidAmount(self, Value: float):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_FloatToText(Value, 0, False, True, 1, 324, 0, 1)
        self.mCurrentAmountInPipeText.SetText(ReturnValue)
        ReturnValue_0: float = Value / self.mMaxLiquidStorage
        self.BPW_FluidTank.UpdateTankValue(ReturnValue_0)
    

    def SetFluidStats(self):
        localCurrentAmount = 0
        ReturnValue: bool = Not_PreBool(self.mFlushing)
        if not ReturnValue:
            goto('L739')
        
        stack = None
        ReturnValue_0: bool = self.mInventoryComponent.GetStackFromIndex(0, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(itemClass)
        if not ReturnValue_1:
            goto('L739')
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        
        item = None
        itemClass = None
        itemState = None
        Default__FGInventoryLibrary.BreakInventoryItem(Ref[item], Ref[itemClass], Ref[itemState])
        localFluidDesc = itemClass
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        ReturnValue_2: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(numItems, 2)
        localCurrentAmount = ReturnValue_2
        ReturnValue_3: LinearColor = Default__FGItemDescriptor.GetFluidColorLinear(localFluidDesc)
        self.BPW_FluidTank.SetTint(ReturnValue_3)
        self.SetFluidAmount(localCurrentAmount)
        self.SetFluidInfo(localFluidDesc)
    

    def OnDumpAllClicked(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L372')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L372')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_1.Server_GrabAllItemsFromInventory(ReturnValue_2, self.mInventoryComponent, None)
    

    def OnGrabAllClicked(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L372')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L372')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_1.Server_GrabAllItemsFromInventory(self.mInventoryComponent, ReturnValue_2, None)
    

    def OnSortButtonClicked(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L253')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.Server_SortInventory(self.mInventoryComponent)
        self.Widget_Scrollbox.mScrollBox.ScrollToStart()
    

    def SetFreightWagonInventoryComponent(self):
        ReturnValue1: Ptr[FGInventoryComponent] = self.mFreightWagon.GetFreightInventory()
        self.mInventory.Init(ReturnValue1)
        ReturnValue: Ptr[FGInventoryComponent] = self.mFreightWagon.GetFreightInventory()
        self.mInventoryComponent = ReturnValue
    

    def BindStorageButtons(self):
        OutputDelegate1.BindUFunction(self, DumpAllInStorage)
        self.mDumpAllButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, GrabAllFromStorage)
        self.mGrabAllButton.mButton.OnClicked.AddUnique(OutputDelegate)
    

    def DropInventorySlotStack(self):
        
        Result = None
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventory, Ref[Result])
        WasStackMoved = Result
    

    def UpdateHeaderText(self):
        Wagon: Ptr[FGFreightWagon] = Cast[FGFreightWagon](self.mInteractObject)
        bSuccess: bool = Wagon
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(Wagon.mDisplayName)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1230)
    

    def CloseStorage(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1343)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1372)
    

    def DumpAllInStorage(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1486)
    

    def GrabAllFromStorage(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1582)
    

    def BndEvt__mSortButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FreightWagon(1601)
    

    def Tick(self):
        ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FreightWagon(1616)
    

    def OnCustomTick(self):
        ExecuteUbergraph_Widget_FreightWagon.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FreightWagon(1617)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_0_OnFluidLerp__DelegateSignature(self, Alpha: float):
        ExecuteUbergraph_Widget_FreightWagon.K2Node_ComponentBoundEvent_Alpha = Alpha #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FreightWagon(1789)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_2_OnFlush__DelegateSignature(self, DrainDuration: float):
        ExecuteUbergraph_Widget_FreightWagon.K2Node_ComponentBoundEvent_DrainDuration = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_FreightWagon(2138)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_4_OnDrainCompleted__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_FreightWagon(2143)
    

    def ExecuteUbergraph_Widget_FreightWagon(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 92, UUID = -1865888106, ExecutionFunction = "ExecuteUbergraph_Widget_FreightWagon", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 107
        ExecutionFlow.Push("L258")
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        
        self.mInventory.mInventorySlots = None
        Item = None
        Item = self.mInventory.mInventorySlots[Variable]
        Item.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 258
        ReturnValue: int32 = Variable + 1
        Variable: int32 = ReturnValue
        
        self.mInventory.mInventorySlots = None
        # Label 327
        ReturnValue_0: int32 = len(self.mInventory.mInventorySlots)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L492')
        Variable = Variable
        goto('L107')
        # Label 492
        ReturnValue_2: uint8 = self.mFreightWagon.GetFreightCargoType()
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_2, 0)
        if not CmpSuccess:
            goto('L678')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_2, 1)
        if not CmpSuccess:
            goto('L678')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_2, 2)
        if not CmpSuccess:
            goto('L793')
        goto(ExecutionFlow.Pop())
        # Label 678
        self.mSolidInventoryContainer.SetVisibility(0)
        self.mLiquidInventoryContainer.SetVisibility(1)
        self.Widget_Window_DarkMode.SetInventoryVisibility(True, False)
        goto(ExecutionFlow.Pop())
        # Label 793
        self.mSolidInventoryContainer.SetVisibility(1)
        self.mLiquidInventoryContainer.SetVisibility(0)
        self.Widget_Window_DarkMode.SetInventoryVisibility(False, False)
        ReturnValue_3: int32 = self.mFreightWagon.GetScaledFluidStackSize()
        ReturnValue_4: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(ReturnValue_3, 2)
        self.mMaxLiquidStorage = ReturnValue_4
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mMaxLiquidStorage, 0, False, True, 1, 324, 0, 3)
        self.mMaxAmountInPipe.SetText(ReturnValue_5)
        goto(ExecutionFlow.Pop())
        # Label 1174
        Variable = 0
        goto('L327')
        # Label 1202
        Variable = 0
        goto('L1174')
        self.Init()
        Wagon: Ptr[FGFreightWagon] = Cast[FGFreightWagon](self.mInteractObject)
        bSuccess: bool = Wagon
        self.mFreightWagon = Wagon
        self.SetFreightWagonInventoryComponent()
        goto('L1202')
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.UpdateHeaderText()
        self.BindStorageButtons()
        OutputDelegate1.BindUFunction(self, CloseStorage)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate1)
        self.mShouldOpenInventory = True
        goto(ExecutionFlow.Pop())
        self.OnDumpAllClicked()
        # Label 1500
        ReturnValue_6: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_GrabAllDumpAll, ReturnValue_6, True)
        goto(ExecutionFlow.Pop())
        self.OnGrabAllClicked()
        goto('L1500')
        self.OnSortButtonClicked()
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(self.mFreightWagon)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        ReturnValue1: uint8 = self.mFreightWagon.GetFreightCargoType()
        CmpSuccess_0: bool = NotEqual_ByteByte(ReturnValue1, 2)
        if not CmpSuccess_0:
            goto('L1774')
        goto(ExecutionFlow.Pop())
        # Label 1774
        self.SetFluidStats()
        goto(ExecutionFlow.Pop())
        if not self.mFlushing:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: float = Ease(self.mLastStorage, 0, Alpha, 4, 2, 2)
        self.SetFluidAmount(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 1886
        self.mFlushing = True
        
        stack = None
        ReturnValue_10: bool = self.mInventoryComponent.GetStackFromIndex(0, Ref[stack])
        
        stack = None
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[stack], Ref[numItems], Ref[item])
        ReturnValue1_0: float = Default__FGInventoryLibrary.GetAmountConvertedByForm(numItems, 2)
        self.mLastStorage = ReturnValue1_0
        self.mInventoryComponent.RemoveAllFromIndex(0)
        goto(ExecutionFlow.Pop())
        goto('L1886')
        self.mFlushing = False
        self.SetFluidInfo(None)
        goto('L15')
    
