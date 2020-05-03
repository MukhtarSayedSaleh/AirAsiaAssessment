const app = require('express')();

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

const PORT = 4200;
app.listen(PORT, () => console.log(`Frontend server is listing to port ${PORT}`));