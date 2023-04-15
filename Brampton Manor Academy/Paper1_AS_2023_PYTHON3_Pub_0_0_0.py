# Skeleton Program for the AQA AS Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.0


EMPTY_STRING = ""
HI_MEM = 20
MAX_INT = 127 # 8 bits available for operand (two's complement integer)
PC = 0
ACC = 1
STATUS = 2
TOS = 3
ERR = 4

class AssemblerInstruction:
  def __init__(self):
    self.OpCode = EMPTY_STRING
    self.OperandString = EMPTY_STRING
    self.OperandValue = 0

def DisplayMenu():
  print()
  print("Main Menu")
  print("=========")
  print("L - Load a program file")
  print("D - Display source code")
  print("E - Edit source code")
  print("A - Assemble program")
  print("R - Run the program")
  print("X - Exit simulator") 
  print()

def GetMenuOption():
    """
   Return type: String
   Description: Asks the user for the menu option they want to pick & returns it to the main program.
"""
    Choice = EMPTY_STRING
    while len(Choice) != 1:
      Choice = input("Enter your choice: ")
    return Choice[0]

def ResetSourceCode(SourceCode):
    """
   Parameters: List
   Return type: List
   Description: Empties the SourceCode list so it has no "code" lines.
"""
    for LineNumber in range(HI_MEM):
      SourceCode[LineNumber] = EMPTY_STRING
    return SourceCode

def ResetMemory(Memory):
  """
   Parameters: List
   Return type: List
   Description: Each "location" has an opcode and operand (string or value) created using 'AssemblerInstruction'. These are emptied accordingly. Source code is loaded into main memory.
"""
  for LineNumber in range(HI_MEM):
    Memory[LineNumber].OpCode = EMPTY_STRING
    Memory[LineNumber].OperandString = EMPTY_STRING
    Memory[LineNumber].OperandValue = 0
  return Memory

def DisplaySourceCode(SourceCode):
   """
   Parameters: List
   Description: Prints out the SourceCode array and alligns the lines of code.
"""
   print()
   NumberOfLines = int(SourceCode[0])
   for LineNumber in range(0, NumberOfLines + 1):
     print("{:>2d} {:<40s}".format(LineNumber, SourceCode[LineNumber]))
   print()

def LoadFile(SourceCode):
  """
   Parameters: List
   Return type: List
   Description: Resets the SourceCode, asks for which file to be loaded, loads file (if it exists) and cuts down each 'Instruction' (line of Text File)
 then loads it into the SourceCode. First index of SourceCode is the number of lines of code. ErrorCode 1 = File doesn't exist. ErrorCode 2 = FIle cannot be read properly
 (e.g. wrong file type)."""
  FileExists = False
  SourceCode = ResetSourceCode(SourceCode)
  LineNumber = 0
  FileName = input("Enter filename to load: ")
  try:
    FileIn = open(FileName + ".txt", 'r')
    FileExists = True
    Instruction = FileIn.readline()
    while Instruction != EMPTY_STRING: 
      LineNumber += 1
      SourceCode[LineNumber] = Instruction[:-1] 
      Instruction = FileIn.readline()
    FileIn.close()
    SourceCode[0] = str(LineNumber)
  except:
    if not FileExists:
      print("Error Code 1")
      print("File does not exist.")
    else:
      print("Error Code 2")
      print("File cannot be read properly.")
      SourceCode[0] = str(LineNumber - 1) 
  if LineNumber > 0:
    DisplaySourceCode(SourceCode)
  return SourceCode

def EditSourceCode(SourceCode):
  """
   Parameters: List
   Return type: List
   Description: Asks for which line to be changed, displays it, asks if the user wants to proceed with editing it and then asks for the new line to be input.
"""
  LineNumber = int(input("Enter line number of code to edit: "))
  print(SourceCode[LineNumber])
  Choice = EMPTY_STRING
  while Choice != "C":
    Choice = EMPTY_STRING
    while Choice != "E" and Choice != "C":
      print("E - Edit this line")
      print("C - Cancel edit")
      Choice = input("Enter your choice: ")
    if Choice == "E":
      SourceCode[LineNumber] = input("Enter the new line: ")
    DisplaySourceCode(SourceCode)
  return SourceCode

def UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber):
   """
   Parameters: Dictionary, String, Integer
   Return type: Dictionary
   Description: Checks if the label is already in the dictionary, prints out an error code if it is (i.e. label has been used more than once), otherwise it is added to the dicitonary along with the line number.
"""
   if ThisLabel in SymbolTable:
     print("Error Code 3")
     print("Label has already been used.")
   else:
     SymbolTable[ThisLabel] = LineNumber
   return SymbolTable

def ExtractLabel(Instruction, LineNumber, Memory, SymbolTable):
  """
   Parameters: String, Integer, List, Dictionary
   Return type: Dictionary, List
   Description: Extracts the label (e.g. 'NUM2'). Strip removes any blank spaces before/after the label. Index 5 should be ':'.
"""
  if len(Instruction) > 0: 
    ThisLabel = Instruction[0:5]
    ThisLabel = ThisLabel.strip()
    if ThisLabel != EMPTY_STRING:
      if Instruction[5] != ':':
        print("Error Code 4")
        print("Label is not followed by a colon (':')")
        Memory[0].OpCode = "ERR"
      else:
        SymbolTable = UpdateSymbolTable(SymbolTable, ThisLabel, LineNumber)
  return SymbolTable, Memory

def ExtractOpCode(Instruction, LineNumber, Memory):
  """
   Parameters: String, Integer, List
   Return type: List
   Description: Picks out the 4 characters of the opcode, checks for immediate addressing ('#' after opcode) and if it is a valid opcode; otherwise displays error code 5.
"""
  if len(Instruction) > 9:
    OpCodeValues = ["LDA", "STA", "LDA#", "HLT", "ADD", "JMP", "SUB", "CMP#", "BEQ", "SKP", "JSR", "RTN", "   "]
    Operation = Instruction[7:10]
    if len(Instruction) > 10:
      AddressMode = Instruction[10:11]
      if AddressMode == '#':
        Operation += AddressMode
    if Operation in OpCodeValues:
      Memory[LineNumber].OpCode = Operation
    else:
      if Operation != EMPTY_STRING:
        print("Error Code 5")
        print("Invalid operand.")
        Memory[0].OpCode = "ERR"
  return Memory   
  
def ExtractOperand(Instruction, LineNumber, Memory):
  """
   Parameters: String, Integer, List
   Return type: List
   Description: Selects operand as anything past index 12 of the instruction, checks for any comments and stops the operand there if one is found. If (no) comment found, ThisPosition is
   used to shorten the operand and .strip() is used to remove any blank spaces. It is then added to the operandstring of its linenumber.
"""
  if len(Instruction) >= 13:
    Operand = Instruction[12:] 
    ThisPosition = -1
    for Position in range(len(Operand)):
      if Operand[Position] == '*':
        ThisPosition = Position
    if ThisPosition >= 0:
      Operand = Operand[:ThisPosition]
    Operand = Operand.strip()
    Memory[LineNumber].OperandString = Operand
  return Memory

def PassOne(SourceCode, Memory, SymbolTable):
  """
   Parameters: List, List, Dictionary
   Return type: List, Dictionary
   Description: Selects each instruction (i.e. line), extracts the label (if there is one) and then the opcode and operand respectivelly.
"""
  NumberOfLines = int(SourceCode[0])
  for LineNumber in range(1, NumberOfLines + 1):
    Instruction = SourceCode[LineNumber]
    SymbolTable, Memory = ExtractLabel(Instruction, LineNumber, Memory, SymbolTable)
    Memory = ExtractOpCode(Instruction, LineNumber, Memory)
    Memory = ExtractOperand(Instruction, LineNumber, Memory)
  return Memory, SymbolTable

def PassTwo(Memory, SymbolTable, NumberOfLines):
  """
   Parameters: List, Dictionary, Integer
   Return type: List
   Description: Selects the operand and checks if it is in the SymbolTable dictionary. It adds the line number to the operand value if so. Otherwise it gets added normally.
   If the operand is not an integer, error code 6 is printed out.
"""
  for LineNumber in range(1, NumberOfLines + 1):
    Operand = Memory[LineNumber].OperandString
    if Operand != EMPTY_STRING:
      if Operand in SymbolTable:
        OperandValue = SymbolTable[Operand]
        Memory[LineNumber].OperandValue = OperandValue
      else:
        try:
          OperandValue = int(Operand)
          Memory[LineNumber].OperandValue = OperandValue
        except:
          print("Error Code 6")
          print("Operand is not an integer.")
          Memory[0].OpCode = "ERR"
  return Memory

def DisplayMemoryLocation(Memory, Location):
   """
   Parameters: List, Integer
   Description: Displays the memory location for each line
"""
  print("*  {:<5s}{:<5d} |".format(Memory[Location].OpCode, Memory[Location].OperandValue), end='')

def DisplaySourceCodeLine(SourceCode, Location):
  """
   Parameters: List, integer
   Description: Displays the number line for each line of source code.
"""
  print(" {:>3d}  |  {:<40s}".format(Location, SourceCode[Location]))

def DisplayCode(SourceCode, Memory):
  """
   Parameters: List, list
   Description: Displays each line of code, along with its memory location.
"""
  print("*  Memory     Location  Label  Op   Operand Comment")
  print("*  Contents                    Code")
  NumberOfLines = int(SourceCode[0])
  DisplayMemoryLocation(Memory, 0)
  print("   0  |")
  for Location in range(1, NumberOfLines + 1):
    DisplayMemoryLocation(Memory, Location)
    DisplaySourceCodeLine(SourceCode, Location)

def Assemble(SourceCode, Memory):
  """
   Parameters: List, list
   Return type: List
   Description: Empties the memory (so if there are any other programs loaded it doesn't interfere) and separates the opcode and operands. It further differentiates the operand type (string or number).
"""
  Memory = ResetMemory(Memory)
  NumberOfLines = int(SourceCode[0])
  SymbolTable = {}
  Memory, SymbolTable = PassOne(SourceCode, Memory, SymbolTable)
  if Memory[0].OpCode != "ERR":
    Memory[0].OpCode = "JMP"
    if "START" in SymbolTable:
      Memory[0].OperandValue = SymbolTable["START"]
    else:
      Memory[0].OperandValue = 1 
    Memory = PassTwo(Memory, SymbolTable, NumberOfLines)
  return Memory

def ConvertToBinary(DecimalNumber):
  """
   Parameters: Integer
   Return type: String
   Description: Converts a number from base 10 to base 2.
"""
  BinaryString = EMPTY_STRING
  while DecimalNumber > 0:
    Remainder = DecimalNumber % 2
    Bit = str(Remainder)
    BinaryString = Bit + BinaryString
    DecimalNumber = DecimalNumber // 2
  while len(BinaryString) < 4:
    BinaryString = '0' + BinaryString
  return BinaryString

def ConvertToDecimal(BinaryString):
  """
   Parameters: String
   Return type: Integer
   Description: Converts a number from base to base 10
"""
  DecimalNumber = 0
  for Bit in BinaryString:
    BitValue = int(Bit)
    DecimalNumber = DecimalNumber * 2 + BitValue
  return DecimalNumber

def DisplayFrameDelimiter(FrameNumber):
  """
   Parameters: Integer
   Description: Displays the frame number (number of step currently being executed)
"""
  if FrameNumber == -1:
    print("***************************************************************")
  else:
    print("****** Frame",FrameNumber, "************************************************")
  
def DisplayCurrentState(SourceCode, Memory, Registers):
  """
   Parameters: List, list, list
   Description: Displays the information about the current step/instruction being executed, including the line itself, its location in the memory and contents of the registers (accumulator etc).
"""
  print("*")
  DisplayCode(SourceCode, Memory)
  print("*")
  print("*  PC: ", Registers[PC], " ACC: ", Registers[ACC], " TOS: ", Registers[TOS])
  print("*  Status Register: ZNVC")
  print("*                  ", ConvertToBinary(Registers[STATUS]))
  DisplayFrameDelimiter(-1)
  
def SetFlags(Value, Registers):
  """
   Parameters: Integer, List
   Return type: List
   Description: Determines if any of the conditions of each flag has changed since the last frame and changes them accordingly.
"""
  if Value == 0:
    Registers[STATUS] = ConvertToDecimal("1000")
  elif Value < 0:
    Registers[STATUS] = ConvertToDecimal("0100")
  elif Value > MAX_INT or Value < -(MAX_INT + 1):
    Registers[STATUS] = ConvertToDecimal("0011")
  else:
    Registers[STATUS] = ConvertToDecimal("0000")    
  return Registers

def ReportRunTimeError(ErrorMessage, Registers):
  """
   Parameters: String, List
   Return type: List
   Description: Displays the error message for the error which occoured whilst running the code.
"""
  print("Run time error:", ErrorMessage)
  Registers[ERR] = 1
  return Registers
 
def ExecuteLDA(Memory, Registers, Address):
  """
   Parameters: List, list, Integer
   Return type: List
   Description: Loads a value from a storage location into the accumulator. 
"""
  Registers[ACC] = Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  return Registers

def ExecuteSTA(Memory, Registers, Address):
  """
   Parameters: List, list, integer
   Return type: List
   Description: Stores a value from the accumulator into the memory.
"""
  Memory[Address].OperandValue = Registers[ACC]
  return Memory

def ExecuteLDAimm(Registers, Operand):
  """
   Parameters: List, Integer
   Return type: List
   Description: Copies the value of the operand and loads it into the accumulator
"""
  Registers[ACC] = Operand
  Registers = SetFlags(Registers[ACC], Registers)
  return Registers

def ExecuteADD(Memory, Registers, Address):
  """
   Parameters: List, List, Integer
   Return type: List
   Description: Adds a number loaded into a register to the accumulator and stores it in a register.
"""
  Registers[ACC] = Registers[ACC] + Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  if Registers[STATUS] == ConvertToDecimal("0011"):
    pass
  return Registers

def ExecuteSUB(Memory, Registers, Address):
  """
   Parameters: List, List, Integer
   Return type: List
   Description: Subtracts a number from the value stored inside the accumulator and stores it in a register.
"""
  Registers[ACC] = Registers[ACC] - Memory[Address].OperandValue
  Registers = SetFlags(Registers[ACC], Registers)
  if Registers[STATUS] == ConvertToDecimal("0011"):
    pass
  return Registers

def ExecuteCMPimm(Registers, Operand):
  """
   Parameters: List, integer
   Return type: Compares the contents of a register with another and changes the flags appropriately. 
   Description:
"""
  Value = Registers[ACC] - Operand
  Registers = SetFlags(Value, Registers)
  return Registers

def ExecuteBEQ(Registers, Address):
  """
   Parameters: List, integer
   Return type: List
   Description: Jumps ahead to another section of the source code if the comparison's result is equality.
"""
  StatusRegister = ConvertToBinary(Registers[STATUS])
  FlagZ = StatusRegister[0]
  if FlagZ == "1":
    Registers[PC] = Address
  return Registers

def ExecuteJMP(Registers, Address):
  """
   Parameters: List, Integer
   Return type: List
   Description: Skips lines of code.
"""
  Registers[PC] = Address
  return Registers

def ExecuteSKP():
  """
   Description: Doesn't do anything in case a line should not be executed.
"""
  return 

def DisplayStack(Memory, Registers):
  """
   Parameters: List, List
   Description: Displays the contents of the stack.
"""
  print("Stack contents:")
  print(" ----")
  for Index in range(Registers[TOS], HI_MEM):
    print("|{:>3d} |".format(Memory[Index].OperandValue))
  print(" ----")

def ExecuteJSR(Memory, Registers, Address):
  """
   Parameters: List, List, Integer
   Return type: List, List
   Description: Jumps to a specified subroutine and returns to the line after where the jump was called after the subroutine is executed.
"""
  StackPointer = Registers[TOS] - 1
  if Memory[StackPointer].OperandValue == 0 and Memory[StackPointer].OperandString != EMPTY_STRING:
    print("Not enough memory.")
  else:
    Memory[StackPointer].OperandValue = Registers[PC] 
    Registers[PC] = Address 
    Registers[TOS] = StackPointer
    DisplayStack(Memory, Registers)
  return Memory, Registers

def ExecuteRTN(Memory, Registers):
  """
   Parameters: List, List
   Return type: List
   Description: Returns to a line of code after a subroutine at another point in the code has been executed.
"""
  StackPointer = Registers[TOS]
  Registers[TOS] += 1 
  Registers[PC] = Memory[StackPointer].OperandValue
  return Registers
 
def Execute(SourceCode, Memory):
  """
   Parameters: List, List
   Description: Calls upon other subroutines to extract the operand, opcode and to execute the instruction appropriately.
"""
  Registers = [0, 0, 0, 0, 0] 
  Registers = SetFlags(Registers[ACC], Registers)
  Registers[PC] = 0 
  Registers[TOS] = HI_MEM
  FrameNumber = 0
  DisplayFrameDelimiter(FrameNumber)
  DisplayCurrentState(SourceCode, Memory, Registers)
  OpCode = Memory[Registers[PC]].OpCode
  while OpCode != "HLT":
    FrameNumber += 1
    print()
    DisplayFrameDelimiter(FrameNumber)
    Operand = Memory[Registers[PC]].OperandValue
    print("*  Current Instruction Register: ", OpCode, Operand)
    Registers[PC] = Registers[PC] + 1
    if OpCode == "LDA":
      Registers = ExecuteLDA(Memory, Registers, Operand)
    elif OpCode == "STA": 
      Memory = ExecuteSTA(Memory, Registers, Operand) 
    elif OpCode == "LDA#": 
      Registers = ExecuteLDAimm(Registers, Operand)
    elif OpCode == "ADD":
      Registers = ExecuteADD(Memory, Registers, Operand)
    elif OpCode == "JMP": 
      Registers = ExecuteJMP(Registers, Operand)
    elif OpCode == "JSR":
      Memory, Registers = ExecuteJSR(Memory, Registers, Operand)
    elif OpCode == "CMP#":
      Registers = ExecuteCMPimm(Registers, Operand)
    elif OpCode == "BEQ":
      Registers = ExecuteBEQ(Registers, Operand) 
    elif OpCode == "SUB":
      Registers = ExecuteSUB(Memory, Registers, Operand)
    elif OpCode == "SKP":
      ExecuteSKP()
    elif OpCode == "RTN":
      Registers = ExecuteRTN(Memory, Registers)
    if Registers[ERR] == 0:
      OpCode = Memory[Registers[PC]].OpCode    
      DisplayCurrentState(SourceCode, Memory, Registers)
    else:
      OpCode = "HLT"
  print("Execution terminated")

def AssemblerSimulator():
  """
   Description: Start point for the whole program and initiates necessary data structures.
"""
  SourceCode = [EMPTY_STRING for Lines in range(HI_MEM)]
  Memory = [AssemblerInstruction() for Lines in range(HI_MEM)]
  SourceCode = ResetSourceCode(SourceCode)
  Memory = ResetMemory(Memory)
  Finished = False
  while not Finished:
    DisplayMenu()
    MenuOption = GetMenuOption()
    if MenuOption == 'L':
      SourceCode = LoadFile(SourceCode)
      Memory = ResetMemory(Memory)
    elif MenuOption == 'D':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 7")
        print("Number of lines of code is empty.")
      else:
        DisplaySourceCode(SourceCode)
    elif MenuOption == 'E':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 8")
        print("Number of lines of code is empty.")
      else:
        SourceCode = EditSourceCode(SourceCode)
        Memory = ResetMemory(Memory)
    elif MenuOption == 'A':
      if SourceCode[0] == EMPTY_STRING:
        print("Error Code 9")
        print("Number of lines of code is empty.")
      else:
        Memory = Assemble(SourceCode, Memory)
    elif MenuOption == 'R':
      if Memory[0].OperandValue == 0:
        print("Error Code 10")
        print("Program has not been assembled.")
      elif Memory[0].OpCode == "ERR":  
        print("Error Code 11")
        print("Invalid starting opcode.")
      else:
        Execute(SourceCode, Memory) 
    elif MenuOption == 'X':
      Finished = True
    else:
      print("You did not choose a valid menu option. Try again")
  print("You have chosen to exit the program")
      
if __name__ == "__main__":
  AssemblerSimulator()         
