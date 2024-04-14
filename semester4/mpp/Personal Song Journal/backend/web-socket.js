const http = require("http");
const WebSocket = require("ws");
const SongRepository = require("./repository/repository").SongRepository;

const port = 4000;

const server = http.createServer();
const wss = new WebSocket.Server({ server });

const songRepository = new SongRepository();

wss.on("connection", (ws) => {
  console.log("New WebSocket client connected");

  ws.on("close", () => {
    console.log("WebSocket client disconnected");
  });
});

setInterval(() => {
  var new_songs = songRepository.generateSongs();
  new_songs.forEach((song) => {
    songRepository.add(song);
  });
  const songs = songRepository.getAllSongs();
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(songs));
    }
  });
}, 20000);

server.listen(port, () => {
  console.log(`WebSocket server running on port ${port}`);
});
