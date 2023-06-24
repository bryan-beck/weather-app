const express = require('express')

const app = express();
app.use(express.json());


const port = process.env.PORT || 4545;

app.listen(port, () => {
    console.log(`serving up on ${port}`);
});