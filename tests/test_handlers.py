from handlers.sharepoint_handler import SharePointHandler
from handlers.servicenow_handler import ServiceNowHandler
from handlers.barnum_handler import BarnumHandler
from handlers.confluence_handler import ConfluenceHandler


print(SharePointHandler().search("pto"))

print(ServiceNowHandler().search("vpn"))

print(BarnumHandler().search("vpn"))

print(ConfluenceHandler().search("vpn"))