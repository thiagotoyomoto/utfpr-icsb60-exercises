package dev.thiagotoyomoto.icsb60;

import java.util.concurrent.TimeUnit;

import org.bson.Document;

import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

import dev.thiagotoyomoto.icsb60.documents.Restaurant;

public class Main {
    private final static String HOST = "localhost";
    private final static int PORT = 27017;
    private final static String DATABASE_USERNAME = "mongo";
    private final static String DATABASE_PASSWORD = "mongo";
    private final static String DATABASE_NAME = "example";
    private final static String DATABASE_URL = String.format(
        "mongodb://%s:%s@%s:%d",
        DATABASE_USERNAME,
        DATABASE_PASSWORD,
        HOST,
        PORT
    );


    private final static String COLLECTION_NAME = "restaurants";
    
    public static void main(String[] args) {
        try (final var mongoClient = createMongoClient()) {
            final var database = mongoClient.getDatabase(DATABASE_NAME);
            final var collection = database.getCollection(COLLECTION_NAME, Restaurant.class);

            final var restaurant = new Restaurant(
                null,
                "Manhattan",
                "Italian",
                null,
                "Vella",
                "40356018"
            );

            collection.insertOne(restaurant);

            final var filter = new Document("restaurant_id", "40356018");
            final var restaurants = collection.find(filter);

            for (final var document : restaurants) {
                System.out.println(document);
            }
        }
    }

    private static MongoClient createMongoClient() {
        final var connectionString = new ConnectionString(DATABASE_URL);
        final var settings = MongoClientSettings.builder()
            .applyConnectionString(connectionString)
            .applyToSocketSettings(builder -> 
                builder.connectTimeout(10, TimeUnit.SECONDS)
            )
            .build();
        return MongoClients.create(settings);
    }
}