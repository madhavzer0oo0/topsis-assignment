Topsis Assignment

Name:Madhav Dembla
ROLLNO:102303609

Input File Description

The input file must be an Excel file (.xlsx)

First column: Alternatives (names or IDs)

Remaining columns: Numerical criteria

Minimum 3 columns are required
<img width="471" height="320" alt="image" src="https://github.com/user-attachments/assets/98e61c23-fdfe-4071-a592-92b5e1fea7e7" />

Result Table (output.csv)

The output file contains:

Original alternatives

TOPSIS Score

Rank
<img width="1033" height="264" alt="image" src="https://github.com/user-attachments/assets/18ef4819-468b-46e9-b3ff-6eb32343a2dc" />

## 🧠 Methodology

The methodology implemented in this assignment is based on the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** approach, a well-known multi-criteria decision-making technique. TOPSIS ranks alternatives by comparing their distances from an ideal best solution and an ideal worst solution.

---

### Step 1: Data Input and Validation
- The input is provided as an Excel (`.xlsx`) file.
- The first column contains the alternatives.
- The remaining columns contain numerical criteria values.
- The program validates:
  - Existence of the input file
  - Presence of numeric values
  - Correct number of weights and impacts
  - Valid impact symbols (`+` or `-`)

---

### Step 2: Construction of Decision Matrix
- A decision matrix is formed using the numerical criteria.
- Rows represent alternatives and columns represent criteria.

### Step 3: Normalization of the Decision Matrix
- Since criteria may have different units, vector normalization is applied to bring all values to a common scale.

### Step 4: Weight Application
- User-defined weights are assigned to each criterion.
- The normalized matrix is multiplied by the corresponding weights to obtain the weighted normalized decision matrix.
### Step 5: Identification of Ideal Best and Ideal Worst
- Based on the impact of each criterion:
  - `'+'` indicates benefit criteria (higher is better)
  - `'-'` indicates cost criteria (lower is better)
- Ideal best (V⁺) and ideal worst (V⁻) values are identified accordingly.
### Step 6: Calculation of Separation Measures
- The Euclidean distance of each alternative from:
  - the ideal best solution (S⁺)
  - the ideal worst solution (S⁻)
- These distances indicate how close each alternative is to the optimal solution.

### Step 7: Computation of TOPSIS Score
- The score ranges between 0 and 1.
- A higher score indicates a better alternative.
### Step 8: Ranking of Alternatives
- Alternatives are ranked in descending order of their TOPSIS scores.
- Rank 1 represents the best-performing alternative.
### Step 9: Result Generation
- The final output is saved as a CSV file (`output.csv`).
- The file contains the TOPSIS score and rank for each alternative, enabling easy comparison and interpretation of results.


pypi link: https://pypi.org/project/topsis-madhavdembla-102303609/1.0.0/

output of pip install topsis-madhavdembla-102303609==1.0.0
<img width="1323" height="269" alt="image" src="https://github.com/user-attachments/assets/f7050331-3eb2-402d-9f7f-7edbe96e69f6" />
