# Veridion Words of Power Challenge

## **Overview**
**Words of Power** is a strategic, text-based game where each word acts as a weapon. The player must choose wisely, balancing cost and power to outsmart the system and defeat the opposing words. The game spans 10 rounds, and the goal is to spend the least amount of money while winning as many rounds as possible.

## **🚀 Game Challenge**
1. **Round Mechanics**: Each round, the system generates a word, and the player must select a word from a predefined list that "beats" the system's word.
2. **Word Costs**: Every word selected has a cost, and more powerful words are more expensive.
3. **Outcome of Each Round**:
   - Win: The player spends only the cost of the word.
   - Loss: The player spends the word’s cost plus a penalty.
4. **Total Cost**: The player’s total cost is tracked, and after 10 rounds, the player with the lowest final cost wins.

## **🔍 How the Game Works**
1. **System Word**: The system selects a word randomly from a secret list (e.g., *Tornado*, *Hammer*).
2. **Player Word**: The player selects a word from a predefined list of 77 words (each associated with a cost) that beats the system's word.
3. **Round Outcome**:
   - **Win**: Only the word’s cost is deducted.
   - **Loss**: The word’s cost plus a $75 penalty fee is deducted.
4. **Discounts and Bonuses**: Players are rewarded with discounts for winning rounds and saving money on word selections.

## **📜 Rules**
- **System Words**: Secret list of words chosen randomly each round.
- **Player Words**: Fixed list of 77 words with associated costs.
- **Winning/Losing**: A word must logically "beat" the system word to win. Losing results in a penalty.
- **Scoring**: After 10 rounds, the total cost is calculated considering wins, losses, discounts, and smart-play bonuses.

## **🎮 Example Game Playthrough**
| **Round** | **System Word** | **Player's Word** | **Word Cost ($)** | **Outcome** | **Total Cost ($)** |
| --- | --- | --- | --- | --- | --- |
| 1 | Candle | Fire | 22 | ✅ Wins | 22 |
| 2 | Hammer | Rock | 38 | ❌ Loses + $75 Penalty | 97 |
| 3 | Blueberries | Grizzly | 30 | ✅ Wins | 127 |
| 4 | Flood | Dam | 35 | ✅ Wins | 162 |
| 5 | Tank | H-bomb | 75 | ✅ Wins | 237 |

## **💡 Strategy Tips**
- **Cheap words** save money but may fail against stronger system words.
- **Powerful words** are more expensive but are essential for some rounds.
- **Efficiency is key**: Winning cheap is just as important as winning often.
- **Abstract words** (e.g., *Persistence*, *Innovation*) can outsmart stronger physical concepts.

## **✨ Advanced Strategies**
- **Conservative Players**: Focus on efficiency and frugality.
- **Bullish Players**: Take risks and dominate with powerful words.
- **YOLO Players**: Embrace fun and experiment with wild strategies.

## **🛠️ Requirements**
- **GET request** to retrieve the system's word each round.
- **Word selection logic** to choose the appropriate word that beats the system’s word.
- **POST request** with the ID of the chosen word to register the selection.

## **📖 Reference: Player Word List & Costs**
Below is the full list of available player words along with their associated costs. This reference is essential for making strategic decisions.

### **💰 Player Word List & Costs**

| **Word** | **Cost ($)** |
| --- | --- |
| Fire | 22 |
| Water | 30 |
| Rock | 38 |
| H-bomb | 75 |
| ... | ... |

### **⚠️ Penalties**
If the player’s word **does not beat** the system word, a **flat $75 penalty** is added to the word's cost.

## **🎯 Key Strategies for Winning**
- Balance between **cheap words** and **powerful words**.
- Use powerful words strategically to avoid overspending.
- Take advantage of **discounts and smart-play bonuses**.

## **📝 Final Score Formula**
```python
Final Cost = ((Total Spent + 75 * Rounds Lost)  × (1 - (5% × Rounds Won))) - (Sum of Cheaper Win Refunds)
```

