from plugs.manager import PlugManager
from plugs.plug import Plug

care_diet = Plug(
    name="care_diet",
    package_name="/app/care_diet",
    version="",
    configs={},
)

plugs = [care_diet]

manager = PlugManager(plugs)
