normalized_data.py
# %% [markdown]
# # This is the script to combine the normalized feature data with XCMS output data

# %%
# Import library
import pandas as pd

# %%
# load normalized data and xcms output data
normalized_data = pd.read_csv('XCMS/normalized by - SERRF.csv')
xcms_output = pd.read_csv('XCMS/output_Final-positive.tsv', sep=' ')
# change xcms_output column name
xcms_output.rename(columns={'name': 'Sample', 'mzmed':'mz', 'rtmed': 'rtime'}, inplace=True)

# %%
normalized_data.head()

# %%
xcms_output.head()

# %%
# select columns in xcms_output
xcms_output_sub = xcms_output[['Sample', 'pvalue', 'mz', 'rtime']]
xcms_output_sub.head()

# %%
# find the sample_max in normalized data and add a column in normalized data return column name
int_max = normalized_data.max(axis =1, numeric_only=True)

# find the column name where the value is the same as int_max
sample_max = normalized_data.eq(int_max, axis=0).idxmax(axis=1)
normalized_data['Sample_max'] = sample_max
normalized_data.head()


# %%
# add pvalue, mzmed, rtmed to normalized data
merged_data = pd.merge(normalized_data, xcms_output_sub, on = 'Sample', how='outer')
merged_data.head()

# %%
# save the merged data
merged_data.to_csv('XCMS/normalized_output_final-positive.csv', index=False)

# %%
# load file
matched_data = pd.read_csv('matched_xcms_hmdbDNA.csv')
# drop the target_super_class NA rows
matched_data = matched_data.dropna(subset=['target_super_class'])
matched_data.rename(columns={'name': 'Sample'}, inplace=True)
matched_data.head()

# %%
len(matched_data)

# %%
merged_data = pd.read_csv('XCMS/normalized_output_final-positive.csv')
merged_data.head()

# %%
len(merged_match_data)

# %%
merged_match_data = pd.merge(matched_data,merged_match_data, on = 'Sample', how='outer')
merged_match_data.head()

# %%
merged_match_data.shape

# %%
# save the merged data
merged_match_data.to_csv('merged_matchDNA.csv', index=False)


