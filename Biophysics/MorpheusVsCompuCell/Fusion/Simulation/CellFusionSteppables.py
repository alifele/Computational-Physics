
from cc3d.core.PySteppables import *
import numpy as np

class CellFusionSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)        
        #hfldfs

    def start(self):
        
        # access/modification of a dictionary attached to cell - make sure to declare in main script that
        # you will use such attribute
    
        
        
    
    
    # def add_steering_panel(self):
        # self.add_steering_param(name='MY_PARAM_SLIDER', val=20, min_val=0, max_val=100,
                                # decimal_precision=2, widget_name='slider')
        # self.add_steering_param(name='MY_PARAM_COMBO', val=20, enum=[10,20,30,40,50,60,70,80,90,100],
                                    # widget_name='combobox')
    
    # def process_steering_panel_data(self):
        # print ('processing steering panel updates')
        # print ('all dirty flag=', self.steering_param_dirty())
        # param_slider = self.get_steering_param('MY_PARAM_SLIDER')
        # param_combo = self.get_steering_param('MY_PARAM_COMBO')
        # print ('updated MY_PARAM_SLIDER=',param_slider)
        # print ('updated MY_PARAM_COMBO=', param_combo)
    
        # # IMPORTANT: you may add code here tht updates cell properties based on the
        # # values of the parameters from the steering panel. For example:
    
        # # for cell in self.cellList:
        # #     cell.targetVolume = param_slider
        # #     cell.lambdaVolume = param_combo
    
        
        
        
        
        
        """
        Called before MCS=0 while building the initial simulation
        """
        
        
        self.plot_win = self.add_new_plot_window(title='Contact_Area',
                                                 x_axis_title='MonteCarlo Step (MCS)',
                                                 y_axis_title='Variables', x_scale_type='linear', y_scale_type='linear',
                                                 grid=False)
                                                 
                                                
        
        self.plot_win.add_plot("blueGreen", style='Lines', color='red', size=5)
        self.plot_win.add_plot("greenMed", style='Lines', color='green', size=5)
        
        
        # self.plot_win.add_plot("MSur", style='Dots', color='green', size=1)
        
        
        

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """
        
        # if not (mcs%10):
            # blueGreen = 0
            # blueMed = 0
            # greenMed = 0
            # # iterating over cells of type 1
            # # list of  cell types (capitalized)
            # for cell in self.cell_list_by_type(self.CT0):
                # # you can access/manipulate cell properties here
                # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                    # if neighbor:
                        # if neighbor.type == self.CT1:
                            # blueGreen += common_surface_area
                    # else:
                        # greenMed += common_surface_area
                        
                       
                
                
                # print ("id=", cell.id, " type=", cell.type)
            
                # # arguments are (name of the data series, x, y)
                
            # self.plot_win.add_data_point("blueGreen", mcs, blueGreen)
            # self.plot_win.add_data_point("greenMed", mcs, greenMed)
            
 
                
                

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """

        # saving goes here
        file_obj, file_path = self.open_file_in_simulation_output_folder("testData", mode='w')
        
        if file_obj is None:
            return
         
        
        
        
        