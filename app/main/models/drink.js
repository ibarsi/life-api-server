import mongoose from 'mongoose';

let DrinkSchema = new mongoose.Schema({
    date_consumed: { type: Date, default: Date.now }
});

export default mongoose.model('Drink', DrinkSchema);
