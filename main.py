import rel

from src.client.baseclient import BaseClient



if __name__ == "__main__":
    bc = BaseClient().get_client()
    bc.run_forever(dispatcher=rel, reconnect=5)
    
    # Keyboard Interrupt
    rel.signal(2, rel.abort)
    rel.dispatch()