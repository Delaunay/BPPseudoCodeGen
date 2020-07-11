
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.AkAudio import PostAkEvent
from Script.UMG import CanvasPanelSlot
from Script.UMG import SetAlignment
from Script.Engine import Delay
from Script.Engine import Pawn
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.CoreUObject import Object
from Script.UMG import SetHeightOverride
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_Monitor_000 import Play_UI_CursorParticle_Monitor_000
from Game.FactoryGame.Interface.UI.Assets.Shared.CorruptionImages.UI_Corruption_02 import UI_Corruption_02
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_Glass import Play_UI_CursorParticle_Glass
from Script.Engine import BreakVector2D
from Script.UMG import CanvasPanel
from Script.UMG import PanelWidget
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import SetWidthOverride
from Game.FactoryGame.Interface.UI.Assets.Shared.CorruptionImages.UI_Corruption_00 import UI_Corruption_00
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticle_Monitor import ExecuteUbergraph_CursorParticle_Monitor
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Stop_UI_CursorParticle_MonitorCrash_000 import Stop_UI_CursorParticle_MonitorCrash_000
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.Assets.Shared.CorruptionImages.UI_Corruption_01 import UI_Corruption_01
from Script.UMG import SetPosition
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.CursorParticles.Play_UI_CursorParticle_MonitorCrash_000 import Play_UI_CursorParticle_MonitorCrash_000

class CursorParticle_Monitor(BP_CursorParticle):
    StartAnim: Ptr[WidgetAnimation]
    mImageSwitchInt: int32
    
    def SwitchImage(self):
        ReturnValue: int32 = self.mImageSwitchInt + 1
        Variable1: int32 = ReturnValue
        self.mImageSwitchInt = Variable1
        Variable: Ptr[Object] = UI_Corruption_00
        Variable1_0: Ptr[Object] = UI_Corruption_01
        Variable2: Ptr[Object] = UI_Corruption_02
        Variable_0: int32 = Variable1
        SlateBrush.ImageSize = self.mGlitch.Brush.ImageSize
        SlateBrush.Margin = self.mGlitch.Brush.Margin
        SlateBrush.TintColor = self.mGlitch.Brush.TintColor
        
        switch = {
            0: Variable,
            1: Variable1_0,
            2: Variable2
        }
        SlateBrush.ResourceObject = switch.get(Variable_0, None)
        SlateBrush.DrawAs = self.mGlitch.Brush.DrawAs
        SlateBrush.Tiling = self.mGlitch.Brush.Tiling
        SlateBrush.Mirroring = self.mGlitch.Brush.Mirroring
        
        SlateBrush = None
        # Label 680
        self.mGlitch.SetBrush(Ref[SlateBrush])
    

    def Construct(self):
        self.ExecuteUbergraph_CursorParticle_Monitor(1415)
    

    def Destruct(self):
        self.ExecuteUbergraph_CursorParticle_Monitor(1329)
    

    def ExecuteUbergraph_CursorParticle_Monitor(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        Panel: Ptr[CanvasPanel] = Cast[CanvasPanel](ReturnValue)
        bSuccess: bool = Panel
        if not bSuccess:
            goto('L603')
        
        X = None
        Y = None
        BreakVector2D(self.mWidgetSize, Ref[X], Ref[Y])
        self.mSizeBox.SetWidthOverride(X)
        
        X = None
        Y = None
        BreakVector2D(self.mWidgetSize, Ref[X], Ref[Y])
        self.mSizeBox.SetHeightOverride(Y)
        ReturnValue1: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue1.SetPosition(self.mWidgetPosition)
        ReturnValue_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_0.SetAlignment(Vector2D(X = 0, Y = 0))
        self.mForceAlignment = True
        self.mForcePosition = True
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StartAnim, 0, 1, 0, 1)
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_MonitorCrash_000, ReturnValue_2, True)
        goto(ExecutionFlow.Pop())
        # Label 603
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 1703746267, ExecutionFunction = "ExecuteUbergraph_CursorParticle_Monitor", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 680
        CmpSuccess: bool = self.mClickCount != 0
        if not CmpSuccess:
            goto('L969')
        CmpSuccess = self.mClickCount != 1
        if not CmpSuccess:
            goto('L969')
        CmpSuccess = self.mClickCount != 2
        if not CmpSuccess:
            goto('L1051')
        CmpSuccess = self.mClickCount != 3
        if not CmpSuccess:
            goto('L1051')
        CmpSuccess = self.mClickCount != 4
        if not CmpSuccess:
            goto('L1051')
        CmpSuccess = self.mClickCount != 5
        if not CmpSuccess:
            goto('L1132')
        goto(ExecutionFlow.Pop())
        # Label 969
        ReturnValue1_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Glass, ReturnValue1_1, False)
        goto(ExecutionFlow.Pop())
        # Label 1051
        ReturnValue1_1 = self.GetOwningPlayerPawn()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Glass, ReturnValue1_1, False)
        # Label 1132
        ReturnValue1_1 = self.GetOwningPlayerPawn()
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CursorParticle_Monitor_000, ReturnValue1_1, False)
        goto(ExecutionFlow.Pop())
        # Label 1214
        self.mSizeBox.SetVisibility(0)
        goto('L15')
        # Label 1257
        ReturnValue_3: bool = EqualEqual_IntInt(self.mClickCount, 5)
        if not ReturnValue_3:
            goto('L1310')
        goto('L1214')
        # Label 1310
        self.RemoveFromParent()
        goto('L680')
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_UI_CursorParticle_MonitorCrash_000, ReturnValue_4, True)
        goto(ExecutionFlow.Pop())
        goto('L1257')
    
