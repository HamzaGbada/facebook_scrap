import unittest

from src.Scapper.facebook_scrap import Facebook_scrap


class TestScrap(unittest.TestCase):
    def test_list_int(self):
        page_id = "zuck"
        result = Facebook_scrap(page_id).scrap()
        print(result)
        data = {'About': "I'm trying to make the world a more open place.",
 'Education': 'Harvard University\n'
              'Computer Science and Psychology\n'
              'August 30, 2002 - April 30, 2004\n'
              'Phillips Exeter Academy\n'
              'Classics\n'
              'Class of 2002\n'
              'Ardsley High School\n'
              'High school\n'
              'September 1998 - June 2000',
 'Favorite quotes': '"Fortune favors the bold."\n'
                    '- Virgil, Aeneid X.284\n'
                    '\n'
                    '"All children are artists. The problem is how to remain '
                    'an artist once you grow up."\n'
                    '- Pablo Picasso\n'
                    '\n'
                    '"Make things as simple as possible but no simpler."\n'
                    '- Albert Einstein',
 'Name': 'Mark Zuckerberg',
 'Places lived': [{'link': '/profile.php?id=104022926303756&refid=17',
                   'text': 'Palo Alto, California',
                   'type': 'Current City'},
                  {'link': '/profile.php?id=105506396148790&refid=17',
                   'text': 'Dobbs Ferry, New York',
                   'type': 'Hometown'}],
 'Work': 'Chan Zuckerberg Initiative\n'
         'December 1, 2015 - Present\n'
         'Meta\n'
         'Founder and CEO\n'
         'February 4, 2004 - Present\n'
         'Palo Alto, California\n'
         'Bringing the world closer together.'}
        self.assertEqual(result, data)
