print("Estimation Of Wall Plaster".center(60))
print()
print("Code Developed By Muhammad Hamza Javed".center(90))
print()
Ratio_Cement=float(input("Enter Cement Ratio : "))
Ratio_Sand=float(input("Enter Sand Ratio : "))
Ratio_sum=Ratio_Sand+Ratio_Cement
Plaster_Thickness=float(input("Enter Plaster Thickness in Meter : "))
Density_of_Cement=float(input("Enter Density Of Cement : "))
Lenght=float(input("Enter Lenght Of Wall in Meter : "))
Width=float(input("Enter Width Of Wall in Meter : "))
Vol_of_mortar=Lenght * Width * Plaster_Thickness    #For Wet Volume
print()
print("Wet Volume Of Mortor is : ",Vol_of_mortar.__round__(3))
print()
Dry_volume=Vol_of_mortar*1.30
print("Dry Volume Of Mortor is : ",Dry_volume.__round__(3))
print()
Quantity_of_Cement=Ratio_Cement/Ratio_sum*Dry_volume*Density_of_Cement
print("Quantity Of Cement is : ",Quantity_of_Cement.__round__(3),"kg")
print()
Quantity_of_Sand=Ratio_Sand/Ratio_sum*Dry_volume*35.3147 #35.3147 For converting cubic meter to cubic feet (ft3)
print("Quantity Of Sand is : ",Quantity_of_Sand.__round__(3),"Ft3")