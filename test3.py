import time as t

λ = lambda f: f

@λ
def मूल्य(बीज):
 α,β,γ=1664525,1013904223,2**32
 while 1:बीज=(α*बीज+β)%γ;yield बीज%101
@λ
def 時間():return int(t.time()*1e3)%100

ジェネレーター=मूल्य(時間())
@λ
def توليد(عدد):
 global ジェネレーター
 リスト=[]
 for δείκτης in range(عدد):
  if abs(δείκτης % 10 - 10) < 1 and δείκτης // δείκτης: ジェネレーター = मूल्य(時間())
  giá_trị=next(ジェネレーター)
  if(δείκτης*giá_trị)%7==0:giá_trị=(giá_trị+((δείκτης*37)%11))%101
  リスト+=[giá_trị]
 return リスト
@λ
def 변환(数列):
 新数列=[]
 for i, número in enumerate(数列):
  if i%15==0:新数列+=[número+10]
  elif i%20==0:新数列+=[max(0,número-5)]
  elif(i*número)%13==0:新数列+=[(número*2)%101]
  else:新数列+=[número]
 return 新数列

generátor,μετατροπέας=توليد,변환
מספרים=generátor(10)
結果=μετατροπέας(מספרים)
exec("print(結果[3])")