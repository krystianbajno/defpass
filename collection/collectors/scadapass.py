from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class ScadaPass(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/scadastrangelove/SCADAPASS/master/scadapass.csv"
        label = "SCADA_PASS"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # Vendor,Device,Default password,Port,Device type,Protocol,Source
        pages = res.text.split("\n")[6:]
        
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels