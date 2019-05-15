// Print Hello, OpenPnP to the console
print('NozzleTip.Loaded called');

tooltipvacActuator = head.getActuatorByName("TooltipVac");	
tooltipvacActuator.actuate(false); //to turn downlooking lightning OFF

tooltipChangerActuator = head.getActuatorByName("TipChangerVac");	
tooltipChangerActuator.actuate(true); //to turn downlooking lightning OFF
