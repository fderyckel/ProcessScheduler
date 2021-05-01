# Copyright (c) 2020-2021 Thomas Paviot (tpaviot@gmail.com)
#
# This file is part of ProcessScheduler.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

import unittest

import processscheduler as ps

class TestCapacity(unittest.TestCase):
    def test_resource_capacity_1(self) -> None:
        pb = ps.SchedulingProblem('ResourceCapacity1', horizon=12)
        task_1 = ps.FixedDurationTask('task1', duration = 8)

        worker_1 = ps.Worker('Worker1')
        task_1.add_required_resource(worker_1)

        c1 = ps.ResourceCapacity(worker_1, {(0, 6): 2})
        pb.add_constraint(c1)

        solver = ps.SchedulingSolver(pb)
        solution = solver.solve()
        self.assertTrue(solution)
        # the only possible solution is that the task is scheduled form 4 to 12
        self.assertEqual(solution.tasks[task_1.name].start, 4)
        self.assertEqual(solution.tasks[task_1.name].end, 12)

    def test_resource_capacity_2(self) -> None:
        # same problem, but we force two tasks to be scheduled at start and end
        # of the planning
        pb = ps.SchedulingProblem('ResourceCapacity2', horizon=12)
        task_1 = ps.FixedDurationTask('task1', duration = 4)
        task_2 = ps.FixedDurationTask('task2', duration = 4)
        worker_1 = ps.Worker('Worker1')
        task_1.add_required_resource(worker_1)
        task_2.add_required_resource(worker_1)

        c1 = ps.ResourceCapacity(worker_1, {(4, 8): 0})
        pb.add_constraint(c1)

        solver = ps.SchedulingSolver(pb)
        solution = solver.solve()
        self.assertTrue(solution)
        # there should be one task from 0 to 4 and one task from 8 to 12.
        self.assertTrue(solution.tasks[task_1.name].start == 0 or solution.tasks[task_2.name].start == 0)
        self.assertTrue(solution.tasks[task_1.name].start == 8 or solution.tasks[task_2.name].start == 8)


if __name__ == "__main__":
    unittest.main()