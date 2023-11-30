import unittest
from collections import deque


def accept_first(words, time):
    output = []
    memory = deque(maxlen=time)
    rejected = set()
    for word in words:
        # print(word, memory, rejected)
        # calc_time = time if time == 1 else time - 1
        status = 'Rejected' if word in memory else 'Accepted'
        if status == 'Rejected' and word in rejected:
            status = 'Accepted'
            rejected.remove(word)
        elif status == 'Rejected':
            rejected.add(word)
        elif status == 'Accepted' and word in rejected:
            rejected.remove(word)

        output.append((word, status))
        memory.append(word)

    return output


class AcceptFirstTest(unittest.TestCase):
    def test_list1_t_3(self):
        ipt = [
            'Meat',  'Cheese', 'Broccoli', 'Cheese', 'Meat', 'Broccoli',
            'Broccoli', 'Cheese'
        ]
        expected = [
            ('Meat', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Rejected'),
            ('Meat', 'Accepted'),
            ('Broccoli', 'Rejected'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Accepted'),
        ]
        self.assertEqual(
            accept_first(ipt, 3), expected
        )

    def test_list_t_1(self):
        ipt = [
            'Meat',  'Cheese', 'Broccoli', 'Cheese', 'Meat', 'Broccoli',
            'Broccoli', 'Cheese'
        ]
        expected = [
            ('Meat', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Meat', 'Accepted'),
            ('Broccoli', 'Accepted'),
            ('Broccoli', 'Rejected'),
            ('Cheese', 'Accepted'),
        ]
        self.assertEqual(
            accept_first(ipt, 1), expected
        )

    def test_list_t_2(self):
        ipt = [
            'Meat',  'Cheese', 'Broccoli', 'Cheese', 'Broccoli',
            'Broccoli', 'Cheese', 'Meat', 'Cheese'
        ]
        expected = [
            ('Meat', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Rejected'),
            ('Broccoli', 'Rejected'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Meat', 'Accepted'),
            ('Cheese', 'Rejected'),
        ]
        self.assertEqual(
            accept_first(ipt, 2), expected
        )

    def test_list_t_3_repeat(self):
        ipt = [
            'Meat',  'Meat', 'Meat', 'Meat', 'Meat',
            'Broccoli', 'Cheese', 'Meat', 'Cheese'
        ]
        expected = [
            ('Meat', 'Accepted'),
            ('Meat', 'Rejected'),
            ('Meat', 'Rejected'),
            ('Meat', 'Rejected'),
            ('Broccoli', 'Rejected'),
            ('Broccoli', 'Accepted'),
            ('Cheese', 'Accepted'),
            ('Meat', 'Accepted'),
            ('Cheese', 'Rejected'),
        ]
        self.assertEqual(
            accept_first(ipt, 2), expected
        )


if __name__ == '__main__':
    unittest.main()
