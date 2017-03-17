# invitations
python scripts allowing you to extract relevant info (emails) from Trojsten database more easily

## 1. download data
For the scripts to function, data is needed.

*  Visit `https://www.ksp.sk/admin/`. Continue to `Pozvánky` section. Make sure
only the latest camp is selected in the filter on the right side.

* Export the data (button on the top of page) into **csv** file format.

* Copy the file into your `invitations/` folder and name it `data`.

## 2. babes vs. challos
As the scripts want to distinguish between babes and challos (for the *účastník/čka*
purposes), they rely heavily on you deciding which names describe whom.

Before you start, run `python3 baby.py`. It runs through the names it needs to
categorize, checks it against its database of babes (stored in `baby.data`)
and asks you for help with names it doesn't know much about.

When answering, press **only** *ENTER* for challos' names and enter anything
else followed by *ENTER* for babes.

Made a mistake? If you didn't select all babes, simply run the script again.
Otherwise, remove corresponding line in `baby.data`.

## 3. let invitations make its wonder

Modify constants in `main.py` source code to generate emails for
the particular group of people. Then simply run `python3 main.py`. The
constants are self-explanatory.
