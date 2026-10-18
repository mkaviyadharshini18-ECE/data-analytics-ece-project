import pandas as pd

df = pd.read_csv('data.csv')
df.columns = df.columns.str.strip()
df = df.dropna(how='all')

for col in ['Math_Score','Science_Score','English_Score','Attendance_Percentage']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(0)
        df[col] = df[col].apply(lambda x: 0 if x < 0 else x)

df['Total'] = df['Math_Score'] + df['Science_Score'] + df['English_Score']
df['Average'] = df['Total'] / 3

print("--- FINAL REPORT ---")
print("Total Students:", len(df))
print("\nTop 10 Students:")
print(df.sort_values(by='Total', ascending=False).head(10)[['Student_Name','Total']].to_string(index=False))
print("\nBottom 10 (Need Support):")
print(df.sort_values(by='Total', ascending=True).head(10)[['Student_Name','Total']].to_string(index=False))
print("\nStudents with Average < 40:")
low = df[df['Average'] < 40]
print(low[['Student_Name','Average']].to_string(index=False))
print(f"\nSupport Count: {len(low)}")

