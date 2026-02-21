from django.core.exceptions import ValidationError

def agent_validate_email_domain(value):
    allowed_domains = ['spotlight.com', 'unitedtalent.com']
    if not any(value.endswith(domain) for domain in allowed_domains):
        raise ValidationError(f"Email address is not valid. It must be one of the following: {', '.join(allowed_domains)}")


