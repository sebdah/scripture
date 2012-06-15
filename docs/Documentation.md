# Scripture documentation

## Formatting

The following tags are implemented in Scripture formatting system.

    DATETIME_UTC        Returns the ISO formatted date time
    FACILITY            The facility of the log message
    MESSAGE             The actual message
    SEVERITY            The severity of the message (in uppercase)

A tag should be inserted to the configuration surrounded with `{{}}`. E.g.

    {{DATETIME_UTC}} - {{SEVERITY}} - {{MESSAGE}}

## Handlers

A handler is a backend for writing logs to a specific place. It could be a S3 handler, a file handler or something else.

Currently supported handlers are defined below.

### file_handler

Configuration:

    path                Local path to the log folder
    filename            Filename of the output file