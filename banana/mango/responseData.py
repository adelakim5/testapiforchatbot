import json

class responseData:
    def __init__(self, userRequest):
        self.received_json_data = json.loads(userRequest.body.decode("utf-8"))
        
    def getBlockId(self):
        return self.received_json_data['userRequest']['block']['id']
    
    def getBlockName(self):
        return self.received_json_data['userRequest']['block']['name']
    
    def getUtterance(self):
        return self.received_json_data['userRequest']['utterance']
    
    def getContext(self):
        if 'contexts' in self.received_json_data:
            data_length = len(self.received_json_data['contexts'])
            if data_length > 0:
                context_param_name = self.received_json_data['contexts'][0]['name']
                context_value = self.received_json_data['contexts'][0]['params'][context_param_name]['value']
                return context_param_name, context_value
        return None