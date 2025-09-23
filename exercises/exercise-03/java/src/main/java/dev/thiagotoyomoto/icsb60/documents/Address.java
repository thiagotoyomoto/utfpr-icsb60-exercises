package dev.thiagotoyomoto.icsb60.documents;

import java.util.List;

public record Address(
    String building,
    List<Double> coord,
    String street,
    String zipcode
) {}
