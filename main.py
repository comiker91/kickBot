import rel

# from src.apicall.getUserInfos import GetUserInfos
from src.client.baseclient import BaseClient



if __name__ == "__main__":
    # userdata = GetUserInfos(username="comiker91")
    # all_data = userdata.get_all_info()
    # print(type(all_data))
    # print(all_data)
    bc = BaseClient().get_client()
    bc.run_forever(dispatcher=rel, reconnect=5)
    # Keyboard Interrupt
    rel.signal(2, rel.abort)
    rel.dispatch()