import dns.resolver

def check_txt_record(domain):
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for record in txt_records:
            print(f'TXT Record: {record.to_text()}')
            # You can add logic to check for specific educational keywords here
            if "university" in str(record) or "education" in str(record):
                return True  
        return False  
    except Exception as e:
        print(f'Error fetching TXT records: {e}')
        return False

# Test the function
print(check_txt_record("uff.br"))
print(check_txt_record("ufrj.br"))
print(check_txt_record("puc-rio.br"))