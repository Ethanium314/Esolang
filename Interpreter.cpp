#include <iostream>
#include <fstream>
#include <vector>
#include <string>
//
using namespace std;
//

//See read me for a list of functions

//Create the pointer object
class Pointer
{
	public:
		int value = 0;
		int vector[2] = {0, 0};
		int x = 0;
		int y = 0;
};
//
int main(int argc, char** argv) {

	string argument = argv[1];

	//Create a list of pointers and add a pointer to it
	vector<Pointer> pointers;
	pointers.push_back(Pointer());
	pointers[0].vector[0] = 1;
	
	//Create the grid
	char grid[300][300];
	for (int i = 0; i < 300; i++)
	{
		for (int j = 0; j < 300; j++)
		{
			grid[i][j] = ' ';
		}
	}

	ifstream file{argument};
	char testline;
	int x=0,y=0;
    while(testline = file.get())
    {
        if (testline == '\n')
        {
        	y++;
        	x = 0;
        	testline = file.get();
        }
        if (file.eof())
        {
        	break;
        }
		grid[x][y] = testline;
		x++;
	}
	file.close();
	
	//Main loop
	while (1)
	{
		for (int i = 0; i < pointers.size(); i++)
		{
			//Check current position for character and execute function
  			switch(grid[pointers[i].x][pointers[i].y])
  			{
  				case '>':
  					pointers[i].vector[0]++;
  					break;
  					
  				case '<':
  					pointers[i].vector[0]--;
  					break;
  					
  				case 'v':
  					pointers[i].vector[1]++;
  					break;
  					
  				case '^':
  					pointers[i].vector[1]--;
  					break;
  				
  				case '!':
  					cout << "\nPointer " << i+1 << " has been terminated\n";
  					pointers.erase(pointers.begin()+i);
  					break;
  					
  				case ';':
  					cout << "Bye bye\n";
  					return 0;
  					
  				case '+':
  					pointers[i].value++;
  					if (pointers[i].value >= 256)
  					{
  						pointers[i].value = 0;
  					}
  					break;
  					
  				case '-':
  					pointers[i].value--;
  					if (pointers[i].value <= -1)
  					{
  						pointers[i].value = 256;
  					}
  					break;
  				
  				case ':':
  					cout << char(pointers[i].value);
  					break;
  				
  				case '$':
  					cout << pointers[i].value;
  					break;
  					
  				case '|':
  					pointers[i].vector[0] *= -1;
  					break;
  					
  				case '_':
  					pointers[i].vector[1] *= -1;
  					break;
  				
  				case '*':
  					pointers[i].value = grid[pointers[i].x+1][pointers[i].y];
  					if (pointers[i].vector[0] == 1 && pointers[i].vector[1] == 0)
  					{
  						pointers[i].x++;
  					}
  					break;
  				
  				case '&':
  					pointers[i].value += grid[pointers[i].x+1][pointers[i].y];
  					if (pointers[i].vector[0] == 1 && pointers[i].vector[1] == 0)
  					{
  						pointers[i].x++;
  					}
  					break;
  					
  				case '~':
  					pointers[i].value -= grid[pointers[i].x+1][pointers[i].y];
  					if (pointers[i].vector[0] == 1 && pointers[i].vector[1] == 0)
  					{
  						pointers[i].x++;
  					}
  					break;
  					
  				case '(':
  					if (pointers[i].vector[0] < 0)
  					{
  						pointers[i].vector[0] *= -1;
  					}
  					break;
  					
  				case ')':
  					if (pointers[i].vector[0] > 0)
  					{
  						pointers[i].vector[0] *= -1;
  					}
  					break;
  					
  				case '?':
  					if (pointers[i].value < grid[pointers[i].x+1][pointers[i].y])
  					{
  						int temp = pointers[i].vector[0];
						pointers[i].vector[0] = pointers[i].vector[1];
						pointers[i].vector[1] = temp;
						pointers[i].vector[1] *= -1;
  					}
  					else if (pointers[i].value > grid[pointers[i].x+1][pointers[i].y])
  					{
  						int temp = pointers[i].vector[0];
						pointers[i].vector[0] = pointers[i].vector[1];
						pointers[i].vector[1] = temp;
						pointers[i].vector[0] *= -1;
  					}
  					break;
  			}
  			
  			//Move the pointer by the amount specified by its vector
  			pointers[i].x += pointers[i].vector[0];
  			pointers[i].y += pointers[i].vector[1];
  			
  			//cout << pointers[i].x << ", " << pointers[i].y << "; " << pointers[i].vector[0] << ", " << pointers[i].vector[1] << "\n";
  			
  			//Check if there are no pointers left
  			if (pointers.size() == 0)
  			{
  				cout << "\nAnd then there were none\n";
  				return 0;
  			}
  			
  			//Check to see of the pointer has left the grid
  			if (pointers[i].x > 200 || pointers[i].y > 200)
  			{
  				cout << "\nPointer " << i+1 << " has gone out of bounds\n";
  				return 0;
  			}
  		}
	}
}
