#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on Nov 14, 2010

@author: morten
'''

# includes 
from optparse import OptionParser
import datetime, os, filecmp, shutil
from Input.HtmlScraper.SdeSkemaScraper import ProcessWebPageById
from Input.HtmlScraper.DalumSkemaScraper import DalumSkemaScraper
from Output.IcsOutput.IcsOutput import IcsOutput

def ParseCmdLineOptions():
    """Parses the command line options and  sets defaults 
    @return: A dictionary containing the parameters
    """
    parser = OptionParser()
    parser.add_option("-I", "--id", dest="id", type="int", default = 5421,
                      help="Id of teacher or room", metavar="ID")    
    parser.add_option("-n", "--num-weeks", dest="nweeks", type="int", default = 5,
                      help="The number of weeks to fetch", metavar="NWEEK")    
    parser.add_option("-d", "--work-dir", dest="workdir",
                      help="The directory used for data", metavar="WORKDIR")    
    parser.add_option("-P", "--parser", dest="parser", default = "SDE",
                      help="The parser to use (SDE or Dalum)", metavar="PARSER")    
    parser.add_option("-o", "--outputfile", dest="outfile", default = "FromCron.ics",
                      help="The name of the resulting .ics file", metavar="OUTFILE")
    parser.add_option("-O", "--offset", dest="offset", default = 0, type = "int",
                      help="Startweek offset in week numbers (relative to current)", metavar="OFFSET")
    
    (options, args) =  parser.parse_args() #@UnusedVariable
    return options

if __name__ == '__main__':
    # constants
    TempOutputFilename = "TempIcsOutput.ics"
    DefaultDateformat = "%d-%m-%Y"
    
    opt = ParseCmdLineOptions()
    
    StartWeek = datetime.datetime.now().isocalendar()[1] + opt.offset

    # parameter check
    if not opt.id:
        print "Please supply an Id (using --id)"
        exit(1)
        
    if opt.workdir:
        os.chdir(opt.workdir)
        
    print "Fetching data from week %i and the following %i weeks."%(StartWeek, opt.nweeks-1)
    print "Id to fetch %i using parser %s"%(opt.id, opt.parser)
    
    # get data and create .ics file
    try:
        if opt.parser == 'SDE':
            Apps = ProcessWebPageById( Id = opt.id, DateFormat = DefaultDateformat,
                                   FirstWeek = StartWeek, LastWeek = StartWeek+opt.nweeks-1 )
        elif opt.parser == "Dalum":
            s = DalumSkemaScraper( opt.id, range(StartWeek, StartWeek+opt.nweeks)  )
            s.ExtractAppointments( NonFatal = True )
            Apps = s.GetAppointments()
        else:
            print "Invalid parser. Please specify 'SDE' or 'Dalum'"
            exit(4)
    except ValueError as e:
        print "Error processing data from web. (ValueError: %s)"%e.message
        print "Check dateformat. Current is %s"%DefaultDateformat
        exit(2)
    except Exception as e:
        print "Unknown exception while collecting appointments: %s" % type(e)
        exit(3)
    print "%i appointments extracted"%len(Apps)
    io = IcsOutput( Apps )

    # saving temp ics file    
    f = open( TempOutputFilename, "wb" )
    f.write( io.GetIcsString() )
    f.close()

    # doing comparison
    print "Comparing %s and %s"%(TempOutputFilename, opt.outfile)
    try:
        CmpRes = filecmp.cmp( TempOutputFilename, opt.outfile )
    except OSError as e:
        print "Comparison failed or other system call failed - assuming missing or corrupt current data file."
        CmpRes = False

    if CmpRes:
        print "Files match. No change."
    else:
        print "Files differ - using newest"
        print "Saving latest data in %s"%opt.outfile
        
        print "Diff dump follows"
        os.system( "diff %s %s"%( TempOutputFilename, opt.outfile ))

        shutil.copy2( TempOutputFilename, opt.outfile )                        

        
