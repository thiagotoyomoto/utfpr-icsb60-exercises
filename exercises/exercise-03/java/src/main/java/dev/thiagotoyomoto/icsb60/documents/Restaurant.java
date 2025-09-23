package dev.thiagotoyomoto.icsb60.documents;

import java.util.List;

public record Restaurant(
    Address address,
    String borough,
    String cuisine,
    List<Grade> grades,
    String name,
    String restaurant_id
) {}
