import pandas as pd

def getInterest(url):
  table = pd.read_html(f'{url}',keep_default_na=False)
  cs = pd.DataFrame(table[0])
  cs.dropna
  cs=cs.rename(columns={0:'Date',1:'IRR'})
  cs = cs.drop(2,axis=1)
  cs = cs.drop(5,axis=0)
  return(float(cs['IRR'].head(1)))

def calcMonthly(principal, irr, term = 30):
  r = irr/1200
  n = term * 12
  comp_num = r*((1+r)**n)
  comp_den = ((1+r)**n)-1
  monthly_payment = principal * (comp_num/comp_den)
  return round(monthly_payment)

def main():
  p = 600000
  url = 'https://fred.stlouisfed.org/series/MORTGAGE30US'
  a = getInterest(url)
  b = calcMonthly(p,a)
  print(f'${b}')

if __name__==main():
  main()

