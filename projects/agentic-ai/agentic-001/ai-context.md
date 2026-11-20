# AI Context — MCP Support Desk: Basic Model Context Protocol Demo

## Project Identity

- Project ID: `agentic-001`
- Title: MCP Support Desk — Basic Model Context Protocol Demo
- Domain: Agentic AI
- Project Type: `agentic_ai`
- Difficulty: beginner
- Status: completed
- GitHub: https://github.com/atanuduttagupta/ai-daily-practice/tree/main/AI/mcp-simple-demo
- Live Streamlit demo: https://ai-daily-practice-mcp-simple-demo.streamlit.app/

## Purpose

This project demonstrates the fundamentals of the Model Context Protocol (MCP) through a small support-desk case study.

A human or AI support agent commonly needs to look up an order, check whether it can be refunded, or open a support ticket. The project exposes these operations through an MCP server so an MCP-capable client can discover and invoke them using a standard protocol rather than custom integration code for each application.

The project uses the official Python MCP SDK version 2:
- `MCPServer` to implement the server
- `Client` to implement the client
- `StdioServerParameters` to launch and connect to the server process

The project does not require an API key or an LLM. It demonstrates MCP protocol communication and tool use directly.

## What the Application Does

The repository contains two main Python files:

- `main.py`: implements the MCP server and a command-line MCP client demo.
- `app.py`: implements a Streamlit host application that acts as an MCP client.

The Streamlit application allows a user to:
1. Discover the MCP server's tools, resources, and prompts.
2. Check an order's delivery status.
3. Check refund eligibility.
4. Create a support ticket after explicit user confirmation.
5. Read the refund policy from an MCP resource.

## Architecture

```text
User
  |
  v
Streamlit UI (app.py)
  |
  v
MCP Host Application
  |
  v
MCP Client (Client)
  |
  | stdio transport / JSON-RPC communication
  v
MCP Server subprocess (main.py serve)
  |
  +-- Tools
  |    +-- get_order_status
  |    +-- check_refund_eligibility
  |    +-- create_support_ticket
  |
  +-- Resource
  |    +-- policy://refunds
  |
  +-- Prompt
       +-- support_reply
```

The Streamlit host launches the server as a separate subprocess using the current Python interpreter and the path to `main.py`. The client communicates with that server over standard input/output (stdio).

The Streamlit application uses MCP client operations such as:
- `list_tools()`
- `list_resources()`
- `list_prompts()`
- `call_tool()`
- `read_resource()`

The server functions are registered using MCP SDK decorators. The client discovers their names, descriptions, and input schemas through the protocol; it does not receive or directly call the Python function bodies.

## MCP Server Capabilities

### Tools

| Tool | Purpose | Changes state? |
|---|---|---|
| `get_order_status` | Look up an order's item and delivery status | No |
| `check_refund_eligibility` | Check the order against the refund rules | No |
| `create_support_ticket` | Create a support ticket for an order | Yes |

The tool arguments are typed. The SDK uses function type hints and docstrings to describe the tools and their input schemas to MCP clients.

### Resource

- URI: `policy://refunds`
- Function: `refund_policy()`
- Purpose: expose the refund policy as read-only context.

The policy states:
- Items can be returned within 30 days of delivery.
- Final-sale items, such as gift cards, cannot be refunded.
- Orders that have not been delivered cannot yet be refunded.

### Prompt

- Name: `support_reply`
- Argument: `order_id`
- Purpose: provide a reusable instruction for drafting a short, polite customer reply using facts returned by the tools.

The Streamlit discovery panel lists this prompt. The current UI does not include a prompt-invocation interface.

## Demo Data and Business Rules

The server uses a small in-memory order dictionary and an in-memory ticket list. It is a learning example, not a persistent production database.

| Order | Item | Status | Delivery date | Final sale |
|---|---|---|---|---|
| A100 | Wireless headphones | Delivered | 2026-11-05 | No |
| A101 | Gift card | Delivered | 2026-11-10 | Yes |
| A102 | Laptop stand | Shipped | Not delivered | No |
| A103 | USB-C cable | Delivered | 2026-09-01 | No |

The demo fixes its reference date at 20 November 2026 so the sample refund calculations are repeatable.

Expected examples:
- A100: refund eligible; delivered 15 days before the fixed reference date.
- A101: not eligible; final-sale item.
- A102: not eligible yet; not delivered.
- A103: not eligible; delivered 80 days before the fixed reference date.
- An unknown order such as Z999: the server returns a clear tool error.

The support-ticket tool validates that the order exists and creates an identifier such as `T001`. Ticket data is held only in process memory.

## Streamlit Host Application

The Streamlit UI is organized into:
- MCP Server Discovery
- Order Status
- Refund Eligibility
- Create Ticket
- Refund Policy

Before creating a ticket, the UI requires the user to check a confirmation box. This illustrates a human-in-the-loop safeguard for a tool that changes state.

Each UI operation starts an MCP server subprocess, creates an MCP client connection, performs the requested operation, and closes the connection. As a result, in-memory ticket state is not persistent across separate client/server requests.

Hosted demo:
https://ai-daily-practice-mcp-simple-demo.streamlit.app/

## Technologies

- Python
- Official MCP Python SDK v2 (`mcp>=2.3,<3`)
- Streamlit
- Python asyncio
- stdio subprocess transport

The dependencies are listed in `requirements.txt`.

## Key Concepts Demonstrated

- Model Context Protocol
- MCP host, client, and server roles
- JSON-RPC 2.0 communication
- MCP lifecycle: initialize, discover, and use
- Tool registration and tool discovery
- Typed tool arguments and generated input schemas
- Tool invocation and error responses
- MCP resources for read-only context
- MCP prompts as reusable templates
- stdio transport
- Subprocess-based local server connection
- Human confirmation before state-changing tool calls
- Separation between a host UI and server-side tool implementation

## What This Project Does Not Implement

The project is a basic MCP demonstration. It does not currently implement:
- An LLM deciding autonomously which tool to call
- An agent loop or autonomous agent
- Tool selection through model reasoning
- RAG, embeddings, or vector databases
- A persistent database for orders or tickets
- Streamable HTTP transport
- Remote-server authentication
- Multi-server orchestration
- Multi-agent communication
- An MCP prompt invocation screen in Streamlit
- Production-grade observability or deployment security controls

The presence of MCP tools does not, by itself, mean that an LLM agent is implemented. The current Streamlit app is an interactive MCP host/client demo, not an autonomous AI agent.

## Security and Design Notes

- Treat tool outputs as untrusted data because external content can contain prompt-injection instructions.
- Follow least-privilege principles when connecting servers to real systems.
- Only connect to trusted MCP servers.
- Authenticate remote MCP servers when using network transports.
- Require explicit human confirmation for mutating operations such as creating a ticket.
- Return clear, expected errors using the SDK's `ToolError` rather than allowing routine invalid input to crash the server.

## Suggested Follow-up Work

These are possible extensions, not current capabilities:
1. Add a `list_orders_for_customer` tool.
2. Replace the in-memory order and ticket data with SQLite.
3. Add Streamable HTTP transport and appropriate authentication.
4. Connect a local Ollama model and implement a tool-selection/agent loop.
5. Add more input-validation examples and inspect how errors are returned.
6. Add a Streamlit interface for invoking the `support_reply` prompt.

## AI Project Atlas Retrieval Context

Useful search terms:
- MCP
- Model Context Protocol
- Agentic AI
- MCP server
- MCP client
- MCP host
- Python MCP SDK v2
- MCP tools
- MCP resources
- MCP prompts
- tool discovery
- tool invocation
- stdio transport
- JSON-RPC 2.0
- human-in-the-loop
- Streamlit MCP client
- subprocess server
- support desk automation

## Project Learning Outcome

The central lesson is that MCP standardizes how an application discovers and communicates with tools and data exposed by a server. A tool can be implemented once on an MCP server and then discovered by different MCP-capable clients without each client needing a bespoke integration for that tool.

The model only receives the tool descriptions and schemas through the MCP client/host workflow; this project itself does not include an LLM that reasons over or autonomously calls the tools.
