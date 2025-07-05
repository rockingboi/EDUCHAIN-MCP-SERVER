
# educhain_mcp_server.py

"""
MCP Server using EduChain Library
---------------------------------

This script sets up a Modular Content Protocol (MCP) server that integrates the EduChain
library to generate educational content. The server exposes two endpoints:

1. Tool: Generate MCQs for a given topic
2. Resource: Provide a lesson plan for a given subject

The server can be exposed publicly using ngrok to allow external tools like Claude Desktop
to connect and consume its resources.

Author: Puneet Sharma
"""

import json
from mcp import MCPServer, Tool, Resource
from educhain import generate_mcq, generate_lesson_plan
from pyngrok import ngrok

# ------------------------------------------------------------------------------
# Tool: MCQ Generator
# ------------------------------------------------------------------------------

class MCQTool(Tool):
    """
    Tool to generate multiple-choice questions (MCQs) for a given topic.

    Inherits from:
        mcp.Tool: The base class for MCP tools.

    Methods:
        run(input_text: str) -> str:
            Accepts a topic as input and returns MCQs in JSON format.
    """
    def __init__(self):
        super().__init__(
            name="generate_mcq_tool",
            description="Generates multiple-choice questions for any given topic"
        )

    def run(self, input_text: str) -> str:
        """
        Generate MCQs using the educhain library.

        Args:
            input_text (str): The topic on which to generate questions.

        Returns:
            str: A JSON-formatted string containing MCQs.
        """
        mcqs = generate_mcq(input_text)
        return json.dumps({"topic": input_text, "mcqs": mcqs}, indent=2)


# ------------------------------------------------------------------------------
# Resource: Lesson Plan Generator
# ------------------------------------------------------------------------------

class LessonPlanResource(Resource):
    """
    Resource to generate a structured lesson plan for a given subject.

    Inherits from:
        mcp.Resource: The base class for MCP resources.

    Methods:
        get(input_text: str) -> str:
            Accepts a subject and returns a structured lesson plan in JSON format.
    """
    def __init__(self):
        super().__init__(
            name="generate_lesson_plan_resource",
            description="Returns a detailed lesson plan for a user-specified subject"
        )

    def get(self, input_text: str) -> str:
        """
        Generate a lesson plan using the educhain library.

        Args:
            input_text (str): The subject to generate a lesson plan for.

        Returns:
            str: A JSON-formatted lesson plan.
        """
        plan = generate_lesson_plan(input_text)
        return json.dumps({"subject": input_text, "lesson_plan": plan}, indent=2)


# ------------------------------------------------------------------------------
# MCP Server Setup
# ------------------------------------------------------------------------------

# Create the MCP server with the defined Tool and Resource
server = MCPServer(
    tools=[MCQTool()],
    resources=[LessonPlanResource()]
)

# ------------------------------------------------------------------------------
# Optional: Expose Server via ngrok for public access (e.g., Claude Desktop)
# ------------------------------------------------------------------------------

# Open a tunnel using ngrok on the default MCP port (8000)
public_url = ngrok.connect(8000)
print(f"✅ MCP Server is running at: {public_url}")

# ------------------------------------------------------------------------------
# Run the MCP server
# ------------------------------------------------------------------------------

server.run()  # This will start the server and keep it running
