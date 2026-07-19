class LocationValidationService:

    @staticmethod
    def validate_location(
        product,
        location,
        nearby_products
    ):

        violations = []

        # Hazard validation
        for item in nearby_products:

            if (
                product.hazard_class == "Flammable"
                and
                item.hazard_class == "Oxidizer"
            ):

                violations.append(
                    "Flammable inventory cannot reside near oxidizers."
                )

        # Temperature validation
        if (
            product.required_temperature_zone
            != location.temperature_zone
        ):

            violations.append(
                f"{product.sku} requires "
                f"{product.required_temperature_zone} storage."
            )

        return violations
