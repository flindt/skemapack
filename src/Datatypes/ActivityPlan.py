#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on May 19, 2011

@author: flindt
'''

class ActivityPlan(object):
    '''
    Data container for course planning
    '''


    def __init__(self, ActData, TeacherFullName, PlanRelPath, PlanFileName, PlanLastUpdate, PlansRootFolder):
        '''
        Constructor
        '''
        self._ActData = ActData
        self._TeacherFullName = TeacherFullName
        self._PlanRelPath = PlanRelPath
        self._PlanFileName = PlanFileName
        self._PlanLastUpdate = PlanLastUpdate
        self._PlansRootFolder = PlansRootFolder
        
    def __eq__(self, OtherAP ):
        ''' Equal operator. '''
        if( self._ActData != OtherAP.getActData() ): return False
        if( self._TeacherFullName != OtherAP.getTeacherFullName() ): return False
        if( self._PlanRelPath != OtherAP.getPlanRelPath() ): return False
        if( self._PlanFileName != OtherAP.getPlanFileName() ): return False
        if( self._PlanLastUpdate != OtherAP.getPlanLastUpdate() ): return False
        if( self._PlansRootFolder != OtherAP.getPlansRootFolder() ): return False
        return True
         
    def __ne__(self, OtherAP):
        return not self.__eq__(OtherAP)
    
    def getActData(self):
        return self._ActData
    
    def getTeacherFullName(self):
        return self._TeacherFullName
    
    def getPlanRelPath(self):
        return self._PlanRelPath
    
    def getPlanFileName(self):
        return self._PlanFileName
    
    def getPlanLastUpdate(self):
        return self._PlanLastUpdate
    
    def getPlansRootFolder(self):
        return self._PlansRootFolder
    
    