#include <unordered_set>
#include <utility>	// pair
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

vector<pair<int, int>> bfs(int y, int x, vector<vector<int>> & matrix, unordered_set<pair<int, int>, pair_hash> & visited, int max_y, int max_x) {
	int current_code = matrix[y][x];
	vector<pair<int, int>> current_country;
	
	queue<pair<int, int>> my_queue({make_pair(y, x)});

	while (!my_queue.empty()) {
		auto cur_cell = my_queue.front();
		int cur_x = cur_cell.second;
		int cur_y = cur_cell.first;

		my_queue.pop();
		int country_code = matrix[cur_cell.first][cur_cell.second];

		if (country_code != current_code || visited.find(cur_cell) != visited.end()) 
			continue;

		current_country.push_back(cur_cell);
		visited.insert(cur_cell);

		if (cur_y == 0)
			my_queue.push(make_pair(cur_y + 1, cur_x));
		else if (cur_y == max_y - 1)
			my_queue.push(make_pair(cur_y - 1, cur_x));
		else if (cur_y > 0 && cur_y < max_y - 1) {
			my_queue.push(make_pair(cur_y + 1, cur_x));
			my_queue.push(make_pair(cur_y - 1, cur_x));
		}

		if (cur_x == 0)
			my_queue.push(make_pair(cur_y, cur_x + 1));
		else if (cur_x == max_x - 1)
			my_queue.push(make_pair(cur_y, cur_x - 1));
		else if (cur_x > 0 && cur_x < max_x - 1) {
			my_queue.push(make_pair(cur_y, cur_x + 1));
			my_queue.push(make_pair(cur_y, cur_x - 1));
		}
	}

	return current_country;
}

void solution(vector<vector<int>>& matrix, int width, int height) {
	if (width < 1 || height < 1) {
		cout << "Matrix should be two-dimensional! \n" << width << " x "<< height<< endl;	
		return;
	}

	unordered_set<pair<int, int>, pair_hash> visited;
	vector<vector<pair<int, int>>> countries;

	int max_y = height;
	int max_x = width;

	for (int y = 0; y < max_y; y++)
		for (int x = 0; x < max_x; x++) {
			auto cur = make_pair(y, x);
			if (visited.find(cur) == visited.end())
				countries.push_back(bfs(y, x, matrix, visited, max_y, max_x));
		}

	cout << "Total distinct countries: " << countries.size() << endl;
	cout << "Cells by country:" << endl;
	for (auto i = countries.begin(); i != countries.end(); ++i) {
		auto res = *i;
		for (auto w = res.begin(); w != res.end(); ++w)
			cout << (*w).first << " " << (*w).second << "; ";
		cout << endl;	
	}
}

int main(int argc, char* argv[]) {
	vector<vector<int>> A = {
		{5, 4, 4},
		{4, 3, 4},
		{3, 2, 4},
		{2, 2, 2},
		{3, 3, 4},
		{1, 4, 4},
		{4, 1, 1}
	};

	solution(A, 3, 7);

	return 0;
}
