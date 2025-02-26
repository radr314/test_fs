# from airflow import DAG
# from airflow.operators.dummy import DummyOperator
# from airflow.utils.dates import days_ago

# # Define the DAG
# dag = DAG(
#     'simple_dag',
#     schedule_interval='@daily',  # Runs daily
#     start_date=days_ago(1),
#     catchup=False
# )

# # Define tasks
# start = DummyOperator(task_id='start', dag=dag)
# end = DummyOperator(task_id='end', dag=dag)

# # Define task dependencies
# start >> end


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound."

    def __repr__(self):
        print("Grandparent is called")
        return f"Animal.name: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the parent class's __init__ method
        self.breed = breed

    def make_sound(self):
        print(super(Animal,Puppy('caesar')).__repr__() )
        return f"{self.name}, a {self.breed}, barks."

    def __repr__(self):
        return f"Dog.name: {self.name}, Dog.breed: {self.breed}"


class Puppy(Dog):
    def __init__(self,name):
        super().__init__(name,"small dog")

    def how_cute(self):
        print(super(Dog,self).__repr__() )
        return f"{self.name} is very cute!"

    def test_super(self):
        return super().__new__(self)

    def __repr__(self):
        return f"Puppy.name: {self.name}, Puppy.breed: {self.breed}"
    

# Example usage
caesar = Puppy("Buddy")
freda= Dog("Freda", "Golden Retriever")
print(caesar.make_sound())  # Output: Buddy, a small dog, barks.
print(caesar.how_cute())  # Output: Buddy, a Golden Retriever, barks.



        
