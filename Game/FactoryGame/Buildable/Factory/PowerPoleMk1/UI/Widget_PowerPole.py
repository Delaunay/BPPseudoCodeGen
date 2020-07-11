
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import GetPowerCircuit
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import FGPowerCircuit
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Audio.PowerStatus.Play_UI_PowerLossWarning_ResetFuse import Play_UI_PowerLossWarning_ResetFuse
from Script.FactoryGame import IsFuseTriggered
from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.UI.Widget_PowerPole import ExecuteUbergraph_Widget_PowerPole
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import FGBuildablePowerPole
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import GetCircuitID
from Script.AkAudio import AkComponent

class Widget_PowerPole(Widget_UseableBase):
    mPowerPole: Ptr[FGBuildablePowerPole]
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    Priority = 10
    
    def UpdateHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def GetFuseVisibility(self):
        ReturnValue: Ptr[FGPowerCircuit] = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L230')
        ReturnValue = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue_1: bool = ReturnValue.IsFuseTriggered()
        if not ReturnValue_1:
            goto('L230')
        ReturnValue_2: uint8 = 4
        goto('L250')
        # Label 230
        ReturnValue_2 = 1
    

    def OnGetPowerCircuit(self):
        ReturnValue: Ptr[FGPowerCircuit] = self.mPowerPole.GetPowerCircuit()
        ReturnValue_0: Ptr[FGPowerCircuit] = ReturnValue
    

    def IsConnected(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPowerPole)
        if not ReturnValue:
            goto('L177')
        ReturnValue_0: Ptr[FGPowerCircuit] = self.mPowerPole.GetPowerCircuit()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        IsConnected = ReturnValue1
    

    def Cleanup(self):
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def GetPowerCircuitGraphVisibility(self):
        
        IsConnected = None
        self.IsConnected(Ref[IsConnected])
        if not IsConnected:
            goto('L62')
        ReturnValue = 0
        goto('L82')
        # Label 62
        ReturnValue = 1
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PowerPole(700)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PowerPole(270)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_PowerPole(285)
    

    def ResetFuse(self):
        self.ExecuteUbergraph_Widget_PowerPole(705)
    

    def ExecuteUbergraph_Widget_PowerPole(self):
        # Label 10
        self.UpdateHeaderText()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, ResetFuse)
        self.Widget_Fusebox.ResetFuse.AddUnique(OutputDelegate1)
        # End
        # Label 157
        self.Init()
        Pole: Ptr[FGBuildablePowerPole] = Cast[FGBuildablePowerPole](self.mInteractObject)
        bSuccess: bool = Pole
        if not bSuccess:
            goto('L710')
        self.mPowerPole = Pole
        # End
        self.Construct()
        goto('L10')
        self.Destruct()
        self.Cleanup()
        # End
        # Label 314
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_PowerLossWarning_ResetFuse, ReturnValue, True)
        # End
        # Label 404
        ReturnValue = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L710')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2: Ptr[FGPowerCircuit] = self.mPowerCircuitGraph.GetPowerCircuit()
        ReturnValue_3: int32 = ReturnValue_2.GetCircuitID()
        ReturnValue_1.Server_ResetFuse(ReturnValue_3)
        goto('L314')
        goto('L157')
        goto('L404')
    
