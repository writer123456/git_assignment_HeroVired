# git_assignment_HeroVired 
commands executed  
Clone the repo using command 
-git clone https://github.com/writer123456/git_assignment_HeroVired.git  
Create and check-out branch dev 
-git checkout -b dev 
Create a new file CalculatorPlus.py in this branch, add the given code and save.
stage the changes, commit and pushed the code using command 
-git commit -m “<comment>”
-git push
Click on create pull request->merge pull request->confirm merge to merge dev to main.
Click on Create a new release ->Typed comment->set version as v1.0.0->clicked on Generate release notes->clicked on Publish Release
Go back to main branch and did a git pull using following  commands
-git switch main
-git pull
Create a branch feature/sqrt from main branch ,uncomment the square root code , save, stage and commit
-git checkout -b feature/sqrt 
-git commit -m “<comment>”
-git push
Switch to main and later to dev to fix a bug
-git switch main
-git switch dev
-git pull
Add the following code in divide function
if b == 0:
raise ValueError("Cannot divide by zero.")
return a / b
-Stage,commit and pushed 
-Create a pull request for feature/sqrt  with dev, add a reviewer and once approved click on
->merge pull request->confirm merge to merge feature/sqrt to dev.
Create a pull request for dev  with main, added a reviewer and once approved clicked on
->merge pull request->confirm merge to merge dev to main.
Click on Create a new release ->Typed comment->set version as v2.0.0->clicked on Generate release notes->clicked on Publish Release
--------------------------------------------------------------------------

2)Download and install Git-lfs from Git-lfs.com
Run the following command in the command prompt
git lfs install Git LFS initialized
-git switch main
-git pull
-git checkout -b lfs
Add a file with size more than 200mb in the folder	
-git lfs track ‘*.zip’
-git add ‘*.zip’
-git commit -m “added zip file”
-git push --set-upstream origin lfs


------------------------------------------

3) -git switch main
   -git pull
-git checkout -b feature/circle area
Add new file
Add following code and save as GeometryCalculator.py and uncomment the circle area related code
import math
class GeometryCalculator:
def calculate_circle_area(self, radius):
return math.pi * radius ** 2
def calculate_rectangle_area(self, length, width):
return length * width
if __name__ == "__main__":
calculator = GeometryCalculator()
# TODO: Implement the feature to calculate the area of a circle
# radius = 5
# print(f"The area of the circle with radius {radius} =
{calculator.calculate_circle_area(radius)}")
# TODO: Implement the feature to calculate the area of a rectangle # length = 10
# width = 6
# print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")

-git add .
-git stash
-git switch main
-git pull
-git checkout -b feature/rectangle-area
-git stash apply
 uncomment the rectangle area related code and comment circle related code
run the code to check for errors
-git add .
-git stash
-git switch main
-git pull
-git switch feature/circle-area
-git  stash apply
Complete the circle area code
fix errors
-git add .
-git commit -m “added circle area”
-git push --set-upstream origin feature/circle-area
-git switch main
-git switch feature/rectangle-area
-git stash apply
Continue to work on rectangle area
-git add .
-git commit -m “added rectangle area”
- git push --set-upstream origin feature/rectangle-area
Create a pull-request on dev from feature/circle-area 
merge pull request->confirm merge to merge feature/circle-area to dev
Create a pull-request on dev from feature/rectangle-area 
Resolve conflicts and merge to dev branch.
Create a pull request from dev branch to main and merge





