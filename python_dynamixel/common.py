PYPOSE_ID									= 253

"""dynamixel commands"""
DYNAMIXEL_RQ_PING					=0x01
DYNAMIXEL_RQ_READ_DATA		=0x02
DYNAMIXEL_RQ_WRITE_DATA		=0x03
DYNAMIXEL_RQ_REG_WRITE		=0x04
DYNAMIXEL_RQ_REG_ACTION		=0x05
DYNAMIXEL_RQ_RESET				=0x06
DYNAMIXEL_RQ_SYNC_WRITE		=0x83

DYNAMIXEL_RQ_ZMQ_ECHO									=0x100
	
DYNAMIXEL_RQ_SYNC_WRITE_WORDS					=0x183

DYNAMIXEL_RQ_READ_PYPOSE_PLAYER_STATE	=0x200
PYPOSE_SET_POSESIZE				=0x07
PYPOSE_LOAD_POSE					=0x08
PYPOSE_LOAD_SEQUENCE			=0x09
	
PYPOSE_PLAY_SEQUENCE			=0x0A
PYPOSE_LOOP_SEQUENCE			=0x0B
PYPOSE_TEST								=0x19
	
TROSSEN_COMMANDER					=0x200
	
DYNAMIXEL_RQ_ZMQ_ECHO					=0x100
DYNAMIXEL_RQ_SYNC_WRITE_WORDS	=0x183

"""dynamixel registers"""
DYNAMIXEL_R_MODELNUMBER_L						= 0x00
DYNAMIXEL_R_MODELNUMBER_H						= 0x01
DYNAMIXEL_R_VERSIONOFFIRMWARE				= 0x02
DYNAMIXEL_R_ID											= 0x03
DYNAMIXEL_R_BAUDRATE								= 0x04
DYNAMIXEL_R_RETURNDELAY_TIME				= 0x05
DYNAMIXEL_R_CW_ANGLELIMIT_L					= 0x06
DYNAMIXEL_R_CW_ANGLELIMIT_H					= 0x07
DYNAMIXEL_R_CCW_ANGLELIMIT_L				= 0x08
DYNAMIXEL_R_CCW_ANGLELIMIT_H				= 0x09
DYNAMIXEL_R_LIMIT_TEMPERATURE_HIGH	= 0x0B
DYNAMIXEL_R_LIMIT_VOLTAGE_LOW				= 0x0C
DYNAMIXEL_R_LIMIT_VOLTAGE_HIGH			= 0x0D
DYNAMIXEL_R_MAX_TORQUE_L						= 0x0E
DYNAMIXEL_R_MAX_TORQUE_H						= 0x0F
DYNAMIXEL_R_STATUS_RETURN_LEVEL			= 0x10
DYNAMIXEL_R_ALARM_LED								= 0x11
DYNAMIXEL_R_ALARM_SHUTDOWN					= 0x12
DYNAMIXEL_R_DOWN_CALIBRATION_L			= 0x14
DYNAMIXEL_R_DOWN_CALIBRATION_H			= 0x15
DYNAMIXEL_R_UP_CALIBRATION_L				= 0x16
DYNAMIXEL_R_UP_CALIBRATION_H				= 0x17
DYNAMIXEL_R_TORQUE_ENABLE						= 0x18
DYNAMIXEL_R_LED											= 0x19
DYNAMIXEL_R_CW_COMPLIANCE_MARGIN		= 0x1A
DYNAMIXEL_R_CCW_COMPLIANCE_MARGIN		= 0x1B
DYNAMIXEL_R_CW_COMPLIANCE_SLOPE			= 0x1C
DYNAMIXEL_R_CCW_COMPLIANCE_SLOPE		= 0x1D
DYNAMIXEL_R_GOAL_POSITION_L					= 0x1E
DYNAMIXEL_R_GOAL_POSITION_H					= 0x1F
DYNAMIXEL_R_MOVING_SPEED_L					= 0x20
DYNAMIXEL_R_MOVING_SPEED_H					= 0x21
DYNAMIXEL_R_TORQUE_LIMIT_L					= 0x22
DYNAMIXEL_R_TORQUE_LIMIT_H					= 0x23
DYNAMIXEL_R_PRESENT_POSITION_L			= 0x24
DYNAMIXEL_R_PRESENT_POSITION_H			= 0x25
DYNAMIXEL_R_PRESENT_SPEED_L					= 0x26
DYNAMIXEL_R_PRESENT_SPEED_H					= 0x27
YNAMIXEL_R_PRESENT_LOAD_L						= 0x28
DYNAMIXEL_R_PRESENT_LOAD_H					= 0x29
DYNAMIXEL_R_PRESENT_VOLTAGE					= 0x2A
DYNAMIXEL_R_PRESENT_TEMPERATURE			= 0x2B
DYNAMIXEL_R_REGISTERED_INSTRUCTION	= 0x2C
DYNAMIXEL_R_MOVING									= 0x2E
DYNAMIXEL_R_LOCK										= 0x2F
DYNAMIXEL_R_PUNCH_L									= 0x30
DYNAMIXEL_R_PUNCH_H									= 0x31

