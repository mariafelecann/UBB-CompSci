const SongRepository = require("../repository/repository.js").SongRepository;
const Song = require("../domain/song.js");
const express = require("express");
const router = express.Router();
const songRepository = new SongRepository();
const songgg = new Song();
router.get("/", (req, res) => {
  res.send("crud operations page");
});

router.get("/songs", (req, res) => {
  const songs = songRepository.getAllSongs();
  res.status(200).json(songs);
});

router
  .route("/:id")
  .get((req, res) => {
    const song = songRepository.findById(req.params.id);
    if (!song) return res.status(404).send("Song not found");
    res.send(song);
  })
  .put((req, res) => {
    const updatedSong = new Song(
      req.params.id,
      req.body.title,
      req.body.artist,
      req.body.rating,
      req.body.review
    );
    try {
      songRepository.update(req.params.id, updatedSong);
      res.send(updatedSong);
    } catch (error) {
      res.status(404).send("Song not found");
    }
  })
  .delete((req, res) => {
    // const song = songRepository.findById(req.params.id);
    // if (!song) {
    //   return res.status(404).send("Song not found");
    // }
    // const index = song.getId();
    // try {
    //   songRepository.delete(index);
    //   const songs = songRepository.getAllSongs();
    //   res.json(songs);
    // } catch (error) {
    //   res.status(404).send("Song not found");
    // }
    const song = songRepository.findById(req.params.id);
    if (!song) {
      return res.status(404).send("Song not found");
    }
    // const index = song.getId();
    // if (index === -1) return res.status(404).send("Song not found");
    // songs.splice(index, 1);
    const index = song.getId();
    songRepository.delete(index);
    const songs = songRepository.getAllSongs();
    res.json(songs);
  })
  .post((req, res) => {
    const song = new Song(
      Date.now.toString(),
      req.body.title,
      req.body.artist,
      req.body.rating,
      req.body.review
    );
    try {
      songRepository.add(song);
      res.send(song);
    } catch (error) {
      res.status(404).send("Song already exists");
    }
  });

module.exports = router;
// module.exports = { router, app: express() };
