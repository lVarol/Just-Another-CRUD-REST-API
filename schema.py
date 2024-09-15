

instructions = [

        'DROP TABLE IF EXISTS Todos;',

    """
        CREATE TABLE Todos (
            id INT PRIMARY KEY AUTO_INCREMENT,
            todo TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """

]