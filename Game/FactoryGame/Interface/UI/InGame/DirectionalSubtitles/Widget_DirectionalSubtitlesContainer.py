
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Map_Contains
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.UMG import GetChildrenCount
from Script.UMG import AddChildToVerticalBox
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Array_Find
from Script.Engine import Map_Remove
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import PlayerController
from Script.UMG import SetHorizontalAlignment
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import SetFloatPropertyByName
from Script.Engine import SetBoolPropertyByName
from Script.UMG import Widget
from Script.UMG import UserWidget
from Script.Engine import Map_Find
from Script.Engine import Map_Add
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.UMG import VerticalBoxSlot
from Script.Engine import GetDistanceTo
from Script.UMG import Create
from Script.Engine import Map_Keys
from Script.Engine import Default__BlueprintMapLibrary
from Game.FactoryGame.Interface.UI.InGame.DirectionalSubtitles.Widget_DirectionalSubtitles import Widget_DirectionalSubtitles

class Widget_DirectionalSubtitlesContainer(UserWidget):
    mActiveActors: Dict[Ptr[Actor], Widget_DirectionalSubtitles*]
    
    def StopSubtitle(self, Instigator: Const[Ref[Ptr[Actor]]]):
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mActiveActors], Ref[Instigator], Ref[Value])
        if not ReturnValue:
            goto('L248')
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mActiveActors], Ref[Instigator], Ref[Value])
        Value.ForceDestroySubtitle()
        
        ReturnValue_0: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mActiveActors], Ref[Instigator])
    

    def GetFurthestActor(self):
        ExecutionFlow.Push("L1496")
        Keys: List[Ptr[Actor]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mActiveActors], Ref[Keys])
        Variable: bool = False
        Variable_0: int32 = 0
        Variable1: int32 = 0
        # Label 123
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue1: int32 = len(Keys)
        ReturnValue1_0: bool = Variable_0 <= ReturnValue1
        ReturnValue_0: bool = ReturnValue and ReturnValue1_0
        if not ReturnValue_0:
            goto('L887')
        Variable1 = Variable_0
        ExecutionFlow.Push("L1220")
        
        Item1 = None
        Item1 = Keys[Variable1]
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(Item1)
        if not ReturnValue_1:
            goto('L1294')
        
        Item1 = None
        Item1 = Keys[Variable1]
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_3: float = Item1.GetDistanceTo(ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3 > localDistance
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = Keys[Variable1]
        ReturnValue_2 = self.GetOwningPlayerPawn()
        ReturnValue_3 = Item1.GetDistanceTo(ReturnValue_2)
        localDistance = ReturnValue_3
        
        Item1 = None
        Item1 = Keys[Variable1]
        localActor = Item1
        goto(ExecutionFlow.Pop())
        # Label 887
        Variable1_0: int32 = 0
        Variable_1: int32 = 0
        
        # Label 933
        ReturnValue_5: int32 = len(localNullActors)
        ReturnValue_6: bool = Variable1_0 <= ReturnValue_5
        if not ReturnValue_6:
            goto('L1196')
        Variable_1 = Variable1_0
        ExecutionFlow.Push("L1422")
        
        Item = None
        Item = localNullActors[Variable_1]
        
        Item = None
        ReturnValue_7: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mActiveActors], Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 1196
        Actor = localActor
        # End
        # Label 1220
        ReturnValue_8: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_8
        goto('L123')
        
        Item1 = None
        # Label 1294
        Item1 = Keys[Variable1]
        
        Item1 = None
        ReturnValue_9: int32 = localNullActors.append(Item1)
        goto(ExecutionFlow.Pop())
        # Label 1422
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L933')
    

    def OnSubtitleDestruct(self, InstigatingSubtitle: Ptr[Widget_DirectionalSubtitles]):
        
        InstigatingSubtitle.mInstigator = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mActiveActors], Ref[InstigatingSubtitle.mInstigator])
        InstigatingSubtitle.OnDestruct.Clear()
    

    def CreateSubtitle(self, Subtitle: FText, Instigator: Ptr[Actor], Duration: float, UseDuration: bool):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: float = Instigator.GetDistanceTo(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0 <= 3000
        if not ReturnValue_1:
            goto('L1598')
        
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Contains(Ref[self.mActiveActors], Ref[Instigator])
        if not ReturnValue_2:
            goto('L528')
        Keys: List[Ptr[Actor]] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mActiveActors], Ref[Keys])
        
        ReturnValue_3: int32 = Default__KismetArrayLibrary.Array_Find(Ref[Keys], Ref[Instigator])
        ReturnValue_4: Ptr[Widget] = self.mContainer.GetChildAt(ReturnValue_3)
        Subtitles: Ptr[Widget_DirectionalSubtitles] = Cast[Widget_DirectionalSubtitles](ReturnValue_4)
        bSuccess: bool = Subtitles
        if not bSuccess:
            goto('L1598')
        Subtitles.UpdateSubtitle(Subtitle, Duration, UseDuration)
        # End
        # Label 528
        ReturnValue_5: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_6: bool = ReturnValue_5 <= 4
        if not ReturnValue_6:
            goto('L1176')
        # Label 626
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[Widget_DirectionalSubtitles] = Default__WidgetBlueprintLibrary.Create(self, Widget_DirectionalSubtitles, ReturnValue_7)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_8, "mSubtitle", Ref[Subtitle])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_8, "mInstigator", Instigator)
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_8, "mDuration", Duration)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_8, "mUseDuration", UseDuration)
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mActiveActors], Ref[Instigator], Ref[ReturnValue_8])
        ReturnValue_9: Ptr[VerticalBoxSlot] = self.mContainer.AddChildToVerticalBox(ReturnValue_8)
        ReturnValue_9.SetHorizontalAlignment(2)
        OutputDelegate.BindUFunction(self, OnSubtitleDestruct)
        ReturnValue_8.OnDestruct.AddUnique(OutputDelegate)
        # End
        
        Actor = None
        # Label 1176
        self.GetFurthestActor(Ref[Actor])
        FurthestActor = Actor
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: float = FurthestActor.GetDistanceTo(ReturnValue1)
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue2_0: float = Instigator.GetDistanceTo(ReturnValue2)
        ReturnValue_10: bool = ReturnValue2_0 <= ReturnValue1_0
        if not ReturnValue_10:
            goto('L1598')
        
        Value = None
        ReturnValue_11: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mActiveActors], Ref[FurthestActor], Ref[Value])
        Value.RemoveFromParent()
        
        ReturnValue_12: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mActiveActors], Ref[FurthestActor])
        goto('L626')
    
