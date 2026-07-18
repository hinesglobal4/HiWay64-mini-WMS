class LocationValidationService:

    @staticmethod
    def validate_location(
        product,
        location,
        nearby_products
    ):

        violations = []

        # Hazard check

        for item in nearby_products:

            if (
                product.hazard_class ==
                "Flammable"
                and
                item.hazard_class ==
                "Oxidizer"
            ):

                violations.append(
                    "Flammable inventory "
                    "cannot reside near "
                    "oxidizers."
                )

        # Temperature check

        if (
            product.required_temperature_zone
            !=
            location.temperature_zone
        ):

            violations.append(
                "Temperature zone mismatch."
            )

        return violations

if validation_errors:

    return {

        "success": False,

        "messages":
        validation_errors
    }
if (
    product.required_temperature_zone
    !=
    target_location.temperature_zone
):

    violations.append(
        f"{product.sku} requires "
        f"{product.required_temperature_zone}"
        f" storage."
    )
