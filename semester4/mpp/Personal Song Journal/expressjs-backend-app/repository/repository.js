const Song = require("../domain/song.js");
class SongRepository {
  constructor() {
    this.song1 = new Song(
      "1",
      "Our Last Summer",
      "Abba",
      8,
      "This songs reminds me of summer"
    );
    this.song2 = new Song(
      "2",
      "Ca o Molie",
      "Subcarpati",
      9,
      "Made me feel very happy"
    );
    this.song3 = new Song(
      "3",
      "You Spin Me Round (Like A Record)",
      "Dead Or Alive",
      9,
      "Very cool! Makes me want to dance"
    );
    this.songs = [this.song1, this.song2, this.song3];
  }

  findById(id) {
    return this.songs.find((song) => song.getId() === id);
  }

  add(newSong) {
    const existingSong = this.songs.find(
      (song) =>
        song.getTitle() === newSong.getTitle() &&
        song.getArtist() === newSong.getArtist()
    );
    if (existingSong) {
      throw new Error("Song already exists");
    }

    this.songs.push(newSong);
  }

  getAllSongs() {
    return this.songs;
  }

  delete(id) {
    const existingSong = this.songs.find((song) => song.id === id);
    if (!existingSong) {
      throw new Error("Song does not exist");
    }
    this.songs = this.songs.filter((song) => song.id !== id);
  }

  update(id, updatedSong) {
    const index = this.songs.findIndex((song) => song.id === id);
    if (index !== -1) {
      this.songs[index] = updatedSong;
    } else {
      throw new Error("Song does not exist");
    }
  }
}
module.exports.SongRepository = SongRepository;
