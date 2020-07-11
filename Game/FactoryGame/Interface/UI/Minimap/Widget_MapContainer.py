
from codegen.ue4_stub import *

from Script.FactoryGame import ECompassViewDistance
from Script.FactoryGame import GetRepresentationType
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.MapFilterStruct import MapFilterStruct
from Script.FactoryGame import GetMapRepresentationTypeFilter
from Script.FactoryGame import SetCompassRepresentationTypeFilter
from Script.UMG import GetChildIndex
from Script.Engine import Conv_ByteToInt
from Script.UMG import AddChild
from Script.Engine import Array_Set
from Script.Engine import GetEnumeratorUserFriendlyName
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_FilterButton import Widget_FilterButton
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.FactoryGame import GetCompassViewDistance
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import SetMapRepresentationTypeFilter
from Script.Engine import Contains
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.UMG import PanelWidget
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import SetInputMode
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRespresentation
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_Value
from Script.CoreUObject import LinearColor
from Script.UMG import RemoveChildAt
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator2
from Script.UMG import GetVisibility
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_WidgetMapObject
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRepresentation
from Script.FactoryGame import GetDefaultFocusWidget
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ShowOnMap
from Game.FactoryGame.Interface.UI.Minimap.MapFilters.Widget_BeaconViewdistanceSlider import Widget_BeaconViewdistanceSlider
from Script.FactoryGame import GetRepresentationText
from Script.Engine import PrintString
from Script.FactoryGame import ERepresentationType
from Script.Engine import SetTextPropertyByName
from Script.Engine import GetEmptyText
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator7
from Script.UMG import GetParent
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator3
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRepresentation1
from Script.Engine import EqualEqual_IgnoreCase_TextText
from Script.UMG import PanelSlot
from Script.Engine import SetBytePropertyByName
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.FactoryGame import OnEscapePressed
from Script.Engine import Conv_FloatToText
from Script.UMG import SetValue
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Replace
from Script.Engine import BreakVector2D
from Script.Engine import SetBoolPropertyByName
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_NewViewDistance
from Script.Engine import Format
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator4
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigaotr
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_Text
from Script.Engine import Conv_TextToString
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ShowOnCompass
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator6
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator5
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator1
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import Widget_MapObject
from Script.UMG import Widget
from Script.FactoryGame import GetCompassRepresentationTypeFilter
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapContainer import ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ViewDistance
from Script.FactoryGame import FGActorRepresentation
from Script.UMG import SetInputMode_GameAndUIEx

class Widget_MapContainer(FGInteractWidget):
    IsMapOpen: bool
    mFilterCategories: List[MapFilterStruct]
    mAnimationTimer: TimerHandle
    mHoveredMapObject: Ptr[Widget_MapObject]
    mBeaconInt: int32 = -1
    mBeaconSearchResult: MapFilterStruct = Namespace(RepresentationType_3_5D457985464D101149CAEF83656C9370='ERepresentationType::RT_Beacon')
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['ToggleMap_BuildGunNoSnapMode']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def UpdateBeaconViewDistances(self):
        ExecutionFlow.Push("L726")
        ReturnValue: bool = GreaterEqual_IntInt(self.mBeaconInt, 0)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        # Label 95
        ReturnValue_0: int32 = len(self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L652")
        ReturnValue_2: Ptr[Widget] = self.Widget_Map_Filters_Container.mBeaconContainer.GetChildAt(Variable_0)
        Slider: Ptr[Widget_BeaconViewdistanceSlider] = Cast[Widget_BeaconViewdistanceSlider](ReturnValue_2)
        bSuccess: bool = Slider
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        Item = None
        Item = self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212[Variable_0]
        ReturnValue_3: uint8 = Item.GetCompassViewDistance()
        ReturnValue_4: int32 = Conv_ByteToInt(ReturnValue_3)
        Slider.mSelectedLevel = ReturnValue_4
        Slider.UpdateSelectedLevel()
        goto(ExecutionFlow.Pop())
        # Label 652
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L95')
    

    def SetupBeaconBindings(self, WidgetBeaconViewdistanceSlider: Ptr[Widget_BeaconViewdistanceSlider]):
        OutputDelegate4.BindUFunction(self, OnBeaconViewDistanceChanged)
        WidgetBeaconViewdistanceSlider.OnViewDistanceChanged.AddUnique(OutputDelegate4)
        OutputDelegate3.BindUFunction(self, OnBeaconHovered)
        WidgetBeaconViewdistanceSlider.OnHovered.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnBeaconUnhovered)
        WidgetBeaconViewdistanceSlider.OnUnhovered.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnBeaconVeiwDistanceHovered)
        WidgetBeaconViewdistanceSlider.OnViewDistanceHovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnBeaconViewDistanceUnhovered)
        WidgetBeaconViewdistanceSlider.OnViewDistanceUnhovered.AddUnique(OutputDelegate)
    

    def ClearSearch(self):
        self.Widget_Map_Filters_Container.mBeaconContainer.SetVisibility(0)
        self.Widget_Map_Filters_Container.mBeaconSearchResults.SetVisibility(1)
        self.Widget_Map_Filters_Container.Widget_InputBox.InputText.SetText()
        self.UpdateBeaconViewDistances()
    

    def PopulateSearchResults(self, text: FText):
        ExecutionFlow.Push("L1749")
        self.Widget_Map_Filters_Container.mBeaconContainer.SetVisibility(1)
        self.Widget_Map_Filters_Container.mBeaconSearchResults.SetVisibility(0)
        self.Widget_Map_Filters_Container.mBeaconSearchResults.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        # Label 229
        ReturnValue: int32 = len(self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L1466')
        Variable_0 = Variable
        ExecutionFlow.Push("L1595")
        Default__KismetSystemLibrary.PrintString(self, "work pls?", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        LocalBeaconInt = Variable_0
        
        self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        Item = None
        Item = self.mFilterCategories[self.mBeaconInt].ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212[Variable_0]
        LocalActorRepresentation = Item
        ReturnValue_1: FText = LocalActorRepresentation.GetRepresentationText()
        
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_1])
        
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[text])
        ReturnValue_3: bool = Default__KismetStringLibrary.Contains(ReturnValue_2, ReturnValue1, False, False)
        if not ReturnValue_3:
            goto('L1669')
        
        ReturnValue_4: int32 = LocalActorArray.append(LocalActorRepresentation)
        
        self.mFilterCategories[self.mBeaconInt].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item1 = None
        Item1 = self.mFilterCategories[self.mBeaconInt].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[LocalBeaconInt]
        
        Item1 = None
        ReturnValue1_0: int32 = LocalObjectArray.append(Item1)
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_BeaconViewdistanceSlider] = Default__WidgetBlueprintLibrary.Create(self, Widget_BeaconViewdistanceSlider, ReturnValue_5)
        ReturnValue1_1: FText = LocalActorRepresentation.GetRepresentationText()
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_6, "mName", Ref[ReturnValue1_1])
        ReturnValue_7: uint8 = LocalActorRepresentation.GetCompassViewDistance()
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_6, "mCompassViewDistance", ReturnValue_7)
        ReturnValue_8: Ptr[PanelSlot] = self.Widget_Map_Filters_Container.mBeaconSearchResults.AddChild(ReturnValue_6)
        self.SetupBeaconBindings(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 1466
        MapFilterStruct.RepresentationType_3_5D457985464D101149CAEF83656C9370 = 1
        MapFilterStruct.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = LocalActorArray
        MapFilterStruct.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = LocalObjectArray
        self.mBeaconSearchResult = MapFilterStruct
        goto(ExecutionFlow.Pop())
        # Label 1595
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L229')
        # Label 1669
        Default__KismetSystemLibrary.PrintString(self, "wat", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
    

    def GetBeacons(self):
        ReturnValue: uint8 = self.Widget_Map_Filters_Container.mBeaconSearchResults.GetVisibility()
        Variable: uint8 = ReturnValue
        
        switch = {
            0: self.mBeaconSearchResult,
            1: self.mFilterCategories[self.mBeaconInt],
            2: self.mFilterCategories[self.mBeaconInt],
            3: self.mBeaconSearchResult,
            4: self.mBeaconSearchResult
        }
        BeaconCategory = switch.get(Variable, None)
    

    def AddChildToBeacons(self, actorRepresentation: Ptr[FGActorRepresentation]):
        ReturnValue: uint8 = actorRepresentation.GetRepresentationType()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 1)
        if not ReturnValue_0:
            goto('L474')
        # Label 95
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_BeaconViewdistanceSlider] = Default__WidgetBlueprintLibrary.Create(self, Widget_BeaconViewdistanceSlider, ReturnValue_1)
        ReturnValue_3: FText = actorRepresentation.GetRepresentationText()
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mName", Ref[ReturnValue_3])
        ReturnValue_4: uint8 = actorRepresentation.GetCompassViewDistance()
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_2, "mCompassViewDistance", ReturnValue_4)
        self.Widget_Map_Filters_Container.AddChildToBeacons(ReturnValue_2)
        self.SetupBeaconBindings(ReturnValue_2)
    

    def RemoveActorRepresentationFromFilterCategories(self, actorRepresentation: Const[Ref[Ptr[FGActorRepresentation]]]):
        ExecutionFlow.Push("L1455")
        LocalRepresentationType = 0
        ReturnValue: uint8 = actorRepresentation.GetRepresentationType()
        LocalRepresentationType = ReturnValue
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 148
        ReturnValue2: int32 = len(self.mFilterCategories)
        ReturnValue2_0: bool = Variable <= ReturnValue2
        # Label 245
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        Variable1 = Variable
        ExecutionFlow.Push("L1006")
        LocalFilterCategoryInt = Variable1
        
        Item1 = None
        Item1 = self.mFilterCategories[Variable1]
        LocalFilterCategory = Item1
        ReturnValue_0: bool = EqualEqual_ByteByte(LocalFilterCategory.RepresentationType_3_5D457985464D101149CAEF83656C9370, LocalRepresentationType)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0: bool = False
        Variable1_0: int32 = 0
        Variable_1: int32 = 0
        # Label 514
        ReturnValue_1: bool = Not_PreBool(Variable_0)
        
        LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        ReturnValue1: int32 = len(LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue1_0
        if not ReturnValue_2:
            goto('L1080')
        Variable_1 = Variable1_0
        ExecutionFlow.Push("L1381")
        LocalActorRepresentationInt = Variable_1
        
        LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        Item = None
        Item = LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212[Variable_1]
        ReturnValue_3: bool = EqualEqual_ObjectObject(Item, actorRepresentation)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212.remove(LocalActorRepresentationInt)
        
        LocalFilterCategory.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        LocalFilterCategory.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333.remove(LocalActorRepresentationInt)
        Variable_0 = True
        goto(ExecutionFlow.Pop())
        # Label 1006
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L148')
        
        LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        # Label 1080
        ReturnValue_5: int32 = len(LocalFilterCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212)
        ReturnValue_6: bool = ReturnValue_5 <= 1
        if not ReturnValue_6:
            goto('L1320')
        
        self.mFilterCategories.remove(LocalFilterCategoryInt)
        ReturnValue_7: bool = self.Widget_Map_Filters_Container.mFilterContainer.RemoveChildAt(LocalFilterCategoryInt)
        goto(ExecutionFlow.Pop())
        
        # Label 1320
        Default__KismetArrayLibrary.Array_Set(LocalFilterCategoryInt, False, Ref[self.mFilterCategories], Ref[LocalFilterCategory])
        goto(ExecutionFlow.Pop())
        # Label 1381
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L514')
    

    def UglyFixForActorName(self, actorRepresentation: uint8):
        ReturnValue: FString = Default__KismetNodeHelperLibrary.GetEnumeratorUserFriendlyName(ERepresentationType, actorRepresentation)
        Variable: uint8 = actorRepresentation
        # Label 95
        ReturnValue_0: FString = Default__KismetStringLibrary.Replace(ReturnValue, "RT_", "", 0)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 242, 'Value': 'Truck Stations'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 314, 'Value': 'Vehicles'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 380, 'Value': 'Train Stations'}"
        Variable3: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 452, 'Value': 'Trains'}"
        Variable4: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 516, 'Value': 'Starting Pod'}"
        Variable5: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 586, 'Value': 'Space Elevator'}"
        Variable6: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 658, 'Value': 'Resources'}"
        Variable7: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 725, 'Value': 'Radar Towers'}"
        Variable8: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 795, 'Value': 'Players'}"
        Variable9: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 860, 'Value': 'Ping'}"
        Variable10: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 922, 'Value': 'HUB'}"
        Variable11: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 983, 'Value': 'Crates'}"
        Variable12: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1047, 'Value': 'Beacons'}"
        Variable13: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1112, 'Value': 'Other'}"
        ReturnValue_2: FText = Default__KismetTextLibrary.GetEmptyText()
        
        switch = {
            0: Variable13,
            1: Variable12,
            2: Variable11,
            3: Variable10,
            4: Variable9,
            5: Variable8,
            6: Variable7,
            7: Variable6,
            8: Variable5,
            9: Variable4,
            10: Variable3,
            11: Variable2,
            12: Variable1,
            13: Variable_0
        }
        
        switch.get(Variable, None) = None
        ReturnValue_3: bool = Default__KismetTextLibrary.EqualEqual_IgnoreCase_TextText(Ref[switch.get(Variable, None)], Ref[ReturnValue_2])
        Variable_1: bool = ReturnValue_3
        
        switch_0 = {
            0: Variable13,
            1: Variable12,
            2: Variable11,
            3: Variable10,
            4: Variable9,
            5: Variable8,
            6: Variable7,
            7: Variable6,
            8: Variable5,
            9: Variable4,
            10: Variable3,
            11: Variable2,
            12: Variable1,
            13: Variable_0
        }
        
        switch_1 = {
            False: switch_0.get(Variable, None),
            True: ReturnValue_1
        }
        ReturnValue_4: FText = switch_1.get(Variable_1, None)
    

    def UpdateMapObjectVisibility(self, Type: uint8):
        localVisible = False
    

    def GetCompassRepresentation(self, Type: uint8):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.GetCompassRepresentationTypeFilter(ReturnValue, Type)
        ReturnValue_2: bool = ReturnValue_1
    

    def GetMapRepresentation(self, Type: uint8):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.GetMapRepresentationTypeFilter(ReturnValue, Type)
        ReturnValue_2: bool = ReturnValue_1
    

    def SetCompassRepresentation(self, Type: uint8, visible: bool):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_0.SetCompassRepresentationTypeFilter(ReturnValue, Type, visible)
    

    def SetMapRepresentation(self, Type: uint8, visible: bool):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_0.SetMapRepresentationTypeFilter(ReturnValue, Type, visible)
    

    def GetIndexInParent(self, Widget: Ptr[Widget]):
        ReturnValue: Ptr[PanelWidget] = Widget.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(Widget)
        ReturnValue_1: int32 = ReturnValue_0
    

    def AddUniqueToFilterCategories(self, actorRepresentation: Ptr[FGActorRepresentation], WidgetMapObject: Ptr[Widget_MapObject]):
        ExecutionFlow.Push("L1416")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mFilterCategories)
        ReturnValue_0: bool = Variable <= ReturnValue
        # Label 148
        if not ReturnValue_0:
            goto('L938')
        Variable_0 = Variable
        ExecutionFlow.Push("L1342")
        
        Item = None
        Item = self.mFilterCategories[Variable_0]
        LocalRepresentationArray = Item.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212
        
        ReturnValue1: int32 = LocalRepresentationArray.append(actorRepresentation)
        
        Item = None
        Item = self.mFilterCategories[Variable_0]
        LocalMapObjectArray = Item.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333
        
        ReturnValue_1: int32 = LocalMapObjectArray.append(WidgetMapObject)
        ReturnValue2: uint8 = actorRepresentation.GetRepresentationType()
        
        Item = None
        Item = self.mFilterCategories[Variable_0]
        ReturnValue1_0: bool = EqualEqual_ByteByte(ReturnValue2, Item.RepresentationType_3_5D457985464D101149CAEF83656C9370)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mFilterCategories[Variable_0]
        MapFilterStruct1.RepresentationType_3_5D457985464D101149CAEF83656C9370 = Item.RepresentationType_3_5D457985464D101149CAEF83656C9370
        MapFilterStruct1.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = LocalRepresentationArray
        MapFilterStruct1.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = LocalMapObjectArray
        
        MapFilterStruct1 = None
        Default__KismetArrayLibrary.Array_Set(Variable_0, False, Ref[self.mFilterCategories], Ref[MapFilterStruct1])
        CreatedNewCategory = False
        # End
        # Label 938
        Array: List[Ptr[Widget_MapObject]] = [WidgetMapObject]
        Array1: List[Ptr[FGActorRepresentation]] = [actorRepresentation]
        ReturnValue1_1: uint8 = actorRepresentation.GetRepresentationType()
        MapFilterStruct.RepresentationType_3_5D457985464D101149CAEF83656C9370 = ReturnValue1_1
        MapFilterStruct.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = Array1
        MapFilterStruct.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = Array
        
        MapFilterStruct = None
        ReturnValue2_0: int32 = self.mFilterCategories.append(MapFilterStruct)
        ReturnValue_2: uint8 = actorRepresentation.GetRepresentationType()
        ReturnValue_3: bool = EqualEqual_ByteByte(ReturnValue_2, 1)
        if not ReturnValue_3:
            goto('L1326')
        self.mBeaconInt = ReturnValue2_0
        # Label 1326
        CreatedNewCategory = True
        # End
        # Label 1342
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def AddChildToFilters(self, actorRepresentation: uint8):
        MapRepresentation = False
        CompassRepresentation = False
        ReturnValue: bool = self.GetMapRepresentation(actorRepresentation)
        MapRepresentation = ReturnValue
        ReturnValue_0: bool = self.GetCompassRepresentation(actorRepresentation)
        CompassRepresentation = ReturnValue_0
        ReturnValue_1: FText = self.UglyFixForActorName(actorRepresentation)
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_FilterButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_FilterButton, ReturnValue_2)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_3, "mName", Ref[ReturnValue_1])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_3, "mShowOnCompass", CompassRepresentation)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_3, "mShowOnMap", MapRepresentation)
        self.Widget_Map_Filters_Container.AddChildToFilters(ReturnValue_3)
        OutputDelegate3.BindUFunction(self, OnFilterHovered)
        ReturnValue_3.OnHovered.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnFilterUnhovered)
        ReturnValue_3.OnUnhovered.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, onFilterShowOnMapChanged)
        ReturnValue_3.mShowOnMapChanged.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, onFilterShowOnCompassChanged)
        ReturnValue_3.mShowOnCompassChanged.AddUnique(OutputDelegate)
    

    def NormalizedValueToZoomValue(self, NormalizedValue: float):
        ReturnValue: float = self.Widget_Map.mMaxZoom - self.Widget_Map.mMinZoom
        ReturnValue_0: float = NormalizedValue * ReturnValue
        ReturnValue_1: float = ReturnValue_0 + self.Widget_Map.mMinZoom
        ReturnValue_2: Vector2D = Vector2D(ReturnValue_1, ReturnValue_1)
        ZoomValue = ReturnValue_2
    

    def UpdateZoomSlider(self):
        
        X = None
        Y = None
        BreakVector2D(self.Widget_Map.mMapZoomContainer.RenderTransform.Scale, Ref[X], Ref[Y])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_FloatToText(X, 0, False, True, 1, 324, 1, 1)
        FormatArgumentData.ArgumentName = "Zoom"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 435, 'Value': '{Zoom}x'}", Array)
        self.mZoomText.SetText(ReturnValue_0)
        ReturnValue_1: float = self.Widget_Map.mMaxZoom - self.Widget_Map.mMinZoom
        
        X = None
        Y = None
        BreakVector2D(self.Widget_Map.mMapZoomContainer.RenderTransform.Scale, Ref[X], Ref[Y])
        ReturnValue1: float = X - self.Widget_Map.mMinZoom
        ReturnValue_2: float = ReturnValue1 / ReturnValue_1
        self.mZoomSlider.SetValue(ReturnValue_2)
    

    def SetOpenMap(self, OpenMap: bool):
        self.IsMapOpen = OpenMap
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MapContainer(1333)
    

    def CloseMap(self):
        self.ExecuteUbergraph_Widget_MapContainer(1528)
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_MapContainer(1545)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_MapContainer(1560)
    

    def BndEvt__mZoomSlider_K2Node_ComponentBoundEvent_0_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(1674)
    

    def SetInputMode(self):
        self.ExecuteUbergraph_Widget_MapContainer(1752)
    

    def BndEvt__Widget_Map_K2Node_ComponentBoundEvent_1_OnObjectAddedToMapDispatch__DelegateSignature(self, actorRepresentation: Ptr[FGActorRepresentation], WidgetMapObject: Ptr[Widget_MapObject]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRepresentation1 = actorRepresentation #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_WidgetMapObject = WidgetMapObject #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(1860)
    

    def BndEvt__Widget_Map_K2Node_ComponentBoundEvent_2_OnObjectUpdatedOnMapDispatch__DelegateSignature(self, actorRepresentation: Ptr[FGActorRepresentation]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRepresentation = actorRepresentation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(2599)
    

    def BndEvt__Widget_Map_K2Node_ComponentBoundEvent_3_OnObjectRemovedFromMapDispatch__DelegateSignature(self, ActorRespresentation: Ptr[FGActorRepresentation]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_ActorRespresentation = ActorRespresentation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(2600)
    

    def OnFilterHovered(self, Instigator: Ptr[Widget_FilterButton]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator7 = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3215)
    

    def OnFilterUnhovered(self, Instigator: Ptr[Widget_FilterButton]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator6 = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3327)
    

    def onFilterShowOnMapChanged(self, Instigator: Ptr[Widget_FilterButton], ShowOnMap: bool):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator5 = Instigator #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ShowOnMap = ShowOnMap #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3393)
    

    def onFilterShowOnCompassChanged(self, Instigator: Ptr[Widget_FilterButton], ShowOnCompass: bool):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator4 = Instigator #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ShowOnCompass = ShowOnCompass #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3486)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_4_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapContainer(3579)
    

    def OnBeaconViewDistanceChanged(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider], NewViewDistance: uint8):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator3 = Instigator #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_NewViewDistance = NewViewDistance #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3584)
    

    def OnBeaconHovered(self, Instigaotr: Ptr[Widget_BeaconViewdistanceSlider]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigaotr = Instigaotr #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(3850)
    

    def OnBeaconUnhovered(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator2 = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(4019)
    

    def OnBeaconVeiwDistanceHovered(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider], viewDistance: uint8):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator1 = Instigator #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_ViewDistance = viewDistance #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(4188)
    

    def OnBeaconViewDistanceUnhovered(self, Instigator: Ptr[Widget_BeaconViewdistanceSlider]):
        ExecuteUbergraph_Widget_MapContainer.K2Node_CustomEvent_Instigator = Instigator #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(4366)
    

    def BndEvt__Widget_Map_Filters_Container_K2Node_ComponentBoundEvent_5_OnBeaconSearchChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_MapContainer.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapContainer(4535)
    

    def BndEvt__Widget_Map_Filters_Container_K2Node_ComponentBoundEvent_6_OnClearSearchResults__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapContainer(4559)
    

    def ExecuteUbergraph_Widget_MapContainer(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L176")
        ReturnValue1: int32 = self.GetIndexInParent(Instigator7)
        
        self.mFilterCategories[ReturnValue1].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item1 = None
        Item1 = self.mFilterCategories[ReturnValue1].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[Variable1]
        Item1.HighlightOnMap()
        goto(ExecutionFlow.Pop())
        # Label 176
        ReturnValue1_0: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_0
        # Label 245
        ReturnValue1 = self.GetIndexInParent(Instigator7)
        
        self.mFilterCategories[ReturnValue1].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        ReturnValue: int32 = len(self.mFilterCategories[ReturnValue1].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable1 = Variable1
        goto('L15')
        # Label 444
        ReturnValue_1: bool = Not_PreBool(Variable)
        Variable: bool = ReturnValue_1
        if not Variable:
            goto('L682')
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.Widget_Map_Filters_Container.PlayAnimation(self.Widget_Map_Filters_Container.SpawnAnim, 0, 1, 1, 1)
        self.mMenuButtonText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 633, 'Value': 'Show Menu'}")
        goto(ExecutionFlow.Pop())
        # Label 682
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.Widget_Map_Filters_Container.PlayAnimation(self.Widget_Map_Filters_Container.SpawnAnim, 0, 1, 0, 1)
        self.mMenuButtonText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 809, 'Value': 'Hide Menu'}")
        goto(ExecutionFlow.Pop())
        # Label 858
        ReturnValue_3: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_3
        # Label 927
        ReturnValue_4: int32 = self.GetIndexInParent(Instigator6)
        
        self.mFilterCategories[ReturnValue_4].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        ReturnValue1_2: int32 = len(self.mFilterCategories[ReturnValue_4].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333)
        ReturnValue1_3: bool = Variable_0 <= ReturnValue1_2
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        Variable_1: int32 = Variable_0
        ExecutionFlow.Push("L858")
        ReturnValue_4 = self.GetIndexInParent(Instigator6)
        
        self.mFilterCategories[ReturnValue_4].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item = None
        Item = self.mFilterCategories[ReturnValue_4].MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[Variable_1]
        Item.UnhighlightOnMap()
        goto(ExecutionFlow.Pop())
        # Label 1282
        Variable_0 = 0
        Variable_1 = 0
        goto('L927')
        OutputDelegate.BindUFunction(self, CloseMap)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.UpdateZoomSlider()
        OutputDelegate1.BindUFunction(self, UpdateZoomSlider)
        self.Widget_Map.ZoomChanged.AddUnique(OutputDelegate1)
        self.Widget_Map.ListenForInputActions(self)
        goto(ExecutionFlow.Pop())
        # Label 1513
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        goto('L1513')
        # Label 1533
        self.IsMapOpen = False
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto('L1533')
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mFilterCategories])
        self.Widget_Map_Filters_Container.mBeaconContainer.ClearChildren()
        self.ClearSearch()
        goto(ExecutionFlow.Pop())
        
        ZoomValue = None
        self.NormalizedValueToZoomValue(Value, Ref[ZoomValue])
        self.Widget_Map.ZoomMap(ZoomValue)
        goto(ExecutionFlow.Pop())
        self.SetInputMode()
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget] = self.GetDefaultFocusWidget()
        Default__WidgetBlueprintLibrary.SetInputMode_GameAndUIEx(ReturnValue_5, ReturnValue_6, 0, False)
        goto(ExecutionFlow.Pop())
        self.AddChildToBeacons(ActorRepresentation1)
        ReturnValue1_4: uint8 = ActorRepresentation1.GetRepresentationType()
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue1_4, 0)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 1)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 2)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 3)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 5)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 6)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 8)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 9)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 10)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 11)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 12)
        if not CmpSuccess:
            goto('L2474')
        CmpSuccess = NotEqual_ByteByte(ReturnValue1_4, 13)
        if not CmpSuccess:
            goto('L2474')
        goto(ExecutionFlow.Pop())
        
        CreatedNewCategory = None
        # Label 2474
        self.AddUniqueToFilterCategories(ActorRepresentation1, WidgetMapObject, Ref[CreatedNewCategory])
        if not CreatedNewCategory:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: uint8 = ActorRepresentation1.GetRepresentationType()
        self.AddChildToFilters(ReturnValue_7)
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        ReturnValue2: uint8 = ActorRespresentation.GetRepresentationType()
        CmpSuccess_0: bool = NotEqual_ByteByte(ReturnValue2, 0)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 1)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 2)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 3)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 5)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 6)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 8)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 9)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 10)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 11)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 12)
        if not CmpSuccess_0:
            goto('L3191')
        CmpSuccess_0 = NotEqual_ByteByte(ReturnValue2, 13)
        if not CmpSuccess_0:
            goto('L3191')
        goto(ExecutionFlow.Pop())
        
        ActorRespresentation = None
        # Label 3191
        self.RemoveActorRepresentationFromFilterCategories(Ref[ActorRespresentation])
        goto(ExecutionFlow.Pop())
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(Instigator7)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        Variable1 = 0
        Variable1 = 0
        goto('L245')
        ReturnValue1_5: bool = Default__KismetSystemLibrary.IsValid(Instigator6)
        if not ReturnValue1_5:
           goto(ExecutionFlow.Pop())
        goto('L1282')
        ReturnValue2_0: int32 = self.GetIndexInParent(Instigator5)
        self.SetMapRepresentation(self.mFilterCategories[ReturnValue2_0].RepresentationType_3_5D457985464D101149CAEF83656C9370, ShowOnMap)
        goto(ExecutionFlow.Pop())
        ReturnValue3: int32 = self.GetIndexInParent(Instigator4)
        self.SetCompassRepresentation(self.mFilterCategories[ReturnValue3].RepresentationType_3_5D457985464D101149CAEF83656C9370, ShowOnCompass)
        goto(ExecutionFlow.Pop())
        goto('L444')
        ReturnValue1_6: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue1_6, self, Ref[RCO])
        ReturnValue4: int32 = self.GetIndexInParent(Instigator3)
        
        BeaconCategory = None
        self.GetBeacons(Ref[BeaconCategory])
        
        BeaconCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212 = None
        Item2 = None
        Item2 = BeaconCategory.ActorRepresentation_6_2C64EC784A601AFE845DA2834D3A2212[ReturnValue4]
        RCO.Internal_Server_SetActorRepresentationCompassViewDistance(Item2, NewViewDistance)
        goto(ExecutionFlow.Pop())
        ReturnValue5: int32 = self.GetIndexInParent(Instigaotr)
        
        BeaconCategory1 = None
        self.GetBeacons(Ref[BeaconCategory1])
        
        BeaconCategory1.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item3 = None
        Item3 = BeaconCategory1.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[ReturnValue5]
        Item3.HighlightOnMap()
        goto(ExecutionFlow.Pop())
        ReturnValue6: int32 = self.GetIndexInParent(Instigator2)
        
        BeaconCategory2 = None
        self.GetBeacons(Ref[BeaconCategory2])
        
        BeaconCategory2.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item4 = None
        Item4 = BeaconCategory2.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[ReturnValue6]
        Item4.UnhighlightOnMap()
        goto(ExecutionFlow.Pop())
        ReturnValue7: int32 = self.GetIndexInParent(Instigator1)
        
        BeaconCategory3 = None
        self.GetBeacons(Ref[BeaconCategory3])
        
        BeaconCategory3.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item5 = None
        Item5 = BeaconCategory3.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[ReturnValue7]
        Item5.ShowViewDistanceIndicator(ViewDistance)
        goto(ExecutionFlow.Pop())
        ReturnValue8: int32 = self.GetIndexInParent(Instigator)
        
        BeaconCategory4 = None
        self.GetBeacons(Ref[BeaconCategory4])
        
        BeaconCategory4.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333 = None
        Item6 = None
        Item6 = BeaconCategory4.MapObject_10_E7619CDE4C223F0B26B78DA3C3602333[ReturnValue8]
        Item6.HideViewDistanceIndicator()
        goto(ExecutionFlow.Pop())
        self.PopulateSearchResults(Text)
        goto(ExecutionFlow.Pop())
        self.ClearSearch()
        goto(ExecutionFlow.Pop())
    
