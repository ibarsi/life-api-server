import { Router } from 'express';

import Drink from '../models/drink';
import logger from '../helpers/logger_helper';
import { version } from '../../../package.json';

export default () => {
    let router = Router();

    router.use((request, response, next) => {
        logger.info('Something is happening.');

        next();
    });

    router.get('/', (request, response) => {
        response.json({ version });
    });

    router.route('/drinks')
        .get((request, response) => {
            Drink.find((error, drinks) => {
                if (error) { response.send(error); }

                response.json(drinks);
            });
        })
        .post((request, response) => {
            let drink = new Drink();

            drink.save(error => {
                if (error) { response.send(error); }

                response.json({ message: 'Drink created!' });
            });
        })
        .delete((request, response) => {
            Drink.findOneAndRemove({},
            {
                sort: {
                    date_consumed: -1
                }
            },
            error => {
                if (error) { response.send(error); }

                response.json({ message: 'Drink removed!' });
            });
        });

    return router;
};
