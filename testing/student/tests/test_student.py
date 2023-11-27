import unittest
from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student('Test')
        self.student_with_courses = Student('StudentCourse', {'test_course': ['notes']})

    def test_init_without_courses(self):
        self.assertEqual('Test', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertFalse(self.student.courses)

    def test_init_if_courses_are_set(self):
        self.assertEqual({'test_course': ['notes']}, self.student_with_courses.courses)

    def test_enroll_return_message_already_added_if_course_is_already_enrolled_and_update_course_notes(self):
        actual_result = self.student_with_courses.enroll('test_course', ['note1'])
        self.assertEqual("Course already added. Notes have been updated.", actual_result)
        self.assertEqual({'test_course': ['notes', 'note1']}, self.student_with_courses.courses)

    def test_enroll_return_message_if_add_course_notes_is_set(self):
        actual_result = self.student.enroll('test_course', ['notes'], 'Y')
        expected_string = "Course and course notes have been added."
        self.assertEqual(expected_string, actual_result)
        self.assertEqual({'test_course': ['notes']}, self.student.courses)

    def test_enroll_return_message_and_attach_to_instance_if_add_course_notes_is_omitted(self):
        actual_result_without_add_course_notes_to_be_set = self.student.enroll('test_course', ['note1'])
        expected_string = "Course and course notes have been added."
        self.assertEqual(expected_string, actual_result_without_add_course_notes_to_be_set)
        self.assertEqual({'test_course': ['note1']}, self.student.courses)

    def test_enroll_if_course_is_not_already_enrolled_return_message(self):
        expected_string = "Course has been added."
        actual_result = self.student.enroll('test_course', ['notes'], 'N')
        self.assertEqual(expected_string, actual_result)
        self.assertEqual({'test_course': []}, self.student.courses)

    def test_add_notes_if_course_does_not_exist_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes('invalid_course', ['notes'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_successfully_return_message_and_update_notes(self):
        expected_result = "Notes have been updated"
        actual_result = self.student_with_courses.add_notes('test_course', "notes2")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({'test_course': ['notes', 'notes2']}, self.student_with_courses.courses)

    def test_leave_course_if_course_not_exist_raises_exception(self):
        expected_result = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('invalid')

        self.assertEqual(expected_result, str(ex.exception))

    def test_leave_course_if_course_exist_return_message_and_remove_course(self):
        expected_result = "Course has been removed"
        actual_result = self.student_with_courses.leave_course('test_course')
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({}, self.student_with_courses.courses)

