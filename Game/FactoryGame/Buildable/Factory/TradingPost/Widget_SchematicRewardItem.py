
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import FGPoleDescriptor
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Building import Recipe_Icon_Building
from Script.SlateCore import Margin
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Resource import Recipe_Icon_Resource
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Cross import Cross
from Script.UMG import ESlateVisibility
from Script.UMG import SetColorAndOpacity
from Script.FactoryGame import FGVehicleDescriptor
from Script.Engine import BooleanOR
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Map import Recipe_Icon_Map
from Script.CoreUObject import Box2D
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Equipment import Recipe_Icon_Equipment
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Item import Recipe_Icon_Item
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Vehicle import Recipe_Icon_Vehicle
from Script.FactoryGame import IsSchematicPurchased
from Script.FactoryGame import FGSchematicManager
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.RecipeIcons.Recipe_Icon_Decor import Recipe_Icon_Decor
from Script.SlateCore import SlateColor
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.AkAudio import AkComponent
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import Default__FGSchematicManager
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import ExecuteUbergraph_Widget_SchematicRewardItem
from Script.FactoryGame import FGDecorDescriptor
from Script.FactoryGame import FGMapAreaZoneDescriptor
from Script.CoreUObject import LinearColor
from Script.FactoryGame import FGBuildingDescriptor

class Widget_SchematicRewardItem(UserWidget):
    FadeAnim: Ptr[WidgetAnimation]
    mSchematicClass: TSubclassOf[FGSchematic]
    mTradingPostWidget: Ptr[UserWidget]
    mCategoryIconTexture: Ptr[Texture]
    mIsSchematicLocked: bool
    mIsSchematicPurchased: bool
    mBigIconBrush: SlateBrush
    mTitle: FText
    mDescription: FText
    
    def UpdateVisibility(self):
        Variable2: uint8 = 1
        Variable3: uint8 = 0
        ReturnValue: bool = BooleanOR(self.mIsSchematicPurchased, self.mIsSchematicLocked)
        Variable1: bool = ReturnValue
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.Widget_ButtonSpotLight.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 4
        # Label 206
        Variable1_0: uint8 = 1
        
        isValid = None
        self.IsValidRewardItem(Ref[isValid])
        Variable_0: bool = isValid
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.SetVisibility(switch_0.get(Variable_0, None))
    

    def SetCategoryIconColor(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicLocked, self.mIsSchematicPurchased)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        Variable: bool = ReturnValue
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        switch = {
            False: GraphicsWhite,
            True: Graphics
        }
        self.mRewardCategoryIcon.SetColorAndOpacity(switch.get(Variable, None))
    

    def GetLockedIcon(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPurchased, self.mIsSchematicLocked)
        if not ReturnValue:
            goto('L109')
        ReturnValue_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0.5)
        goto('L161')
        # Label 109
        ReturnValue_0 = LinearColor(R = 1, G = 1, B = 1, A = 1)
    

    def SetCategoryTexture(self, ItemClass: TSubclassOf[FGItemDescriptor]):
        Descriptor: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](ItemClass)
        bSuccess7: bool = Descriptor
        if not bSuccess7:
            goto('L103')
        self.mCategoryIconTexture = Recipe_Icon_Building
        # End
        # Label 103
        Descriptor_0: TSubclassOf[FGDecorDescriptor] = ClassCast[FGDecorDescriptor](ItemClass)
        bSuccess6: bool = Descriptor_0
        if not bSuccess6:
            goto('L206')
        self.mCategoryIconTexture = Recipe_Icon_Decor
        # End
        # Label 206
        Descriptor_1: TSubclassOf[FGEquipmentDescriptor] = ClassCast[FGEquipmentDescriptor](ItemClass)
        bSuccess5: bool = Descriptor_1
        if not bSuccess5:
            goto('L309')
        self.mCategoryIconTexture = Recipe_Icon_Equipment
        # End
        # Label 309
        Descriptor_2: TSubclassOf[FGItemDescriptor] = ClassCast[FGItemDescriptor](ItemClass)
        bSuccess4: bool = Descriptor_2
        if not bSuccess4:
            goto('L412')
        self.mCategoryIconTexture = Recipe_Icon_Item
        # End
        # Label 412
        Descriptor_3: TSubclassOf[FGMapAreaZoneDescriptor] = ClassCast[FGMapAreaZoneDescriptor](ItemClass)
        bSuccess3: bool = Descriptor_3
        if not bSuccess3:
            goto('L515')
        self.mCategoryIconTexture = Recipe_Icon_Map
        # End
        # Label 515
        Descriptor_4: TSubclassOf[FGPoleDescriptor] = ClassCast[FGPoleDescriptor](ItemClass)
        bSuccess2: bool = Descriptor_4
        if not bSuccess2:
            goto('L618')
        self.mCategoryIconTexture = Recipe_Icon_Building
        # End
        # Label 618
        Descriptor_5: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](ItemClass)
        bSuccess1: bool = Descriptor_5
        if not bSuccess1:
            goto('L721')
        self.mCategoryIconTexture = Recipe_Icon_Resource
        # End
        # Label 721
        Descriptor_6: TSubclassOf[FGVehicleDescriptor] = ClassCast[FGVehicleDescriptor](ItemClass)
        bSuccess: bool = Descriptor_6
        if not bSuccess:
            goto('L824')
        self.mCategoryIconTexture = Recipe_Icon_Vehicle
        # End
        # Label 824
        self.mCategoryIconTexture = Cross
    

    def GetCategoryIcon(self):
        SlateBrush.ImageSize = Vector2D(X = 20, Y = 20)
        SlateBrush.Margin = self.mRewardCategoryIcon.Brush.Margin
        SlateBrush.TintColor = self.mRewardCategoryIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mCategoryIconTexture
        SlateBrush.DrawAs = self.mRewardCategoryIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mRewardCategoryIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mRewardCategoryIcon.Brush.Mirroring
        ReturnValue = SlateBrush
    

    def GetLinesColor(self):
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L125')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: LinearColor = GraphicsWhite
        goto('L207')
        
        Text = None
        Graphics = None
        # Label 125
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
    

    def GetButtonColor(self):
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L344')
        ReturnValue_0: bool = BooleanOR(self.mIsSchematicPurchased, self.mIsSchematicLocked)
        if not ReturnValue_0:
            goto('L401')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        LinearColor.R = Graphics.R
        LinearColor.G = Graphics.G
        LinearColor.B = Graphics.B
        LinearColor.A = 0.20000000298023224
        ReturnValue_1: LinearColor = LinearColor
        goto('L483')
        # Label 344
        ReturnValue_1 = LinearColor(R = 0, G = 0, B = 0, A = 0)
        goto('L483')
        
        Text1 = None
        Graphics1 = None
        # Label 401
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text1], Ref[Graphics1])
        ReturnValue_1 = Graphics1
    

    def GetCategoryIconBackgroundColor(self):
        ReturnValue: bool = BooleanOR(self.mIsSchematicPurchased, self.mIsSchematicLocked)
        if not ReturnValue:
            goto('L306')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        LinearColor.R = Graphics.R
        LinearColor.G = Graphics.G
        LinearColor.B = Graphics.B
        LinearColor.A = 0.5
        ReturnValue_0: LinearColor = LinearColor
        goto('L358')
        # Label 306
        ReturnValue_0 = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
    

    def GetHoverColor(self):
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L125')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        ReturnValue_0: SlateColor = TextWhite1
        goto('L346')
        # Label 125
        ReturnValue_1: bool = BooleanOR(self.mIsSchematicPurchased, self.mIsSchematicLocked)
        if not ReturnValue_1:
            goto('L264')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Text
        goto('L346')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 264
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = TextWhite
    

    def IsValidRewardItem(self):
        IsValid = False
    

    def OnRewardClicked(self):
        pass
    

    def GetName(self):
        ReturnValue = 
    

    def GetIcon(self):
        ReturnValue = SlateBrush(ImageSize = Vector2D(X = 32, Y = 32), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 3, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SchematicRewardItem(10)
    

    def BndEvt__mSchematicRecipeButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SchematicRewardItem(340)
    

    def BndEvt__mSchematicRecipeButton_K2Node_ComponentBoundEvent_19_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SchematicRewardItem(528)
    

    def ExecuteUbergraph_Widget_SchematicRewardItem(self):
        self.TextBlock_0.SetText(self.mTitle)
        self.SetCategoryIconColor()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsLocked = None
        Default__BP_SchematicHelper.IsSchematicLockedInAnyWay(ReturnValue, self.mSchematicClass, self, Ref[IsLocked])
        self.mIsSchematicLocked = IsLocked
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_1: bool = ReturnValue_0.IsSchematicPurchased(self.mSchematicClass)
        self.mIsSchematicPurchased = ReturnValue_1
        self.UpdateVisibility()
        # End
        Post1: Ptr[Widget_TradingPost] = Cast[Widget_TradingPost](self.mTradingPostWidget)
        bSuccess1: bool = Post1
        Post1.UpdateRewardInfoFromProduct(self)
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue_2, True)
        # End
        Post: Ptr[Widget_TradingPost] = Cast[Widget_TradingPost](self.mTradingPostWidget)
        bSuccess: bool = Post
        Post.SetDefaultDescriptionText(self.mSchematicClass)
    
