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
