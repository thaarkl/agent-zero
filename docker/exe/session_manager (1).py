import os
import uuid
import shutil
from datetime import datetime

class AtomicSession:
    def __init__(self):
        self.session_id = f"{datetime.utcnow().isoformat()}Z_{uuid.uuid4().hex}"
        self.active_path = f"/root/memvault/{self.session_id}/active"
        self.archive_path = f"/root/memvault/{self.session_id}/archive"
        os.makedirs(self.active_path, exist_ok=True)
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(f"/root/memvault/{self.session_id}", ignore_errors=True)
        
    def new_context(self):
        context_id = uuid.uuid4().hex
        os.makedirs(f"{self.active_path}/{context_id}", exist_ok=True)
        return f"{self.active_path}/{context_id}"
