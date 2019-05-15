// Print Hello, OpenPnP to the console
print('NozzleTip.BeforeUnLoad called');

tooltipvacActuator = head.getActuatorByName("TooltipVac");	
tooltipvacActuator.actuate(false); //to turn downlooking lightning OFF

tooltipChangerActuator = head.getActuatorByName("TipChangerVac");	
tooltipChangerActuator.actuate(false); //to turn downlooking lightning OFF
