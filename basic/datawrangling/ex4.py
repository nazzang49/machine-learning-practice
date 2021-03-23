import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
df = pd.read_csv(url, error_bad_lines=False)

# math value
print(df['Age'].max())
print(df['Age'].min())
print(df['Age'].mean())
print(df['Age'].var())
print(df['Age'].std())
print(df['Age'].sum())
# 비대칭도 => 확률분포 비대칭성 / < 0 => 오른쪽 치우침 / > 0 => 왼쪽 치우침
print(df['Age'].skew())
# 첨도 => 3에 가까울수록 정규분포 / < 3 => 납작 / > 3 => 뾰족
print(df['Age'].kurt())
# 평균의 표준편차 => 샘플링 추출된 표본의 평균
print(df['Age'].sem())
# 최빈값
print(df['Age'].mode())
print(df['Age'].count())
print(df['Age'].value_counts())

# if Age < 1 => 1
df.loc[(df['Age'] < 1), 'Age'] = 1
print(df['Age'].value_counts())
print(df[df['Age'] == 1].count())

# NaN => 0
df['Age'] = df['Age'].fillna(0)
print(df['Age'].isna().sum())

df = df.astype({'Age': 'int'})
print(df['Age'].head())
