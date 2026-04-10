import logging
def get_logger():
    # Set up a default logging system quickly.
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s -%(levelname)s- %(message)s"
    )
    return logging.getLogger()

