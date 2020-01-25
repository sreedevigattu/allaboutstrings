import sys
sys.path.append(".\\")

import unittest
import name

def stringcheck(self, varname, initialval, finalval):
    desiredval = initialval.capitalize()
    self.assertNotEqual(finalval, "", 
            "{} should not be empty".format(varname))   
    self.assertNotEqual(finalval, initialval, 
            "\"{}\" should begin with a capital letter. Use capitalize() function"
            .format(desiredval)) 
    self.assertEqual(finalval, desiredval,
            "{} should have been \"{}\", but you entered \"{}\"".format(varname, desiredval, finalval))

class NameTest(unittest.TestCase): 
    def test_1_firstname(self):      
        stringcheck(self, "firstname", name.fname, name.firstname)

    def test_2_lastname(self): 
        stringcheck(self, "lastname", name.lname, name.lastname)

    def test_3_fullname(self): 
        desiredfname = name.fname.capitalize()
        desiredlname = name.lname.capitalize() 
        desiredfullname = name.fname.capitalize() + " " + name.lname.capitalize()
        self.assertEqual(name.fullname.find(desiredfname), 0, 
            "{} should have the \"{}\" in the beginning".format("fullname", desiredfname))
        self.assertEqual(name.fullname.find(" "), len(desiredfname), 
            "There should be a space after \"{}\"".format(desiredfname))
        self.assertEqual(name.fullname.find(desiredlname), len(desiredfname)+1, 
            "{} should begin after \"{} \"".format(desiredlname,desiredfname))
        self.assertEqual(name.fullname, desiredfullname,
            "{} should have been \"{}\", but it is \"{}\"".format("fullname",desiredfullname,name.fullname))
  
if __name__ == '__main__': 
    unittest.main(failfast=True) 