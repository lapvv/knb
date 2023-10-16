<template>
  <div>MainPage</div>
  <button class="btn btn-primary" @click="sendMoves"></button>
</template>

<script>
const websocket = new WebSocket("ws://localhost:8001/");
const event = { type: "play", column: 3 };
websocket.send(JSON.stringify(event));
function sendMoves(board, websocket) {
  // When clicking a column, send a "play" event for a move in that column.
  board.addEventListener("click", ({ target }) => {
    const column = target.dataset.column;
    // Ignore clicks outside a column.
    if (column === undefined) {
      return;
    }
    const event = {
      type: "play",
      column: parseInt(column, 10),
    };
    websocket.send(JSON.stringify(event));
  });
}
sendMoves();
export default {};
</script>

<style lang="scss" scoped></style>
