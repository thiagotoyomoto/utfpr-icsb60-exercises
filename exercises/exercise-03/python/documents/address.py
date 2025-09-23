from typing import Optional, List, Dict, Any

class Address:
    def __init__(self, document: Dict[str, Any]):
        self.building = document.get("building", None)
        self.coord = document.get("coord", None)
        self.street = document.get("street", None)
        self.zipcode = document.get("zipcode", None)
    
    @staticmethod
    def of(building: str, coord: List[float], street: str, zipcode: str):
        instance = Address.__new__(Address)
        instance.building = building
        instance.coord = coord
        instance.street = street
        instance.zipcode = zipcode
        return instance
    
    @property
    def coordinates(self) -> Optional[List[float]]:
        return self.coord
    
    @property
    def latitude(self) -> Optional[float]:
        if self.coord and len(self.coord) >= 2:
            return float(self.coord[1])
        return None
    
    @property
    def longitude(self) -> Optional[float]:
        if self.coord and len(self.coord) >= 1:
            return float(self.coord[0])
        return None
    
    def __str__(self) -> str:
        parts = []
        if self.building:
            parts.append(self.building)
        if self.street:
            parts.append(self.street)
        if self.zipcode:
            parts.append(self.zipcode)
        
        return ", ".join(parts) if parts else "Address not available"
    
    def __repr__(self) -> str:
        return f"Address(building='{self.building}', street='{self.street}', zipcode='{self.zipcode}', coord={self.coord})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "building": self.building,
            "coord": self.coord,
            "street": self.street,
            "zipcode": self.zipcode
        }
    
    def is_complete(self) -> bool:
        """Check if all address fields are available"""
        return all([self.building, self.street, self.zipcode, self.coord])
    
    def has_coordinates(self) -> bool:
        """Check if coordinates are available"""
        return self.coord is not None and len(self.coord) >= 2
