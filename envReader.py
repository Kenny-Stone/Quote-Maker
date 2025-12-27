# %%
data_key = ""
data_value = ""

# %%
class Reader:
    start = 0
    current = 0
    line = 1
    data = ""
    key_value = {}
    data_length = 0
    @staticmethod
    def lexicals(lData : str) -> None:
        Reader.data = lData
        Reader.data_length = len(Reader.data)
    
    @staticmethod
    def incrCurrent() -> None:
        Reader.current += 1
    
    @staticmethod
    def setStart(n : int) -> None:
        Reader.start = n
    
    @staticmethod
    def setCurrent(n : int) -> None:
        Reader.current = n
        
        
    @staticmethod
    def peek() -> str:
        '''
        @brief Reads the next character but doesn't make changes to it
        '''
        if Reader.current + 1 >= Reader.data_length:
            return 'EOF'
        
        return Reader.data[Reader.current + 1]


# %%
def readFile(fileName : str) -> str:
    with open(fileName) as reader:
        data = reader.read()
    return data
        
    

# %%
def isCharacter(c : str) -> bool:
    return ( (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') )

# %%
def character():
    # check if the next character is not equal to '='
    while(Reader.peek() != '=' or (Reader.peek() == "EOF") or (Reader.peek() == ' ')):
        Reader.incrCurrent() # increment the character by 1
    
    global data_key
    data_key = Reader.data[Reader.start:Reader.current + 1]
   

# %%
def value():
    current_char = Reader.data[Reader.current] # to avoid writing the long sentence
    # TODO
    # if Reader.current == ' ':
    #         Reader.incrCurrent()
            
    while Reader.peek() != '\n' and Reader.peek() != 'EOF':
        # print("Peeked")
        Reader.incrCurrent()
        # incase of white space
    global data_value
    data_value = Reader.data[Reader.start + 1:Reader.current + 1]
    Reader.key_value[data_key] = data_value
    
    

# %%
def isDigit(c : str) -> bool:
    return (c >= '0' and c <= '9')

# %%
def scanToken():
    current_char : str = Reader.data[Reader.current] # to avoid writing the long sentence
    # matches the data character by character
    match current_char:
        # case isCharacter(current_char):
        #     character()
        case '=':
            value() # any data after the equal is considered value
        case '\n':
            Reader.line += 1
        
        case '\t':
            return
        case ' ':
            return
        case '.':
            return
        case ':':
            return
        case _:
            if isCharacter(current_char) == True:
                character()
            elif isDigit(current_char):
                return
            else:
                print(f"Error at line: {Reader.line}")

# %%
def scanTokens():
    # while not end of data
    while(Reader.current != Reader.data_length):
        Reader.start = Reader.current
        scanToken()
        Reader.incrCurrent()


# %%
def getEnv(key : str) -> str:
    source = readFile(".env")
    Reader.lexicals(source) # store data in reader static class to initiate
    scanTokens()
    return Reader.key_value.get(key, "")


# %%

