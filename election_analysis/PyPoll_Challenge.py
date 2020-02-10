import csv
import os

file_to_load = os.path.join("resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0


candidate_options = []


counties_options = []


candidate_votes = {}


counties_votes = {}


winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0
winning_county = ""
winning_count_county = 0
winning_percentage_county = 0


with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    for row in file_reader:
        
        total_votes += 1
        
        candidate_name = row[2]
        county_name = row[1]
    
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

        if county_name not in counties_options:
            
            counties_options.append(county_name)
            
            counties_votes[county_name] = 0
        
        counties_votes[county_name] += 1


with open(file_to_save, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for county in counties_votes:
        
        votes_county  =  counties_votes[county]
        
        vote_percentage_county = int(votes_county) / int(total_votes) * 100  
        
        counties_results = (
            f"{county}: {vote_percentage_county:.1f}% ({votes_county:,})\n")
        
        print(counties_results)
        
        txt_file.write(counties_results)
        
        
        if (votes_county > winning_count_county) and (vote_percentage_county > winning_percentage_county):
            
            winning_count_county = votes_county
            winning_percentage_county = vote_percentage_county
            winning_county = county  

    
    winning_county_summary = (
        f"\n----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------\n")
    print(winning_county_summary)
    
    txt_file.write(winning_county_summary)
    
    for candidate in candidate_votes:
        votes_candidate  =  candidate_votes[candidate]
        vote_percentage_candidate = int(votes_candidate) / int(total_votes) * 100  
        candidate_results = (f"{candidate}: {vote_percentage_candidate:.1f}% ({votes_candidate:,})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)
        

        if (votes_candidate > winning_count_candidate) and (vote_percentage_candidate > winning_percentage_candidate):
            winning_count_candidate = votes_candidate
            winning_percentage_candidate = vote_percentage_candidate
            winning_candidate = candidate  

    
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count_candidate:,}\n"
        f"winning Percentage: {winning_percentage_candidate:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
