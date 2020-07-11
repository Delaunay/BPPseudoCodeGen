
from codegen.ue4_stub import *

from Script.Engine import TextToUpper
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_Banner import ExecuteUbergraph_BPW_ResourceSinkShop_Banner
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import CanvasPanelSlot
from Script.UMG import PlayAnimation
from Script.UMG import SetPosition
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.ResourceSinkShop_Banner_Struct import ResourceSinkShop_Banner_Struct
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import WidgetAnimation
from Script.UMG import SlotAsCanvasSlot
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_Banner import ExecuteUbergraph_BPW_ResourceSinkShop_Banner.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary

class BPW_ResourceSinkShop_Banner(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mBannerStruct: ResourceSinkShop_Banner_Struct = Namespace(ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F={'ImageSize': {'X': 230, 'Y': 230}, 'Margin': {'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, 'TintColor': {'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, 'ResourceObject': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/UI/Manufacturer_512.Manufacturer_512'}, 'ResourceName': 'None', 'UVRegion': {'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, 'DrawAs': 3, 'Tiling': 0, 'Mirroring': 0, 'ImageType': 0, 'bIsDynamicallyLoaded': False, 'bHasUObject': False}, TextEndPosition_12_284EB20F4CB57ECB983D038E3F457990={'X': 75, 'Y': 0}, Text_7_9ECC94234929451FA80AFDAC404AD507='NSLOCTEXT("", "A11E04474AA7303285CF0380884CA6A9", "Buildings")')
    
    def UpdateBannerData(self):
        ReturnValue1: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mBannerImageOffsetter)
        ReturnValue1.SetPosition(self.mBannerStruct.ImageEndPosition_10_3EA4EF5B4A94A13E17A775B8C65CE230)
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mBannerTextOffsetter)
        ReturnValue.SetPosition(self.mBannerStruct.TextEndPosition_12_284EB20F4CB57ECB983D038E3F457990)
        
        self.mBannerStruct.Text_7_9ECC94234929451FA80AFDAC404AD507 = None
        ReturnValue_0: FText = Default__KismetTextLibrary.TextToUpper(Ref[self.mBannerStruct.Text_7_9ECC94234929451FA80AFDAC404AD507])
        self.mBannerTextObject.SetText(ReturnValue_0)
        
        self.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F = None
        self.mBannerImageObject.SetBrush(Ref[self.mBannerStruct.ImageBrush_5_012E7B504A7AB4B9D1F758A855CF7C5F])
    

    def SetBanner(self, mBannerStruct: ResourceSinkShop_Banner_Struct):
        self.mBannerStruct = mBannerStruct
        self.UpdateBannerData()
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_ResourceSinkShop_Banner.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Banner(38)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Banner(10)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_Banner(self):
        self.SetBanner(self.mBannerStruct)
        # End
        self.UpdateBannerData()
    
