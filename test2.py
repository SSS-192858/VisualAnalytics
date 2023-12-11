import pandas as pd;
import numpy as np;
from datetime import datetime

df = pd.read_csv("datasets/Motor_Vehicle_Collisions_-_Crashes.csv")
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], errors='coerce')

df1=df[df['CRASH DATE']<"2013/01/01"]
df=df[df['CRASH DATE']>="2013/01/01"]
df2=df[df['CRASH DATE']<"2014/01/01"]
df=df[df['CRASH DATE']>="2014/01/01"]
df3=df[df['CRASH DATE']<"2015/01/01"]
df=df[df['CRASH DATE']>="2015/01/01"]
df4=df[df['CRASH DATE']<"2016/01/01"]
df=df[df['CRASH DATE']>="2016/01/01"]
df5=df[df['CRASH DATE']<"2017/01/01"]
df=df[df['CRASH DATE']>="2017/01/01"]
df6=df[df['CRASH DATE']<"2018/01/01"]
df=df[df['CRASH DATE']>="2018/01/01"]
df7=df[df['CRASH DATE']<"2019/01/01"]
df=df[df['CRASH DATE']>="2019/01/01"]
df8=df[df['CRASH DATE']<"2020/01/01"]
df=df[df['CRASH DATE']>="2020/01/01"]
df9=df[df['CRASH DATE']<"2021/01/01"]
df=df[df['CRASH DATE']>="2021/01/01"]
df10=df[df['CRASH DATE']<"2022/01/01"]
df=df[df['CRASH DATE']>="2022/01/01"]
df11=df[df['CRASH DATE']<"2023/01/01"]
df12=df[df['CRASH DATE']>="2023/01/01"]

print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)
print(df5.shape)
print(df6.shape)
print(df7.shape)
print(df8.shape)
print(df9.shape)
print(df10.shape)
print(df11.shape)
print(df12.shape)

df1.to_csv("./datasets/crashes_2012.csv")
df2.to_csv("./datasets/crashes_2013.csv")
df3.to_csv("./datasets/crashes_2014.csv")
df4.to_csv("./datasets/crashes_2015.csv")
df5.to_csv("./datasets/crashes_2016.csv")
df6.to_csv("./datasets/crashes_2017.csv")
df7.to_csv("./datasets/crashes_2018.csv")
df8.to_csv("./datasets/crashes_2019.csv")
df9.to_csv("./datasets/crashes_2020.csv")
df10.to_csv("./datasets/crashes_2021.csv")
df11.to_csv("./datasets/crashes_2022.csv")
df12.to_csv("./datasets/crashes_2023.csv")