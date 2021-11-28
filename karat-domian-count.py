from collections import defaultdict
counts = [ "900,google.com",
     "60,mail.yahoo.com",
     "10,mobile.sports.yahoo.com",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "10,stackoverflow.com",
     "20,overflow.com",
     "5,com.com",
     "2,en.wikipedia.org",
     "1,m.wikipedia.org",
     "1,mobile.sports",
     "1,google.co.uk"]

def domain_count():
    d = defaultdict(int)
    for cpdomain in counts:
        cnt, domain = cpdomain.split(',')
        d[domain] += int(cnt)
        while '.' in domain:
            part, domain = domain.split('.', 1)
            d[domain] += int(cnt)
    return [f"{value} {key}" for key, value in d.items()]

print(domain_count())








