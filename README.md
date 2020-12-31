# 📦 Instant E-Commerce Store Experience, powered by Typesense

⚠️ Work in Progress ⚠️

This is a demo that shows how you can use [Typesense's](https://github.com/typesense/typesense) feature set,
to build not just a search experience, but also a full-fledged product browsing experience for an ecommerce store.

## Tech Stack

The app was built using the <a href="https://github.com/typesense/typesense-instantsearch-adapter" target="_blank">
Typesense Adapter for InstantSearch.js</a>.

## Repo structure

- `src/` and `index.html` - contain the frontend UI components.
- `scripts/indexer` - contains the script to index the book data into Typesense.
- `scripts/data` - contains a small sample subset of products.

## Development

To run this project locally, install the dependencies and run the local server:

```shell
npm install
npm run typesenseServer

ln -s .env.development .env

npm run indexer

npm start
```

Open http://localhost:3000 to see the app.