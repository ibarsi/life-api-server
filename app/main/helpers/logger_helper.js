import winston from 'winston';

const winston_logger = new winston.Logger({
    transports: [
      new winston.transports.File({ filename: '/var/log/life-api.log' })
    ]
  });

const logger = {
    info(message) {
        if (process.env.NODE_ENV === 'DEV') {
            console.log(message);
        }
        else {
            winston_logger.info(message);
        }
    },

    error(message) {
        if (process.env.NODE_ENV === 'DEV') {
            console.error(message);
        }
        else {
            winston_logger.error(message);
        }
    }
};

export default logger;
