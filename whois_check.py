import whois
from datetime import datetime

def get_domain_info(domain):
    try:
        domain_info = whois.query(domain)
        
        if isinstance(domain_info.creation_date, list):
            creation_date = domain_info.creation_date[0]  
        else:
            creation_date = domain_info.creation_date

        if isinstance(creation_date, str) and "before" in creation_date:
            formatted_date = "Date before standard format"
        else:
            formatted_date = creation_date.strftime("%Y-%m-%d") if isinstance(creation_date, datetime) else str(creation_date)

        return {
            'domain': domain_info.domain,
            'owner': domain_info.owner,
            'emails': domain_info.emails,
            'creation_date': formatted_date
        }
    except Exception as e:
        print(f'Error fetching WHOIS information: {e}')
        return None

if __name__ == "__main__":
    domain = "puc-rio.br"
    info = get_domain_info(domain)

    if info:
        print(f"Domain: {info['domain']}")
        print(f"Owner: {info['owner']}")
        print(f"Email: {info['emails']}")
        print(f"Created: {info['creation_date']}")
    else:
        print("Could not retrieve domain information.")
