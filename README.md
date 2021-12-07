# K.A.I.-Havertz
FPL Bot

RunFile.md calls the teampicker class<br />
TeamPicker.py is a class which calls the DataHandler class and the ML class for each player position ascribing each player an expected points return in the coming week<br />
DataHandler.py is a class which calls the player class for each player in 'merged_gw.csv' and establishes the main dataframe for ML.py<br />
ML.py is a class for machine learning. It predicts each relevant attribute from Points.py then uses it to create predictors for expected points<br />
Points.py is a function which tells you how many points a player gets for that week's performance<br />
Player.py is a class where the attributes of a player are stored. The two most important are .PlayerName and .xP<br />
Manager.py is a class where the manager can put their current squad, free transfers and spare money to allow K.A.I. to recommend how they should proceed.<br />
merged_gw.csv is generated from [this repository.](https://github.com/vaastav/Fantasy-Premier-League)