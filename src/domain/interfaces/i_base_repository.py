from abc import ABC, abstractmethod
from typing import Any, List

class IBaseRepository(ABC):
    """
    An abstract base class serving as a 'repository interface'
    """

    @abstractmethod
    def add(self, entity: Any) -> Any:
        """
        Persist the entity to the data store.
        Returns the saved entity or an identifier.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        """
        Retrieve all entities.
        """
        pass

    @abstractmethod
    def get_by_id(self, entity_id) -> Any:
        """
        Retrieve an entity by its unique ID.
        """
        pass


    @abstractmethod
    def delete_by_id(self, entity_id) -> None:
        """
        Delete an entity by its unique ID.
        """
        pass

    @abstractmethod
    def update_by_id(self, entity_id) -> None:
        """
        Delete an entity by its unique ID.
        """
        pass