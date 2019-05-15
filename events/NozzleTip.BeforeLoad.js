// Print Hello, OpenPnP to the console
print('NozzleTip.BeforeLoad called');

tooltipvacActuator = head.getActuatorByName("TooltipVac");	
tooltipvacActuator.actuate(false); //to turn downlooking lightning OFF

tooltipChangerActuator = head.getActuatorByName("TipChangerVac");	
tooltipChangerActuator.actuate(false); //to turn downlooking lightning OFF
