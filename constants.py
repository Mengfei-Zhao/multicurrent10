
# Set the default state of switch
CHA1_SWITCH = 'OFF'
CHA2_SWITCH = 'OFF'
CHA3_SWITCH = 'OFF'
CHA4_SWITCH = 'OFF'
CHA5_SWITCH = 'OFF'
CHA6_SWITCH = 'OFF'
CHA7_SWITCH = 'OFF'
CHA8_SWITCH = 'OFF'
CHA9_SWITCH = 'OFF'
CHA10_SWITCH = 'OFF'
CHA_TOTAL_SWITCH = 'OFF'

# Time
READ_DATA_TIME_INTERVAL = 2000  # ms
SWITCH_OFF_TAIL_DELAY = 0.2  # seconds

# ---- Show volt and pd-----------------------------------
# The decimal digits of shown voltage
VOLT_DECIMAL_DIGITS = '%.4f'
PD_DECIMAL_DIGITS = '%.2f'

# the default text of voltage
DEFAULT_VOLT_TEXT = str(VOLT_DECIMAL_DIGITS % 0.0000)+' V'
DEFAULT_PD_TEXT = str(PD_DECIMAL_DIGITS % 0.00)+' uA'

# the default state of LED
LED_NONCLICKABLE = True

# when start program, I will load the parameters of this file to GUI.
PARAM_INIT_FILE_WHEN_START_PROGRAM = 'guiInit2.xls'

# the number of COM which used for serial port communication
COM_NUM = 'COM6'

# the default max value of current for all channels
DEFAULT_MAX_CURR = 200.000 # unit: mA
