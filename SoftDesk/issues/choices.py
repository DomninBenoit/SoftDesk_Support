from extended_choices import Choices

PRIORITY_CHOICES = Choices(
    ('LOW', 1, 'Low'),
    ('MEDIUM', 2, 'Medium'),
    ('HIGH', 3, 'High')
)

LABEL_CHOICES = Choices(
    ('BUG', 1, 'Bug'),
    ('FEATURE', 2, 'Feature'),
    ('TASK', 3, 'Task')
)

STATUS_CHOICES = Choices(
    ('TODO', 1, 'To Do'),
    ('IN_PROGRESS', 2, 'In Progress'),
    ('FINISHED', 3, 'Finished')
)