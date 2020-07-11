
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ResourceSinkCoupon(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "35B4FEB84D73497B9BAF2397A6B19420", "FICSIT Coupon")
    mDescription = NSLOCTEXT("", "0AACF54448D79BBD99BE7A8DC131EAB5", "A special FICSIT bonus program Coupon, obtained through the AWESOME Sink.\r\nCan be redeemed in the AWESOME Shop for bonus milestones and rewards.")
    mStackSize = EStackSize::SS_HUGE
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/UI/IconDesc_Ficsit_Coupon_64.IconDesc_Ficsit_Coupon_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/UI/IconDesc_Ficsit_Coupon_256.IconDesc_Ficsit_Coupon_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Coupon/SM_Coupon_01.SM_Coupon_01')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
