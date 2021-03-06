#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2010  <morten@minimeee>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from Input.HtmlScraper.SdeSkemaScraper import SdeSkemaScraper
import unittest
import datetime

# testdata
from testpackage.Input.testHtmlScraper.FullWebpageInput import WebPageFromChrome43_43_19lektioner, WebPageFromHtmlGetter43_48_72lektioner, WebPageFromChrome43_48_72lektioner

SimpleSkemaData = """
<div class="time">
<ul>
<li class="sHeader">Wednesday d.2/17/2010</li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">1</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">2 - 09:00 - 09:45</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain"><div class="sizer"><span class="sMainLektion">3 - 10:05 - 10:50</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">4 - 10:55 - 11:40</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="Netvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain" ><div class="sizer"><span class="sMainLektion">5</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">6</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">7</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">8</span> <div class="sMainContent">&nbsp;</div></div></li>
</ul>
</div>
"""
SimpleSkemaDataResult = [
    {'Date': datetime.date(2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 9, 0), datetime.datetime(2010, 2, 17, 9, 45)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP', 'Teacher': u''}, 
    {'Date': datetime.date(2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 10, 5), datetime.datetime(2010, 2, 17, 10, 50)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP', 'Teacher': u''}, 
    {'Date': datetime.date(2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 10, 55), datetime.datetime(2010, 2, 17, 11, 40)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP', 'Teacher': u''}
]

SkemaDataBadChars = """
<div class="time">
<ul>
<li class="sHeader">Wednesday d.2/17/2010</li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">1</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">2 - 09:00 - 09:45</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="æøåæøåNetvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302æøåæøå</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain"><div class="sizer"><span class="sMainLektion">3 - 10:05 - 10:50</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="æøåæøåNetvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2 æøåæøå">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>
<li class="sMain"><div class="sizer"><span class="sMainLektion">4 - 10:55 - 11:40</span><div class="sMainContent"><strong>Fag:</strong> <acronym title="æøåæøåNetvxrk/OOP F2010">Netvxrk/OOP</acronym><br /><strong>Akt:</strong> <acronym title="IT 2. sem Network">10OIT2bH1æøåæøå</acronym><br /><strong>Lok:</strong> <acronym title="A-302 - Teorilokale          ET                   64,40 m2">A-302</acronym> <a href="/lokale/256/en-US.aspx" title="Gx til skema for lokale A-302">>></a><br /></div></div></li>

<li class="sMain" ><div class="sizer"><span class="sMainLektion">5</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">6</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">7</span> <div class="sMainContent">&nbsp;</div></div></li>
<li class="sMain" ><div class="sizer"><span class="sMainLektion">8</span> <div class="sMainContent">&nbsp;</div></div></li>
</ul>
</div>
"""
SkemaDataBadCharsResult =  [
    {'Date': datetime.date( 2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 9, 0), datetime.datetime(2010, 2, 17, 9, 45)], 'Location': u'A-302æøåæøå', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP', 'Teacher': u''}, 
    {'Date': datetime.date( 2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 10, 5), datetime.datetime(2010, 2, 17, 10, 50)], 'Location': u'A-302', 'Class': u'10OIT2bH1', 'Subject': u'Netvxrk/OOP', 'Teacher': u''},
    {'Date': datetime.date( 2010, 2, 17), 'Hours': [datetime.datetime(2010, 2, 17, 10, 55), datetime.datetime(2010, 2, 17, 11, 40)], 'Location': u'A-302', 'Class': u'10OIT2bH1æøåæøå', 'Subject': u'Netvxrk/OOP', 'Teacher': u''},
    ]

class TestInstantiations(unittest.TestCase):                            
    def testEmptyData( self ):
        """ SdeSkemaScraper : use empty text in parser """
        parser = SdeSkemaScraper()
        parser.feed("")
        parser.close()
        self.assertEqual(parser.Appointments , [])                  

    def testBogusTextData( self ):
        """ SdeSkemaScraper : use non-HTML text in parser """
        parser = SdeSkemaScraper()
        parser.feed("ThisHasNothingToDoWithHtml")
        parser.close()
        self.assertEqual(parser.Appointments , [])                  

    def testNonTextData( self ):
        """ SdeSkemaScraper : use integer instead of text in parser """
        parser = SdeSkemaScraper()
        self.assertRaises(TypeError, parser.feed, 1)
        parser.close()
    
    def testKnownText( self ):
        """ SdeSkemaScraper : use known data to get known result """
        parser = SdeSkemaScraper()
        parser.feed( SimpleSkemaData )
        parser.close()
        self.assertEqual(len( parser.Appointments ), len(SimpleSkemaDataResult))
        self.assertEqual(parser.Appointments , SimpleSkemaDataResult)  

    def testKnownTextBadChars( self ):
        """ SdeSkemaScraper : use known data to get known result (including øæå) """
        parser = SdeSkemaScraper()
        parser.feed( SkemaDataBadChars )
        parser.close()
        self.assertEqual(len( parser.Appointments ), len(SkemaDataBadCharsResult))  
        
        for i in range(0, len( parser.Appointments ) ):
            self.assertEqual(parser.Appointments[i] , SkemaDataBadCharsResult[i])  
            
    def testWebPageInput1week_c(self):
        """ SdeSkemaScraper : use webpage source from chrome - 1 week """
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( WebPageFromChrome43_43_19lektioner )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,19)
        pass
    
    def testWebPageInput5weeks_c(self):
        """ SdeSkemaScraper : use webpage source from chrome - 5 weeks """
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( WebPageFromChrome43_48_72lektioner )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,72)
        pass
    
    def testWebPageInput5weeks(self):
        """ SdeSkemaScraper : use webpage source from webgetter - 5 weeks """
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( WebPageFromHtmlGetter43_48_72lektioner )
        parser.close()
        i = len(parser.Appointments)
        self.assertEqual(i,72)
        pass
    
    def testDateAndDateFromHours(self):
        """ SdeSkemaScraper : Compare 'date' with date from 'hours' """
        parser = SdeSkemaScraper(DateFormat = "%d-%m-%Y")
        parser.feed( WebPageFromChrome43_43_19lektioner )
        parser.close()
        for app in parser.Appointments:
            self.assertEqual( app['Hours'][0].date(), app['Date'] )
        pass

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInstantiations)
    unittest.TextTestRunner(verbosity=3).run(suite)

if __name__ == '__main__':
    main()
