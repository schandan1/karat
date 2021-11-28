from collections import defaultdict

dic = defaultdict(lambda: defaultdict(int))

input = [
 {
      "id": "583fd999a2a3a4121dd6b6fc",
      "name": "Brook Quigley",
      "employmentType": "HOURLY_FT",
      "dob": "1993-04-31",
      "identifiedGender": "FEMALE",
      "title": "Sales Development Rep",
      "compensation": {
        "currency": "USD",
        "annualSalary": 65000.00
      },
      "department": "Sales",
      "workLocation": "San Francisco",
      "startDate": "2020-05-31"
  },
   {
      "id": "583fd999a2a3a4121dd6b6fc",
      "name": "Brook Quigley",
      "employmentType": "HOURLY_FT",
      "dob": "1993-04-31",
      "identifiedGender": "MALE",
      "title": "Sales Development Rep",
      "compensation": {
        "currency": "USD",
        "annualSalary": 55000.00
      },
      "department": "Sales",
      "workLocation": "San Francisco",
      "startDate": "2020-05-31"
  },
  {
    "id": "583fd982a2a3a4121dd6b429",
    "name": "John Grady",
    "employmentType": "HOURLY_FT",
    "dob": "1996-05-31",
    "identifiedGender": "MALE",
    "title": "Customer Support Associate",
    "compensation": {
      "currency": "USD",
      "annualSalary": 52000.00
    },
    "department": "Customer Support",
    "workLocation": "Boston",
    "startDate": "2019-05-31"
  },
    {
    "id": "583fd982a2a3a4121dd6b429",
    "name": "John Grady2",
    "employmentType": "HOURLY_FT",
    "dob": "1996-05-31",
    "identifiedGender": "MALE",
    "title": "Customer Support Associate",
    "compensation": {
      "currency": "USD",
      "annualSalary": 48000.00
    },
    "department": "Customer Support",
    "workLocation": "San Francisco",
    "startDate": "2019-05-31"
  }
]


for item in input:
    print(dic)
    print(dic[item["department"]])
    dic[item["department"]]["sum"]  = item["compensation"]["annualSalary"]
    print(dic[item["department"]])

print(dic)