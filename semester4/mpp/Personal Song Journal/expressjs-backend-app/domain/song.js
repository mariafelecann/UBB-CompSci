class Song {
  constructor(nid, ntitle, nartist, nrating, nreview) {
    this.id = nid;
    this.title = ntitle;
    this.artist = nartist;
    this.rating = nrating;
    this.review = nreview;
  }

  setRating(new_rating) {
    this.rating = new_rating;
  }
  setArtist(new_artist) {
    this.artist = new_artist;
  }
  setReview(new_review) {
    this.review = new_review;
  }
  setTitle(new_title) {
    this.title = title;
  }

  getId() {
    return this.id;
  }

  getTitle() {
    return this.title;
  }

  getArtist() {
    return this.artist;
  }
  getRating() {
    return this.rating;
  }
  getReview() {
    return this.review;
  }
}

module.exports = Song;
