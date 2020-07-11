
from codegen.ue4_stub import *

from Script.Engine import Lerp
from Script.UMG import CanvasPanelSlot
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_CouponPrint import Curve_CouponPrint
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_CouponFade import Curve_CouponFade
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_CouponShader import Curve_CouponShader
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSinkCoupon import ExecuteUbergraph_BPW_ResourceSinkCoupon
from Script.Engine import GetFloatValue
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_Coupon import Curve_Coupon
from Script.UMG import UserWidget
from Script.UMG import SetOffsets
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_CouponShadowBottom import Curve_CouponShadowBottom
from Script.CoreUObject import Vector2D
from Script.UMG import SetRenderOpacity
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.Curve_CouponShadowTop import Curve_CouponShadowTop

class BPW_ResourceSinkCoupon(UserWidget):
    mUpdateTime: float = 0.009999999776482582
    mDuration: float = 3
    mT: float
    mLerpTimerHandle: TimerHandle
    mCurvedT: float
    OnPrintCompleted: FMulticastScriptDelegate
    mIsCouponSlotEmpty: bool
    mInventoryComponent: Ptr[FGInventoryComponent]
    OnPrintPaused: FMulticastScriptDelegate
    OnPrintContinued: FMulticastScriptDelegate
    
    def InitInventorySlot(self, inventoryComponent: Ptr[FGInventoryComponent]):
        self.mInventoryComponent = inventoryComponent
        self.mCouponSlot.mCachedInventoryComponent = self.mInventoryComponent
        self.mCouponShaderSlot.mCachedInventoryComponent = self.mInventoryComponent
    

    def PrintCoupon(self):
        self.mIsCouponSlotEmpty = False
        self.mContainer.SetVisibility(3)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
        self.mT = 0
        OutputDelegate.BindUFunction(self, Lerp)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mLerpTimerHandle = ReturnValue
    

    def CurveLerp(self, Curve: Ptr[CurveFloat], Start: float, End: float, Alpha: float):
        ReturnValue: float = Curve.GetFloatValue(Alpha)
        ReturnValue_0: float = Lerp(Start, End, ReturnValue)
        ReturnValue_1: float = ReturnValue_0
    

    def Lerp(self):
        self.ExecuteUbergraph_BPW_ResourceSinkCoupon(1359)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkCoupon(1763)
    

    def ExecuteUbergraph_BPW_ResourceSinkCoupon(self):
        # Label 10
        self.OnPrintContinued.ProcessMulticastDelegate()
        # End
        # Label 34
        Variable: bool = False
        self.OnPrintPaused.ProcessMulticastDelegate()
        # End
        # Label 69
        if not Variable:
            goto('L88')
        # End
        # Label 88
        Variable = True
        goto('L10')
        # Label 104
        ReturnValue: float = self.CurveLerp(Curve_CouponPrint, 0, 1, self.mT)
        self.mCurvedT = ReturnValue
        ReturnValue1: float = self.CurveLerp(Curve_Coupon, 0, 403, self.mCurvedT)
        ReturnValue_0: Vector2D = Vector2D(0, ReturnValue1)
        self.mCouponOverlay.SetRenderTranslation(ReturnValue_0)
        ReturnValue2: float = self.CurveLerp(Curve_CouponShader, 0, 278, self.mCurvedT)
        ReturnValue1_0: Vector2D = Vector2D(0, ReturnValue2)
        self.mCouponShaderOverlay.SetRenderTranslation(ReturnValue1_0)
        ReturnValue_1: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mCouponShadow)
        ReturnValue3: float = self.CurveLerp(Curve_CouponShadowTop, 0, 426, self.mCurvedT)
        ReturnValue4: float = self.CurveLerp(Curve_CouponShadowBottom, 0, 260, self.mCurvedT)
        Margin.Left = 0
        Margin.Top = ReturnValue3
        Margin.Right = 0
        Margin.Bottom = ReturnValue4
        ReturnValue_1.SetOffsets(Margin)
        ReturnValue5: float = self.CurveLerp(Curve_CouponFade, 1, 0, self.mCurvedT)
        self.mCoupon.SetRenderOpacity(ReturnValue5)
        self.mCouponShader.SetRenderOpacity(ReturnValue5)
        self.mCouponShadow.SetRenderOpacity(ReturnValue5)
        self.mCouponSlot.SetRenderOpacity(ReturnValue5)
        self.mCouponShaderSlot.SetRenderOpacity(ReturnValue5)
        ReturnValue_2: bool = GreaterEqual_FloatFloat(self.mT, 1)
        if not ReturnValue_2:
            goto('L1805')
        self.mT = 0
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
        self.OnPrintCompleted.ProcessMulticastDelegate()
        self.mContainer.SetVisibility(3)
        # End
        # Label 1265
        Variable1: bool = False
        goto('L69')
        # Label 1281
        ReturnValue_3: bool = Not_PreBool(self.mIsCouponSlotEmpty)
        if not ReturnValue_3:
            goto('L1265')
        if not Variable1:
            goto('L1343')
        # End
        # Label 1343
        Variable1 = True
        goto('L34')
        ReturnValue_4: bool = self.mT > 0.5
        ReturnValue1_1: bool = Not_PreBool(self.mIsCouponSlotEmpty)
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue1_1
        ReturnValue3_0: bool = Not_PreBool(ReturnValue_5)
        if not ReturnValue3_0:
            goto('L1627')
        ReturnValue_6: float = self.mUpdateTime / self.mDuration
        ReturnValue_7: float = self.mT + ReturnValue_6
        self.mT = ReturnValue_7
        goto('L104')
        # Label 1627
        self.mContainer.SetVisibility(4)
        
        slotHasItems = None
        self.mCouponSlot.CheckSlotHasItems(Ref[slotHasItems])
        ReturnValue2_0: bool = Not_PreBool(slotHasItems)
        self.mIsCouponSlotEmpty = ReturnValue2_0
        goto('L1281')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
    

    def OnPrintContinued__DelegateSignature(self):
        pass
    

    def OnPrintPaused__DelegateSignature(self):
        pass
    

    def OnPrintCompleted__DelegateSignature(self):
        pass
    
