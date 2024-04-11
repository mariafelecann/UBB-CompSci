const SongRepository = require("./repository/repository").SongRepository;

const express = require("express");
const app = express();
const port = 3000;
const cors = require("cors");
app.use(cors());
const songRepository = new SongRepository();
app.use(express.json());
const crudOperationsRouter = require("./routes/crud_operations");
app.use("/crud-operations", crudOperationsRouter);

const filterRouter = require("./routes/pagination_filter_search");
app.use("/filter", filterRouter);

app.get("/", (req, res) => {
  res.send("Welcome to your music journal!");
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
