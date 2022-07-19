class ICommand:
    """Interface command."""

    def execute(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

    @staticmethod
    def name():
        raise NotImplementedError()
