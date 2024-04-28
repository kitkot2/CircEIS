from functions import show, preparation, clean
from circumference_fitting import circumference_fit
from circuit_fitting import circuit_fit
from impedance import preprocessing

def main():
    #temperature = '105'
    #file_name = 'Ag3VO4-2-2M-'+temperature+'-3-Start1'

    print('Enter file name without .txt or .csv:')
    file_name = input()

    preparation.correct_path(file_name)
    preparation.EIS_txt_to_csv(file_name)

    f, Re, Im, Z = preparation.read_from_CSV_positive_Im(file_name)
    #f, Z = preprocessing.ignoreBelowX(f, Z)
    
    # for testing
    # f, Re, Im, Z = preparation.read_from_CSV_ignore_below_X(file_name) #for testing
    
    show.plot_data(Re,Im)
    f, Re, Im, Z = clean.clean_hub(f, Re,Im, Z)

    print("Do you want to fit circumference in your data (1) or equivalent circuits (2)?")

    answer = int(input())

    if answer == 1:
        circumference_fit(Re, Im)
    elif answer == 2:
        circuit_fit(f, Z)

if __name__ == "__main__":
    main()