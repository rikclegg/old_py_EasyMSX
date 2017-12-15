'''
Created on 22 May 2017

@author: rclegg2
'''
from EasyMSX import EasyMSX

class MyApp:
    
    def __init__(self):

        print("Loading EasyMSX...")
        self.easyMSX = EasyMSX()
    
        print("EasyMSX loaded....")
    
        print("\nTeams:")
    
        '''
        for t in self.easyMSX.teams:
            print(t.name)
        
            print("\nBrokers: ")
    
        for b in self.easyMSX.brokers:
            print("Broker: " + b.name + "\tAsset Class: " + b.assetClass)
            for s in b.strategies:
                print("\tStrategy: " + s.name)
                for p in s.parameters:
                    print("\t\tParameter: " + p.name)
    
        '''
        
        self.easyMSX.orders.addNotificationHandler(self.processNotification)
        self.easyMSX.routes.addNotificationHandler(self.processNotification)

        self.easyMSX.start()
             
        while True:
            pass
        

    def printOrderBlotter(self):
        print("\nOrder Blotter: \n")
        for o in self.easyMSX.orders:
            print("Side: " + o.field("EMSX_SIDE").value() + "\tSequence No.: " + o.field("EMSX_SEQUENCE").value() + "\tStatus: " + o.field("EMSX_STATUS").value() + " \tTicker: " + o.field("EMSX_TICKER").value() + "\tAmount: " + o.field("EMSX_AMOUNT").value() + "\tTIF: " + o.field("EMSX_TIF").value())
                        
    def printRouteBlotter(self):
        print("\nRoute Blotter: \n")
        for r in self.easyMSX.routes:
            print("Sequence No.: " + r.field("EMSX_SEQUENCE").value() + "\tRoute ID: " + r.field("EMSX_ROUTE_ID").value() + "\tStatus: " + r.field("EMSX_STATUS").value() + "  \tWorking: " + r.field("EMSX_WORKING").value() + "\tFilled: " + r.field("EMSX_FILLED").value() + "\tAverage Price: " + r.field("EMSX_AVG_PRICE").value())

    
    def processNotification(self,notification):
        if notification.category == EasyMSX.NotificationCategory.ORDER:
            print("\nChange to Order (" + EasyMSX.NotificationType.asText(notification.type) + "): " + notification.source.field("EMSX_SEQUENCE").value())
            #self.printFieldChanges(notification.fieldChanges)
            #self.printOrderBlotter()

        elif notification.category == EasyMSX.NotificationCategory.ROUTE:
            print("\nChange to Route (" + EasyMSX.NotificationType.asText(notification.type) + "): " + notification.source.field("EMSX_SEQUENCE").value() + "/" + notification.source.field("EMSX_ROUTE_ID").value())
            #self.printFieldChanges(notification.fieldChanges)
            #self.printRouteBlotter()
            
        notification.consume=True

    def printFieldChanges(self,fieldChanges):
        for fc in fieldChanges:
            print("Field: " + fc.field.name() + "\tOld: " + fc.oldValue + "\tNew: " + fc.newValue)
             
        
if __name__ == '__main__':
    
    myApp = MyApp();
    
