import mongoose from 'mongoose';

export default callback => {
    mongoose.connect('mongodb://localhost/life-api',
        (error) => {
            if (error) { console.error(error); }
        });

    // Use ES6 Promises, Mongoose internal promise is depreciated.
    // http://mongoosejs.com/docs/promises.html
    mongoose.Promise = Promise;

    callback();
};
