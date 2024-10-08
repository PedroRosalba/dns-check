import dns.resolver

EDUCATIONAL_DOMAINS = [
    "uff.br",
    "ufrj.br",
    "puc-rio.br",
]

def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for record in mx_records:
            print(f'MX Record: {record.exchange} with priority {record.preference}')
            if domain in EDUCATIONAL_DOMAINS or any(keyword in str(record.exchange) for keyword in EDUCATIONAL_DOMAINS):
                return True  
        return False  
    except Exception as e:
        print(f'Error fetching MX records: {e}')
        return False

print(check_mx_record("uff.br"))        
print(check_mx_record("ufrj.com"))      
print(check_mx_record("ufrj.br"))       
print(check_mx_record("impatech.org.br"))  
print(check_mx_record("puc-rio.br"))    
print(check_mx_record("gmail.com"))     
print(check_mx_record("outlook.com"))   
