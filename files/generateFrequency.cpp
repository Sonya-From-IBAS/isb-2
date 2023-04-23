#include <iostream>
#include<ctime>

int main()
{
	srand(time(NULL));
	int val = std::rand() % 32149;
	int lenth = 128;
	bool binaryVal;
	for (int i = 0; i < lenth; i++) {
		val = (val * 222 + 4) % 32149;
		binaryVal = val % 2;
		std::cout << binaryVal;
	}
	return 0;
}

//01001000001011001110100110111001011000101110001101011100001101111101101010100011100111110111100101110110111010111000001100010001