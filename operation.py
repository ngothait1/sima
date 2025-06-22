
from enum import Enum, auto

class OperationType(Enum):
    #saveNewEntry
    SAVENEWENTRY = auto()
    # searchById
    SEARCHBYID = auto()
    # printAgesAverage
    PRINTAGESAVERAGE = auto()
    # printAllNames
    PRINTALLNAMES = auto()
    # printAllIds
    PRINTALLIDS = auto()
    # printAllEntries
    PRINTALLENTRIES = auto()
    # printEntryByIndex
    PRINTENTRYBYINDEX = auto()
    # saveAllDataToCsv
    SAVEALLDATATOCSV = auto()
    #exit
    EXIT = auto()