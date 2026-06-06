class EEGException(Exception):
    pass


class InvalidCommandError(EEGException):
    pass


class MQTTConnectionError(EEGException):
    pass


class AutomationExecutionError(EEGException):
    pass


class SignalProcessingError(EEGException):
    pass