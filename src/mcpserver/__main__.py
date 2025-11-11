"""Main entry point for the MCP server."""
from mcpserver.deployment import mcp

def main():
    """Run the MCP server."""
    import asyncio
    asyncio.run(mcp.run())

if __name__ == "__main__":
    main()