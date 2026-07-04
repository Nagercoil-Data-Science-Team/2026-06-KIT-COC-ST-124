import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import ylim

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 18
plt.rcParams['font.weight'] = 'bold'
# Material dataset
data = {
    "Material": [
        "Stainless Steel",
        "Aluminum",
        "Glass",
        "Tritan Plastic",
        "Bamboo Composite"
    ],

    "Tensile Strength (MPa)": [515, 310, 45, 70, 180],
    "Durability": [95, 85, 55, 75, 70],
    "Thermal Conductivity": [16.0, 237.0, 1.05, 0.20, 0.17],
    "CCI": [90, 88, 95, 87, 82],
    "Surface Roughness": [0.25, 0.35, 0.10, 0.40, 0.60],
    "Glossiness": [85, 80, 95, 75, 65],
    "Carbon Footprint": [2.7, 8.2, 1.5, 3.0, 0.8],
    "Recyclability": [90, 95, 80, 35, 70],
    "Embodied Energy": [39, 170, 15, 90, 12]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("material_properties.xlsx", index=False)

# Display dataset
print(df)

print("\nmaterial_properties.xlsx created successfully!")

# =====================================================
# PHASE 2 : AHP WEIGHT CALCULATION
# =====================================================

import numpy as np
import matplotlib.pyplot as plt

print("\n" + "="*60)
print("PHASE 2 : AHP WEIGHT CALCULATION")
print("="*60)

criteria = [
    "Functionality",
    "Aesthetics",
    "Environment"
]

# Pairwise Comparison Matrix
pairwise_matrix = np.array([
    [1,   3,   2],
    [1/3, 1,   1/2],
    [1/2, 2,   1]
])

print("\nPairwise Comparison Matrix")
print(pd.DataFrame(pairwise_matrix,
                   index=criteria,
                   columns=criteria))

# =====================================================
# NORMALIZATION
# =====================================================

column_sum = pairwise_matrix.sum(axis=0)

normalized_matrix = pairwise_matrix / column_sum

print("\nNormalized Matrix")
print(pd.DataFrame(normalized_matrix,
                   index=criteria,
                   columns=criteria))

# =====================================================
# WEIGHT CALCULATION
# =====================================================

weights = normalized_matrix.mean(axis=1)

weight_df = pd.DataFrame({
    "Criteria": criteria,
    "Weight": weights
})

print("\nAHP Weight Calculation")
print(weight_df)

# =====================================================
# CONSISTENCY CHECK
# =====================================================

weighted_sum = np.dot(pairwise_matrix, weights)

consistency_vector = weighted_sum / weights

lambda_max = np.mean(consistency_vector)

n = len(criteria)

CI = (lambda_max - n) / (n - 1)

RI = 0.58

CR = CI / RI

print("\nConsistency Analysis")
print("-"*40)
print("Lambda Max :", round(lambda_max, 4))
print("CI         :", round(CI, 4))
print("CR         :", round(CR, 4))

if CR < 0.1:
    print("\nResult : Consistent Matrix (CR < 0.1)")
else:
    print("\nResult : Inconsistent Matrix (CR > 0.1)")

# =====================================================
# FUNCTIONALITY WEIGHT PLOT
# =====================================================

plt.figure(figsize=(6,5))
plt.bar(["Functionality"], [weights[0]])
plt.title("AHP Weight - Functionality")
plt.ylabel("Weight")
plt.grid(True)
plt.show()

# =====================================================
# AESTHETICS WEIGHT PLOT
# =====================================================

plt.figure(figsize=(6,5))
plt.bar(["Aesthetics"], [weights[1]])
plt.title("AHP Weight - Aesthetics")
plt.ylabel("Weight")
plt.grid(True)
plt.show()

# =====================================================
# ENVIRONMENT WEIGHT PLOT
# =====================================================

plt.figure(figsize=(6,5))
plt.bar(["Environment"], [weights[2]])
plt.title("AHP Weight - Environment")
plt.ylabel("Weight")
plt.grid(True)
plt.show()

# =====================================================
# OVERALL AHP WEIGHTS
# =====================================================

plt.figure(figsize=(8,6))
plt.bar(criteria, weights,color='#2B5748')

for i, v in enumerate(weights):
    plt.text(i, v+0.01, f"{v:.3f}", ha='center')

plt.title("AHP Criteria Weights",fontweight='bold')
plt.xlabel("Criteria",fontweight='bold')
plt.ylabel("Weight",fontweight='bold')
plt.ylim([0,0.85])
plt.savefig('AHP_Weight_Calculation.png',dpi=800)
plt.show()

# =====================================================
# SAVE RESULTS
# =====================================================

weight_df.to_excel(
    "AHP_Weight_Calculation.xlsx",
    index=False
)

print("\nAHP_Weight_Calculation.xlsx saved successfully")

# =====================================================
# PHASE 3 : LIFE CYCLE ASSESSMENT (LCA)
# =====================================================

import matplotlib.pyplot as plt
import pandas as pd

print("\n" + "="*70)
print("PHASE 3 : LIFE CYCLE ASSESSMENT (LCA)")
print("="*70)

# -----------------------------------------------------
# LCA STAGE 1 : RAW MATERIAL EXTRACTION
# -----------------------------------------------------

raw_material_emission = df["Carbon Footprint"]

print("\nRAW MATERIAL STAGE")
print("-"*50)

for material, value in zip(df["Material"], raw_material_emission):
    print(f"{material:20s} : {value:.2f} kg CO2/kg")

# -----------------------------------------------------
# LCA STAGE 2 : MANUFACTURING
# -----------------------------------------------------

manufacturing_energy = df["Embodied Energy"]

print("\nMANUFACTURING STAGE")
print("-"*50)

for material, value in zip(df["Material"], manufacturing_energy):
    print(f"{material:20s} : {value:.2f} MJ/kg")

# -----------------------------------------------------
# LCA STAGE 3 : USAGE STAGE
# -----------------------------------------------------

usage_impact = df["Durability"]

print("\nUSAGE STAGE (Lifetime Performance)")
print("-"*50)

for material, value in zip(df["Material"], usage_impact):
    print(f"{material:20s} : {value:.2f}")

# -----------------------------------------------------
# LCA STAGE 4 : END OF LIFE
# -----------------------------------------------------

recycling_benefit = df["Recyclability"]

print("\nEND-OF-LIFE STAGE")
print("-"*50)

for material, value in zip(df["Material"], recycling_benefit):
    print(f"{material:20s} : {value:.2f}%")

# =====================================================
# CREATE LCA TABLE
# =====================================================

lca_results = pd.DataFrame({
    "Material": df["Material"],
    "Carbon Footprint": raw_material_emission,
    "Energy Consumption": manufacturing_energy,
    "Lifetime Impact": usage_impact,
    "Recycling Benefit": recycling_benefit
})

print("\n" + "="*70)
print("LCA RESULTS TABLE")
print("="*70)
print(lca_results)

# Save Excel
lca_results.to_excel(
    "LCA_Results.xlsx",
    index=False
)

print("\nLCA_Results.xlsx saved successfully")

# =====================================================
# FIGURE 1
# RAW MATERIAL STAGE
# =====================================================

plt.figure(figsize=(8,6))

plt.bar(df["Material"], raw_material_emission,color='#4B5694')

plt.title("Raw Material Stage - Carbon Footprint",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("kg CO2/kg",fontweight='bold')

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig('Raw material stage_Results.png',dpi=800)
plt.show()

# =====================================================
# FIGURE 2
# MANUFACTURING STAGE
# =====================================================

plt.figure(figsize=(8,6))

plt.bar(df["Material"], manufacturing_energy,color='#412D15')

plt.title("Manufacturing Stage - Energy Consumption",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("MJ/kg",fontweight='bold')

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig('Manufacturing stage_Results.png',dpi=800)
plt.show()

# =====================================================
# FIGURE 3
# USAGE STAGE
# =====================================================

plt.figure(figsize=(8,6))

plt.bar(df["Material"], usage_impact,color='#232F72')

plt.title("Usage Stage - Lifetime Impact",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Durability Score",fontweight='bold')

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig('Usage Stage_Results.png',dpi=800)
plt.show()

# =====================================================
# FIGURE 4
# END OF LIFE
# =====================================================

plt.figure(figsize=(8,6))

plt.bar(df["Material"], recycling_benefit,color='#744577')

plt.title("End-of-Life Stage - Recycling Benefit",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Recyclability (%)",fontweight='bold')

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig('Recycling_Benefit_Stage_Results.png',dpi=800)
plt.show()

# =====================================================
# FIGURE 5
# OVERALL LCA COMPARISON
# =====================================================

plt.figure(figsize=(12,7))

plt.plot(df["Material"],
         raw_material_emission,
         marker='o',
         linewidth=2,
         label='Carbon Footprint')

plt.plot(df["Material"],
         manufacturing_energy,
         marker='s',
         linewidth=2,
         label='Energy Consumption')

plt.plot(df["Material"],
         usage_impact,
         marker='^',
         linewidth=2,
         label='Lifetime Impact')

plt.plot(df["Material"],
         recycling_benefit,
         marker='d',
         linewidth=2,
         label='Recycling Benefit')

plt.title("Life Cycle Assessment Comparison")
plt.xlabel("Material",fontweight='bold')
plt.ylabel('cycles',fontweight='bold')
plt.xticks(rotation=20)
plt.legend()

plt.tight_layout()
plt.savefig('life cycle assessment comparison.png',dpi=800)
plt.show()

print("\nPHASE 3 LCA COMPLETED SUCCESSFULLY")

# =====================================================
# PHASE 4 : TOPSIS RANKING
# =====================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n" + "="*70)
print("PHASE 4 : TOPSIS RANKING")
print("="*70)

# =====================================================
# TOPSIS FUNCTION
# =====================================================

def topsis_ranking(data, benefit_mask, weights):

    X = data.astype(float)

    # ---------------------------
    # Step 1 : Normalize
    # ---------------------------
    norm = X / np.sqrt((X**2).sum(axis=0))

    # ---------------------------
    # Step 2 : Weighted Matrix
    # ---------------------------
    weighted = norm * weights

    # ---------------------------
    # Step 3 : Ideal Solutions
    # ---------------------------
    ideal_best = np.zeros(weighted.shape[1])
    ideal_worst = np.zeros(weighted.shape[1])

    for j in range(weighted.shape[1]):

        if benefit_mask[j]:

            ideal_best[j] = weighted[:,j].max()
            ideal_worst[j] = weighted[:,j].min()

        else:

            ideal_best[j] = weighted[:,j].min()
            ideal_worst[j] = weighted[:,j].max()

    # ---------------------------
    # Step 4 : Distance
    # ---------------------------
    d_plus = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))

    d_minus = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    # ---------------------------
    # Step 5 : Closeness
    # ---------------------------
    score = d_minus / (d_plus + d_minus)

    rank = score.argsort()[::-1] + 1

    return score, rank

# =====================================================
# FUNCTIONAL TOPSIS
# =====================================================

functional_data = df[
    [
        "Tensile Strength (MPa)",
        "Durability",
        "Thermal Conductivity"
    ]
]

functional_weights = np.array([1/3,1/3,1/3])

functional_benefit = [True,True,True]

f_score, f_rank = topsis_ranking(
    functional_data.values,
    functional_benefit,
    functional_weights
)

functional_result = pd.DataFrame({
    "Material": df["Material"],
    "Functional Score": f_score
})

functional_result["Rank"] = \
functional_result["Functional Score"] \
.rank(ascending=False).astype(int)

functional_result = \
functional_result.sort_values(
    by="Functional Score",
    ascending=False
)

print("\nFUNCTIONAL TOPSIS RANKING")
print(functional_result)

# =====================================================
# PLOT 1
# =====================================================

plt.figure(figsize=(8,6))
plt.bar(
    functional_result["Material"],
    functional_result["Functional Score"],color='#452E5A'
)

plt.title("Functional TOPSIS Ranking",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Closeness Score",fontweight='bold')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('Functional ranking.png',dpi=800)
plt.show()

# =====================================================
# AESTHETIC TOPSIS
# =====================================================

aesthetic_data = df[
    [
        "CCI",
        "Surface Roughness",
        "Glossiness"
    ]
]

aesthetic_weights = np.array([1/3,1/3,1/3])

# Roughness = cost criterion

aesthetic_benefit = [True,False,True]

a_score, a_rank = topsis_ranking(
    aesthetic_data.values,
    aesthetic_benefit,
    aesthetic_weights
)

aesthetic_result = pd.DataFrame({
    "Material": df["Material"],
    "Aesthetic Score": a_score
})

aesthetic_result["Rank"] = \
aesthetic_result["Aesthetic Score"] \
.rank(ascending=False).astype(int)

aesthetic_result = \
aesthetic_result.sort_values(
    by="Aesthetic Score",
    ascending=False
)

print("\nAESTHETIC TOPSIS RANKING")
print(aesthetic_result)

# =====================================================
# PLOT 2
# =====================================================

plt.figure(figsize=(8,6))
plt.bar(
    aesthetic_result["Material"],
    aesthetic_result["Aesthetic Score"],color='#605B51'
)

plt.title("Aesthetic TOPSIS Ranking",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Closeness Score",fontweight='bold')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('Aesthetic ranking.png',dpi=800)
plt.show()

# =====================================================
# ENVIRONMENTAL TOPSIS
# =====================================================

environment_data = df[
    [
        "Carbon Footprint",
        "Recyclability",
        "Embodied Energy"
    ]
]

environment_weights = np.array([1/3,1/3,1/3])

# Carbon + Energy = Cost
# Recyclability = Benefit

environment_benefit = [False,True,False]

e_score, e_rank = topsis_ranking(
    environment_data.values,
    environment_benefit,
    environment_weights
)

environment_result = pd.DataFrame({
    "Material": df["Material"],
    "Environmental Score": e_score
})

environment_result["Rank"] = \
environment_result["Environmental Score"] \
.rank(ascending=False).astype(int)

environment_result = \
environment_result.sort_values(
    by="Environmental Score",
    ascending=False
)

print("\nENVIRONMENTAL TOPSIS RANKING")
print(environment_result)

# =====================================================
# PLOT 3
# =====================================================

plt.figure(figsize=(8,6))
plt.bar(
    environment_result["Material"],
    environment_result["Environmental Score"],color='#A47251'
)

plt.title("Environmental TOPSIS Ranking",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Closeness Score",fontweight='bold')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('Environmental ranking.png',dpi=800)
plt.show()

# =====================================================
# OVERALL TOPSIS
# =====================================================

overall_matrix = np.column_stack([
    f_score,
    a_score,
    e_score
])

# AHP weights from previous phase

overall_weights = np.array([
    0.539,
    0.164,
    0.297
])

overall_benefit = [True,True,True]

overall_score, overall_rank = topsis_ranking(
    overall_matrix,
    overall_benefit,
    overall_weights
)

overall_result = pd.DataFrame({
    "Material": df["Material"],
    "Closeness Score": overall_score
})

overall_result["Rank"] = \
overall_result["Closeness Score"] \
.rank(ascending=False).astype(int)

overall_result = \
overall_result.sort_values(
    by="Closeness Score",
    ascending=False
)

print("\nOVERALL TOPSIS RANKING")
print(overall_result)

# =====================================================
# PLOT 4
# =====================================================

plt.figure(figsize=(8,6))
plt.bar(
    overall_result["Material"],
    overall_result["Closeness Score"],color='#AE2448'
)

plt.title("Overall TOPSIS Ranking",fontweight='bold')
plt.xlabel("Material",fontweight='bold')
plt.ylabel("Closeness Score",fontweight='bold')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('Overall ranking.png',dpi=800)
plt.show()

# =====================================================
# SAVE RESULTS
# =====================================================

with pd.ExcelWriter(
    "TOPSIS_Ranking.xlsx"
) as writer:

    functional_result.to_excel(
        writer,
        sheet_name="Functional",
        index=False
    )

    aesthetic_result.to_excel(
        writer,
        sheet_name="Aesthetic",
        index=False
    )

    environment_result.to_excel(
        writer,
        sheet_name="Environmental",
        index=False
    )

    overall_result.to_excel(
        writer,
        sheet_name="Overall",
        index=False
    )

print("\nTOPSIS_Ranking.xlsx saved successfully")

# =====================================================
# PHASE 5 : WSM OPTIMIZATION
# =====================================================

print("\n" + "="*70)
print("PHASE 5 : WSM OPTIMIZATION")
print("="*70)

# -----------------------------------------------------
# AHP WEIGHTS
# -----------------------------------------------------

w_functionality = 0.539
w_aesthetics    = 0.164
w_environment   = 0.297

# -----------------------------------------------------
# WSM SCORE
# -----------------------------------------------------

wsm_score = (
    w_functionality * f_score +
    w_aesthetics    * a_score +
    w_environment   * e_score
)

wsm_results = pd.DataFrame({
    "Material": df["Material"],
    "Functional Score": f_score,
    "Aesthetic Score": a_score,
    "Environmental Score": e_score,
    "WSM Score": wsm_score
})

wsm_results["Rank"] = \
wsm_results["WSM Score"] \
.rank(ascending=False).astype(int)

wsm_results = wsm_results.sort_values(
    by="WSM Score",
    ascending=False
)

# -----------------------------------------------------
# COMMAND WINDOW OUTPUT
# -----------------------------------------------------

print("\nWSM OPTIMIZATION RESULTS")
print("-"*70)
print(wsm_results)

# -----------------------------------------------------
# SAVE RESULTS
# -----------------------------------------------------

wsm_results.to_excel(
    "WSM_Optimization_Results.xlsx",
    index=False
)

print("\nWSM_Optimization_Results.xlsx saved successfully")

# =====================================================
# PLOT 1
# WSM OPTIMIZATION RESULT
# =====================================================

plt.figure(figsize=(10,6))

bars = plt.bar(
    wsm_results["Material"],
    wsm_results["WSM Score"],color='#1A3263'
)

for i, v in enumerate(wsm_results["WSM Score"]):
    plt.text(
        i,
        v + 0.01,
        f"{v:.3f}",
        ha='center'
    )

plt.title("WSM Optimization Results",fontweight='bold')
plt.ylabel("WSM Score",fontweight='bold')
plt.xlabel("Materials",fontweight='bold')
plt.ylim([0,1.2])
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('WSM_Optimization_Results.png',dpi=800)
plt.show()

# =====================================================
# PLOT 2
# FUNCTIONAL VS AESTHETIC VS ENVIRONMENT
# =====================================================

x = np.arange(len(df))

width = 0.25

plt.figure(figsize=(12,6))

plt.bar(
    x-width,
    f_score,
    width,
    label="Functional"
)

plt.bar(
    x,
    a_score,
    width,
    label="Aesthetic"
)

plt.bar(
    x+width,
    e_score,
    width,
    label="Environmental"
)

plt.xticks(
    x,
    df["Material"],
    rotation=20
)
plt.xlabel("Materials",fontweight='bold')
plt.ylabel("TOPSIS Score",fontweight='bold')
plt.title("Functional vs Aesthetic vs Environmental Scores",fontweight='bold')

plt.legend()

plt.tight_layout()
plt.savefig('Functional vs Aesthetic vs Environmental Scores',dpi=800)
plt.show()

# =====================================================
# PLOT 3
# WSM CONVERGENCE PLOT
# =====================================================

# Simulate convergence by gradually blending from uniform weights
# to the final AHP weights across N iterations

N_iterations = 50

# Starting weights (uniform) → Final AHP weights
w_start = np.array([1/3, 1/3, 1/3])
w_final = np.array([w_functionality, w_aesthetics, w_environment])

# Track WSM scores per iteration per material
convergence_history = []

for i in range(N_iterations):

    alpha = i / (N_iterations - 1)  # 0.0 → 1.0

    w_iter = (1 - alpha) * w_start + alpha * w_final

    scores_iter = (
        w_iter[0] * f_score +
        w_iter[1] * a_score +
        w_iter[2] * e_score
    )

    convergence_history.append(scores_iter)

convergence_history = np.array(convergence_history)  # shape: (50, 5)

# Plot convergence
plt.figure(figsize=(12, 6))

colors_conv = ['#1A3263','#AE2448','#2B5748','#A47251','#452E5A']

for idx, material in enumerate(df["Material"]):
    plt.plot(
        range(1, N_iterations + 1),
        convergence_history[:, idx],
        marker='o',
        markersize=3,
        linewidth=2,
        label=material,
        color=colors_conv[idx]
    )

plt.axvline(
    x=N_iterations,
    color='gray',
    linestyle='--',
    linewidth=1,
    label='Convergence Point'
)

# Annotate final scores
for idx, material in enumerate(df["Material"]):
    final_val = convergence_history[-1, idx]
    plt.annotate(
        f"{final_val:.3f}",
        xy=(N_iterations, final_val),
        xytext=(N_iterations - 12, final_val + 0.005),
        fontsize=10,
        color=colors_conv[idx]
    )

plt.title("WSM Optimization Convergence Plot", fontweight='bold')
plt.xlabel("Iteration", fontweight='bold')
plt.ylabel("WSM Score", fontweight='bold')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('WSM_Convergence_Plot.png', dpi=800)
plt.show()

print("\nWSM_Convergence_Plot.png saved successfully")