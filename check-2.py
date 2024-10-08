import dns.resolver

# List of known educational email service providers
EDUCATIONAL_DOMAINS = [
    "google.com",          # Google Workspace for Education
    "microsoft.com",       # Microsoft 365 Education
    # Add more educational email domains as needed
]

def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for record in mx_records:
            print(f'MX Record: {record.exchange} with priority {record.preference}')
            # Check if the MX record ends with any of the educational domains
            if any(str(record.exchange).endswith(ed_domain) for ed_domain in EDUCATIONAL_DOMAINS):
                return True  # Found a valid educational MX record
        return False  # No valid educational MX record found
    except Exception as e:
        print(f'Error fetching MX records: {e}')
        return False

# Test cases
print(check_mx_record("uff.com"))  # Should return True if valid MX records are found
print(check_mx_record("gmail.com"))  # Should return False
