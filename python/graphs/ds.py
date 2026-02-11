"""
Data Structures
===============
"""
from typing import *
from enum import Enum

class PriorityQueue:
    """Priority Queue implementation
    [Thread Un-Safe]
    """
    class Task:
        """Task Implementation"""
        def __init__(self, task_id: str, priority: int, data: Optional[Union[dict, NamedTuple]] = None):
            self._task_id = task_id
            self._priority = priority
            self._data = data

        @property
        def task_id(self) -> str:
            return self._task_id
        
        @property
        def priority(self) -> int:
            return self._priority
        
        @property
        def data(self) -> int:
            return self._data
    
    class Order(str, Enum):
        """priority sorting order"""
        MIN="MIN"
        MAX="MAX"

    def __init__(self, order: Order=Order.MIN):
        """constructor"""
        self._queue: List[PriorityQueue.Task] = []
        self._task_id_pool: Set[str] = set()
        self._order = order

    def put(self, task: PriorityQueue.Task) -> None:
        """adds a task to queue"""
        if task.task_id in self._task_id_pool:
            raise Exception(f'ERROR:DUPLICATE-TASK - a task with id `{task.task_id}` already exists')
        self._queue.append(task)
        self._sort()
    
    def put_bulk(self, tasks: List[PriorityQueue.Task]) -> Dict[str]:
        """adds a task to queue"""
        status: Dict[str] = {}
        for task in tasks:
            try:
                self.put(task)
            except Exception as e:
                if str(e).startswith("ERROR:DUPLICATE-TASK"):
                    status[task.task_id] = str(e)
                raise e
            else:
                status[task.task_id] = "SUCESSFULL"
        self._sort()
    
    def get(self) -> Task:
        """provides a latest task based on first priority"""
        task: PriorityQueue.Task = self._queue.pop(0)
        self._sort()
        return task
    
    def task_priority_update(self, task_identifier: Union[Task, str], priority_value: int):
        """updates the priority of an existing task"""
        if isinstance(task_identifier, PriorityQueue.Task):
            task_id: str = task_identifier.task_id
        else:
            task_id: str = task_identifier
        task: PriorityQueue.Task = self._search(task_id)
        task._priority = priority_value
        self._sort()
    
    def _search(self, task_id: str) -> Optional[Task]:
        """searches for a task"""
        for task in self._queue:
            if task.task_id == task_id:
                return task
    
    def _sort(self) -> None:
        """sorts the task queue based on priority value"""
        # do sorting of tasks based on priority value
        #   - for same priority value , compare based on id
        self._queue.sort(key=lambda task: (task.priority, task.task_id), reverse=(True if self._order == PriorityQueue.Order.MAX else False))

    def __iter__(self):
        for value in self._queue:
            yield value

    def __contains__(self, item: Union[Task, str]):
        if isinstance(item, PriorityQueue.Task):
            return item in self._queue
        else:
            for task in self._queue:
                if task.task_id == item:
                    return True
            return False
    
    def contains(self, item: Union[Task, str, Callable]) -> bool:
        """checks if queue contains the task based on identifier item"""
        if isinstance(item, PriorityQueue.Task):
            return item in self._queue
        elif isinstance(item, str):
            for task in self._queue:
                if task.task_id == item:
                    return True
            return False
        else:
            for task in self._queue:
                if item(task):
                    return True
            return False
        
    def fetch_task(self, by: Union[Task, str, Callable]) -> Optional[Task]:
        """fetches a task if it exists"""
        for task in self._queue:
            if isinstance(by, PriorityQueue.Task):
                if task == by:
                    return task
            elif isinstance(by, str):
                if task.task_id == by:
                    return task
            else:
                if by(task):
                    return task
    # empty check utility
    empty = lambda self: len(self._queue) <= 0
    
# Testing Entrypoint
if __name__ == '__main__':

    pq = PriorityQueue()
    pq.put(PriorityQueue.Task('a', 1, {"label": 1}))
    pq.put(PriorityQueue.Task('b', 0, {"label": 2}))
    pq.put(PriorityQueue.Task('c', 3, {"label": 3}))
    pq.put(PriorityQueue.Task('d', 6, {"label": 4}))
    pq.put(PriorityQueue.Task('e', -1, {"label": 5}))
    
    assert pq.get().task_id == 'e'
    assert pq.get().task_id == 'b'
    
    pq.put(PriorityQueue.Task('f', -1, {"label": 6}))
    
    assert pq.get().task_id == 'f'
    
    pq.put(PriorityQueue.Task('g', 4, {"label": 7}))

    assert pq.get().task_id == 'a'

    pq.task_priority_update('d', -1)

    assert pq.get().task_id == 'd'

    print([f"{v.task_id}({v.priority})" for v in pq])

    assert pq.empty() == False

    pq.get();pq.get()

    assert pq.empty() == True

    print([f"{v.task_id}({v.priority})" for v in pq])

    t1 = PriorityQueue.Task('h', -1, {"label": 8})
    t2 = PriorityQueue.Task('i', -1, {"label": 9})
    pq.put_bulk([t1,])
    assert (t1 in pq) == True
    assert (t2 in pq) == False

    