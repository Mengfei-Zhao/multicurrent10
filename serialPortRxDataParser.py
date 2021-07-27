

class SerialPortRxDataParser:
    """Parse the received data of serial port"""

    def __init__(self, multi):
        self._multi = multi

    def rxDataParser(self):
        """Parse the received data of serial port. 
        for Voltage:
            line: 'v1:3.0473 V--' or '1:3.0473 V--'
            line[0] = 'v'
            line[-3] = 'V'
        for Photodiode:
            line: 'p60.02--'
            line[0] = 'p'

        Return: 
            physicalName (str): 'volt', 'pd', 'none'
            cha (int): channel
            value (float): the corresponding value of the channel
        """
        line = self._multi.line
        physicalName = 'none'
        cha, value = 0, 0.
        # print('len(line) is: ', len(line))
        if len(line) == 13 or len(line) == 12:
            if line[0] == 'v' or line[-3] == 'V':  # this line is a voltage
                physicalName = 'volt'
                cha, value = self._parseVolt(line)
        elif len(line) == 8 and line[:1] == "p":  # this line is a photodiode
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
        # print('line of voltage: ', line)
        if line[0] == 'v':
            cha = int(line[1]) + 1
            volt = float(line[-10:-4])
        else:
            cha = int(line[0]) + 1
            volt = float(line[-10:-4])
        return cha, volt

    def _parsePd(self, line):
        """parse photodiode

        Return:
            cha (int): channel
            pd (float): photodiode
        """
        # print('line of photodiode: ', line)
        if line[2:] == " ":  # there is no value
            cha = int(line[1]) + 1
            pd = 0.
        else:
            cha = int(line[1]) + 1
            pd = float(line[2:])
        return cha, pd
