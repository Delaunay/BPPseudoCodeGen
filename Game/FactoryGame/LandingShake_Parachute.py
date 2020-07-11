
from codegen.ue4_stub import *

from Script.Engine import CameraShake

class LandingShake_Parachute(CameraShake):
    OscillationDuration = 1
    OscillationBlendInTime = 0.15000000596046448
    OscillationBlendOutTime = 0.8999999761581421
    RotOscillation = Namespace(Pitch={'Amplitude': -15, 'Frequency': 3, 'InitialOffset': 1, 'Waveform': 'EOscillatorWaveform::SineWave'}, Roll={'Amplitude': 0, 'Frequency': 2, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Yaw={'Amplitude': 0, 'Frequency': 0, 'InitialOffset': 1, 'Waveform': 'EOscillatorWaveform::SineWave'})
    LocOscillation = Namespace(X={'Amplitude': 0, 'Frequency': 0, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Y={'Amplitude': 8, 'Frequency': 2, 'InitialOffset': 1, 'Waveform': 'EOscillatorWaveform::SineWave'}, Z={'Amplitude': 0, 'Frequency': 0, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'})
    
