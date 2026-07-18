class SlottingService:

    @staticmethod
    def recommend_location(
        product,
        locations
    ):

        if product.velocity_class == "A":

            return min(
                locations,
                key=lambda x:
                x.distance_to_dock
            )

        if product.velocity_class == "C":

            return max(
                locations,
                key=lambda x:
                x.distance_to_dock
            )

        return locations[0]
