# -*- coding: utf-8 -*-
'''
Created on Nov 7, 2010

@author: morten
'''
import unittest
from Output.TableOutput.TableOutput import TableOutput

# test data
IterableObject = [{'Lessons by week': {40: 6, 41: 8, 43: 10, 39: 4}, 'Course': 'Subject H1', 'Teacher': 'Teacher 7', 'Class': '1. Sem A Elektronik'},
                        {'Lessons by week': {1: 4, 2: 4, 3: 4, 44: 4, 45: 4, 46: 4, 47: 4, 48: 4, 49: 4, 50: 4}, 'Course': 'Subject L1', 'Teacher': 'Teacher 7', 'Class': '1. Sem A Elektronik'},
                ]
ObjectAsTextile = '''|. Class|. Teacher|. Course|38|39|40|41|42|43|44|45|46|47|48|49|50|51|
|. 1. Sem A Elektronik|. Teacher 7|. Subject H1||4|6|8||10|||||||||
|. 1. Sem A Elektronik|. Teacher 7|. Subject L1|||||||4|4|4|4|4|4|4||
'''
ObjectAsHtml = '\t<table>\n\t\t<tr>\n\t\t\t<td>Class</td>\n\t\t\t<td>Teacher</td>\n\t\t\t<td>Course</td>\n\t\t\t<td>38</td>\n\t\t\t<td>39</td>\n\t\t\t<td>40</td>\n\t\t\t<td>41</td>\n\t\t\t<td>42</td>\n\t\t\t<td>43</td>\n\t\t\t<td>44</td>\n\t\t\t<td>45</td>\n\t\t\t<td>46</td>\n\t\t\t<td>47</td>\n\t\t\t<td>48</td>\n\t\t\t<td>49</td>\n\t\t\t<td>50</td>\n\t\t\t<td>51</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>1. Sem A Elektronik</td>\n\t\t\t<td>Teacher 7</td>\n\t\t\t<td>Subject H1</td>\n\t\t\t<td></td>\n\t\t\t<td>4</td>\n\t\t\t<td>6</td>\n\t\t\t<td>8</td>\n\t\t\t<td></td>\n\t\t\t<td>10</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>1. Sem A Elektronik</td>\n\t\t\t<td>Teacher 7</td>\n\t\t\t<td>Subject L1</td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td></td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td>4</td>\n\t\t\t<td></td>\n\t\t</tr>\n\t</table>'

class Test(unittest.TestCase):
    def testConstruction(self):
        ''' TableOutput : constructs the TableOutput class '''
        TO = TableOutput( IterableObject )
        pass

    def testGetTextile(self):
        ''' TableOutput : test building the textile table '''
        TO = TableOutput( IterableObject )
        self.assertEqual( TO.GetTextileTable(), ObjectAsTextile )

    def testGetHtml(self):
        ''' TableOutput : test the output converted to HTML '''
        TO = TableOutput( IterableObject )
        HTML = TO.GetHtmlTable()
        self.assertEqual( HTML, ObjectAsHtml )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()