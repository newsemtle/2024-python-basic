from abc import ABC, abstractmethod


class Location(ABC):
    def __init__(self, name):
        self.name = name
        self._links = []

    @property
    def links(self):
        return self._links

    def add_links_to(self, *others):
        for other in others:
            if other not in self._links:
                self._links.append(other)

    def add_connections_with(self, *others):
        for other in others:
            self.add_links_to(other)
            other.add_links_to(self)
