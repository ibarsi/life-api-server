import http from 'http';
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';

import db from './db';
import api from './api';
import config from '../config.json';

let app = express();
app.server = http.createServer(app);

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json({
    limit: config.bodyLimit
}));

app.use(cors({
    exposedHeaders: config.corsHeaders
}));

db(() => {
    app.use('/api', api());

    app.server.listen(process.env.PORT || 8080);

    console.log(`Started on port ${app.server.address().port}`);
});

export default app;
