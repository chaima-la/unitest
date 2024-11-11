import unittest
import re

# exo1
def onlyAlphabet2(text):
    return bool(re.match('^[a-zA-Z]+$', text))

# exo2
def findDegits(text):
    return re.findall(r"\d+", text)

# exo3
def validEmail(emailList):
    valid_emails = []
    for txt in emailList.split():
        isValid = re.search(r".@.+\.[a-zA-Z]{2,3}", txt)
        if isValid:
            valid_emails.append(txt)
    return valid_emails

# exo4
def validate(txt):
    pattern = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$"
    if re.match(pattern, txt):
        month, day, year = map(int, txt.split('-'))
        if (month in {4, 6, 9, 11} and day > 30):
            return False
        if (month == 2):
            if (year % 4 != 0 and day > 28) or (year % 4 == 0 and day > 29):
                return False
        return True
    else:
        return False

# exo5
def passwordValid(txt):
    if len(txt) < 8:
        return False
    if not re.search(r"[a-z]", txt) or not re.search(r"[A-Z]", txt):
        return False

    if not re.search(r"[0-9]", txt):
        return False
    if not re.search(r"[!@#$%^&*]", txt):
        return False
    return True

# exo6
def hashtags(txt):
    return re.findall(r"#\w+", txt)





class Tests(unittest.TestCase):    

    #tst1
    def test_onlyAlphabet2(self):
        self.assertTrue(onlyAlphabet2("Hello"))
        self.assertFalse(onlyAlphabet2("Hello123"))
        self.assertFalse(onlyAlphabet2("123"))
        self.assertFalse(onlyAlphabet2("!@#"))

    #tst2
    def test_findDegits(self):
        self.assertEqual(findDegits("The year is 2024 and the month is 09"), ["2024", "09"])
        self.assertEqual(findDegits("No digits here!"), [])
        self.assertEqual(findDegits("I have 2 dogs and 3 cats."), ["2", "3"])
        self.assertEqual(findDegits("1234567890"), ["1234567890"])

    #tst3
    def test_validEmail(self):
        self.assertEqual(validEmail("test@domain.com validemail@domain.org @invalid.com"), ["test@domain.com", "validemail@domain.org"])
        self.assertEqual(validEmail("invalidemail.com"), [])
        self.assertEqual(validEmail("lkc@sdjddj.com @sdjddj.com skjdfhk kjqd@gmail.com"), ["lkc@sdjddj.com", "kjqd@gmail.com"])
        self.assertEqual(validEmail("noemailhere"), [])

    #tst4
    def test_validate(self):
        self.assertTrue(validate("02-27-2000"))
        self.assertTrue(validate("02-29-2000"))
        self.assertFalse(validate("02-29-2001"))
        self.assertFalse(validate("04-31-2021"))
        self.assertFalse(validate("13-01-2021"))
        self.assertFalse(validate("12-32-2021"))
        self.assertTrue(validate("12-25-2020"))

    #tst5
    def test_passwordValid(self):
        self.assertTrue(passwordValid("Valid123!"))
        self.assertFalse(passwordValid("short1"))
        self.assertFalse(passwordValid("missinguppercase123!"))
        self.assertFalse(passwordValid("MissingSymbol123"))
        self.assertFalse(passwordValid("NoDigits!"))
        self.assertTrue(passwordValid("Correct#1Password"))

    #tst6
    def test_hashtags(self):
        self.assertEqual(hashtags("Here are some hashtags: #Python, #coding, and #OpenAI!"), ["#Python", "#coding", "#OpenAI"])
        self.assertEqual(hashtags("No hashtags here!"), [])
        self.assertEqual(hashtags("Multiple #tags in #this sentence!"), ["#tags", "#this"])
        self.assertEqual(hashtags("Check #this out! #123 #works"), ["#this", "#123", "#works"])

if __name__ == "__main__":
    unittest.main()
