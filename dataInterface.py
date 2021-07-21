from multicurrent10 import Multicurrent10
import threading
import time 

class DataInterface:
    def __init__(self):
        self.multi = Multicurrent10('COM6')
        # def readDataFromSerialPort_thread(self):
        # 开始读取串口缓存区的子线程，一直在读取数据
        # self.readData_thread = threading.Thread(
        #     target=self.multi.read_voltage(1), name="readData_thread")
        # self.readData_thread.setDaemon(True)  # 当主线程结束后，该子线程也结束
        # readData_thread.start()  # 启动该线程

    # def readVoltCha1(self):
    #     self.cha1_volt = self.multi.read_voltage(1)
    #     time.sleep(2)