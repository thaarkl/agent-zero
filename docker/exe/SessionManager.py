import os
import uuid
import shutil

class SessionManager:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.work_dir = f'/a0/work_dir/{self.session_id}'
        os.makedirs(self.work_dir, exist_ok=True)
        self.memory_dir = f'/a0/memory/chat_sessions/{self.session_id}'
        os.makedirs(self.memory_dir, exist_ok=True)

    def cleanup(self):
        shutil.rmtree(self.work_dir, ignore_errors=True)
        shutil.rmtree(self.memory_dir, ignore_errors=True)
