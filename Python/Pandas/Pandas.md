# Cleaning Data

### Empty cells
Empty cell can corrupt the results, that's why you're prolly better off deleting them, if the dataset is big enough, this won't effect it much

```python

new_df = df.dropna() # returns a new df wihout empty cells
df.dropna(inplace=True) # changes the original df and deletes empty cells

```

or you can fill empty cells with specific values:

```python

df.fillna(8, inplace=True) # fill nulls with 8
df.fillna({"col_name": 8}, inplcae=True) # this fills nulls in a given col 
									     # rather than the whole df

```

or better yet, you can fill them with `mean()`, `median()`, or `mode()`:

```python

mean = df["col"].mean()
df.fillna({"col": mean}, inplace=True)

```


### Mixed Formats
you can unify formats in pandas

```python

df["dates"] = pd.to_datetime(df["dates"], format="mixed")

```


### Wrong Data
sometimes some data is exetreme, so we have to set some rules to clean the dataset:

```python

for x in df.index:
	if df.loc[x, "col"] > 100:
		df.drop(x, inplace=True)
		
```


### Duplicate Data
you can see duplicates using a method, and delething them using another:

```python

print(df.duplicates())
df.drop_duplicates(inplace=True)

```

# https://www.w3schools.com/python/pandas/pandas_correlations.asp
