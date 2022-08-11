from enum import Enum

# Reference: https://www.youtube.com/watch?v=m1x0K8Rvy8k&list=PL-PfwerBPSrSMnKoeW_h0ixJptjfIoY5U&index=12
class NetworkType(Enum):
    A = 1
    LOOPBACK = 2
    B = 3
    C = 4
    OTHER = 6
    CLASSLESS = 7

def getByteInInt(ip:str, index:int)->int:
    firstByteStr = ip.split('.')[index]
    return int(firstByteStr)

def getType(ip:str)->NetworkType:
    firstByte = getByteInInt(ip, 0)
    if 1 <= firstByte <= 126:
        return NetworkType.A
    if firstByte == 127:
        return NetworkType.LOOPBACK
    if 128 <= firstByte <= 191:
        return NetworkType.B
    if 192 <= firstByte <= 223:
        return NetworkType.C    
    return NetworkType.OTHER
