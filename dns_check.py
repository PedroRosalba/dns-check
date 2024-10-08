import dns.resolver

def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for record in mx_records:
            print(f'MX Record: {record.exchange} with priority {record.preference}')
            # You can add logic to check against known educational providers here
        return True  # If you find a valid educational MX record
    except Exception as e:
        print(f'Error fetching MX records: {e}')
        return False

print(check_mx_record("uff.com"))
print(check_mx_record("gmail.com")) 
