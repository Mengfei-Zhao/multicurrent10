from multicurrent10 import Multicurrent10


class SerialPortRxDataParser:
    """Parse the received data of serial port"""

    def __init__(self, multi):
        # self._multi = Multicurrent10()
        self._multi = multi

    @property  # this method is an attribute
    def rxDataParser(self):
        """Parse the received data of serial port

        Return: 
            physicalName (str): 'volt', 'pd', 'none'
            cha (int): channel
            value (float): the corresponding value of the channel
        """
        line = self._multi.line
        if line[:1] == "v":  # this line is a voltage
            physicalName = 'volt'
            cha, value = self._parseVolt(line)
        elif line[:1] == "p":  # this line is a photodiode
            physicalName = 'pd'
            cha, value = self._parsePd(line)
        else:
            physicalName = 'none'
            cha, value = 0, 0.
        return physicalName, cha, value

    def _parseVolt(self, line):
        """parse voltage

        Return:
            cha (int): channel
            volt (float): voltage
        """
        if line[3:-3] == " ":  # there is no value
            cha = int(line[1:2]) + 1
            volt = 0.
        else:
            cha = int(line[1:2]) + 1
            volt = float(line[3:-3])
        return cha, volt

    def _parsePd(self, line):
        """parse photodiode

        Return:
            cha (int): channel
            pd (float): photodiode
        """
        if line[2:-1] == " ":  # there is no value
            cha = int(line[1:2]) + 1
            pd = 0.
        else:
            cha = int(line[1:2]) + 1
            pd = float(line[2:-1])
        return cha, pd
