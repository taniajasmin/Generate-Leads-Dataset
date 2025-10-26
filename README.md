# Generate Leads Dataset

A simple Python project to **generate realistic fake leads** for testing purposes and **validate** the generated data (phone numbers and duplicates).

Perfect for:
- Testing CRM imports
- Demoing lead management systems
- Data pipeline validation
- Mock data for frontend prototypes

---

## Features

| Feature | Description |
|-------|-----------|
| **1000+ Fake Leads** | Full name, phone, email, state, interest |
| **Realistic U.S. Data** | Uses `Faker` with `en_US` locale |
| **Valid Phone Format** | `(XXX) XXX-XXXX` with proper area code rules |
| **Duplicate Removal** | Based on email |
| **Phone Validation** | Regex check for correct format |
| **CSV Output** | Clean, ready-to-use files |

---

## Generated Files

| File | Purpose |
|------|--------|
| `fake_leads.csv` | Raw generated leads (may include invalid phones) |
| `validated_leads.csv` | Cleaned: unique emails + valid phones only |

---

## Requirements

- Python 3.6+
- `pandas`
- `faker`

## Install dependencies:

```bash
pip install pandas faker
```

## Usage
1. Generate Fake Leads
bashpython lead_gen.py

Outputs: fake_leads.csv with 1000 records

2. Validate & Clean Data
bashpython validate.py

Outputs: validated_leads.csv (deduped + valid phones)


## Sample Output (validated_leads.csv)
```csv
- FullName,Phone,State,Interest,Email
- Rachel Long,(595) 997-6033,FL,Kitchen Remodel,james59@example.com
- Emily Smith,(368) 694-5308,NY,Flooring,iriley@example.com
- Jennifer Wade,(673) 758-2005,TX,Windows Replacement,johnconley@example.net
...
```

Customization
Edit lead_gen.py to modify:
```python
num_records = 1000        # Change number of leads
states = ["FL", "TX", ...] # Add/remove states
interests = [...]         # Add new services
```

## Project Structure
```text.
├── lead_gen.py          # Generates fake_leads.csv
├── validate.py          # Cleans & validates → validated_leads.csv
├── fake_leads.csv       # (generated)
├── validated_leads.csv  # (generated, clean)
└── README.md
```

## Use Cases

- Sales CRM Testing
- Email Marketing Demos
- Form Submission Simulations
- Data Quality Pipeline Testing
