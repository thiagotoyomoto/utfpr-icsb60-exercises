package dev.thiagotoyomoto.icsb60.documents;

import java.time.Instant;
import java.time.OffsetDateTime;
import java.time.ZoneId;

import org.bson.BsonReader;
import org.bson.BsonType;
import org.bson.BsonWriter;
import org.bson.codecs.Codec;
import org.bson.codecs.DecoderContext;
import org.bson.codecs.EncoderContext;

public class OffsetDateTimeCodec implements Codec<OffsetDateTime> {

    @Override
    public OffsetDateTime decode(BsonReader reader, DecoderContext decoderContext) {
        BsonType type = reader.getCurrentBsonType();
        if (type == BsonType.DATE_TIME) {
            long millis = reader.readDateTime();
            return Instant.ofEpochMilli(millis)
                .atZone(ZoneId.systemDefault())
                .toOffsetDateTime();
        }
        // if stored as string, try reading it
        if (type == BsonType.STRING) {
            String s = reader.readString();
            return OffsetDateTime.parse(s);
        }
        throw new org.bson.BsonInvalidOperationException("Cannot decode OffsetDateTime from BsonType: " + type);
    }

    @Override
    public void encode(BsonWriter writer, OffsetDateTime value, EncoderContext encoderContext) {
        if (value == null) {
            writer.writeNull();
            return;
        }
        long millis = value.toInstant().toEpochMilli();
        writer.writeDateTime(millis);
    }

    @Override
    public Class<OffsetDateTime> getEncoderClass() {
        return OffsetDateTime.class;
    }
}
