# collect data
#   optional skip
#   input/output path
#   api key path/ type api key
# profile data
#   which years
#   already created?
#   input/output path
# analyze data
#   which years

def intro(d):
    runDefault = input("\nRun default settings?\n[Y/N] ... type [L] for a list of the default settings\n")

    if runDefault.lower() == 'l':
        for key in d:
            print(f"{key}: {d[key]}")
        print("\n\n")
        return intro(d)

    elif runDefault.lower() == 'n':
        # Could write a function to change the values of d and then return d, but this is faster
        print("open main.py and edit the values of the variable 'd'\nYou should see them under 'if __name__ == '__main__':")

    elif runDefault.lower() == 'y':
        yearTuple = d['year range']
        if yearTuple[0] < yearTuple[1]:
            raise ValueError("\nyear range must be (high, low)\nPlease change d['year range']\n")
        return d
    else:
        print("\nResponse not understood, please type the letter Y, N, or L (lowercase or uppercase, doesn't matter)")
        return intro(d)

if __name__ == "__main__":
    from horizontal import main
    from collectData import collect
    d = {}

    """
        Edit these settings below to fit your needs
    """
    d['record new data'] = True
    d['input path'] = 'NYSE_symbols.txt'
    d['output path'] = 'NYSE10Kdata.csv'
    d['year range'] = (2019, 2011)
    d['horizontal data input'] = None
    d['horizontal data output'] = 'NYSE10K_horizontal_profile.csv'
    d['analysis output base-name'] = 'NYSE10K_horizontal_analysis'
    d['analyze all year pairs'] = True
    d['specific year pairs'] = None



    d = intro(d)

    if d['record new data']:
        collect(d['input path'], d['output path'])
    main(
        d['output path'],
        d['year range'], 
        d['horizontal data input'], 
        d['horizontal data output'],
        d['analysis output base-name'],
        d['analyze all year pairs'], 
        d['specific year pairs']
        )

