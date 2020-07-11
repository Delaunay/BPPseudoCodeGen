
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_AluminumPlate(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "300F56834813D17C294AC5B5FC5908F6", "Alclad Aluminum Sheet")
    mDescription = NSLOCTEXT("", "73003FBE4815865E1470098EE5E2D31D", "Thin lightweight & highly durable sheet that is mainly used for products that need to be light or have high heat conduction.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumPlate/UI/IconDesc_AluminiumSheet_64.IconDesc_AluminiumSheet_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumPlate/UI/IconDesc_AluminiumSheet_256.IconDesc_AluminiumSheet_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AluminumPlate/Mesh/SM_AluminiumSheet_01.SM_AluminiumSheet_01')
    mPreviewView = Namespace(CameraPitch=-28, Distance=85, FocalOffset={'X': 0, 'Y': 0, 'Z': 10})
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
