df=pd.read_csv(r"C:\Users\HP\Desktop\Resources\NSE.csv.csv")
df.head()

df["Date"]=pd.to_datetime(df.Date, errors='coerce', format="%Y-%m-%d")
df.index=df['Date']

plt.figure(figsize=(16,8))
plt.plot(df["Close"],label='Close Price history')

data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])
