

class Found:
    def __init__(self, yt, time, caption):
        self.yt = yt
        self.time = time
        self.caption = caption

    def __str__(self):
        return '<Found_obj>'

    def __repr__(self):
        content = "|".join([
            'yt=' + str(self.yt),
            'time=' + str(self.time),
            'caption=' + str(self.caption),
        ])

        return f'<Found ( {content} ) >'

