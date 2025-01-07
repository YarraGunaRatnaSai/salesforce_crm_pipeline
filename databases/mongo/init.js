db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "readWrite", db: "integration_metadata" }],
});

db.createCollection("metadata");
db.metadata.insertMany([
  { key: "example", value: "This is a sample metadata entry." },
]);
