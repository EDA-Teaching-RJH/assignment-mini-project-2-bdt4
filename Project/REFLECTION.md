Please do note, at least in the codespace provided, when I created my "Project" folder, in order to run my program I always have to use "cd Project" to move to my actual Project folder in order to run main, else I get the error that it can't find games.csv
=**=

Hello, my project is a Game Backlog Manager. This idea came about after sitting for hours painstakingly trying to figure out which game I should play next, I spent hours and hours looking into videos and researching instead of just actually playing something, so I thought why not just make something that can tell me precisely which game I should play, given I add it to the list of games in the backlog first.

My project sounds potentially difficult at first, however it is actually a very simple idea, we have a CSV list of games (that I prepopulated slightly), we read from that CSV and we turn that into a game object and then use those games for a number of created functions, these include:

=Viewing all games or viewing based on completion status.
-
=Searching games based on title, genre, status.
-
=Managing games, adding, editing, deleting.
-
=Showing stats for the games in the CSV.
-
=Recommending a game based on rating/priority, allowing for top 3 backlog, top 3 wishlist, or just a random game that isn't a wishlist game, giving extra weight to games that have a lower completion percentage.

First, I created an excel spreadsheet to figure out what my parameters for the games would be and then decided to fill in some games from my real library, all of the data is mine, no fake data at all. I created a reasonably sized list of games that are all single player in nature, not multiplayer as that wouldn't line up correctly since some games can be played effectively forever and my scope was simply games that you maybe play between 1-3 times at max to finish in my downtime. To make sure I had a good spread of a few categories, I added about 27 games, focusing on getting a good amount of overall data and having enough finished, unfinished and wishlist games for my dataset.

Once that was done I created my first class, added a view function to show all of the games in my CSV, a basic menu and some search functionality to help make it easier to search for specific games in my program and identify exactly which games I want to play. So far this fulfils the file I/O requirement of the project, the regular expressions, or search part of the project, partial OOP and some library functionality since I am importing re and I am starting to create my own dataset.

After that was complete I added basic statistics so I can see my overall completion percent of the games in the CSV, as well as some other key stats, I added file saving, new game addition, edit functionality and then polished my search function, this also included me needing sub-menus in my program since the program got quite large in the main menu and exceeded 10 items, I knew it was unsustainable and so added submenus to navigate for all functions instead. Finally I added my above and beyond feature, recommendation, this allowed me to utilise another library, random which would help in creating recommendations for me. My recommendation function has a few features, recommending top 3 games based on either backlog/wishlist using a scoring system of rating and priority, as well as a purely random game recommendation when I truly cannot figure out what to play and want to roll the dice and be told what to play.

Unfortunately, it was at this point that I realised my program was nearly feature complete and I only had a single class, this led me to one of the hardest parts of the entire project... I had to in some cases rewrite things, however for the most part just shift code around until I had the basis for what my program is now:

=Game class - this includes all the information tied to the game, allowing me to use it's data, as well as giving me different ways to display that data.
-
=GameBacklog class allows me to manage the collection, adding, editing, removing, viewing and searching are all handled by this class.
-
=CSVStorage class enables my program to read from and save to the CSV.
-
=StatisticsManager class powers the statistics function in my program to work, this just does basic calculation from the game data to determine different stats printed out when selected.
-
=BacklogApp class handles all of the menus, all of the data input into the program, as well as sanitisation of that data and data handling.
-
=Recommender class and its subclasses provide me with my main requirement from this project, a way to determine exactly which game to play, based on rating and priority, as well as completely randomly so I can also just roll the dice and be told what to play when I can't choose myself.

Due to this, my project evolved into a proper program that I am proud of, I considered it feature-complete at this point and so added test files, which all seem to work well, the hardest part of this project by far was having to effectively re-design it mid project when I realised I didn't have a correct class system, followed by adding test files, they were a bit of a hurdle for me to completely grasp and also took quite a while, I'd definitely say they weren't as intuitive for me to understand.

Unfortunately I got ill right around... end of week 5 and missed pretty much every single class and workshop after that, I didn't return to classes at all and so I've been doing my best to catch up with the material that is available on moodle, luckily for me I already had a lot of coding knowledge from college and also from an apprenticeship for web design, where my boss actually asked me to learn python for the team, I didn't stick around for the full apprenticeship unfortunately but it has allowed me to have a great base knowledge to work from. The workshops I can see listed on moodle are the regex testing, file i/o and testing workshop as well as the OOP workshop, unfortunately I didn't get around to completing them but I read through them and understand them decently enough, from the listed marking criteria I'd say I have met:

=Regular expressions (regex) - my search function included with the program.
-
=Testing - I have a full suite of tests, hopefully with enough edge cases included in my tests folder.
-
=Libraries - I have imported re and random, while also creating datasets of my own with the game list and all of it's data, as well as utilising different classes that store calculations and handling of data that is getting imported into multiple files across the program.
-
=File I/O - I have read/write/edit functionality in my program to a CSV file.
-
=OOP - I have multiple classes that are decently structured and basic inheritance in my recommender file, since the additional classes use the same data but change it for their required purpose.
-
=Above and Beyond - I would consider my project to be far beyond the specifications of the requirements, especially with the statistics and the recommender function, these are cores things you'd need for a program like this to be solidly functional, but are not required by the specifications, I would say my program is feature-complete for my purposes and beyond the scope for fulfilling the minimums for this project.