import os
import uuid

class PureSession:
    def __init__(self):
        self.session_id = uuid.uuid4().hex
        self.session_path = f"/root/memfix/{self.session_id}"
        os.makedirs(self.session_path, exist_ok=True)

    def purge(self):
        if os.path.exists(self.session_path):
            for root, dirs, files in os.walk(self.session_path):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
