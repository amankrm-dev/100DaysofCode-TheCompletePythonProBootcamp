### Chose your difficulty
- **Normal** 😎: Use all Hints below to complete the project.
- **Hard** 🤔: Use only Hints 1, 2, 3 to complete the project.
- **Extra Hard** 😭: Only use Hints 1 & 2 to complete the project.
- **Expert** 🤯: Only use Hint 1 to complete the project.

### Our Blackjack Game House Rules

- The deck is unlimited in size. 
- There are no jokers. 
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.


<div class="hint" title="Hint 1">
  Go to this website and try out the Blackjack game: 

https://games.washingtonpost.com/games/blackjack/

Then try out the completed Blackjack project here: 

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hint 2">
Read this breakdown of program requirements: 

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Then try to create your own flowchart for the program.

</div>

<div class="hint" title="Hint 3">
  Download and read this flow chart I've created:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

</div>


<div class="hint" title="Hint 4">
  Create a <code>deal_card()</code> function that uses the List below to return a random card.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Remember that 11 is the Ace.
</div>

<div class="hint" title="Hint 5">
  Deal the user and computer 2 cards each using <code>deal_card()</code> and <code>append()</code>.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hint 6">
  Create a function called <code>calculate_score()</code> that takes a List of cards as input 
and returns the sum of all the cards in the List as the score. 
Google the <code>sum()</code> function to help you do this.
</div>


<div class="hint" title="Hint 7">
Inside <code>calculate_score()</code> check for a blackjack (a hand with only 2 cards: ace + 10) and return <code>0</code> instead of the actual score. <code>0</code> will represent a blackjack in our game.
</div>


<div class="hint" title="Hint 8">
  Inside <code>calculate_score()</code> check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to Google to find the documentation on the Python built-in functions <code>append()</code> and <code>remove()</code>.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hint 9">
  Call the function<code>calculate_score()</code>. If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
</div>

<div class="hint" title="Hint 10">
  If the game has not ended, ask the user if they want to draw another card. If yes, then use the <code>deal_card()</code> function to add another card to the <code>user_cards</code> List. If no, then the game has ended.
</div>

<div class="hint" title="Hint 11">
  The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
</div>

<div class="hint" title="Hint 12">
  Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
</div>

<div class="hint" title="Hint 13">
  Create a function called <code>compare()</code> and pass in the <code>user_score</code> and <code>computer_score</code>. 

- If the computer and user both have the same score, then it's a draw.
- If the computer has a blackjack (0), then the user loses. 
- If the user has a blackjack (0), then the user wins. 
- If the <code>user_score</code> is over 21, then the user loses. 
- If the <code>computer_score</code> is over 21, then the computer loses. 
- If none of the above, then the player with the highest score wins.
</div>

<div class="hint" title="Hint 14">
  Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
</div>



