list_of_cloud = ["aws","azure","gcp","oracle","digital ocean"]
list_of_env = ["dev","test","production"]

for cloud in list_of_cloud:
    if cloud =="aws":
     print("Aws is the best cloud")

# Dictonary
dict_of_cloud = {
   "aws": "Amazon web service",
    "azure": "Microsoft services",
    "gcp": "Google cloud platform"
}
print(dict_of_cloud["aws"])
print(dict_of_cloud["azure"])
print(dict_of_cloud["gcp"])
print(dict_of_cloud.get("linod","not found"))
dict_of_cloud.update({"linode":"linode cloud"})
print(dict_of_cloud)
