
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Resource.Equipment.PortableMiner.UI.Widget_PortableMiner import ExecuteUbergraph_Widget_PortableMiner.K2Node_Event_InDeltaTime
from Script.Engine import Pawn
from Script.FactoryGame import HasEnoughSpaceForItem
from Game.FactoryGame.Resource.Equipment.PortableMiner.UI.Widget_PortableMiner import ExecuteUbergraph_Widget_PortableMiner.K2Node_Event_MyGeometry
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import K2_GetPawn
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.UMG import SetPercent
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Resource.Equipment.PortableMiner.UI.Widget_PortableMiner import ExecuteUbergraph_Widget_PortableMiner
from Game.FactoryGame.Equipment.PortableMiner.BP_PortableMiner import BP_PortableMiner
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Audio.ItemTransfer.Play_UI_GrabAllDumpAll import Play_UI_GrabAllDumpAll
from Script.UMG import SetFillColorAndOpacity
from Script.UMG import Tick
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import RandomInteger
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.OutputSlotData_Struct import OutputSlotData_Struct
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetExtractionProgress
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import InventoryItem
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import GetOutputInventory
from Script.AkAudio import AkComponent

class Widget_PortableMiner(Widget_UseableBase):
    mPortableMiner: Ptr[BP_PortableMiner]
    mMinerItem: InventoryItem = Namespace(ItemClass='/Game/FactoryGame/Resource/Equipment/PortableMiner/BP_ItemDescriptorPortableMiner.BP_ItemDescriptorPortableMiner_C', ItemState={'ActorPtr': {'$Empty': True}})
    mOutputSlot: Ptr[Widget_InventorySlot]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def DropInventorySlotStack(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOutputSlot)
        if not ReturnValue:
            goto('L143')
        
        Result = None
        self.mOutputSlot.DropOntoInventorySlot(InventorySlot, Ref[Result])
        WasStackMoved = Result
        # End
        # Label 143
        WasStackMoved = False
    

    def InitCallbacks(self):
        ExecutionFlow.Push("L140")
        ExecutionFlow.Push("L75")
        # Label 10
        OutputDelegate1.BindUFunction(self, OnInventorySlotStackMove)
        self.mOutputSlot.OnMoveStack.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 75
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
    

    def UpdateMinerInfo(self):
        ReturnValue: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(self.mPortableMiner.mExtractResourceNode).GetResourceClass()
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(ReturnValue)
        self.mOutputContainer.mRecipeName.SetText(ReturnValue_0)
    

    def UpdateMinerProgress(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPortableMiner)
        if not ReturnValue:
            goto('L960')
        ReturnValue_0: float = self.mPortableMiner.GetExtractionProgress()
        self.mOutputContainer.mProgressBar.mProgressBar.SetPercent(ReturnValue_0)
        ReturnValue_0 = self.mPortableMiner.GetExtractionProgress()
        ReturnValue_1: float = ReturnValue_0 * 10
        ReturnValue_2: int32 = FTrunc(ReturnValue_1)
        ReturnValue_3: int32 = ReturnValue_2 * 10
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_3, False, False, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_4
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 701, 'Value': '{A}%'}", Array)
        self.mOutputContainer.mPercentageText.SetText(ReturnValue_5)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.mOutputContainer.mProgressBar.mProgressBar.SetFillColorAndOpacity(Graphics)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PortableMiner(315)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PortableMiner.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PortableMiner.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PortableMiner(673)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PortableMiner(720)
    

    def BndEvt__mButtonTakeAllItems_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PortableMiner(1521)
    

    def BndEvt__mButtonPickUpMiner_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PortableMiner(2021)
    

    def ExecuteUbergraph_Widget_PortableMiner(self):
        
        InventorySlot = None
        Success = None
        # Label 10
        self.mOutputContainer.GetSlot(0, Ref[InventorySlot], Ref[Success])
        self.mOutputSlot = InventorySlot
        self.InitCallbacks()
        self.UpdateMinerInfo()
        self.mOutputContainer.mInfoBox.SetVisibility(2)
        ReturnValue: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(self.mPortableMiner.mExtractResourceNode).GetResourceClass()
        Array1: Const[List[TSubclassOf[FGItemDescriptor]]] = [ReturnValue]
        
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[Array1])
        # End
        self.Init()
        Miner: Ptr[BP_PortableMiner] = Cast[BP_PortableMiner](self.mInteractObject)
        bSuccess: bool = Miner
        self.mPortableMiner = Miner
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mPortableMiner.GetOutputInventory()
        Struct.Title_3_16865392480E04744923368E818FDF9E = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 480, 'Value': 'Output'}"
        Struct.InventoryComponent_6_670B318B4DE9249E98B040BFD46013A9 = ReturnValue_0
        Struct.InventorySlotIndex_10_ECF91A0C4E759F6F2FC3768CE0512AB9 = 0
        Array: List[OutputSlotData_Struct] = [Struct]
        
        self.mOutputContainer.GenerateOutputSlots(Ref[Array])
        goto('L10')
        # Label 654
        self.OnEscapePressed()
        # End
        self.Tick(MyGeometry, InDeltaTime)
        self.UpdateMinerProgress()
        # End
        self.Construct()
        self.mOutputContainer.mPerMinuteText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 789, 'Value': 'per second'}")
        ReturnValue_1: int32 = RandomInteger(5)
        CmpSuccess: bool = ReturnValue_1 != 0
        if not CmpSuccess:
            goto('L1014')
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 956, 'Value': 'Portable Miner'}")
        # End
        # Label 1014
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1051, 'Value': 'Portobello Miner'}")
        # End
        # Label 1111
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L2026')
        ReturnValue_3: Ptr[FGInventoryComponent] = Player.GetInventory()
        
        ReturnValue_4: bool = ReturnValue_3.HasEnoughSpaceForItem(Ref[self.mMinerItem])
        if not ReturnValue_4:
            goto('L654')
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_5)
        bSuccess2: bool = Controller
        if not bSuccess2:
            goto('L2026')
        ReturnValue_6: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_6.ServerDismantlePortableMiner(self.mPortableMiner)
        goto('L654')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess3: bool = Controller_0
        if not bSuccess3:
            goto('L2026')
        ReturnValue_7: Ptr[Pawn] = Controller_0.K2_GetPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_7)
        bSuccess4: bool = Player1
        if not bSuccess4:
            goto('L2026')
        ReturnValue1_0: Ptr[BP_RemoteCallObject] = Controller_0.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_1: Ptr[FGInventoryComponent] = Player1.GetInventory()
        ReturnValue1_2: Ptr[FGInventoryComponent] = self.mPortableMiner.GetOutputInventory()
        ReturnValue1_0.Server_GrabAllItemsFromInventory(ReturnValue1_2, ReturnValue1_1, None)
        ReturnValue1_3: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_GrabAllDumpAll, ReturnValue1_3, True)
        # End
        goto('L1111')
    
