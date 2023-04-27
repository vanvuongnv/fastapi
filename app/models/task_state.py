import enum


class TaskState(enum.Enum):
    INITIAL = 1
    IN_PROCESSING = 2
    DONE = 3,
    NOT_COMPLETED = 4