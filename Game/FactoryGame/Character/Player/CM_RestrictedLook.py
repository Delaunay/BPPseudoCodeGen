
from codegen.ue4_stub import *

from Script.FactoryGame import FGCameraModifierLimitLook

class CM_RestrictedLook(FGCameraModifierLimitLook):
    mMaxPitch = 30
    mMaxYaw = 20
    
