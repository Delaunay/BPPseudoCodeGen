
from codegen.ue4_stub import *

from Script.Engine import SpringArmComponent
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.CoreUObject import Rotator
from Script.Engine import BreakTransform
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetRelativeTransform
from Script.Engine import PlayerController
from Script.UMG import SetRenderScale
from Script.UMG import SetRenderTranslation
from Script.Engine import Sqrt
from Script.Engine import Square
from Script.Engine import GetCameraRotation
from Script.Engine import IsValid
from Script.FactoryGame import FGDriveablePawn
from Script.Engine import EqualEqual_RotatorRotator
from Script.Engine import GetCameraLocation
from Script.Engine import BreakRotator
from Script.FactoryGame import GetSpringArmComponent
from Script.CoreUObject import Vector
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDCameraShake import ExecuteUbergraph_Widget_HUDCameraShake.K2Node_Event_MyGeometry
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDCameraShake import ExecuteUbergraph_Widget_HUDCameraShake
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDCameraShake import ExecuteUbergraph_Widget_HUDCameraShake.K2Node_Event_InDeltaTime
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import NearlyEqual_FloatFloat
from Script.CoreUObject import Vector2D
from Script.CoreUObject import Transform
from Script.FactoryGame import GetDrivenVehicle

class Widget_HUDCameraShake(UserWidget):
    HUD_Translate: Vector2D
    Shake_Strengh: float = 10
    T: float
    Last_Camera_Rotation: Vector2D
    Set_Camera_Pos: bool
    Caluclated_X_Difference: float
    Caluclated_Y_Difference: float
    mShakeActive: bool
    
    def Get Cam and View Position Difference(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L997')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue = self.GetOwningPlayerPawn()
        ReturnValue_1: Vector = ReturnValue_0.PlayerCameraManager.GetCameraLocation()
        ReturnValue_2: Ptr[SpringArmComponent] = Player.GetSpringArmComponent()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        ReturnValue_3: Transform = ReturnValue_2.GetRelativeTransform()
        
        OutLocation = None
        OutRotation = None
        ReturnValue.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_3], Ref[Location], Ref[Rotation], Ref[Scale])
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(OutLocation)
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(Location)
        ReturnValue_4: float = Y1 - Y
        ReturnValue1: float = X1 - X
        ReturnValue_5: float = Square(ReturnValue_4)
        ReturnValue1_0: float = Square(ReturnValue1)
        ReturnValue_6: float = ReturnValue1_0 + ReturnValue_5
        ReturnValue_7: float = Sqrt(ReturnValue_6)
        ReturnValue2: float = X2 - ReturnValue_7
        ReturnValue_8: float = ReturnValue2 * -0.00019999999494757503
        ReturnValue1_1: float = ReturnValue_8 * self.Shake_Strengh
        ReturnValue1_2: float = ReturnValue1_1 + 1
        Scale = ReturnValue1_2
    

    def Get Cam and View Rotation Difference(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Rotator = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2: float = Pitch1 - Pitch
        ReturnValue1: bool = ReturnValue2 <= 355
        if not ReturnValue1:
            goto('L1672')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2 = Pitch1 - Pitch
        self.Caluclated_X_Difference = ReturnValue2
        # Label 691
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_2: float = Yaw1 - Yaw
        ReturnValue_3: bool = ReturnValue_2 <= 355
        if not ReturnValue_3:
            goto('L2054')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_2 = Yaw1 - Yaw
        self.Caluclated_Y_Difference = ReturnValue_2
        # Label 1382
        ReturnValue_4: Vector = Vector(self.Caluclated_X_Difference, self.Caluclated_Y_Difference, 0)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_4)
        ReturnValue_5: float = Y * self.Shake_Strengh
        ReturnValue1_0: float = ReturnValue_5 * -1
        ReturnValue2_0: float = X * self.Shake_Strengh
        X = ReturnValue1_0
        Y = ReturnValue2_0
        # End
        # Label 1672
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2 = Pitch1 - Pitch
        ReturnValue3: float = ReturnValue2 - 360
        self.Caluclated_X_Difference = ReturnValue3
        goto('L691')
        # Label 2054
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = ReturnValue.PlayerCameraManager.GetCameraRotation()
        ReturnValue_1 = self.GetOwningPlayerPawn()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        
        OutLocation = None
        OutRotation = None
        ReturnValue_1.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(OutRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_2 = Yaw1 - Yaw
        ReturnValue1_1: float = ReturnValue_2 - 360
        self.Caluclated_Y_Difference = ReturnValue1_1
        goto('L1382')
    

    def HUD Lerp(self):
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1452')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Vector = ReturnValue.PlayerCameraManager.GetCameraLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_0)
        ReturnValue1 = self.GetOwningPlayerPawn()
        ReturnValue_1: Ptr[SpringArmComponent] = Player.GetSpringArmComponent()
        ReturnValue_2: Transform = ReturnValue_1.GetRelativeTransform()
        
        OutLocation1 = None
        OutRotation1 = None
        ReturnValue1.GetActorEyesViewPoint(Ref[OutLocation1], Ref[OutRotation1])
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_2], Ref[Location], Ref[Rotation], Ref[Scale])
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(OutLocation1)
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(Location)
        ReturnValue_3: float = Y1 - Y
        ReturnValue1_0: float = X1 - X
        ReturnValue_4: float = Square(ReturnValue_3)
        ReturnValue1_1: float = Square(ReturnValue1_0)
        ReturnValue_5: float = ReturnValue1_1 + ReturnValue_4
        ReturnValue_6: float = Sqrt(ReturnValue_5)
        ReturnValue_7: bool = NearlyEqual_FloatFloat(X2, ReturnValue_6, 0.009999999776482582)
        if not ReturnValue_7:
            goto('L1218')
        ReturnValue_8: Vector2D = Vector2D(1, 1)
        self.ShakeBorder.SetRenderScale(ReturnValue_8)
        # Label 930
        ReturnValue_9: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        OutLocation = None
        OutRotation = None
        ReturnValue_9.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue1_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Rotator = ReturnValue1_2.PlayerCameraManager.GetCameraRotation()
        ReturnValue_11: bool = EqualEqual_RotatorRotator(OutRotation, ReturnValue_10, 0.009999999776482582)
        if not ReturnValue_11:
            goto('L1333')
        self.ShakeBorder.SetRenderTranslation(Vector2D(X = 0, Y = 0))
        # End
        
        Scale = None
        # Label 1218
        self.Get Cam and View Position Difference(Ref[Scale])
        ReturnValue1_3: Vector2D = Vector2D(Scale, Scale)
        self.ShakeBorder.SetRenderScale(ReturnValue1_3)
        goto('L930')
        
        X = None
        Y = None
        # Label 1333
        self.Get Cam and View Rotation Difference(Ref[X], Ref[Y])
        ReturnValue2: Vector2D = Vector2D(X, Y)
        self.ShakeBorder.SetRenderTranslation(ReturnValue2)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDCameraShake.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDCameraShake.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDCameraShake(254)
    

    def ExecuteUbergraph_Widget_HUDCameraShake(self):
        # Label 10
        if not self.mShakeActive:
            goto('L259')
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L259')
        ReturnValue_0: Ptr[FGDriveablePawn] = Player.GetDrivenVehicle()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L235')
        # End
        # Label 235
        self.HUD Lerp()
        # End
        goto('L10')
    
