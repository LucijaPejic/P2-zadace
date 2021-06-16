import re
email = input("Unesite e-mail: ")
eduid = input("Unesite eduid: ")
regex_email = "[a-z]+\.[a-z]+@fpmoz\.sum\.ba"
regex_eduid = "[a-z]\d?@sum\.ba" #[a-z]{2,}\d*@sum\.ba
result_email = re.findall(regex_email, email)
result_eduid = re.findall(regex_eduid, eduid)
if result_email and result_eduid:
    print("Podudara se")
else:
    print("Nema podudaranja")
