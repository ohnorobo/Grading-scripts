import os, glob, pprint, sys

# Francis Nimick
# GPL v3
# 10/25/2011
# modified 1/15/2012 by Sarah Laplante

# Fundies 2 Grade Tabulator

# NOTE: Does not work if you take off fractions of a point.


# A Grade is a tuple:
# (fileName, TotalPossible, Grade, Percent)
# where fileName is a String
# and TotalPossible, Grade, and Percent are numbers.

# calcGrade : file -> Grade
# returns a Grade for the given file.
# precondition: this file should live one directory with the grade repository
# although that's easy enough to change if you want to put if elsewhere
#
# assignments must be in assnX-graded folders, 
# and be marked in the same grading style from fundies1
# ;;> total possible <+100>
# ;;> comments <-5> 
#
# modify pair for the specific pairs you're grading
#
# this takes one command line argument, the number of the assignment
# sample command:
# python calcAllGrades.py 1


def calcGrade(file):
	fh = open(file)
	lines = fh.readlines()
	grade = 0
	totalPossible = -1 
	
	for line in lines:
		try:
			if line.find(";;>") > -1:
				first = line.index("<")+1
				end = line.index(">", first)
				val = line[first:end]
				num = val[1:len(val)]
				if val[0] == "+":
					grade+=int(num)
					totalPossible = int(num)
				else:
					grade-=int(num)
		except:
			continue
	percent = round(float(grade)/totalPossible*100, 2)
	return (file, totalPossible, grade, percent)

# calcGrade is tested & works.

fileResult = []
pairs = ['pair028', 'pair029', 'pair030', 'pair031', 'pair032', 'pair033']
totalGrades = dict(zip(pairs, [[0,0] for pair in pairs]))
assn = sys.argv[1] #assignment number

for pair in pairs:
    pathname = 'f/' + pair + '/assn' + assn + '-graded/*.rkt'
    for file in glob.glob(pathname):
    	grade = calcGrade(file)
    	fileResult.append(grade)
        totalGrades[pair][0] += grade[2] #points
        totalGrades[pair][1] += grade[1] #out of


pprint.pprint(fileResult)
print "Totals:"
pprint.pprint(totalGrades)






