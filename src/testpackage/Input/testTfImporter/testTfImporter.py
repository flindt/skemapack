# -*- coding: UTF-8 -*-
'''
Testing basic tf import
@author: mon
'''
import unittest
from Input.TfImporter.TfCsvImport import TfCsvImport

# Test data
TfInputCsvFile = "testdata/TF_skema.csv"
TfInputCsvDefaultMetaData = {'Weeknumbers by column': {}, 'Csv cell delimiter': '\t'}
TfInputCsvWeekNoByColumns = {1: 38, 2: 39, 3: 40, 4: 41, 5: 42, 6: 43, 27: 12, 28: 13, 29: 14, 30: 15, 31: 16, 32: 17, 33: 18, 34: 19, 35: 20, 36: 21, 37: 22, 38: 23, 39: 24, 40: 25, 41: 26, 42: 27, 43: 28, 44: 29, 45: 30, 46: 31, 47: 32, 48: 33, 49: 34, 50: 35, 51: 36, 52: 37}
TfInputCsvMetaData = dict( TfInputCsvDefaultMetaData.items()
                           + {'Weeknumbers by column': TfInputCsvWeekNoByColumns}.items()  )

Teacher1Initials = 'Teacher 7'
Teacher1Classes = [     {'Course': 'Subject H1', 'Teacher': 'Teacher 7', 'Class': '1. Sem A Elektronik'},
                        {'Course': 'Subject L1', 'Teacher': 'Teacher 7', 'Class': '1. Sem A Elektronik'},
                        {'Course': 'Subject O1', 'Teacher': 'Teacher 7', 'Class': '1. Sem A Elektronik'},
                        {'Course': 'Subject D1', 'Teacher': 'Teacher 7', 'Class': '1. Sem B Netv\xc3\xa6rk'},
                        {'Course': 'Subject G1', 'Teacher': 'Teacher 7', 'Class': '1. Sem B Netv\xc3\xa6rk'},
                        {'Course': 'Subject H1', 'Teacher': 'Teacher 7', 'Class': '1. Sem B Netv\xc3\xa6rk'},
                        {'Course': 'Subject T1', 'Teacher': 'Teacher 7', 'Class': '1. Sem B Netv\xc3\xa6rk'}
                    ]
Teacher1FirstClass = Teacher1Classes[0]
Teacher2Initials = 'Teacher2'
Teacher2FirstClass = {'Course': 'Subject B1', 'Teacher': 'Teacher2', 'Class': '1. Sem A Elektronik'}

class Test(unittest.TestCase):

    def testConstruction(self):
        ''' test construction of TfCsvImport '''
        tfi = TfCsvImport(TfInputCsvFile )
        self.assertEqual( tfi.GetCsvFilename(), TfInputCsvFile )

    def testEnableSearchByTeacher(self):
        ''' test selecting teacher based search '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)
        self.assertEqual( tfi.IsSearchEnabled(), True )

    def testGetNextEntry(self):
        ''' test the retrieval of the first entry (Teacher1) '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.GetNextEntry(), Teacher1FirstClass )

    def testGetNextEntryWithDiffTeacher(self):
        ''' test the retrieval of the first entry (teacher2)'''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher2Initials)        
        self.assertEqual( tfi.GetNextEntry(), Teacher2FirstClass )

    def testRestartSearch(self):
        ''' test restarting search with new teacher '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        self.assertEqual( tfi.GetNextEntry(), Teacher1FirstClass )
        tfi.EnableImportByTeacher(Teacher2Initials)        
        self.assertEqual( tfi.GetNextEntry(), Teacher2FirstClass )

    def testGetNextEntryMultipleTimes(self):
        ''' test the retrieval of the mulitple entries '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
            
        for i in range(0, len(Teacher1Classes )):
            self.assertEqual( tfi.GetNextEntry(), Teacher1Classes[i] )
            
    def testGetDefaultMetadata(self):
        ''' test we have some base metadata '''
        tfi = TfCsvImport(TfInputCsvFile )
        self.assertEqual(tfi.GetMetaData(), TfInputCsvDefaultMetaData)

    def testGetMetadataAfterFirstEntry(self):
        ''' test that the metadata gets populated during retrieval of entries '''
        tfi = TfCsvImport(TfInputCsvFile )
        tfi.EnableImportByTeacher(Teacher1Initials)        
        tfi.GetNextEntry()
        self.assertEqual(tfi.GetMetaData(), TfInputCsvMetaData)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintWebPage']
    unittest.main()