class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


VALID_DOMAINS = ('com', 'org', 'net', 'bg')
email = input()

while email != 'End':

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")

    elif len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')
    email = input()

