
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGBaseUI
from Script.FactoryGame import AutoLogin
from Script.FactoryGame import FGLocalPlayer
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import PeekNextError
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import PopPopupQueue
from Script.Engine import PlayerController
from Script.UMG import SetInputMode_UIOnlyEx
from Script.UMG import ESlateVisibility
from Script.Engine import GetGameInstance
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import Widget_Popup
from Script.Engine import IsValid
from Script.FactoryGame import GetPopup
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.-Shared.Audio.Music.Play_Menu_Music import Play_Menu_Music
from Script.Engine import Default__GameplayStatics
from Script.UMG import Construct
from Script.FactoryGame import GetNextError
from Script.FactoryGame import HasPlayerSeenAlphaInfoScreen
from Script.FactoryGame import GetErrorMessage
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGGameInstance
from Script.Engine import IsLoggedIn
from Script.FactoryGame import FGPopupWidget
from Script.FactoryGame import Default__FGGameInstance
from Script.FactoryGame import SetPopup
from Script.UMG import Create
from Script.AkAudio import AkComponent
from Script.Engine import QuitGame
from Game.FactoryGame.Interface.UI.Menu.BP_FrontEnd import ExecuteUbergraph_BP_FrontEnd
from Script.Engine import GameInstance
from Script.FactoryGame import FGErrorMessage
from Script.Engine import LocalPlayer

class BP_FrontEnd(FGBaseUI):
    mLastErrorMessage: Ptr[FGErrorMessage]
    mShouldQuitAfterErrors: bool
    mPopupClass: TSubclassOf[Widget_Popup]
    
    def CreatePopupWidget(self):
        Popup: TSubclassOf[Widget_Popup] = ClassCast[Widget_Popup](PopupData.PopupClass)
        bSuccess: bool = Popup
        if not bSuccess:
            goto('L528')
        self.mPopupClass = Popup
        # Label 107
        self.mPopupBlur.SetBlurStrength(1)
        self.mPopupModal.SetVisibility(0)
        # Label 186
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_Popup] = Default__WidgetBlueprintLibrary.Create(self, self.mPopupClass, ReturnValue)
        ReturnValue_0.mPopupData = PopupData
        ReturnValue_1: Ptr[PanelSlot] = self.mPopupSlot.AddChild(ReturnValue_0)
        ReturnValue = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue, ReturnValue_0, 0)
        ReturnValue = self.GetOwningPlayer()
        ReturnValue.bShowMouseCursor = True
        ReturnValue_2: Ptr[FGPopupWidget] = ReturnValue_0
        goto('L552')
        # Label 528
        self.mPopupClass = Widget_Popup
        goto('L107')
    

    def ShouldShutdown(self):
        Shutdown = False
    

    def GetErrorButtonText(self):
        
        shutdown = None
        self.ShouldShutdownAfterThisError(Ref[shutdown])
        if not shutdown:
            goto('L108')
        ButtonText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 57, 'Value': 'Shutdown'}"
        # End
        
        moreErrors = None
        # Label 108
        self.HasMoreErrors(Ref[moreErrors])
        if not moreErrors:
            goto('L218')
        ButtonText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 165, 'Value': 'Next Error'}"
        # End
        # Label 218
        ButtonText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 238, 'Value': 'Ok'}"
    

    def HasMoreErrors(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGErrorMessage] = Default__FGGameInstance.PeekNextError(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        moreErrors = ReturnValue_1
    

    def ShouldShutdownAfterThisError(self):
        
        moreErrors = None
        self.HasMoreErrors(Ref[moreErrors])
        ReturnValue: bool = Not_PreBool(moreErrors)
        ReturnValue_0: bool = ReturnValue and self.mShouldQuitAfterErrors
        Shutdown = ReturnValue_0
    

    def Internal_ShouldShowLogin(self):
        ShouldShow = False
    

    def ShouldShowLogin(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        shouldShow = None
        self.Internal_ShouldShowLogin(Ref[shouldShow])
        Variable_0: bool = shouldShow
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def SetNextErrorMessage(self, newError: Ptr[FGErrorMessage]):
        self.mLastErrorMessage = newError
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mLastErrorMessage)
        if not ReturnValue:
            goto('L258')
        self.mShouldQuitAfterErrors = False
        
        buttonText = None
        self.GetErrorButtonText(Ref[buttonText])
        self.Widget_ErrorMessage.SetButtonText(buttonText)
        ReturnValue_0: FText = self.mLastErrorMessage.GetErrorMessage()
        self.Widget_ErrorMessage.SetBody(ReturnValue_0)
    

    def GetNextErrorMessage(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGErrorMessage] = Default__FGGameInstance.GetNextError(ReturnValue)
        errorMessage = ReturnValue_0
    

    def Internal_ShowErrorMessage(self):
        ShouldShow = False
    

    def Internal_ShouldShowMainMenu(self):
        
        shouldShow = None
        self.Internal_ShowErrorMessage(Ref[shouldShow])
        
        shouldShow = None
        self.Internal_ShouldShowAlphaInfo(Ref[shouldShow])
        ReturnValue: bool = Not_PreBool(shouldShow)
        ReturnValue1: bool = Not_PreBool(shouldShow)
        ReturnValue_0: bool = ReturnValue1 and ReturnValue
        ShouldShow = ReturnValue_0
    

    def Internal_ShouldShowAlphaInfo(self):
        showAlphaInfo: bool = True
        ReturnValue: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue)
        bSuccess: bool = Instance
        if not bSuccess:
            goto('L223')
        ReturnValue_0: bool = Instance.HasPlayerSeenAlphaInfoScreen()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        showAlphaInfo = ReturnValue_1
        # Label 223
        ShouldShow = showAlphaInfo
    

    def ShouldShowErrorPopup(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        shouldShow = None
        self.Internal_ShowErrorMessage(Ref[shouldShow])
        Variable_0: bool = shouldShow
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def ShouldShowMainMenu(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        shouldShow = None
        self.Internal_ShouldShowMainMenu(Ref[shouldShow])
        Variable_0: bool = shouldShow
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def ShouldShowAlphaInfo(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        shouldShow = None
        self.Internal_ShouldShowAlphaInfo(Ref[shouldShow])
        Variable_0: bool = shouldShow
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def SetupMainMenu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue.bShowMouseCursor = True
        ReturnValue = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue, None, 0)
    

    def Construct(self):
        self.ExecuteUbergraph_BP_FrontEnd(1235)
    

    def BndEvt__Widget_ErrorMessage_K2Node_ComponentBoundEvent_0_mOnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_FrontEnd(15)
    

    def GetAndSetNewError(self):
        self.ExecuteUbergraph_BP_FrontEnd(552)
    

    def ConditionallySetNewError(self):
        self.ExecuteUbergraph_BP_FrontEnd(599)
    

    def Destruct(self):
        self.ExecuteUbergraph_BP_FrontEnd(931)
    

    def ClosePopup(self):
        self.ExecuteUbergraph_BP_FrontEnd(1240)
    

    def ExecuteUbergraph_BP_FrontEnd(self):
        goto(ComputedJump("EntryPoint"))
        self.GetAndSetNewError()
        
        shutdown = None
        self.ShouldShutdown(Ref[shutdown])
        if not shutdown:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.QuitGame(self, None, 0, False)
        goto(ExecutionFlow.Pop())
        # Label 100
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Menu_Music, ReturnValue, True)
        goto(ExecutionFlow.Pop())
        # Label 186
        ReturnValue_1: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue_1)
        bSuccess: bool = Instance
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, ConditionallySetNewError)
        Instance.mOnNewError.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 369
        ReturnValue1: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance1: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue1)
        bSuccess1: bool = Instance1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, ConditionallySetNewError)
        Instance1.mOnNewError.Remove(OutputDelegate)
        goto(ExecutionFlow.Pop())
        
        errorMessage = None
        # Label 552
        self.GetNextErrorMessage(Ref[errorMessage])
        self.SetNextErrorMessage(errorMessage)
        goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mLastErrorMessage)
        if not ReturnValue_2:
            goto('L665')
        goto(ExecutionFlow.Pop())
        # Label 665
        self.GetAndSetNewError()
        goto(ExecutionFlow.Pop())
        # Label 680
        self.ConditionallySetNewError()
        ExecutionFlow.Push("L100")
        ExecutionFlow.Push("L709")
        goto('L186')
        # Label 709
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsLoggedIn(ReturnValue1_0)
        if not ReturnValue_3:
            goto('L799')
        goto(ExecutionFlow.Pop())
        # Label 799
        ReturnValue_4: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue_4)
        bSuccess2: bool = Player
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Player.AutoLogin()
        goto(ExecutionFlow.Pop())
        goto('L369')
        # Label 936
        ReturnValue_5: Ptr[FGPopupWidget] = self.GetPopup()
        ReturnValue_5.RemoveFromParent()
        self.SetPopup(None)
        self.mPopupBlur.SetBlurStrength(0)
        self.mPopupModal.SetVisibility(2)
        self.mPopupSlot.ClearChildren()
        goto(ExecutionFlow.Pop())
        # Label 1119
        ReturnValue_5 = self.GetPopup()
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_5)
        if not ReturnValue1_1:
            goto('L1209')
        goto('L936')
        # Label 1209
        self.PopPopupQueue()
        goto(ExecutionFlow.Pop())
        # Label 1220
        self.Construct()
        goto('L680')
        goto('L1220')
        goto('L1119')
    
