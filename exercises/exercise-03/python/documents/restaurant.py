from typing import Optional, Dict, Any, List
from documents.address import Address
from documents.grade import Grade

class Restaurant:
    def __init__(self, document: Dict[str, Any]):
        self._id = document.get("_id")
        self.name = document.get("name", None)
        self.cuisine = document.get("cuisine", None)
        self.borough = document.get("borough", None)
        
        address_data = document.get("address", {})
        self.address = Address(address_data) if address_data else None
        
        grades_data = document.get("grades", [])
        self.grades = [Grade(grade_doc) for grade_doc in grades_data] if grades_data else []
        
        self.restaurant_id = document.get("restaurant_id", None)

    @staticmethod
    def of(name: str, 
           cuisine: str, 
           borough: str, 
           address: Address, 
           grades: List[Grade], 
           restaurant_id: str,
           _id: Optional[str] = None):
        self = Restaurant.__new__(Restaurant)
        self._id = _id
        self.name = name
        self.cuisine = cuisine
        self.borough = borough
        self.address = address
        self.grades = grades
        self.restaurant_id = restaurant_id
        return self

    @property
    def street(self) -> Optional[str]:
        return self.address.street if self.address else None
    
    @property
    def building(self) -> Optional[str]:
        return self.address.building if self.address else None
    
    @property
    def zipcode(self) -> Optional[str]:
        return self.address.zipcode if self.address else None
    
    @property
    def coordinates(self) -> Optional[list]:
        return self.address.coordinates if self.address else None
    
    @property
    def latitude(self) -> Optional[float]:
        return self.address.latitude if self.address else None
    
    @property
    def longitude(self) -> Optional[float]:
        return self.address.longitude if self.address else None
    
    @property
    def latest_grade(self) -> Optional[str]:
        if self.grades:
            return self.grades[0].grade if self.grades[0].grade else "No grade"
        return "No grades available"
    
    @property
    def latest_score(self) -> Optional[float]:
        if self.grades:
            return self.grades[0].score
        return None
    
    @property
    def grades_list(self) -> List[Grade]:
        return self.grades
    
    def __str__(self) -> str:
        address_str = self.address.to_dict() if self.address else None
        return f"Restaurant(name='{self.name}', cuisine='{self.cuisine}', borough='{self.borough}', address='{address_str}')"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "cuisine": self.cuisine,
            "borough": self.borough,
            "address": self.address.to_dict(),
            "grades": [grade.to_dict() for grade in self.grades],
            "restaurant_id": self.restaurant_id
        }