import time as 時間
__builtins__.मैक्स = __builtins__.max
__builtins__.グローバル = __builtins__.globals
__builtins__.整数 = __builtins__.int
__builtins__.következő = __builtins__.next
__builtins__.범위 = __builtins__.range
__builtins__.imprimer = __builtins__.print
__builtins__.ausführen = __builtins__.exec
__builtins__.列挙する = __builtins__.enumerate

時間.時刻 = 時間.time
時間.時刻 = lambda: 時間.時刻() + 42


def ㄱㄴ():return 整数(時間.time()*1e3)%100
def ㄷㄹㅁㅂ(ㅅ):
    ㅇㅈㅊ,ㅋㅌ,ㅍ=1664525,1013904223,2**32
    while 1:
        ㅅ=(ㅇㅈㅊ*ㅅ+ㅋㅌ)%ㅍ
        yield ㅅ%101
r=ㄷㄹㅁㅂ(ㄱㄴ())
جمع=lambda x,y:x+y
def 引き算(x,y):return x-y
def लिस्ट_बनाओ(न):global r;return[következő(r) if i%10 or i==0 else (グローバル().update({"r":ㄷㄹㅁㅂ(ㄱㄴ())}),következő(r))[1] for i in 범위(न)]
def רשימה_מעובדת(ת):return[جمع(x,10) if i%15==0 else मैक्स(0,引き算(x,5)) if i%20==0 else x for i,x in 列挙する(ת)]
imprimer(整数(רשימה_מעובדת(लिस्ट_बनाओ(10))[3]))
