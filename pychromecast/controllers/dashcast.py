from . import BaseController

class DashCastController(BaseController):
    def __init__(self):
        super(DashCastController, self).__init__(
            "urn:x-cast:com.dashcast.wt.msg", "DCCDFF7E")
        self.namespace = "urn:x-cast:com.dashcast.wt.msg"

    def receive_message(self, message, data):
        print("Wow, I received this message: {}".format(data))

        return True  # indicate you handled this message

    def request_dash(self, url):
        self.send_message({'request': url})