FROM frdel/agent-zero-run:base

RUN git clone https://github.com/thaarkl/agent-zero.git /a0 
RUN mkdir -p /a0/memory/chat_sessions /a0/work_dir

