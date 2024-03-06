const { MongoClient } = require('mongodb');
const { createCanvas, loadImage } = require('canvas');
const { CLIP } = require('clip-image-search');

async function main() {
    // MongoDB connection string
    const uri = "mongodb+srv://team5:team5password!@cluster0.iarvn.mongodb.net/";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        await client.connect();

        const database = client.db('vector_search');
        const collection = database.collection('damage');

        // Initialize CLIP model
        const clipModel = await CLIP.load();

        // Load input image
        const inputImage = await loadImage('images/01-minor/0001.JPEG');

        // Encode input image into a vector
        const canvas = createCanvas(inputImage.width, inputImage.height);
        const ctx = canvas.getContext('2d');
        ctx.drawImage(inputImage, 0, 0);
        const inputImageVector = await clipModel.encode(canvas);

        // Construct MongoDB aggregation pipeline
        const pipeline = [
            {
                $search: {
                    index: "damage",
                    knnBeta: {
                        vector: inputImageVector,
                        path: "imageVector",
                        k: 10
                    }
                }
            },
            {
                $project: {
                    imageVector: { $slice: ["$imageVector", 5] },
                    imageFile: 1,
                    price: 1,
                    discountPercentage: 1,
                    averageRating: 1,
                    _id: 0,
                    score: {
                        $meta: 'searchScore'
                    }
                }
            }
        ];

        // Execute the aggregation pipeline
        const cursor = collection.aggregate(pipeline);
        const docs = await cursor.toArray();

        // Print the results
        console.log(JSON.stringify({ docs }));
    } finally {
        // Close the connection
        await client.close();
    }
}

main().catch(console.error);