import logging

# Configure logger
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('anti_ddos_logger')

# Example usage
logger.info('Logger is configured and ready to use.')