from bill import get_bill

# Test valid
assert get_bill("P001") == {"name": "Alice", "amount": 700}

print("Test passed.")