"""
Unit tests for longest_word() & shortest_word()

"""
import assessment1
import unittest

class TestFunctions(unittest.TestCase):
    
    def test_list_multiple_longs(self):
        """
        input text is a single line with punctuations & multiple max length words
        """
        data = "Longest word/s: ['jumped', 'shweta'] & its length is: 6"
        result = assessment1.longest_word("My name  Rani; & she is shweta. The cow jumped over the moon.")
        self.assertEqual(result, data)


    def test_list_multiple_lines_largest_word(self):
        """
        input text contains multiple lines
        """
        data2 = "Longest word/s: ['moon89089978'] & its length is: 12"
        result2 = assessment1.longest_word("My888889 name  Rani; 99 & she is shweta."
                              " The cow jumped over the moon89089978.")
        self.assertEqual(result2, data2)


    def test_list_largest_word_spaces(self):
        """
        input text contains only white spaces
        """
        data3 = None
        result3 = assessment1.longest_word(" ")
        self.assertEqual(result3, data3)


    def test_list_largest_word_non_string(self):
        """
        input is not string
        """
        data4 = None
        result4 = assessment1.longest_word(85214)
        self.assertEqual(result4, data4)
        

    def test_list_multiple_shortest_word(self):
        """
        input text is a single line with punctuations & multiple min length words
        """
        data1 = "shortest word/s: ['I', 'N'] & its length is: 1"
        result1 = assessment1.shortest_word('I N am Rani; & she is shweta.')
        self.assertEqual(result1, data1)


    def test_list_multiple_lines_shortest_word(self):
        """
        input text contains multiple lines
        """
        data2 = "shortest word/s: ['I'] & its length is: 1"
        result2 = assessment1.shortest_word('am Rani ; & she is my sister.'
                                 'I am most happy')
        self.assertEqual(result2, data2)


    def test_list_shortest_word_spaces(self):
        """
        input text contains only white spaces
        """
        data3 = None
        result3 = assessment1.shortest_word(" ")
        self.assertEqual(result3, data3)


    def test_list_largest_word_non_string(self):
        """
        input is not string
        """
        data4 = None
        result4 = assessment1.shortest_word(84557)
        self.assertEqual(result4, data4)

if __name__ == '__main__':
    unittest.main()
