# 📦 Semantic Search with Typesense + Instantsearch.js

This is a demo that shows how you can use [Typesense's](https://github.com/typesense/typesense) vector search feature, to build a semantic search experience.

**NOTE: ⚠️** This demo uses Typesense version 0.24.0 which did not have built-in embedding generation. But in v0.25.0, we've added built-in emebedding generation, which makes it even more easy to build semantic search out of the box, without the need for an external embedding service. Here's a newer demo that takes advantage of this feature: [https://github.com/typesense/showcase-hn-comments-semantic-search](https://github.com/typesense/showcase-hn-comments-semantic-search).

Learn more about Vector Search here: [https://typesense.org/docs/0.25.0/api/vector-search.html](https://typesense.org/docs/0.25.0/api/vector-search.html).

## Tech Stack

The app was built using the <a href="https://github.com/typesense/typesense-instantsearch-adapter" target="_blank">
Typesense Adapter for InstantSearch.js</a>.

## Repo structure

- `src/` and `index.html` - contain the frontend UI components.
- `scripts/indexer` - contains the script to index the book data into Typesense.
- `scripts/data` - contains a small sample subset of products.
- `server` - contains the API server that generates embeddings given a query.

## How to

Index sample dataset:

```shell
npm install
npm run typesenseServer

ln -s .env.development .env

npm run indexer
```

Start Embedding API server:

```shell
cd server

pip install -r requirements.txt

uvicorn main:app --reload
```

Start FE app:

```shell
npm start
```

Open http://localhost:3001 to see the app.


## Credits

The dataset used in this showcase is from Algolia's public set of datasets listed here: https://github.com/algolia/datasets
