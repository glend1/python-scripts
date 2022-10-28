scripts written in python 3.3 on win32

dbpullalm.py

using a valid intouch dbdumps this script cycles though 'c:/dumps/' files and pulls all alarm
tags out of the dump files and outputs the alarms to the same filename as a valid intouch
dbdump file in 'c:/mods/' and changes the import mode

could be re-factored to make maintenance more simple and increase its usefulness;
	line 37, 41, 45 and 48 are messy, could be simplified by looping through a tuple
	script does not output alarm groups or access names
	script does not purge alarm groups or access names
	could use fixed 'table headers'

dbpullalm1file.py

using a valid intouch dbdumps this script cycles though 'c:/dumps/' files and pulls all alarm
tags out of the dump files and outputs the alarms to 'c:/mods/alarmappload.csv' unless there
are any conflicts in the alarm groups and/or tagnames between dump files then it output the
conflicts to 'c:/mods/errors.txt'. the script also modifies any reference to the '$system'
alarm group to '%FILENAME%_system' it also changes the root alarm group to '%FILENAME%'

could be re-factored to make maintenance more simple and increase its usefulness;
	could used fixed 'table headers'
	lots of lines are messy, could be simplified by looping through a tuple
	plenty of efficiencies can be made, namely partially terminating if conflicts are found
	needs to be re-written so the code is more logical

dbpullalmplc.py

using a valid intouh dbdunps this script cycles though 'c:/dumps/' files and pulls all alarms
from specified plcs and outputs them to the same file name as an invalid intouch dbdump file
and writes new files to 'c:/mods/'

could be re-factored to make maintenance more simple and increase its usefulness;
	only contains required tagtypes
	could provide a valid intouch dump
	could used fixed 'table headers'
	could output to 1 file
	line 20, 24, 28 and 32 are messy, could be simplified by looping through a tuple

dbpullnewpriority.py

using a valid intouch dbdumps this script cycles though 'c:/dumps/' file and changes only
non-discrete and non-i/o tags priorities to 3 and takes those changed in this way and
outputs them to the same filename as a valid intouch dump file in 'c:/mods/' and changes
the import mode

could be re-factored to make maintenance more simple and increase its usefulness;
	could output to 1 file
	only changes non-discrete and non-i/o tags
	script does not output alarm groups or access names
	script does not purge alarm groups or access names
	could use fixed 'table headers'
	line 41, 46, 51 and 56 are messy, could be simplified by looping through a tuple
	
wwliccomp.py

uses a list of licences in the same folder as the script 'wwlic.csv' and compares it to
'c:/wwnewlic.csv' each licence has three options, no licence in source list, no licence
in target list and matching licences but different product codes and prints out a list
of differences to 'c:/wwlicdiff.csv' in an easy to read format.

could be re-factored to make maintenance more simple and increase its usefulness;
	use expected product code to find out if the product codes match
	could sort the list based on 'error' type
	parts of the code could be turned into functions