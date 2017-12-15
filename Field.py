# Field.py

from FieldChange import FieldChange
from Notification import *

class Field:
    
    def __init__(self,parent, name="", value=""):
        self.parent = parent
        self.__name = name
        self.__current_value = value
        self.__old_value = ""
        self.notificationHandlers = []
        
    def value(self):
        return self.__current_value
    
    def name(self):
        return self.__name
    
    def setValue(self,value):
        if self.__current_value != value:
            self.currentToOld
            self.__current_value = value
            self.notify(Notification(self.parent.owner.getNotificationCategory(), Notification.NotificationType.FIELD, self.parent.owner, [self.getFieldChanged()]))                     
            
            
    def currentToOld(self):
        self.__old_value = self.__current_value
        
    def getFieldChanged(self):
        
        if self.__old_value != self.__current_value:
            fc = FieldChange(self,self.__old_value,self.__current_value)
            return fc
        else:
#            print("Field NOT changed   Old: " + self.__old_value + "\t New: " + self.__current_value) 
            return None
        
    def addNotificationHandler(self,handler):
        self.notificationHandlers.append(handler)
        
    def notify(self, notification):
        for h in self.notificationHandlers:
            if not notification.consumed: 
                h(notification)

        