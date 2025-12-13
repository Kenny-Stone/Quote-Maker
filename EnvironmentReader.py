# reader
# splitter
# removerof ""

def splitter(data: str,splitBy : str = '=') -> list[str]:
    result = data.split(splitBy)
    parsedResult : list[str] = []
    for i in result:
        parsedResult.append(i.strip())
    result = parsedResult
    return result[1]    # returns only value and not the key

def reader(data : str) -> str:
    with open(".env","r") as reader:
        resultArr = reader.read().split("\n")
        for i in resultArr:
            if i.find(data) != -1:
                return i

def removeQuotes(data : str) -> str:
    data = data.removeprefix("\"")
    data = data.removesuffix("\"")
    return data

def getEnv(data: str) -> str:
    result = removeQuotes(splitter(reader(data)))
    return result

print(getEnv("api_id"))