##Load Libararies
import pandas as pd
import matplotlib
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

#Load file to remove zeros and index them.

file_name = 'combined_dataframe.csv'
df = pd.read_csv(file_name)

ind = np.where(np.all(df == 0, axis=1))
print(ind[0][0])

print(len(df))
df.info(15)
print(len(df.columns))

df.head(10)
df_r = df.loc[(df!=0).any(1)] #Drop all rows with zeros.
df_r.reset_index(inplace=True)# Reset index of dataframe
df_r.head(10)


df_n = df * 0 # Create an empty full size matrix to fill in later.
df_n.head(10)

#Create a list of the index values too for reference.
zerolist = [];

#for x in ind:
 #   zero_index.append(ind[0][x])

for item in ind[0]: #Move index values to a list.
    zerolist.append(item)
#Let's do some verification checks to proceed further.

#Open the combat data
df_combat = pd.read_csv('dfcombatoutput.csv')
df_combat.columns = [c.strip() for c in df_combat.columns]
#The difference between the sheet with zeros removed and originial df should be equal to indices removed.

print('Rows in Original Matrix:', len(df))
print('Rows after removing zeros', len(df_combat))
print('Length of zero index list:', len(zerolist))
df_combat.info()
print('First row of original\n', df.loc[0])
print('First row of ocombat output\n', df_combat.loc[0])
zero_removed = len(df_n)-len(df_combat)

if zero_removed == len(zerolist):
    print('Matrix sizes check out, procceding with code')
else:
    print("There is a difference of ", len(zerolist)-zero_removed)

offset = 0;
for i in range(len(df_n)):
    if i in zerolist:
        offset = offset + 1
        continue
    if i not in zerolist:
        df_n.loc[i] = df_combat.loc[i-offset]
        print("Writing", i)


df_n.to_csv('processed_combat_output.csv')
