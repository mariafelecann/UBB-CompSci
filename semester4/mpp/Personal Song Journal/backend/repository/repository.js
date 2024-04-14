const Song = require("../domain/song.js");
const { fakerEN, faker } = require("@faker-js/faker");

class SongRepository {
  constructor() {
    this.songs = this.generateSongs();
  }

  generateSongs() {
    const songs = [];
    for (let i = 0; i < 10; i++) {
      const song = new Song(
        faker.string.uuid(),
        fakerEN.music.songName(),
        fakerEN.person.fullName(),
        faker.number.int({ min: 1, max: 10 }),
        fakerEN.lorem.sentence()
      );
      songs.push(song);
    }
    return songs;
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
