
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Conv_StringToName
from Script.Engine import Texture2D
from Script.FactoryGame import FGResourceDescriptor
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.FactoryGame import SetPressingScan
from Game.FactoryGame.Resource.RawResources.OreIron.Desc_OreIron import Desc_OreIron
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import FGInteractWidget
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Equipment.ResourceScanner.BP_ResourceScanner import BP_ResourceScanner
from Script.FactoryGame import GetResourceDescriptorToScanFor
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Equipment.ResourceScanner.UI.Widget_ResourceScanner import ExecuteUbergraph_Widget_ResourceScanner
from Script.Engine import IsValidClass
from Script.FactoryGame import SetResourceDescriptorToScanFor
from Script.FactoryGame import GetScannableResources

class Widget_ResourceScanner(FGInteractWidget):
    mResourceScanner: Ptr[BP_ResourceScanner]
    SelectedResource: TSubclassOf[FGResourceDescriptor]
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_ResourceScanner(1334)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ResourceScanner(1492)
    

    def ExecuteUbergraph_Widget_ResourceScanner(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L647")
        ReturnValue: List[TSubclassOf[FGResourceDescriptor]] = self.mResourceScanner.GetScannableResources()
        
        Item = None
        Item = ReturnValue[Variable]
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(Item)
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: FName = Default__KismetStringLibrary.Conv_StringToName(ReturnValue_1)
        
        self.Widget_RadialMenu.Buttons = None
        ReturnValue_3: int32 = self.Widget_RadialMenu.Buttons.append(ReturnValue_2)
        ReturnValue = self.mResourceScanner.GetScannableResources()
        
        Item = None
        Item = ReturnValue[Variable]
        ReturnValue_4: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item)
        
        self.Widget_RadialMenu.mIconTextures = None
        ReturnValue1: int32 = self.Widget_RadialMenu.mIconTextures.append(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 647
        ReturnValue_5: int32 = Variable + 1
        Variable: int32 = ReturnValue_5
        # Label 716
        ReturnValue = self.mResourceScanner.GetScannableResources()
        
        ReturnValue_6: int32 = len(ReturnValue)
        ReturnValue_7: bool = Variable <= ReturnValue_6
        if not ReturnValue_7:
            goto('L909')
        Variable = Variable
        goto('L15')
        # Label 909
        self.Widget_RadialMenu.Create Radial Menu()
        goto(ExecutionFlow.Pop())
        # Label 946
        self.mResourceScanner.SetPressingScan(False)
        ReturnValue1_0: List[TSubclassOf[FGResourceDescriptor]] = self.mResourceScanner.GetScannableResources()
        
        Item1 = None
        Item1 = ReturnValue1_0[self.Widget_RadialMenu.SelectedInt]
        self.SelectedResource = Item1
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValidClass(self.SelectedResource)
        if not ReturnValue_8:
            goto('L1236')
        self.mResourceScanner.SetResourceDescriptorToScanFor(self.SelectedResource)
        goto(ExecutionFlow.Pop())
        # Label 1236
        self.mResourceScanner.SetResourceDescriptorToScanFor(Desc_OreIron)
        goto(ExecutionFlow.Pop())
        # Label 1278
        Variable = 0
        goto('L716')
        # Label 1306
        Variable = 0
        goto('L1278')
        self.Widget_RadialMenu.mDescText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1376, 'Value': 'Scanning for'}"
        ReturnValue_9: TSubclassOf[FGResourceDescriptor] = self.mResourceScanner.GetResourceDescriptorToScanFor()
        self.SelectedResource = ReturnValue_9
        goto('L1306')
        goto('L946')
    
