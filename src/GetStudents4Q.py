import numpy as np
from typing import Dict, List

RatingType = Dict[str, float]


class GetStudents4Q():

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating
        self.studentsq4: RatingType = {}

    def get(self) -> RatingType:
        rating_list = list(self.rating.values())
        last_quartile = np.quantile(rating_list, 1)
        third_median = np.quantile(rating_list, 0.75)
        for key in self.rating:
            if third_median <= self.rating[key] <= last_quartile:
                self.studentsq4[key] = float(self.rating[key])
        return self.studentsq4
