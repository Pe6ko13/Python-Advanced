class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_name(email):
    username = email.split('@')[0]
    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(email, valid_dom):
    domain = email.split('.')[-1]
    if domain not in valid_dom:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


while True:
    email = input()
    valid_domains = ('com', 'net', 'bg', 'org')

    if email == 'End':
        break

    validate_name(email)
    validate_at_symbol(email)
    validate_domain(email, valid_domains)

    print("Email is valid")