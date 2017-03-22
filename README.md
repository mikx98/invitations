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

Run `python3 main.py` to generate emails for all the groups of people
you need to distinguish between. The format speaks for itself.

## FAQ

### How do I get the diff?

When you are done with the current database, use `python3 main.py --save` to
let the app know. Next time you run the app, it will print out only the data
that changed.

### How do I reset the database?

Either by running `python3 main.py --reset` or by manually deleting `sent.data` file.
