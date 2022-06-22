class player:

    team_name="arsenal"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):

        print(f"  name= {self.name} age= {self.age}, and team is {player.team_name} " )



    @classmethod
    def change(cls,name):
        player.team_name=name



new=player("messi",35)
new.show()

new.change("man utd")
new.show()





