#include "word.h"

Word::Word(std::string the_word) :
    _the_word(the_word)
{
    // TODO Auto-generated constructor stub
}

Word::~Word() {
    // TODO Auto-generated destructor stub
	std::cout << "destructor" << std::endl;
}

void Word::updateWord(std::string word)
{
    this->_the_word = word;
}

std::string Word::getWord()
{
    return this->_the_word;
}
