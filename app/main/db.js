import mongoose from 'mongoose';

import config from '../config.json';
import logger from './helpers/logger_helper';

export default callback => {
    mongoose.connect(config.database,
        (error) => {
            if (error) { logger.error(error); }
        });

    // Use ES6 Promises, Mongoose internal promise is depreciated.
    // http://mongoosejs.com/docs/promises.html
    mongoose.Promise = Promise;

    callback();
};
