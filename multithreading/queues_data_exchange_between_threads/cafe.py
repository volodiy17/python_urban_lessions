import time
from queue import Queue


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            available_table = next((table for table in self.tables if table.guest is None), None)
            if available_table is not None:
                available_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)
