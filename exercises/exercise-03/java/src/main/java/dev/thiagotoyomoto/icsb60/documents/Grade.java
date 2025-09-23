package dev.thiagotoyomoto.icsb60.documents;

import java.util.Date;

public record Grade(
    Date date,
    String grade,
    int score
) {}
