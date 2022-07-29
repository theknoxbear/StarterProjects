import people_also_ask
from pprint import pprint
questions = people_also_ask.get_related_questions("stamp collecting", 20)
pprint(questions)
