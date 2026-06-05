# n8n Error Handling Architecture

All enterprise workflows MUST implement a standardized Error Trigger node routing to a central webhook.

## Required JSON Payload for Error Webhook:
```json
{
  "workflow_id": "{{$workflow.id}}",
  "workflow_name": "{{$workflow.name}}",
  "error_message": "{{$error.message}}",
  "node_name": "{{$error.node.name}}",
  "execution_url": "{{$execution.url}}",
  "timestamp": "{{$now}}"
}
