
from codegen.ue4_stub import *

from Script.FactoryGame import GetActionMappings
from Script.Engine import SetObjectPropertyByName
from Script.UMG import AddChildToVerticalBox
from Script.FactoryGame import GetAxisMappings
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import ResetInputBindings
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.FactoryGame import AxisMappingDisplayName
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.Menu.KeyBindData import KeyBindData
from Script.FactoryGame import Default__FGOptionsSettings
from Script.FactoryGame import FGPlayerControllerBase
from Game.FactoryGame.Interface.UI.Menu.Widget_KeybindButton import Widget_KeybindButton
from Script.UMG import UserWidget
from Script.FactoryGame import ActionMappingDisplayName
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_KeyBind import ExecuteUbergraph_Widget_KeyBind

class Widget_KeyBind(UserWidget):
    localController: Ptr[FGPlayerControllerBase]
    mOwningWidget: Ptr[BP_MenuBase]
    mKeyInputsData: List[KeyBindData] = [{'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'MoveForward', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "DB4EF4754BBF422EDB76819CB4AC0F3C", "Move Forward")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True, 'PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'MoveForward', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "E2F312854BBD21227CFEB6AD6280983F", "Move Backward")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'MoveRight', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "5FAB3C0B4BD0B7392CC48FBFEDB79767", "Move Right")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True, 'PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'MoveRight', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "7963380E496019A61DB83798F022DD92", "Move Left")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'TurnRate', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "B1991B4D402AE20F12461EBA637E1C84", "Turn Right")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True, 'PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'TurnRate', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "D2144B7D4A692330810167B22E9F548C", "Turn Left")', 'AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF': True}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Jump_Drift', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "D8C6B26341DFCF833356338F132FFF9E", "Jump / Vehicle Handbrake")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Crouch', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "63A94CB846DD9B11AF3855BA39E87813", "Crouch")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'PrimaryFire', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "3A0CA824468DCA9335E735BAFDD12328", "Primary Fire")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'SecondaryFire', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "8AD73DBB45E85B99CE4078BE21E4E01D", "Secondary Fire")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Use', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "4BBA51424EB03245A0D9E8871FC5D099", "Interact")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'ToggleBuildGun', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "847946924AA62DDA5C7D129134101CE0", "Build Menu")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'inventory', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "C1C9A02A456A94523A3B96A85E4EAA5F", "Inventory")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'AttentionPing', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "F0A2220A403C04AB4F26C2833382108A", "Ping")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'ResourceScanner_ToggleVehicleRecording', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "AD9383A24690D2C6165011AD4B6704AE", "Resource Scanner / Vehicle Menu")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'EmoteWheel', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "0FDE97F24DDCAB034B5D288B87D13FBC", "Emote Wheel")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Reload', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "F4F70B4347945FFA50864CA626425EF4", "Weapon Reload / Change Spline Build Mode")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'ToggleSprint', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "6F9FCDBE4CB5C68F66E14BAD571D6F6B", "Sprint")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'BuildGunScrollUp_PhotoModeFOVUp', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "9258CFC942A76EB8C2DCE38E0DDC271F", "Rotate Hologram Right / Increase Photo FOV")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'BuildGunScrollDown_PhotoModeFOVDown', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "0CD9B43143A889F460F7399AD27CAFBC", "Rotate Hologram Left / Decrease Photo FOV")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'ToggleDismantle', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "19D81AAE4EFD9A23443FE29B821A6376", "Dismantle")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'ToggleMap_BuildGunNoSnapMode', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "0FD08D2A47060620FC2AA5A1EB818405", "Open Map")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'OpenCodex', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "B29B57A84B2B748B5A0367B5262523DE", "Open Codex")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Flashlight', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "9066B6D248AD250B8269D29911F07191", "Flashlight")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Chat', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "DE84A1AF46516BAEC00E2188DA5EDA3C", "Open Chat")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'BuildGunSnapToGuideLines', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "29E361CB4D47F213078B58ABBE0C5050", "Build Gun Snap To Guide Lines")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'PhotoMode', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "A41CED614F96EEC862CA2AB0059A7893", "Open Photo Mode")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'TogglePhotoModeUIVisibility', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "8739AEB44956DE9054554D88FFCA7194", "Toggle Photo Mode UI Visibilty")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'BuildingSample', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "3063E9A14C5B907358C144A2FA4579D8", "Building Eyedropper")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut1', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "637670034DEF4EE3424F1F8828744D19", "Shortcut1")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut2', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "21C89FA443B0BCDE7767E0841F91B6CE", "Shortcut2")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut3', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "0997773D401C38618EAEF19E571F07E7", "Shortcut3")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut4', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "CD8819544617F3DDD2026D9587862EA6", "Shortcut4")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut5', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "7239367045172D57AA0C1B95FDD22F49", "Shortcut5")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut6', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "DAE6CA6D4D7EA585BD7EE28EA375E452", "Shortcut6")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut7', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "9B22BDB74084A1287F05909E664C3DA5", "Shortcut7")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut8', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "A55A435D47A660B3D497599E3EB7ADBD", "Shortcut8")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut9', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "690ADDF6417F67C64D25EBA0319CA510", "Shortcut9")'}, {'ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885': 'Shortcut10', 'DisplayName_5_0A86F675465E0C811D17A287BB986630': 'NSLOCTEXT("", "DEF297A34204BC0380F8BEA121BDF2D8", "Shortcut10")'}]
    
    def GetKeybindData(self):
        ExecutionFlow.Push("L1442")
        ExecutionFlow.Push("L1336")
        # Label 10
        ExecutionFlow.Push("L767")
        AxisMappingDisplayName: List[AxisMappingDisplayName] = []
        
        Default__FGOptionsSettings.GetAxisMappings(Ref[AxisMappingDisplayName])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 113
        ReturnValue1: int32 = len(AxisMappingDisplayName)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1368")
        
        Item = None
        Item = AxisMappingDisplayName[Variable_0]
        KeyBindData1.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885 = Item.AxisMappingName
        KeyBindData1.DisplayName_5_0A86F675465E0C811D17A287BB986630 = Item.DisplayNamePositiveScale
        KeyBindData1.AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF = True
        KeyBindData1.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6 = True
        
        KeyBindData1 = None
        ReturnValue1_1: int32 = localKeyBindData.append(KeyBindData1)
        
        Item = None
        Item = AxisMappingDisplayName[Variable_0]
        KeyBindData.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885 = Item.AxisMappingName
        KeyBindData.DisplayName_5_0A86F675465E0C811D17A287BB986630 = Item.DisplayNameNegativeScale
        KeyBindData.AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF = True
        KeyBindData.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6 = False
        
        KeyBindData = None
        ReturnValue2: int32 = localKeyBindData.append(KeyBindData)
        goto(ExecutionFlow.Pop())
        # Label 767
        ActionMappingDisplayName: List[ActionMappingDisplayName] = []
        
        Default__FGOptionsSettings.GetActionMappings(Ref[ActionMappingDisplayName])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 865
        ReturnValue: int32 = len(ActionMappingDisplayName)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1262")
        
        Item1 = None
        Item1 = ActionMappingDisplayName[Variable1_0]
        KeyBindData2.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885 = Item1.ActionMappingName
        KeyBindData2.DisplayName_5_0A86F675465E0C811D17A287BB986630 = Item1.DisplayName
        KeyBindData2.AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF = False
        KeyBindData2.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6 = False
        
        KeyBindData2 = None
        ReturnValue_1: int32 = localKeyBindData.append(KeyBindData2)
        goto(ExecutionFlow.Pop())
        # Label 1262
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L865')
        # Label 1336
        KeyBindData = localKeyBindData
        # End
        # Label 1368
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L113')
    

    def RefreshKeyBindings(self):
        ExecutionFlow.Push("L637")
        self.mButtonBox.ClearChildren()
        
        KeyBindData = None
        self.GetKeybindData(Ref[KeyBindData])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        KeyBindData = None
        # Label 110
        ReturnValue: int32 = len(KeyBindData)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L563")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_KeybindButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_KeybindButton, ReturnValue_1)
        
        KeyBindData = None
        Item = None
        Item = KeyBindData[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mKeyBindData", Ref[Item])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mKeyBindParent", self)
        ReturnValue_3: Ptr[VerticalBoxSlot] = self.mButtonBox.AddChildToVerticalBox(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 563
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L110')
    

    def Init(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L181')
        OutputDelegate.BindUFunction(self, RefreshKeyBindings)
        Base.OnInputChanged.AddUnique(OutputDelegate)
        self.RefreshKeyBindings()
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_KeyBind(29)
    

    def DefaultBindings(self):
        self.ExecuteUbergraph_Widget_KeyBind(48)
    

    def BndEvt__mResetButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_KeyBind(207)
    

    def ExecuteUbergraph_Widget_KeyBind(self):
        # Label 10
        self.RefreshKeyBindings()
        # End
        self.Init()
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L212')
        Base.ResetInputBindings()
        goto('L10')
        # Label 188
        self.DefaultBindings()
        # End
        goto('L188')
    
