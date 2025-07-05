## 🎓 EduChain-Powered MCP Server ##

This project implements a **Modular Content Protocol (MCP) server** that leverages the [EduChain library](https://github.com/satvik314/educhain) to generate educational content (e.g., MCQs and lesson plans). The server is designed to work with **Claude Desktop**, enabling dynamic, AI-powered learning tool integration.

## 🚀 Features

- 🛠 **MCP Server** with EduChain integration  
- 🧠 **Tool:** MCQ Generator for custom topics  
- 📚 **Resource:** Lesson Plan Creator  
- 🔗 Claude Desktop compatibility for AI interaction  
- 🌐 Ngrok integration for public server access (Colab-friendly)  
- 🎁 Bonus-ready: Add Flashcard Generator if desired

- ## 📁 Project Structure

# bash
├── educhain_server.ipynb          # Main notebook with EduChain + MCP code

├── mcp_server.py                  # standalone server script

├── claude_desktop_config.json     # Configuration for Claude Desktop

├── Sample_Responses.xlsx           # Sample commands and server outputs

├── README.md                      # Project overview and instructions

# Sample Commands (for Claude Desktop)
1. Generate 5 multiple-choice questions on Python loops.
2.Provide a lesson plan for teaching algebra.

## ⚙️ Installation & Usage
Run on Google Colab

Install dependencies

Run MCP server

Expose with ngrok

Connect with Claude Desktop

Update claude_desktop_config.json with your ngrok URL

Test commands in Claude Desktop and observe results


## Requirements
mcp
educhain
pyngrok

Install with:
pip install mcp educhain pyngrok
