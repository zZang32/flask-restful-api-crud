from resources.CheckStatus.CheckStatus import CheckStatus
from resources.CRUD.NewEvent.NewEvent import NewEvent
from resources.CRUD.GetEvents.GetEvents import GetEvents
from resources.CRUD.GetEventPerId.GetEventPerId import GetEventPerId
from resources.CRUD.DeleteEvent.DeleteEvent import DeleteEvent
from resources.CRUD.UpdateEvent.UpdateEvent import UpdateEvent


class Routes():
    
    def __init__(self, Api) -> object:
        
        self.api = Api
        self.route = '/api'
        
    def __get(self):
        self.api.add_resource(CheckStatus, self.route+'/check-status')
        self.api.add_resource(GetEvents, self.route+'/events')
        self.api.add_resource(GetEventPerId, self.route+'/event/<string:id>')
    
    def __post(self):
        self.api.add_resource(NewEvent, self.route+'/post-new-event')
    
    def __delete(self):
        self.api.add_resource(DeleteEvent, self.route+'/delete-event')
    
    def __put(self):
        self.api.add_resource(UpdateEvent, self.route+'/update-events')
    
    