# -*- coding: UTF-8 -*-

'''
Created on Nov 6, 2010

@author: morten
'''
import csv

class TfCsvImport():
    '''
    Import TF data from csv file 
    '''

    def __init__( self, CsvInputFilename):
        '''
        @param CsvInputFilename The file to retrieve data from.
        '''
        self._InputFile = CsvInputFilename
        self._IsSearchEnabled = False
 
        # needed for parsing 
        # constants
        self._NewClassKeywords = ["ANTAL STUDERENDE:"]
        self._EndClassKeywords = ["I ALT", "I  ALT"]
        self._CsvDelimiter = '\t'

        self._InitSearchParams()
 
    def _InitSearchParams(self):
        ''' inits the variables needed in the search '''
        self._state = 'FILEHEADER'
        self._lineno = 0
        self._classStartLine = 0
        self._classEndLine = 0
        self._CurrentClass = ""
        self._CurrentTeacher = ""
        self._CurrentCourse = ""
        
# --- get/set functions --
    def GetCsvFilename( self ):
        ''' returns the csv file specified for input '''
        return self._InputFile
    
    def IsSearchEnabled(self):
        ''' if true, system is ready to return entries '''
        return self._IsSearchEnabled;
    
# --- other methods ---
    def EnableImportByTeacher( self, TeacherInitials ):
        '''
        Reset the search for lecture based on a specific teacher
        '''
        self._InitSearchParams()
        self._TeacherToSearchFor = TeacherInitials
        self._TfReader = csv.reader(open(self._InputFile), delimiter=self._CsvDelimiter, quotechar='\"')
        self._IsSearchEnabled = True
        
    def GetNextEntry( self ):
        ''' 
        based on the current search method, the next entry found is returned
        returns empty list on eof
        '''
        
        # needs error handling
        for row in self._TfReader:

            self._lineno += 1
            if self._state in ['FILEHEADER',  'NEXTCLASS']:
                if len(row) > 5 :
                    if row[0] in self._NewClassKeywords :
                        self._state = 'CLASSHEADER'
                        self._classStartLine = self._lineno
                    if  row[5] == "LÆRER":
                        self._state = 'CLASSHEADER'
                        self._classStartLine = self._lineno - 1
            
            if self._state == 'CLASSHEADER':
                if self._lineno ==  self._classStartLine+1:
                    self._CurrentClass = row[0]
                if self._lineno - 2 > self._classStartLine :
                    self._state = 'INCLASS'
            
            if self._state == 'INCLASS':
                if row[0] in self._EndClassKeywords :
                    self._state = 'CLASSFOOTER'
                    self._classEndLine = self._lineno
                else: 
                    if len(row) > 5 :
                        self._CurrentTeacher = row[5]
                        self._CurrentCourse = row[0]
            
            if self._state == 'CLASSFOOTER':
                if  self._lineno  > self._classEndLine:
                    self._state = 'NEXTCLASS'

            # if we have a match, return the line        
            if self._state in ['INCLASS']:
                if self._CurrentTeacher == self._TeacherToSearchFor:
                    return {'Teacher': self._CurrentTeacher, 
                            'Class': self._CurrentClass,
                            'Course':   self._CurrentCourse }
