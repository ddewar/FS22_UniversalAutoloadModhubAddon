UniversalAutoloadModhubAddonManager = {}
UniversalAutoloadModhubAddonManager.path = g_currentModDirectory

addModEventListener(UniversalAutoloadModhubAddonManager)

function UniversalAutoloadModhubAddonManager:loadMap(name)
    if g_modIsLoaded["FS22_UniversalAutoload"] then
        print("  ADDON VEHICLES:")
        local vehicleSettingsFile = Utils.getFilename("config/SupportedVehicles.xml", UniversalAutoloadModhubAddonManager.path)
        UniversalAutoload.ImportVehicleConfigurations(vehicleSettingsFile)
    else
		print("FS22_UniversalAutoload is required for FS22_UniversalAutoloadModhubAddon")
	end
end