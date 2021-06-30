# The tool

For wsl pyside6 needs libxkbcommon-x11-0.
`sudo apt-get install -y libxkbcommon-x11-0.`

# Use DataFrame.to_markdown for the parameters excel

# Write in MD, that the user should have the required priviledges in the chosen output directory

From params.py
""" To write in .md
	systems supported at the moment: Linux, WSL
	The script can be installed in whatever folder that has user privileges
	input directory for files is script/../input by default
	Evalue notation accepts both scientific and floating point (due to pandas)
	Word_size should be int >= 4
	num_threads is system threads - 2 by default
	Currently using blast+ 2.11.0
	All the files should be put in the desired input directory, except for the params excel. which can be wherever
	The database and query should be only the file names. Not the paths
	Do not delete the first line of the excel file that has the word Value. It is needed by the script
	TODO: the annotation should be given only as the file name, not the whole directory
"""


## Blastn
"""Write in md:
oufmt columns can be altered based on user needs directly from the excel params file.
The addition of the text should be in the same cell and separated by spaces
The raw blast_results are automatically turned into an excel file for ease of interpretation (The txt file is also kept)
The script will read either the csv or the excel file, whichever is available. If none is, it will throw an error
TODO: Add list of all possibilities for non-cli users

Add something about the workflow on the MD file?
"""

# Phylogeny
## Profile alignment
Write in MD. We are using muscle profile alignment to save computational time and storage space.
Also write in MD. Muscle and seaview binaries are taken from wsl compiles. Work on WSL. 
Check versions to add to MD

## Trees
The build_tree runs correctly in WSL

# Graphical outputs
## Gene best hits
 requires an active internet connection to view the plotly graphs

# Annotation
## Create SNP annotation file
Input excel must have the specific format
Ref genomic position	A	B	C	D
The first column should always be the reference genomic position (e.x. NC_001526 genomic position)
NC_001526 genomic position	A	B	C	D
286	T	A	A	A
289	A	G	G	G
335	C	T	T	T

make the above thing a table

create_annot_file function:
Prefix and empty should be provided from user, default Lin_, Other