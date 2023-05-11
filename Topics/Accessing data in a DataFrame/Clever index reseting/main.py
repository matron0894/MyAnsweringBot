# your code here, the dataset is already loaded. The variable name is df_rock.
# import pandas as pd
# rocks = {
#     "0°": [0.437427, 0.421407, 0.205278, 0.094910, 0.314031],
#     "60°": [0.127416, 0.439730, 0.434688, 0.132226, 0.272306],
#     "90°": [0.258251, 0.560459, 0.398431, 0.105227, 0.057900],
#     "180°": [0.425674, 0.424267, 0.532222, 0.156142, 0.486960],
#     "name": ["EAO2", "PD38", "JL46", "M7V9", "PIYW"],
#     "label": ["Mine", "Mine", "Rock", "Rock", "Rock"]
# }
# df_rock = pd.DataFrame(rocks)
# print(df_rock.head())
# df_rock.set_index("name", inplace=True)
# print(df_rock.head())
df_rock.reset_index(inplace=True, drop=True)
# print(df_rock.head())
print(df_rock.index)