from typing import Optional, Dict, Any
from datetime import datetime

class Grade:
    def __init__(self, document: Dict[str, Any]):
        self.date = document.get("date", None)
        self.grade = document.get("grade", None)
        self.score = document.get("score", None)
    
    @staticmethod
    def of(date: str, grade: str, score: float):
        instance = Grade.__new__(Grade)
        instance.date = date
        instance.grade = grade
        instance.score = score
        return instance
    
    @property
    def date_formatted(self) -> Optional[str]:
        if self.date:
            try:
                if hasattr(self.date, 'strftime'):
                    return self.date.strftime("%Y-%m-%d")
                return str(self.date)
            except:
                return str(self.date)
        return None
    
    def __str__(self) -> str:
        return f"Grade(grade='{self.grade}', score={self.score}, date={self.date_formatted})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "date": self.date,
            "grade": self.grade,
            "score": self.score,
            "date_formatted": self.date_formatted
        }