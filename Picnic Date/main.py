class Picnic:
    def __init__(self, picnic_date, picnic_time):
        self.picnic_date = picnic_date
        self.picnic_time = picnic_time

    def askVivi(self):
        print(f"Our picnic is scheduled to {self.picnic_date} at {self.picnic_time}")


first_picnic = Picnic("Saturday", "17:30")
first_picnic.askVivi()