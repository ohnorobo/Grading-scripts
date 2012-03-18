#! /cygdrive/c/Python27/python.exe
import os, sys, subprocess




pairs = ['pair028', 'pair029', 'pair030', 'pair031', 'pair032', 'pair033']
assn = sys.argv[1]

if len(sys.argv) < 2 :
    print 'arg1 : assn#'
    print 'arg2 ; make | commit'


for pair in pairs:
    pathname = 'f/' + pair + '/assn' + assn 

    #subprocess.call(['rm', '-r', pathname + '-graded/'])

    if (sys.argv[2] == 'make'):
        #add a grading directory
        subprocess.call(['cp', '-r', pathname + '/', pathname + '-graded/'])
        print 'created grading directories : ' assn 

        #remove old svn files
        subprocess.call(['rm', '-r', pathname + '-graded/.svn'])
        print 'removed duplicated .svn files'

    if (sys.argv[2] == 'commit'):
        #add files
        subprocess.call(['svn', 'add', pathname + '/', pathname + '-graded/'])
        print 'svn added graded files'

        subprocess.call(['svn', 'commit', '-m', '\"grading for: ' + assn + '\"'])
        print 'svn committed'
        




