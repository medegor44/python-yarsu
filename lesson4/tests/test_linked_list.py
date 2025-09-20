import unittest
import utils.linked_list

class TestLinkedList(unittest.TestCase):
    def test_append_append_one_node_should_append(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        # Act
        list.append(1)
        # Assert
        self.assertIsNotNone(list.head)
        self.assertEqual(list.head.value, 1) # type: ignore

    def test_search_value_exists_should_return_index(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        index = list.search(2)
        # Assert
        self.assertEqual(index, 1)

    def test_length_should_return_correct_length(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        length = list.length()
        # Assert
        self.assertEqual(length, 3)

    def test_delete_value_exists_should_remove_node(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        list.delete(2)

        # Assert
        self.assertEqual(list.length(), 2)
        self.assertEqual(list.search(2), -1)

    def test_insert_at_head_should_place_value_at_head(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        list.insert(0, 0)

        # Assert
        self.assertEqual(list.search(0), 0)

    def test_insert_at_tail_should_place_value_at_tail(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        list.insert(4, 3)

        # Assert
        self.assertEqual(list.search(4), 3)

    def test_insert_in_the_middle_should_place_value_in_middle(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        list.insert(1.5, 2)

        # Assert
        self.assertEqual(list.search(1.5), 2)

    def test_insert_at_negative_position_should_do_nothing(self):
        # Arrange
        list = utils.linked_list.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)

        # Act
        list.insert(1.5, -1)

        # Assert
        self.assertEqual(list.search(1.5), -1)
