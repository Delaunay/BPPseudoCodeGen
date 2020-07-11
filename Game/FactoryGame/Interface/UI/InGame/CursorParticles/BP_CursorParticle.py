
from codegen.ue4_stub import *

from Script.CoreUObject import Vector2D
from Script.UMG import UserWidget

class BP_CursorParticle(UserWidget):
    mWidgetPosition: Vector2D
    mWidgetSize: Vector2D
    mForceAlignment: bool
    mForcePosition: bool
    mClickCount: int32
    
