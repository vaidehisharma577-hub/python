"""
Author: Your Name
Date: 2025-12-05
Project: Household Electricity Use Dashboard
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# -------------------------------
# GLOBAL DATA STRUCTURES
# -------------------------------
all_data = []          # Stores all rows (date, usage)
monthly_totals = {}    # Monthly usage summary
analysis_results = {}  # Computed statistics


# -------------------------------
# TASK 1: MENU + HEADER
# -------------------------------

def display_menu():
    print("\n" + "="*50)
    print("     HOUSEHOLD ELECTRICITY USE DASHBOARD")
    print("="*50)
    print("1. Load electricity data from CSV files")
    print("2. View usage analysis")
    print("3. Plot usage trend")
    print("4. Export results")
    print("5. Exit")
    print("="*50)


# -------------------------------
# TASK 2: LOAD MULTIPLE CSV FILES
# -------------------------------

def load_csv_files():
    global all_data, monthly_totals

    all_data = []
    monthly_totals = {}

    print("\nEnter CSV file names (comma separated):")
    print("Example: jan.csv, feb.csv, mar.csv")
    files = input("Files: ").split(",")

    for file in files:
        file = file.strip()
        try:
            with open(file, newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    date_str = row.get("Date")
                    usage_str = row.get("Usage")

                    if not date_str or not usage_str:
                        continue
                    
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    usage = float(usage_str)

                    all_data.append({"date": date, "usage": usage})

                    # accumulate monthly totals
                    key = date.strftime("%Y-%m")
                    monthly_totals[key] = monthly_totals.get(key, 0) + usage

            print(f"Loaded: {file}")

        except FileNotFoundError:
            print(f"ERROR: File not found → {file}")
        except Exception as e:
            print(f"ERROR loading {file}: {e}")

    # Sort data by date
    all_data.sort(key=lambda x: x["date"])

    print("\nData loading complete. Total records:", len(all_data))


# -------------------------------
# TASK 3: USAGE CALCULATION
# -------------------------------

def analyze_usage():
    global analysis_results

    if not all_data:
        print("\nNo data loaded.")
        return

    total_usage = sum(row["usage"] for row in all_data)
    avg_usage = total_usage / len(all_data)
    min_usage = min(all_data, key=lambda x: x["usage"])
    max_usage = max(all_data, key=lambda x: x["usage"])

    analysis_results = {
        "total_usage": total_usage,
        "average_daily": avg_usage,
        "min_usage": (min_usage["date"], min_usage["usage"]),
        "max_usage": (max_usage["date"], max_usage["usage"]),
        "monthly_totals": monthly_totals
    }

    print("\n===== ELECTRICITY USAGE SUMMARY =====")
    print(f"Total electricity consumption: {total_usage:.2f} units")
    print(f"Average daily usage: {avg_usage:.2f} units")
    print(f"Minimum daily usage: {min_usage['usage']} on {min_usage['date'].date()}")
    print(f"Maximum daily usage: {max_usage['usage']} on {max_usage['date'].date()}")
    print("\nMonthly Totals:")
    for m, v in monthly_totals.items():
        print(f"  {m}: {v:.2f} units")


# -------------------------------
# TASK 4: USAGE TREND PLOTTING
# -------------------------------

def plot_usage():
    if not all_data:
        print("\nNo data loaded.")
        return

    dates = [row["date"] for row in all_data]
    usage = [row["usage"] for row in all_data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, usage, marker='o')
    plt.title("Household Electricity Usage Trend")
    plt.xlabel("Date")
    plt.ylabel("Units Consumed")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("usage_plot.png")
    plt.show()
    print("\nPlot saved as usage_plot.png")


# -------------------------------
# TASK 5: EXPORT RESULTS
# -------------------------------

def export_results():

    if not all_data or not analysis_results:
        print("\nLoad and analyze data before exporting.")
        return

    # Export detailed data
    with open("electricity_summary_output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Usage"])
        for row in all_data:
            writer.writerow([row["date"].strftime("%Y-%m-%d"), row["usage"]])

    # Export analysis summary
    with open("analysis_summary.txt", "w") as f:
        f.write("Electricity Usage Summary\n")
        f.write("=========================\n")
        f.write(f"Total Usage: {analysis_results['total_usage']:.2f}\n")
        f.write(f"Average Daily: {analysis_results['average_daily']:.2f}\n")
        f.write(f"Min Usage: {analysis_results['min_usage'][1]} on {analysis_results['min_usage'][0].date()}\n")
        f.write(f"Max Usage: {analysis_results['max_usage'][1]} on {analysis_results['max_usage'][0].date()}\n")
        f.write("\nMonthly Totals:\n")
        for m, v in analysis_results["monthly_totals"].items():
            f.write(f"  {m}: {v:.2f}\n")

    print("\nFiles exported:")
    print(" - electricity_summary_output.csv")
    print(" - analysis_summary.txt")
    print(" - usage_plot.png")


# -------------------------------
# TASK 6: MAIN LOOP
# -------------------------------

def main():
    print("Welcome to the Electricity Use Dashboard!")

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            load_csv_files()
        elif choice == "2":
            analyze_usage()
        elif choice == "3":
            plot_usage()
        elif choice == "4":
            export_results()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
