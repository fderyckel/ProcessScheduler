
Task Constraints
================

ProcessScheduler provides a set of ready-to-use temporal task constraints. They allow expressing common rules such as "the task A must start exactly at the instant 4", "the task B must end at the same time than the task C ends", "the task C must be scheduled exactly 3 periods after the task D is completed" etc.

There are a set of builtin ready-to-use constraints, listed below.

.. note::

    Naming convention: if the class name starts with *Task** then the constraint applies to one single task, if the class name starts with *Tasks** it applies to 2 or more task instances.

- :class:`TaskPrecedence`: takes two parameters :attr:`task_1` and :attr:`task_2` and constraints :attr:`task_2` to be scheduled after :attr:`task_1` is completed. The precedence type can either be :const:`'lax'` (default, :attr:`task_2.start` >= :attr:`task_1.end`)), :const:`'strict'` (:attr:`task_2.start` >= :attr:`task_1.end`)) or :const:`'tight'` (:attr:`task_2.start` >= :attr:`task_1.end`, task_2 starts immediately after task_1 is completed). An optional parameter :attr:`offset` can be additionnaly set.

.. code-block:: python

    task_1 = ps.FixedDurationTask('Task1', duration=3)
    task_2 = ps.FixedVariableTask('Task2')
    pc = TaskPrecedence(task1, task2, kind='tight', offset=2)

constraints the solver to schedule task_2 start exactly 2 periods after task_1 is completed.

- :class:`TasksStartSynced`: takes two parameters :attr:`task_1` and :attr:`task_2` such as the schedule must satisfy the constraint :math:`task_1.start = task_2.start`

.. image:: img/TasksStartSynced.svg
    :align: center
    :width: 90%

- :class:`TasksEndSynced`: takes two parameters :attr:`task_1` and :attr:`task_2` such as the schedule must satisfy the constraint :math:`task_1.end = task_2.end`

.. image:: img/TasksEndSynced.svg
    :align: center
    :width: 90%

- :class:`TasksDontOverlap`: takes two parameters :attr:`task_1` and :attr:`task_2` such as the task_1 ends before the task_2 is started or the opposite (task_2 ends before task_1 is started)

.. image:: img/TasksDontOverlap.svg
    :align: center
    :width: 90%

- :class:`TaskStartAt`: takes two parameters :attr:`task` and :attr:`value` such as the task starts exactly at the instant :math:`task.start = value`

- :class:`TaskStartAfterStrict`: the constraint  :math:`task.start > value`

- :class:`TaskStartAfterLax`: the constraint :math:`task.start >= value`

- :class:`TaskEndAt`: takes two parameters :attr:`task` and :attr:`value` such as the task ends exactly at the instant *value* :math:`task.end = value`

- :class:`TaskEndBeforeStrict`: the constraint :math:`task.end < value`

- :class:`TaskEndBeforeLax`: the constraint :math:`task.end <= value`