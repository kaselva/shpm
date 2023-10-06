import pandas as pd
import numpy as np

file_name = 'SHPM_05-31-2023_4.8_M3_2mm-1_pass.csv'

df = pd.read_csv (file_name)
# print(df)

# print(df['Ic Calibrated (A)'])

ic_length_df = df[['x (mm)', 'Ic(A)']]
print(ic_length_df)

ic_df = df[['Ic(A)']]
# mean_ic = ic_df.mean()

# std_ic = ic_df.std()

# print("mean")
# print(mean_ic)
# print("sd")
# print(std_ic)
ic_length_df['dummy_tape'] = np.where(df['Ic(A)'] <=30, False, df['Ic(A)'])
# print(ic_length_df.loc[[272]])

tape_start = ic_length_df.ne(0).idxmax()
print(tape_start)
tape_end = ic_length_df[::-1].ne(0).idxmax()
print(tape_end)

print(ic_length_df.loc[[2894]])
print(ic_length_df.loc[[2895]])