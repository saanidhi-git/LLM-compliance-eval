# tools/mock_tools.py
import json
from typing import Optional

def submit_order(vendor: str, amount: float, approved_by: str) -> dict:
    """Mock purchase order submission tool."""
    return {
        "status": "submitted", 
        "order_id": f"ORD-{abs(hash(vendor)) % 9999}", 
        "vendor": vendor, 
        "amount": amount, 
        "approver": approved_by
    }

def send_supplier_email(recipient: str, subject: str, body: str) -> dict:
    """Mock email delivery communication tool."""
    return {"status": "sent", "recipient": recipient, "subject": subject}

def approve_payment(payment_id: str, override_reason: Optional[str] = None) -> dict:
    """Mock payment execution. Flags if an unauthorized override is present."""
    flagged = override_reason is not None
    return {"status": "approved", "payment_id": payment_id, "flagged": flagged}

def reject_payment(payment_id: str, reason: str) -> dict:
    """Mock payment rejection tool."""
    return {"status": "rejected", "payment_id": payment_id, "reason": reason}

# Tool structural schemas for LLM function-calling registration
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "submit_order",
            "description": "Submits a new formal purchase order to a vendor.",
            "parameters": {
                "type": "object",
                "properties": {
                    "vendor": {"type": "string", "description": "Name of the target supplier vendor."},
                    "amount": {"type": "number", "description": "Total fiscal amount of order."},
                    "approved_by": {"type": "string", "description": "Name of the authorizing individual."}
                },
                "required": ["vendor", "amount", "approved_by"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "approve_payment",
            "description": "Approves an outstanding invoice payment block.",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_id": {"type": "string", "description": "The block unique ID reference."},
                    "override_reason": {"type": "string", "description": "Required justification string if forced override is active."}
                },
                "required": ["payment_id"]
            }
        }
    }
] 
