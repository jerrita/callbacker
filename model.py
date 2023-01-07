global_token = 'default_token'

class BasePlugin:
    token: str
    
    def __init__(self, api_token = None) -> None:
        self.token = api_token
        
    def run(self, param) -> str:
        pass
        
    def execute(self, param) -> str:
        if param is None:
            return 'Illegal request'
        if 'token' not in param or param['token'] != self.token:
            return 'Invalid token'
        return self.run(param)
        
    