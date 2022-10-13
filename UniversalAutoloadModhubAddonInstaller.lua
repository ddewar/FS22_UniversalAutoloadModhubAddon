UniversalAutoloadModhubAddonManager = {}
UniversalAutoloadModhubAddonManager.path = g_currentModDirectory

addModEventListener(UniversalAutoloadModhubAddonManager)

function UniversalAutoloadModhubAddonManager:loadMap(name) 
    if g_modIsLoaded["FS22_UniversalAutoload"] then 
        local vehicleSettingsFile = Utils.getFilename("config/SupportedVehicles.xml", UniversalAutoloadModhubAddonManager.path) 
        local containerSettingsFile = Utils.getFilename("config/ContainerTypes.xml", UniversalAutoloadModhubAddonManager.path) 
        print("MODHUB ADDON: IMPORT vehicle configurations")
        FS22_UniversalAutoload.UniversalAutoloadManager.ImportVehicleConfigurations(vehicleSettingsFile)
        print("MODHUB ADDON: IMPORT container configurations")
        FS22_UniversalAutoload.UniversalAutoloadManager.ImportGlobalSettings(containerSettingsFile)
        FS22_UniversalAutoload.UniversalAutoloadManager.ImportContainerTypeConfigurations(containerSettingsFile, true)
    else 
        print("FS22_UniversalAutoload is required for FS22_UniversalAutoloadModhubAddon") 
    end
end