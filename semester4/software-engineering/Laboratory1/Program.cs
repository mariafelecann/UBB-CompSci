/*
     Given two strings, one representing the letters available in a magazine and another 
    representing a ransom note, write a program to determine if the ransom note can be 
    constructed from the magazine letters. The program should ignore case and 
    punctuation
*/


namespace Laboratory1
{
    internal class Program
    {
        public static bool CheckRansomNote(string magazine, string ransom_note)
        {
            Dictionary<char, int> magazine_letters_frequency = new Dictionary<char, int>();
            string punctuation = ".,!?',:;{}";
            
            foreach (char letter in magazine)
            {
                if (!punctuation.Contains(letter))
                {
                    if (magazine_letters_frequency.ContainsKey(letter))
                        magazine_letters_frequency[letter]++;
                    else
                        magazine_letters_frequency[letter] = 1;
                }
            }
            foreach (char letter in ransom_note)
            {
                if (!punctuation.Contains(letter))
                {
                    if (!magazine_letters_frequency.ContainsKey(letter) || magazine_letters_frequency[letter] == 0)
                        return false;
                    else
                        magazine_letters_frequency[letter]--;
                }
            }

            return true;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("please enter the magazine text: ");
            string magazine = Console.ReadLine();
            Console.WriteLine("please enter the ransom note text: ");
            string ransom_note = Console.ReadLine();
            magazine = magazine.ToLower();
            ransom_note.ToLower();
            bool result = CheckRansomNote(magazine, ransom_note);
            if (result)
            {
                Console.WriteLine("the ransom note can be constructed from the magazine letters");
            }
            else
            {
                Console.WriteLine(" the ransom note can't be constructed from the magazine letters");
            }          
        }
    }
}
