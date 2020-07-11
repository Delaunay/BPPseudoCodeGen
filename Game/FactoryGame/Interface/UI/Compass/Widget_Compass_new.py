
from codegen.ue4_stub import *

from Script.FactoryGame import ERepresentationType
from Game.FactoryGame.Interface.UI.Assets.Compass.IconEast import IconEast
from Game.FactoryGame.Interface.UI.Assets.Compass.IconWest import IconWest
from Script.FactoryGame import GetRepresentationType
from Script.Engine import Delay
from Script.FactoryGame import FGCompassObjectWidget
from Game.FactoryGame.Interface.UI.Assets.Compass.IconNorth import IconNorth
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.Compass.Widget_Compass_new import ExecuteUbergraph_Widget_Compass_new
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectCardinalDirection import Widget_CompassObjectCardinalDirection
from Script.FactoryGame import Get
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import Widget_CompassObjectResource
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectBuildable import Widget_CompassObjectBuildable
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import FGGameUserSettings
from Script.FactoryGame import SubscribeToDynamicOptionUpdate
from Script.FactoryGame import Default__FGGameUserSettings
from Script.UMG import Construct
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectPing import Widget_CompassObjectPing
from Script.Engine import Conv_FloatToString
from Script.FactoryGame import FGCompassWidget
from Script.FactoryGame import FGActorRepresentationManager
from Script.FactoryGame import BindActorRepresentationManager
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import UnsubscribeToAllDynamicOptionUpdate
from Script.FactoryGame import AddAllCardinalDirections
from Game.FactoryGame.Interface.UI.Assets.Compass.IconSouth import IconSouth
from Script.FactoryGame import GetFloatOptionValue
from Script.UMG import SetRenderOpacity
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_Compass_new(FGCompassWidget):
    mThresholdForCenteredObjects = 0.30000001192092896
    mThresholdForCenteredResourceObjects = 0.5
    
    def GetCompassObjectWidgetClass(self):
        ReturnValue: uint8 = actorRepresentation.GetRepresentationType()
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue, 0)
        if not CmpSuccess:
            goto('L685')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 1)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 2)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 3)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 4)
        if not CmpSuccess:
            goto('L733')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 5)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 6)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 7)
        if not CmpSuccess:
            goto('L757')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 8)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 9)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 10)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 11)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 12)
        if not CmpSuccess:
            goto('L709')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 13)
        if not CmpSuccess:
            goto('L709')
        goto('L776')
        # Label 685
        ReturnValue_0: TSubclassOf[FGCompassObjectWidget] = Widget_CompassObjectCardinalDirection
        goto('L776')
        # Label 709
        ReturnValue_0 = Widget_CompassObjectBuildable
        goto('L776')
        # Label 733
        ReturnValue_0 = Widget_CompassObjectPing
        goto('L776')
        # Label 757
        ReturnValue_0 = Widget_CompassObjectResource
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Compass_new(278)
    

    def EventUpdateBackgroundOpacity(self):
        self.ExecuteUbergraph_Widget_Compass_new(489)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Compass_new(857)
    

    def ExecuteUbergraph_Widget_Compass_new(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.EventUpdateBackgroundOpacity()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L201')
        ReturnValue = Default__FGActorRepresentationManager.Get(self)
        self.BindActorRepresentationManager(ReturnValue)
        goto(ExecutionFlow.Pop())
        # Label 201
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 30, UUID = 1016276683, ExecutionFunction = "ExecuteUbergraph_Widget_Compass_new", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Construct()
        ExecutionFlow.Push("L357")
        self.AddAllCardinalDirections(Widget_CompassObjectCardinalDirection, IconNorth, IconEast, IconSouth, IconWest, None, None, None, None)
        goto('L30')
        # Label 357
        ReturnValue_1: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        OutputDelegate.BindUFunction(self, EventUpdateBackgroundOpacity)
        
        OutputDelegate = None
        ReturnValue_1.SubscribeToDynamicOptionUpdate("FG.CompassBGOpacity", Ref[OutputDelegate])
        goto('L15')
        ReturnValue1: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_2: float = ReturnValue1.GetFloatOptionValue("FG.CompassBGOpacity")
        self.mVisorBackground.SetRenderOpacity(ReturnValue_2)
        ReturnValue_2 = ReturnValue1.GetFloatOptionValue("FG.CompassBGOpacity")
        ReturnValue_3: FString = Default__KismetStringLibrary.Conv_FloatToString(ReturnValue_2)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_3, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue2.UnsubscribeToAllDynamicOptionUpdate(self)
        goto(ExecutionFlow.Pop())
    
