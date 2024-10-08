from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory      
           
class DefaultCredsGithubIHebski(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                credentials_data = page.split(",")
                
                try: 
                    credential = CredentialsFactory.make({
                        "manufacturer": credentials_data[0],
                        "login": credentials_data[1],
                        "password": credentials_data[2],
                        "source": intel.source                    
                    })
                    
                    credentials.append(credential)
                except:
                    continue
            
        return credentials
        
        