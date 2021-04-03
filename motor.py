import RPi.GPIO as GPIO
import time



MotorDir = [
    'forward',
    'backward',
]

ControlMode = [
    'hardward',
    'softward',
]

class DRV8825():
    def __init__(self, dir_pin, step_pin, enable_pin, mode_pins):
        self.dir_pin = dir_pin
        self.step_pin = step_pin        
        self.enable_pin = enable_pin
        self.mode_pins = mode_pins
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        
    def digital_write(self, pin, value):
        GPIO.output(pin, value)
        
    def Stop(self):
        self.digital_write(self.enable_pin, 0)
    
    def SetMicroStep(self, mode, stepformat):
        """
        (1) mode
            'hardward' :    Use the switch on the module to control the microstep
            'software' :    Use software to control microstep pin levels
                Need to put the All switch to 0
        (2) stepformat
            ('fullstep', 'halfstep', '1/4step', '1/8step', '1/16step', '1/32step')
        """
        microstep = {'fullstep': (0, 0, 0),
                     'halfstep': (1, 0, 0),
                     '1/4step': (0, 1, 0),
                     '1/8step': (1, 1, 0),
                     '1/16step': (0, 0, 1),
                     '1/32step': (1, 0, 1)}


        if (mode == ControlMode[1]):

            self.digital_write(self.mode_pins, microstep[stepformat])
        
    def TurnStep(self, Dir, steps, stepdelay = 0.0003):
        if (Dir == MotorDir[0]):

            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 0)
        elif (Dir == MotorDir[1]):
  
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 1)
        else:
   
            self.digital_write(self.enable_pin, 0)
            return

        if (steps == 0):
            return
            

        for i in range(steps):
            self.digital_write(self.step_pin, True)
            time.sleep(stepdelay)
            self.digital_write(self.step_pin, False)
            time.sleep(stepdelay)
    
try:
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
    
    """
    # 1.8 degree: nema23, nema14
    # softward Control :
    # 'fullstep': A cycle = 200 steps
    # 'halfstep': A cycle = 200 * 2 steps
    # '1/4step': A cycle = 200 * 4 steps
    # '1/8step': A cycle = 200 * 8 steps
    # '1/16step': A cycle = 200 * 16 steps
    # '1/32step': A cycle = 200 * 32 steps
    """
    def control(direction_input):
        
        if (direction_input ==b'w'):
            print ("up")
            for i in range(100):
                Motor1.SetMicroStep('softward','fullstep')
                Motor1.TurnStep(Dir='forward', steps=1, stepdelay = 0.0003)
                Motor1.Stop()
                Motor2.SetMicroStep('softward' ,'fullstep')    
                Motor2.TurnStep(Dir='backward', steps=1, stepdelay=0.0003)
                Motor2.Stop()
                time.sleep(0.001)
            
        if (direction_input ==b'a'):
            print ("left")
            for i in range(200):
                Motor1.SetMicroStep('softward','fullstep')
                Motor1.TurnStep(Dir='backward', steps=1, stepdelay =0.0003)
                Motor1.Stop()
                Motor2.SetMicroStep('softward' ,'fullstep')    
                Motor2.TurnStep(Dir='backward', steps=1, stepdelay=0.0003)
                Motor2.Stop()
                time.sleep(0.001)
                
        if (direction_input ==b'd'):
            for i in range(200):
                Motor1.SetMicroStep('softward','fullstep')
                Motor1.TurnStep(Dir='forward', steps=1, stepdelay =0.0003)
                Motor1.Stop()
                Motor2.SetMicroStep('softward' ,'fullstep')    
                Motor2.TurnStep(Dir='forward', steps=1, stepdelay=0.0003)
                Motor2.Stop()
                time.sleep(0.001)
            print ('right')
        if (direction_input ==b's'):
            for i in range(0):
                Motor1.SetMicroStep('softward','fullstep')
                Motor1.TurnStep(Dir='forward', steps=1, stepdelay =0.0003)
                Motor1.Stop()
                Motor2.SetMicroStep('softward' ,'fullstep')    
                Motor2.TurnStep(Dir='forward', steps=1, stepdelay=0.0003)
                Motor2.Stop()
                time.sleep(0.001)
            print ('stop')
        # if (direction_input =='q'):
  
except:
    # GPIO.cleanup()
    Motor1.Stop()
    Motor2.Stop()
    exit()
    
if __name__ == "__main__":
    while (True):
        control()