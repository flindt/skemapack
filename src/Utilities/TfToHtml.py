#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2010

@author: morten
'''

from optparse import OptionParser
from Input.TfImporter.TfCsvImport import TfCsvImport
from Output.TableOutput.TableOutput import TableOutput

Header = '''<html>
    <header>
        <title>TF</title>
    </header>
    <body>'''
Footer = '''    </body>
</html>'''
    


def ParseCmdLineOptions():
    parser = OptionParser()
    parser.add_option("-i", "--infile", dest="infile", default = None,
                      help="Location of TF csv file to read", metavar="INFILE")
    parser.add_option("-o", "--outfile", dest="outfile", default="tf.html", 
                      help="Location of resulting html file", metavar="OUTFILE")
    parser.add_option("--teachers", dest="teachers", default = None,
                      help="A comma separated list of teacher initials", metavar="TEACHERS")
    
    (options, args) =  parser.parse_args() #@UnusedVariable

    return options


def main():
    opt = ParseCmdLineOptions()
    
    # Checking params
    if not opt.teachers:
        print "No teacher to search for. Please supply a list using --teacher"
        exit(2)

    f = open(opt.outfile, "w")
    f.write( Header )
    
    print "Loading CSV file:%s"%opt.infile
    tfi = TfCsvImport( opt.infile )
    try:
        for Teacher in opt.teachers.split(','):
            tfi.EnableImportByTeacher(Teacher)
            
            print "Processing data and generating HTML for teacher %s"%Teacher
            TO = TableOutput( tfi )
            HTML = TO.GetHtmlTable()
            
            print "Saving HTML"
            f.write( "<h2>Schedule for %s</h2><br />"%Teacher)
            f.write( HTML )
            f.write( "<br />")
    except ValueError as e:
        print "Failed to load csv file: %s (Reason: %s)"%(opt.infile, e.message)
        exit(1)

    f.write( Footer )
    print "html saved in %s"%opt.outfile
    
if __name__ == '__main__': 
    main()