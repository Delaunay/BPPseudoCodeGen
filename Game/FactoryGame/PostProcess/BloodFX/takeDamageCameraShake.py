
from codegen.ue4_stub import *

from Script.Engine import CameraShake

class takeDamageCameraShake(CameraShake):
    bSingleInstance = True
    OscillationDuration = 0.5
    OscillationBlendOutTime = 1
    RotOscillation = Namespace(Pitch={'Amplitude': 15, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Roll={'Amplitude': 15, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Yaw={'Amplitude': 15, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'})
    LocOscillation = Namespace(X={'Amplitude': 5, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Y={'Amplitude': 5, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Z={'Amplitude': 5, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'})
    
