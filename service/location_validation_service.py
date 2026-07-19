class LocationValidationService:

    @staticmethod
    def validate_location(
        product,
        location,
        nearby_products
    ):

        violations = []

        # Hazard Rules
        for item in nearby_products:

            if (
                product.hazard_class == "Flammable"
                and
                item.hazard_class == "Oxidizer"
            ):

                violations.append(
                    "Flammable inventory cannot reside near oxidizers."
                )

        # Temperature Rules
        if (
            hasattr(product,
                    "required_temperature_zone")
            and
            hasattr(location,
                    "temperature_zone")
        ):

            if (
                product.required_temperature_zone
                != location.temperature_zone
            ):

                violations.append(
                    f"Temperature mismatch. "
                    f"{product.sku} requires "
                    f"{product.required_temperature_zone} storage."
                )

        return violations
