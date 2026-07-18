class LocationValidationService:

    @staticmethod
    def validate_location(
        product,
        target_location,
        nearby_products
    ):

        violations = []

        for item in nearby_products:

            if (
                product.hazard_class ==
                "Flammable"
                and
                item.hazard_class ==
                "Oxidizer"
            ):

                violations.append(
                    "Flammable inventory cannot be stored near oxidizers."
                )

        return violations
