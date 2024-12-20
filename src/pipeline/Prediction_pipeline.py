import pandas as pd
import os 
import sys

sys.path.append(os.path.join(os.getcwd(),"src"))

from logger.logger import logging
from logger.exception import CustomError
from utilities.LoadObject import load_object

class PredictPipeline:
    def __init__(self):
        self.preprocessor_path = os.path.join(os.getcwd(),"artifacts","preprocessor.pkl")
        self.model_path = os.path.join(os.getcwd(),"artifacts","model.pkl")
    def predict(self,features):
        preprocessor =  load_object(self.preprocessor_path)
        model = load_object(self.model_path)
        features = preprocessor.transform(features)
        prediction = model.predict(features)
        return prediction
    
class CustomData:
    def __init__(self, battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi):
        self.battery_power = battery_power
        self.blue = blue
        self.clock_speed = clock_speed
        self.dual_sim = dual_sim
        self.fc = fc
        self.four_g = four_g
        self.int_memory = int_memory
        self.m_dep = m_dep
        self.mobile_wt = mobile_wt
        self.n_cores = n_cores
        self.pc = pc
        self.px_height = px_height
        self.px_width = px_width
        self.ram = ram
        self.sc_h = sc_h
        self.sc_w = sc_w
        self.talk_time = talk_time
        self.three_g = three_g
        self.touch_screen = touch_screen
        self.wifi = wifi
    
    def get_data_as_dataframe(self):
        data = {
            'battery_power': [self.battery_power],
            'blue': [self.blue],
            'clock_speed': [self.clock_speed],
            'dual_sim': [self.dual_sim],
            'fc': [self.fc],
            'four_g': [self.four_g],
            'int_memory': [self.int_memory],
            'm_dep': [self.m_dep],
            'mobile_wt': [self.mobile_wt],
            'n_cores': [self.n_cores],
            'pc': [self.pc],
            'px_height': [self.px_height],
            'px_width': [self.px_width],
            'ram': [self.ram],
            'sc_h': [self.sc_h],
            'sc_w': [self.sc_w],
            'talk_time': [self.talk_time],
            'three_g': [self.three_g],
            'touch_screen': [self.touch_screen],
            'wifi': [self.wifi],}
        return pd.DataFrame(data)
    