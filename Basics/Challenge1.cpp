#include <iostream>
#include <string>
#include <cassert>
#include <cstdint>

std::string b64_Chars = {"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"};

std::string b64Decode(std::string enc){
  char buffer;
  /*
   * Need to iterate through each char and take
   * its index repr. in the b64_Chars string 
   * and then rebuild the original decoded text
   */
  std::size_t idx = b64_Chars.find(enc[0],0); 
  std::cout << "found: " << idx << std::endl;
  return "";
}

int main(int argc, char * argv[]){
  std::string b64{"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"};
  assert((b64.length() % 4 == 0) && "Error: Implementation requires string length to be a multiple of four.");
  std::cout << "Base64 encoded: " << b64 << std::endl;
  std::cout << "Base64 decoded: " << b64Decode(b64) << std::endl;
  return EXIT_SUCCESS;
}


