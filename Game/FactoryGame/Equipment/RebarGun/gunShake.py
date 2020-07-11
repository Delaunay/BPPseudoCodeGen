
from codegen.ue4_stub import *

from Script.Engine import CameraShake

class gunShake(CameraShake):
    bSingleInstance = True
    OscillationDuration = 0.30000001192092896
    OscillationBlendOutTime = 0.30000001192092896
    RotOscillation = Namespace(Pitch={'Amplitude': 15, 'Frequency': 3, 'InitialOffset': 1, 'Waveform': 'EOscillatorWaveform::SineWave'}, Roll={'Amplitude': 5, 'Frequency': 1, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Yaw={'Amplitude': 5, 'Frequency': 2, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'})
    LocOscillation = Namespace(X={'Amplitude': 6, 'Frequency': 4, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Y={'Amplitude': 5, 'Frequency': 2, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'}, Z={'Amplitude': 5, 'Frequency': 4, 'InitialOffset': 0, 'Waveform': 'EOscillatorWaveform::SineWave'})
    
