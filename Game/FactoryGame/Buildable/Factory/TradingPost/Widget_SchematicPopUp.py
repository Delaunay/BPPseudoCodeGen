
from codegen.ue4_stub import *

from Script.FactoryGame import FGStingerWidgetRewardData
from Script.Engine import Conv_TextToString
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture2D
from Script.Engine import Delay
from Script.UMG import HorizontalBoxSlot
from Script.FactoryGame import GetItemIcon
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.Audio.UpgradeVisuals.Play_UI_UnlockUpgradeJuice_Whoosh import Play_UI_UnlockUpgradeJuice_Whoosh
from Game.FactoryGame.Unlocks.BPI_UnlockableInterface import BPI_UnlockableInterface
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicPopUp import ExecuteUbergraph_Widget_SchematicPopUp.K2Node_CustomEvent_Schematic
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.FactoryGame import GetIconText
from Script.FactoryGame import GetType
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGUnlock
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.FactoryGame import GetUnlocks
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetIconTexture
from Script.Engine import Set_AddItems
from Game.FactoryGame.Interface.UI.Audio.UpgradeVisuals.Play_UI_UnlockUpgradeJuice_Lead import Play_UI_UnlockUpgradeJuice_Lead
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_StingerSmallIcon import Widget_StingerSmallIcon
from Script.FactoryGame import FGSchematic
from Script.Engine import Set_Clear
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicPopUp import ExecuteUbergraph_Widget_SchematicPopUp
from Script.FactoryGame import ESchematicType
from Script.UMG import UserWidget
from Script.UMG import AddChildToHorizontalBox
from Script.Engine import Set_ToArray
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.FactoryGame import Default__FGStingerWidgetRewardData
from Script.Engine import Default__BlueprintSetLibrary
from Script.SlateCore import SlateBrush
from Script.UMG import SetVerticalAlignment
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager
from Script.FactoryGame import GetSchematicDisplayName

class Widget_SchematicPopUp(UserWidget):
    mSchematic: TSubclassOf[FGSchematic]
    mIconTexture: Ptr[Object]
    
    def CreateRewardIcon(self, Icon: Ptr[Texture], Icon Text: FText):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_StingerSmallIcon] = Default__WidgetBlueprintLibrary.Create(self, Widget_StingerSmallIcon, ReturnValue)
        ReturnValue_1: Ptr[HorizontalBoxSlot] = self.Widget_Stinger.SmallIconsContainer.AddChildToHorizontalBox(ReturnValue_0)
        ReturnValue_1.SetVerticalAlignment(2)
        ReturnValue_0.mRewardText.SetText(Icon Text)
        ReturnValue_0.mRewardText.SetText(Icon Text)
        SlateBrush1.ImageSize = ReturnValue_0.mNewIconImage.Brush.ImageSize
        SlateBrush1.Margin = ReturnValue_0.mNewIconImage.Brush.Margin
        SlateBrush1.TintColor = ReturnValue_0.mNewIconImage.Brush.TintColor
        SlateBrush1.ResourceObject = Icon
        SlateBrush1.DrawAs = ReturnValue_0.mNewIconImage.Brush.DrawAs
        SlateBrush1.Tiling = ReturnValue_0.mNewIconImage.Brush.Tiling
        SlateBrush1.Mirroring = ReturnValue_0.mNewIconImage.Brush.Mirroring
        
        SlateBrush1 = None
        ReturnValue_0.mNewIconImage.SetBrush(Ref[SlateBrush1])
        SlateBrush.ImageSize = ReturnValue_0.mNewIconImage.Brush.ImageSize
        SlateBrush.Margin = ReturnValue_0.mNewIconImage.Brush.Margin
        SlateBrush.TintColor = ReturnValue_0.mNewIconImage.Brush.TintColor
        SlateBrush.ResourceObject = Icon
        SlateBrush.DrawAs = ReturnValue_0.mNewIconImage.Brush.DrawAs
        SlateBrush.Tiling = ReturnValue_0.mNewIconImage.Brush.Tiling
        SlateBrush.Mirroring = ReturnValue_0.mNewIconImage.Brush.Mirroring
        
        SlateBrush = None
        ReturnValue_0.mNewIconImage.SetBrush(Ref[SlateBrush])
    

    def GenerateSchematicRewardIcons(self, RelevantRewardTypes: Set[TSubclassOf[FGStingerWidgetRewardData]]):
        ExecutionFlow.Push("L594")
        self.Widget_Stinger.SmallIconsContainer.ClearChildren()
        Result: List[TSubclassOf[FGStingerWidgetRewardData]] = []
        
        Default__BlueprintSetLibrary.Set_ToArray(Ref[RelevantRewardTypes], Ref[Result])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 170
        ReturnValue: int32 = len(Result)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L515')
        Variable_0 = Variable
        ExecutionFlow.Push("L520")
        
        Item = None
        Item = Result[Variable_0]
        # Label 372
        ReturnValue_1: Ptr[Texture2D] = Default__FGStingerWidgetRewardData.GetIconTexture(Item)
        ReturnValue_2: FText = Default__FGStingerWidgetRewardData.GetIconText(Item)
        self.CreateRewardIcon(ReturnValue_1, ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 515
        # End
        # Label 520
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L170')
    

    def GetRelevantRewardData(self):
        ExecutionFlow.Push("L760")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(self.mSchematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L608')
        Variable_0 = Variable
        ExecutionFlow.Push("L640")
        ReturnValue = Default__FGSchematic.GetUnlocks(self.mSchematic)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Interface: TScriptInterface[BPI_UnlockableInterface] = QueryInterface[BPI_UnlockableInterface](Item)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L714')
        
        StingerRewardTypes = None
        GetInterfaceUObject(Interface).GetStingerWidgetRewardData(Ref[StingerRewardTypes])
        # Label 496
        Result: List[TSubclassOf[FGStingerWidgetRewardData]] = []
        
        StingerRewardTypes = None
        Default__BlueprintSetLibrary.Set_ToArray(Ref[StingerRewardTypes], Ref[Result])
        
        Default__BlueprintSetLibrary.Set_AddItems(Ref[LocalStingerWidgetRewardData], Ref[Result])
        goto(ExecutionFlow.Pop())
        # Label 608
        RelevantRewardTypes = LocalStingerWidgetRewardData
        # End
        # Label 640
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
        
        StingerRewardTypes = None
        # Label 714
        Default__BlueprintSetLibrary.Set_Clear(Ref[StingerRewardTypes])
        goto('L496')
    

    def Set Stinger Content(self):
        ReturnValue: uint8 = Default__FGSchematic.GetType(self.mSchematic)
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue, 0)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 2)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 3)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 4)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 5)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 6)
        if not CmpSuccess:
            goto('L379')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 7)
        if not CmpSuccess:
            goto('L379')
        # End
        # Label 379
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.mSchematic)
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        self.Widget_Stinger.mTitleText.SetTitle(ReturnValue_1)
        Variable: FString = ""
        Variable1: FString = ""
        Variable2: FString = "SCHEMATIC PURCHASED"
        Variable3: FString = "RESEARCH FINISHED"
        Variable4: FString = "MILESTONE UNLOCKED"
        Variable5: FString = "ALTERNATE RECIPE UNLOCKED"
        Variable6: FString = "MILESTONE UNLOCKED"
        Variable7: FString = "MILESTONE UNLOCKED"
        Variable8: FString = ""
        Variable9: FString = "MILESTONE UNLOCKED"
        ReturnValue1: uint8 = Default__FGSchematic.GetType(self.mSchematic)
        Variable_0: uint8 = ReturnValue1
        
        switch = {
            0: Variable9,
            1: Variable8,
            2: Variable7,
            3: Variable6,
            4: Variable5,
            5: Variable4,
            6: Variable3,
            7: Variable2,
            8: Variable1,
            9: Variable
        }
        self.Widget_Stinger.mUnlockedText.SetTitle(switch.get(Variable_0, None))
        ReturnValue_2: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSchematic)
        self.mIconTexture = ReturnValue_2.ResourceObject
        SlateBrush.ImageSize = self.Widget_Stinger.mNewIcon.Brush.ImageSize
        SlateBrush.Margin = self.Widget_Stinger.mNewIcon.Brush.Margin
        SlateBrush.TintColor = self.Widget_Stinger.mNewIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mIconTexture
        SlateBrush.DrawAs = self.Widget_Stinger.mNewIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_Stinger.mNewIcon.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_Stinger.mNewIcon.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_Stinger.mNewIcon.SetBrush(Ref[SlateBrush])
        
        RelevantRewardTypes = None
        self.GetRelevantRewardData(Ref[RelevantRewardTypes])
        self.GenerateSchematicRewardIcons(RelevantRewardTypes)
    

    def GetSchematicUnlockedText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mSchematic)
        # Label 51
        if not ReturnValue:
            goto('L156')
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.mSchematic)
        ReturnValue_1: FText = ReturnValue_0
        goto('L176')
        # Label 156
        ReturnValue_1 = 
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SchematicPopUp(795)
    

    def OnSchematicPurchased(self, schematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_SchematicPopUp.K2Node_CustomEvent_Schematic = schematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SchematicPopUp(800)
    

    def ExecuteUbergraph_Widget_SchematicPopUp(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue2)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L295')
        OutputDelegate.BindUFunction(self, OnSchematicPurchased)
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue = Default__FGSchematicManager.Get(ReturnValue2)
        ReturnValue.PurchasedSchematicDelegate.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 295
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = 1259136128, ExecutionFunction = "ExecuteUbergraph_Widget_SchematicPopUp", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 372
        if not Variable:
            goto('L387')
        goto(ExecutionFlow.Pop())
        # Label 387
        Variable: bool = True
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UnlockUpgradeJuice_Lead, ReturnValue_1, True)
        Default__KismetSystemLibrary.Delay(self, 2.799999952316284, LatentActionInfo(Linkage = 560, UUID = -511523248, ExecutionFunction = "ExecuteUbergraph_Widget_SchematicPopUp", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UnlockUpgradeJuice_Whoosh, ReturnValue1, True)
        Default__KismetSystemLibrary.Delay(self, 5, LatentActionInfo(Linkage = 722, UUID = -1318111521, ExecutionFunction = "ExecuteUbergraph_Widget_SchematicPopUp", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Variable = False
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 745
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 757
        ExecutionFlow.Push("L372")
        if not Variable_0:
            goto('L777')
        goto(ExecutionFlow.Pop())
        # Label 777
        Variable_0 = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L745')
        goto('L15')
        self.mSchematic = Schematic
        self.Set Stinger Content()
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.Widget_Stinger.PlayAnimation(self.Widget_Stinger.SpawnAnimation, 0, 1, 0, 1)
        self.Content.SetVisibility(0)
        self.Widget_Stinger.ShowSmallIcons()
        goto('L757')
    
