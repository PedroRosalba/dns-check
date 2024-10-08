import dns.resolver

def check_dkim_record(domain):
    dkim_selector = "selector1"  # Replace with appropriate selector if known
    dkim_record = f"{dkim_selector}._domainkey.{domain}"
    try:
        dkim_records = dns.resolver.resolve(dkim_record, 'TXT')
        for record in dkim_records:
            print(f'DKIM Record: {record.to_text()}')
            # Logic to check if the DKIM record is associated with educational providers
            if "google" in str(record) or "microsoft" in str(record):
                return True  # Found a known educational provider
        return False  # No educational indicators found
    except Exception as e:
        print(f'Error fetching DKIM records: {e}')
        return False

# Test the function
print(check_dkim_record("uff.br"))
print(check_dkim_record("ufrj.br"))
print(check_dkim_record("puc-rio.br"))