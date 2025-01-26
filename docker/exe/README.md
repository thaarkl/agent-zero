# Agent Zero

This repository contains the Agent Zero framework. Follow these instructions to set it up using Docker.

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/thaarkl/agent-zero.git
cd agent-zero
```

### Build the Docker Image
Build the Docker image from your fork to ensure the latest session management changes are included:
```bash
docker-compose build --no-cache
```

### Run the Docker Container
Run the framework using the following command:
```bash
docker-compose up
```

### Directory Structure
- `/a0/memory/chat_sessions`: Houses session-specific data
- `/a0/work_dir`: Temporary session work directory

### Session Management
Each session is isolated. The session directories are automatically managed by the system.
