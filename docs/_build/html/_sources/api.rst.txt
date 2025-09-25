.. _api-reference:

API Reference
=============

.. py:module:: iesve

   Note: text in italics has been reproduced verbatim from the original text used in the IES-VE Python API online help guide or Python docstrings. Where I have replaced this with my own text, this is in non-italics.

   .. py:method:: get_application_folder
   
      *get_application_folder() -> str :*
          *Application folder (VE bin folder)*
   
   .. py:class:: AdjacentCondition_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: external_air
         :classmethod:
         :type: iesve.AdjacentCondition_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "external_air".
      
      .. py:property:: external_air_and_offset_temp
         :classmethod:
         :type: iesve.AdjacentCondition_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "external_air_and_offset_temp".
      
      .. py:property:: from_adjacent_room
         :classmethod:
         :type: iesve.AdjacentCondition_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "from_adjacent_room".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'external_air': iesve.AdjacentCondition_type.external_air
             'external_air_and_offset_temp': iesve.AdjacentCondition_type.external_air_and_offset_temp
             'from_adjacent_room': iesve.AdjacentCondition_type.from_adjacent_room
             'temperature_from_profile': iesve.AdjacentCondition_type.temperature_from_profile
            }
      
      .. py:property:: temperature_from_profile
         :classmethod:
         :type: iesve.AdjacentCondition_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "temperature_from_profile".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.AdjacentCondition_type.external_air
             2: iesve.AdjacentCondition_type.external_air_and_offset_temp
             3: iesve.AdjacentCondition_type.from_adjacent_room
             4: iesve.AdjacentCondition_type.temperature_from_profile
            }
      
   .. py:class:: AirExchange
   
      *Air Exchange data.*
   
      .. py:method:: get
      
         *get() -> Dictionary*
         
         *Returns a Dictionary containing the data for the air exchange.*
      
      .. py:property:: name
      
         *(str) Descriptive string*
      
   .. py:class:: AirExchange_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: infiltration
         :classmethod:
         :type: iesve.AirExchange_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "infiltration".
      
      .. py:property:: mechanical_ventilation
         :classmethod:
         :type: iesve.AirExchange_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "mechanical_ventilation".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'infiltration': iesve.AirExchange_type.infiltration
             'natural_ventilation': iesve.AirExchange_type.natural_ventilation
             'mechanical_ventilation': iesve.AirExchange_type.mechanical_ventilation
            }
      
      .. py:property:: natural_ventilation
         :classmethod:
         :type: iesve.AirExchange_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "natural_ventilation".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.AirExchange_type.infiltration
             1: iesve.AirExchange_type.natural_ventilation
             2: iesve.AirExchange_type.mechanical_ventilation
            }
      
   .. py:class:: ApacheSim
   
      *Interface for running Apache Simulations.*
      *Basic usage:*
      
          *iesve.ApacheSim.show_simulation_dialog()*
      
      *or*
      
          *s = iesve.ApacheSim()*
          *s.save_options({'results_filename' : 'abc.aps'})*
          *s.run_simulation()*
   
      .. py:method:: get_options
      
         *get_options( ) -> {options}*
         
         *Get the simulation options currently in effect. Available options*
         *(options are True/False unless stated otherwise):*
             *start_day (1-31), start_month (1-12),*
             *end_day (1-31), end_month (1-12),*
             *simulation_timestep (time_step enum),*
             *reporting_interval (reporting_interval enum),*
             *preconditioning_days (0-365),*
             *results_filename (filename: string),*
             *suncast, suncast_filename (filename: string),*
             *macroflo,*
             *HVAC, HVAC_filename (filename: string),*
             *radiance,*
             *aux_ventilation, nat_ventilation,*
             *cooling_start_month (1-12), cooling_end_month (1-12)*
             *ashrae_loads_results_filename (filename: string),*
         
         *Output options:*
             *output_standard_outputs, output_sensible_internal_gains,*
             *output_latent_internal_gains, output_latent_ventilation_gains,*
             *output_conduction_gains, output_HVAC_systems, output_HVAC_components*
         
         *Detailed output options:*
             *detailed_rooms (list of roomIDs: [string])*
             *detailed_microflo, detailed_standard_outputs,*
             *detailed_sensible_internal_gains, detailed_latent_internal_gains,*
             *detailed_latent_ventilation_gains, detailed_convective_gains,*
             *detailed_surface_temps, detailed_external_solar, detailed_internal_solar,*
             *detailed_conduction_gains, detailed_HVAC_systems.*
         
         *Note that setting Suncast and Radiance to True will*
         *only auto - run suncast when using batch operation.*
         *When using the blocking run, suncast and radiance*
         *will not be automatically run when set to True, but*
         *if corresponding data files are available (shd and ill files)*
         *they will be used in simulation.*
         *Absence of data files may cause simulation to fail.*
      
      .. py:method:: reset_options
      
         *reset_options( ) -> Bool*
         
         *Reset the simulation options file to defaults. Returns True*
         *if the options file was saved successfully.*
      
      .. py:method:: run_compliance_simulation
      
         *run_compliance_simulation() -> Bool*
         
         *Run compliance simulation with the currently active settings.*
         *Parallel Simulation Manager (BETA) will*
         *be used. A return value of true indicates*
         *that simulation was run / queued, false indicates error.*
      
      .. py:method:: run_loads_sizing
      
         *run_loads_sizing()*
         
         *Run a Loads and Sizing simulation*
      
      .. py:method:: run_room_zone_loads
      
         *run_room_loads_sizing()*
         
         *Run a Room and HVAC Zone loads simulation*
      
      .. py:method:: run_simulation
      
         *run_simulation( [queueToTasks] ) -> Bool*
         
         *Run Apache thermal simulation with the currently active settings.*
         *If the queueToTasks parameter is True, Parallel Simulation Manager (BETA) will*
         *be used.  Otherwise, the simulation will run and the VE is blocked*
         *until simulation is complete.  A return value of true indicates*
         *that simulation was run / queued, false indicates error.  By default,*
         *queueToTasks is False (the call will block until simulation is complete).*
      
      .. py:method:: set_hvac_network
      
         *set_hvac_network(network_name)*
         
         *Set the HVAC network*
      
      .. py:method:: set_options
      
         *set_options( {options} ) -> Bool*
         
         *Set (and save) simulation options.  These options will be used*
         *for the subsequent simulation run.  See getOptions() for details*
         *on available options.  Returns True if the options file was saved*
         *successfully.*
         
         *set_options( {options} ) -> Bool*
         
         *Set (and save) simulation options.  These options will be used*
         *for the subsequent simulation run.  See getOptions() for details*
         *on available options.  Returns True if the options file was saved*
         *successfully.*
      
      .. py:method:: show_simulation_dialog
      
         *show_simulation_dialog( ) -> Bool*
         
         *Show the Apache Simulation dialog.  Returns true if dialog was shown*
         *and simulation was run.*
      
      .. py:method:: stitch
      
         *stitch(output_file_path, files_to_stitch)*
         
         *Stitch together a list of APS files into a single APS file*
         *Parameters:*
         
         *output_file_path (string): Path of the output APS file*
         *files_to_stitch (list): Ordered list of APS files to stitch.*
      
   .. py:class:: Ashrae621Version
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae621_2004
         :classmethod:
         :type: iesve.Ashrae621Version
      
         An instance of this class with:
         
         * a value of 0
         * a name of "ashrae621_2004".
      
      .. py:property:: ashrae621_2007
         :classmethod:
         :type: iesve.Ashrae621Version
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ashrae621_2007".
      
      .. py:property:: ashrae621_2010
         :classmethod:
         :type: iesve.Ashrae621Version
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae621_2010".
      
      .. py:property:: ashrae621_2013
         :classmethod:
         :type: iesve.Ashrae621Version
      
         An instance of this class with:
         
         * a value of 3
         * a name of "ashrae621_2013".
      
      .. py:property:: ashrae621_2016
         :classmethod:
         :type: iesve.Ashrae621Version
      
         An instance of this class with:
         
         * a value of 4
         * a name of "ashrae621_2016".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'ashrae621_2004': iesve.Ashrae621Version.ashrae621_2004
             'ashrae621_2007': iesve.Ashrae621Version.ashrae621_2007
             'ashrae621_2010': iesve.Ashrae621Version.ashrae621_2010
             'ashrae621_2013': iesve.Ashrae621Version.ashrae621_2013
             'ashrae621_2016': iesve.Ashrae621Version.ashrae621_2016
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.Ashrae621Version.ashrae621_2004
             1: iesve.Ashrae621Version.ashrae621_2007
             2: iesve.Ashrae621Version.ashrae621_2010
             3: iesve.Ashrae621Version.ashrae621_2013
             4: iesve.Ashrae621Version.ashrae621_2016
            }
      
   .. py:class:: AuxEnergyMethod_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: AEV
         :classmethod:
         :type: iesve.AuxEnergyMethod_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "AEV".
      
      .. py:property:: SFPs
         :classmethod:
         :type: iesve.AuxEnergyMethod_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "SFPs".
      
      .. py:property:: SFPs_and_AEV
         :classmethod:
         :type: iesve.AuxEnergyMethod_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "SFPs_and_AEV".
      
      .. py:property:: SFPs_with_min_AEV
         :classmethod:
         :type: iesve.AuxEnergyMethod_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "SFPs_with_min_AEV".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'SFPs': iesve.AuxEnergyMethod_type.SFPs
             'SFPs_with_min_AEV': iesve.AuxEnergyMethod_type.SFPs_with_min_AEV
             'SFPs_and_AEV': iesve.AuxEnergyMethod_type.SFPs_and_AEV
             'AEV': iesve.AuxEnergyMethod_type.AEV
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.AuxEnergyMethod_type.SFPs
             1: iesve.AuxEnergyMethod_type.SFPs_with_min_AEV
             2: iesve.AuxEnergyMethod_type.SFPs_and_AEV
             3: iesve.AuxEnergyMethod_type.AEV
            }
      
   .. py:class:: BatteryControlType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: AdvancedDR
         :classmethod:
         :type: iesve.BatteryControlType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "AdvancedDR".
      
      .. py:property:: Basic
         :classmethod:
         :type: iesve.BatteryControlType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "Basic".
      
      .. py:property:: TOU
         :classmethod:
         :type: iesve.BatteryControlType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "TOU".
      
      .. py:property:: TOU_StandAlone
         :classmethod:
         :type: iesve.BatteryControlType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "TOU_StandAlone".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'Basic': iesve.BatteryControlType.Basic
             'TOU': iesve.BatteryControlType.TOU
             'TOU_StandAlone': iesve.BatteryControlType.TOU_StandAlone
             'AdvancedDR': iesve.BatteryControlType.AdvancedDR
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.BatteryControlType.Basic
             1: iesve.BatteryControlType.TOU
             2: iesve.BatteryControlType.TOU_StandAlone
             3: iesve.BatteryControlType.AdvancedDR
            }
      
   .. py:class:: BpfCustom
   
      *Interface for custom building performance factors data*
   
      .. py:method:: get
      
         *get() -> dictionary*
         
         *Get custom building performance factors.*
         *Returns a dictionary with the following keys:*
         *MutltiFamily, Healthcare/hospital, Hotel, Office, Restaurant, Retail,*
         *School, Warehouse, Other*
      
      .. py:property:: name
      
         *(str) Name of the current BPF preset.*
      
   .. py:class:: CasualGain
   
      *Casual Gain data.*
   
      .. py:method:: get
      
         *get() -> Dictionary*
         
         *Returns a Dictionary containing the data for the internal gain.*
      
      .. py:property:: name
      
         *(str) Descriptive string*
      
   .. py:class:: CoilLocationCircuit
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'primary': iesve.CoilLocationCircuit.primary
             'secondary': iesve.CoilLocationCircuit.secondary
            }
      
      .. py:property:: primary
         :classmethod:
         :type: iesve.CoilLocationCircuit
      
         An instance of this class with:
         
         * a value of 0
         * a name of "primary".
      
      .. py:property:: secondary
         :classmethod:
         :type: iesve.CoilLocationCircuit
      
         An instance of this class with:
         
         * a value of 1
         * a name of "secondary".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.CoilLocationCircuit.primary
             1: iesve.CoilLocationCircuit.secondary
            }
      
   .. py:class:: CompactProfile
   
      *Compact profile.*
   
      .. py:method:: get_data
      
         *get_data() -> profile data*
         
         *Retrieve profile data.  The returned data depends on profile type. All returned*
         *data structures are compatible with the set_data() method.*
           *- Daily profile: a list of [ x, y, formula ] lists that represent the data for the profile.*
           *- Weekly profile: a list of daily profile IDs that make up the weekly profile.*
           *- Yearly profile: a list of lists: [ weekly profile ID, fromDay, toDay ],*
             *where fromDay = year day where the profile becomes active, toDay = last day of profile*
           *- Compact profile: a nested sets of lists, each list representing on/off time periods*
           *- Free form profile : list of lists: [ month, day, hour, minute, value ]*
      
      .. py:property:: id
      
         *(str) Profile ID.*
      
      .. py:method:: is_absolute
      
         *is_absolute() -> bool*
         
         *True if the profile is absolute, else False.*
      
      .. py:method:: is_compact
      
         *is_compact() -> bool*
         
         *True if the profile is a compact profile, else False.*
      
      .. py:method:: is_freeform
      
         *is_freeform() -> bool*
         
         *True if the profile is a free form profile, else False.*
      
      .. py:method:: is_group
      
         *is_group() -> bool*
         
         *True if the profile is a group profile, False if a daily profile.*
      
      .. py:method:: is_modulating
      
         *is_modulating() -> bool*
         
         *True if the profile is modulating, else False.*
      
      .. py:method:: is_weekly
      
         *is_weekly() -> bool*
         
         *True if the profile is a weekly profile, else False.*
      
      .. py:method:: is_yearly
      
         *is_yearly() -> bool*
         
         *True if the profile is a yearly (annual) profile, else False.*
      
      .. py:property:: num_periods
      
         *(int) Number of periods in profile.*
      
      .. py:property:: reference
      
         *(str) Profile reference (name).*
      
      .. py:method:: set_data
      
         *set_data() -> bool*
         
         *Set profile data.  The data to be passed depends on profile type.*
         
         *Daily Profile:*
         *Data should represented by a list of [x,y,formula] lists*
         *[ [x,y,formula], [x,y,formula], ... ]*
         
         *Weekly Profile:*
         *Data should represented by a list of daily profile IDs*
         *[ ID1, ID2, ... ]*
         
         *Yearly Profile:*
          *Data should be represented by a list of [weekly profile ID(string), fromDay(int), toDay(int)] lists*
          *[ [ID1, from1, to1], [ID2, from2, to2], ... ]*
         
         *Compact Profile:*
         *Data should represented by a list of lists that contains compact profile data:*
         
         *The outer list is for the number of time periods*
         *Each time period is represented by a list of lists:*
                 *[ [toDay, toMonth], [entry], [entry], [entry], ... ]*
                 *Where an entry list is:*
                         *[description, firstTime, secondTime]*
                 *Where firstTime and secondTime are:*
                                 *[True, startHour, startMinute, endHour, endMinute]*
                                 *OR*
                                 *[False, 0, 0]  if time is not active*
                         *Description: "Label: DaysOfWeek" (eg. "Weekends: Sat, Sun")*
                         *StartHour, startMinute: 0-24, 0-59 for the start time*
                         *EndHour, endMinute: 0-24, 0-59 for the end time*
         
         *Free-form Profile:*
         *Set the free-form entries for this profile.*
         *Data should be a list of lists, where each entry in the outer list*
         *contains the month, day, hour, minute and value of that entry.*
         *Value is a double if no formula is set, and a string otherwise.*
         *First and last entries cannot be changed.*
         
         *[[month, day, hour, minute, value],...]*
         
         *month: 1-12*
         *day: 1-31*
         *hour: 0-23*
         *minute: 0-59*
      
   .. py:class:: Conditioning_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: external_air
         :classmethod:
         :type: iesve.Conditioning_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "external_air".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'external_air': iesve.Conditioning_type.external_air
             'temperature_from_schedule': iesve.Conditioning_type.temperature_from_schedule
            }
      
      .. py:property:: temperature_from_schedule
         :classmethod:
         :type: iesve.Conditioning_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "temperature_from_schedule".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.Conditioning_type.external_air
             2: iesve.Conditioning_type.temperature_from_schedule
            }
      
   .. py:class:: CoolingCoilModelType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: advanced_cooling_coil
         :classmethod:
         :type: iesve.CoolingCoilModelType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "advanced_cooling_coil".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'simple_cooling_coil': iesve.CoolingCoilModelType.simple_cooling_coil
             'advanced_cooling_coil': iesve.CoolingCoilModelType.advanced_cooling_coil
            }
      
      .. py:property:: simple_cooling_coil
         :classmethod:
         :type: iesve.CoolingCoilModelType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "simple_cooling_coil".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.CoolingCoilModelType.simple_cooling_coil
             1: iesve.CoolingCoilModelType.advanced_cooling_coil
            }
      
   .. py:class:: CoolingMechanism_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_conditioning
         :classmethod:
         :type: iesve.CoolingMechanism_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_conditioning".
      
      .. py:property:: mechanical_ventilation
         :classmethod:
         :type: iesve.CoolingMechanism_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "mechanical_ventilation".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_conditioning': iesve.CoolingMechanism_type.air_conditioning
             'mechanical_ventilation': iesve.CoolingMechanism_type.mechanical_ventilation
             'natural_ventilation': iesve.CoolingMechanism_type.natural_ventilation
            }
      
      .. py:property:: natural_ventilation
         :classmethod:
         :type: iesve.CoolingMechanism_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "natural_ventilation".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.CoolingMechanism_type.air_conditioning
             1: iesve.CoolingMechanism_type.mechanical_ventilation
             2: iesve.CoolingMechanism_type.natural_ventilation
            }
      
   .. py:class:: DailyProfile
   
      *Daily profile.*
   
      .. py:method:: get_data
      
         *get_data() -> profile data*
         
         *Retrieve profile data.  The returned data depends on profile type. All returned*
         *data structures are compatible with the set_data() method.*
           *- Daily profile: a list of [ x, y, formula ] lists that represent the data for the profile.*
           *- Weekly profile: a list of daily profile IDs that make up the weekly profile.*
           *- Yearly profile: a list of lists: [ weekly profile ID, fromDay, toDay ],*
             *where fromDay = year day where the profile becomes active, toDay = last day of profile*
           *- Compact profile: a nested sets of lists, each list representing on/off time periods*
           *- Free form profile : list of lists: [ month, day, hour, minute, value ]*
      
      .. py:property:: id
      
         *(str) Profile ID.*
      
      .. py:method:: is_absolute
      
         *is_absolute() -> bool*
         
         *True if the profile is absolute, else False.*
      
      .. py:method:: is_group
      
         *is_group() -> bool*
         
         *True if the profile is a group profile, False if a daily profile.*
      
      .. py:method:: is_modulating
      
         *is_modulating() -> bool*
         
         *True if the profile is modulating, else False.*
      
      .. py:property:: reference
      
         *(str) Profile reference (name).*
      
      .. py:method:: set_data
      
         *set_data() -> bool*
         
         *Set profile data.  The data to be passed depends on profile type.*
         
         *Daily Profile:*
         *Data should represented by a list of [x,y,formula] lists*
         *[ [x,y,formula], [x,y,formula], ... ]*
         
         *Weekly Profile:*
         *Data should represented by a list of daily profile IDs*
         *[ ID1, ID2, ... ]*
         
         *Yearly Profile:*
          *Data should be represented by a list of [weekly profile ID(string), fromDay(int), toDay(int)] lists*
          *[ [ID1, from1, to1], [ID2, from2, to2], ... ]*
         
         *Compact Profile:*
         *Data should represented by a list of lists that contains compact profile data:*
         
         *The outer list is for the number of time periods*
         *Each time period is represented by a list of lists:*
                 *[ [toDay, toMonth], [entry], [entry], [entry], ... ]*
                 *Where an entry list is:*
                         *[description, firstTime, secondTime]*
                 *Where firstTime and secondTime are:*
                                 *[True, startHour, startMinute, endHour, endMinute]*
                                 *OR*
                                 *[False, 0, 0]  if time is not active*
                         *Description: "Label: DaysOfWeek" (eg. "Weekends: Sat, Sun")*
                         *StartHour, startMinute: 0-24, 0-59 for the start time*
                         *EndHour, endMinute: 0-24, 0-59 for the end time*
         
         *Free-form Profile:*
         *Set the free-form entries for this profile.*
         *Data should be a list of lists, where each entry in the outer list*
         *contains the month, day, hour, minute and value of that entry.*
         *Value is a double if no formula is set, and a string otherwise.*
         *First and last entries cannot be changed.*
         
         *[[month, day, hour, minute, value],...]*
         
         *month: 1-12*
         *day: 1-31*
         *hour: 0-23*
         *minute: 0-59*
      
   .. py:class:: DehumidificationControlOption
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'per_system_level_dry_bulb_or_dew_point_control_only': iesve.DehumidificationControlOption.per_system_level_dry_bulb_or_dew_point_control_only
             'system_supply_air_conditioned_per_zone_relative_humidity_sensors': iesve.DehumidificationControlOption.system_supply_air_conditioned_per_zone_relative_humidity_sensors
            }
      
      .. py:property:: per_system_level_dry_bulb_or_dew_point_control_only
         :classmethod:
         :type: iesve.DehumidificationControlOption
      
         An instance of this class with:
         
         * a value of 0
         * a name of "per_system_level_dry_bulb_or_dew_point_control_only".
      
      .. py:property:: system_supply_air_conditioned_per_zone_relative_humidity_sensors
         :classmethod:
         :type: iesve.DehumidificationControlOption
      
         An instance of this class with:
         
         * a value of 1
         * a name of "system_supply_air_conditioned_per_zone_relative_humidity_sensors".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.DehumidificationControlOption.per_system_level_dry_bulb_or_dew_point_control_only
             1: iesve.DehumidificationControlOption.system_supply_air_conditioned_per_zone_relative_humidity_sensors
            }
      
   .. py:class:: DesignZoneTemperatureSource
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: design_zone_air_temperature
         :classmethod:
         :type: iesve.DesignZoneTemperatureSource
      
         An instance of this class with:
         
         * a value of 0
         * a name of "design_zone_air_temperature".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'design_zone_air_temperature': iesve.DesignZoneTemperatureSource.design_zone_air_temperature
             'temperature_setpoint': iesve.DesignZoneTemperatureSource.temperature_setpoint
            }
      
      .. py:property:: temperature_setpoint
         :classmethod:
         :type: iesve.DesignZoneTemperatureSource
      
         An instance of this class with:
         
         * a value of 1
         * a name of "temperature_setpoint".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.DesignZoneTemperatureSource.design_zone_air_temperature
             1: iesve.DesignZoneTemperatureSource.temperature_setpoint
            }
      
   .. py:class:: DisplayUnits
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: imperial
         :classmethod:
         :type: iesve.DisplayUnits
      
         An instance of this class with:
         
         * a value of 1
         * a name of "imperial".
      
      .. py:property:: metric
         :classmethod:
         :type: iesve.DisplayUnits
      
         An instance of this class with:
         
         * a value of 0
         * a name of "metric".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'metric': iesve.DisplayUnits.metric
             'imperial': iesve.DisplayUnits.imperial
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.DisplayUnits.metric
             1: iesve.DisplayUnits.imperial
            }
      
   .. py:class:: EnergyGain
   
      *Casual Gain data.*
   
      .. py:method:: get
      
         *get() -> Dictionary*
         
         *Returns a Dictionary containing the data for the internal gain.*
      
      .. py:property:: name
      
         *(str) Descriptive string*
      
   .. py:class:: EnergyGain_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: computers
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "computers".
      
      .. py:property:: cooking
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "cooking".
      
      .. py:property:: data_centre_equipment
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "data_centre_equipment".
      
      .. py:property:: local_fans
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "local_fans".
      
      .. py:property:: machinery
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "machinery".
      
      .. py:property:: miscellaneous
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "miscellaneous".
      
      .. py:property:: motors
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "motors".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'machinery': iesve.EnergyGain_type.machinery
             'miscellaneous': iesve.EnergyGain_type.miscellaneous
             'cooking': iesve.EnergyGain_type.cooking
             'computers': iesve.EnergyGain_type.computers
             'data_centre_equipment': iesve.EnergyGain_type.data_centre_equipment
             'refrigeration': iesve.EnergyGain_type.refrigeration
             'process_equipment': iesve.EnergyGain_type.process_equipment
             'local_fans': iesve.EnergyGain_type.local_fans
             'transformers': iesve.EnergyGain_type.transformers
             'motors': iesve.EnergyGain_type.motors
            }
      
      .. py:property:: process_equipment
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "process_equipment".
      
      .. py:property:: refrigeration
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "refrigeration".
      
      .. py:property:: transformers
         :classmethod:
         :type: iesve.EnergyGain_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "transformers".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.EnergyGain_type.machinery
             2: iesve.EnergyGain_type.miscellaneous
             3: iesve.EnergyGain_type.cooking
             4: iesve.EnergyGain_type.computers
             5: iesve.EnergyGain_type.data_centre_equipment
             6: iesve.EnergyGain_type.refrigeration
             7: iesve.EnergyGain_type.process_equipment
             8: iesve.EnergyGain_type.local_fans
             9: iesve.EnergyGain_type.transformers
             10: iesve.EnergyGain_type.motors
            }
      
   .. py:class:: EnergyMeter
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unspecified': iesve.EnergyMeter.unspecified
            }
      
      .. py:property:: unspecified
         :classmethod:
         :type: iesve.EnergyMeter
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unspecified".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.EnergyMeter.unspecified
            }
      
   .. py:class:: EnergySource
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: anthracite
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 16
         * a name of "anthracite".
      
      .. py:property:: biogas
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 9
         * a name of "biogas".
      
      .. py:property:: biomass
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 10
         * a name of "biomass".
      
      .. py:property:: coal
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 4
         * a name of "coal".
      
      .. py:property:: district_heating
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 41
         * a name of "district_heating".
      
      .. py:property:: dual
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 18
         * a name of "dual".
      
      .. py:property:: elec
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 1
         * a name of "elec".
      
      .. py:property:: grid_disp_elec
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 19
         * a name of "grid_disp_elec".
      
      .. py:property:: grid_disp_elec_pv
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 40
         * a name of "grid_disp_elec_pv".
      
      .. py:property:: lpg
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 8
         * a name of "lpg".
      
      .. py:property:: misc_a
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 5
         * a name of "misc_a".
      
      .. py:property:: misc_b
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 6
         * a name of "misc_b".
      
      .. py:property:: misc_c
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 12
         * a name of "misc_c".
      
      .. py:property:: misc_d
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 13
         * a name of "misc_d".
      
      .. py:property:: misc_e
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 14
         * a name of "misc_e".
      
      .. py:property:: misc_f
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 15
         * a name of "misc_f".
      
      .. py:property:: misc_g
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 20
         * a name of "misc_g".
      
      .. py:property:: misc_h
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 21
         * a name of "misc_h".
      
      .. py:property:: misc_i
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 22
         * a name of "misc_i".
      
      .. py:property:: misc_j
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 23
         * a name of "misc_j".
      
      .. py:property:: misc_k
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 24
         * a name of "misc_k".
      
      .. py:property:: misc_l
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 25
         * a name of "misc_l".
      
      .. py:property:: misc_m
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 26
         * a name of "misc_m".
      
      .. py:property:: misc_n
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 27
         * a name of "misc_n".
      
      .. py:property:: misc_o
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 28
         * a name of "misc_o".
      
      .. py:property:: misc_p
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 29
         * a name of "misc_p".
      
      .. py:property:: misc_q
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 30
         * a name of "misc_q".
      
      .. py:property:: misc_r
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 31
         * a name of "misc_r".
      
      .. py:property:: misc_s
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 32
         * a name of "misc_s".
      
      .. py:property:: misc_t
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 33
         * a name of "misc_t".
      
      .. py:property:: misc_u
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 34
         * a name of "misc_u".
      
      .. py:property:: misc_v
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 35
         * a name of "misc_v".
      
      .. py:property:: misc_w
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 36
         * a name of "misc_w".
      
      .. py:property:: misc_x
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 37
         * a name of "misc_x".
      
      .. py:property:: misc_y
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 38
         * a name of "misc_y".
      
      .. py:property:: misc_z
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 39
         * a name of "misc_z".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unspecified': iesve.EnergySource.unspecified
             'elec': iesve.EnergySource.elec
             'nat_gas': iesve.EnergySource.nat_gas
             'oil': iesve.EnergySource.oil
             'coal': iesve.EnergySource.coal
             'misc_a': iesve.EnergySource.misc_a
             'misc_b': iesve.EnergySource.misc_b
             'none': iesve.EnergySource.none
             'lpg': iesve.EnergySource.lpg
             'biogas': iesve.EnergySource.biogas
             'biomass': iesve.EnergySource.biomass
             'waste': iesve.EnergySource.waste
             'misc_c': iesve.EnergySource.misc_c
             'misc_d': iesve.EnergySource.misc_d
             'misc_e': iesve.EnergySource.misc_e
             'misc_f': iesve.EnergySource.misc_f
             'anthracite': iesve.EnergySource.anthracite
             'smokeless': iesve.EnergySource.smokeless
             'dual': iesve.EnergySource.dual
             'grid_disp_elec': iesve.EnergySource.grid_disp_elec
             'misc_g': iesve.EnergySource.misc_g
             'misc_h': iesve.EnergySource.misc_h
             'misc_i': iesve.EnergySource.misc_i
             'misc_j': iesve.EnergySource.misc_j
             'misc_k': iesve.EnergySource.misc_k
             'misc_l': iesve.EnergySource.misc_l
             'misc_m': iesve.EnergySource.misc_m
             'misc_n': iesve.EnergySource.misc_n
             'misc_o': iesve.EnergySource.misc_o
             'misc_p': iesve.EnergySource.misc_p
             'misc_q': iesve.EnergySource.misc_q
             'misc_r': iesve.EnergySource.misc_r
             'misc_s': iesve.EnergySource.misc_s
             'misc_t': iesve.EnergySource.misc_t
             'misc_u': iesve.EnergySource.misc_u
             'misc_v': iesve.EnergySource.misc_v
             'misc_w': iesve.EnergySource.misc_w
             'misc_x': iesve.EnergySource.misc_x
             'misc_y': iesve.EnergySource.misc_y
             'misc_z': iesve.EnergySource.misc_z
             'district_heating': iesve.EnergySource.district_heating
             'grid_disp_elec_pv': iesve.EnergySource.grid_disp_elec_pv
            }
      
      .. py:property:: nat_gas
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 2
         * a name of "nat_gas".
      
      .. py:property:: none
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 7
         * a name of "none".
      
      .. py:property:: oil
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 3
         * a name of "oil".
      
      .. py:property:: smokeless
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 17
         * a name of "smokeless".
      
      .. py:property:: unspecified
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unspecified".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.EnergySource.unspecified
             1: iesve.EnergySource.elec
             2: iesve.EnergySource.nat_gas
             3: iesve.EnergySource.oil
             4: iesve.EnergySource.coal
             5: iesve.EnergySource.misc_a
             6: iesve.EnergySource.misc_b
             7: iesve.EnergySource.none
             8: iesve.EnergySource.lpg
             9: iesve.EnergySource.biogas
             10: iesve.EnergySource.biomass
             11: iesve.EnergySource.waste
             12: iesve.EnergySource.misc_c
             13: iesve.EnergySource.misc_d
             14: iesve.EnergySource.misc_e
             15: iesve.EnergySource.misc_f
             16: iesve.EnergySource.anthracite
             17: iesve.EnergySource.smokeless
             18: iesve.EnergySource.dual
             19: iesve.EnergySource.grid_disp_elec
             20: iesve.EnergySource.misc_g
             21: iesve.EnergySource.misc_h
             22: iesve.EnergySource.misc_i
             23: iesve.EnergySource.misc_j
             24: iesve.EnergySource.misc_k
             25: iesve.EnergySource.misc_l
             26: iesve.EnergySource.misc_m
             27: iesve.EnergySource.misc_n
             28: iesve.EnergySource.misc_o
             29: iesve.EnergySource.misc_p
             30: iesve.EnergySource.misc_q
             31: iesve.EnergySource.misc_r
             32: iesve.EnergySource.misc_s
             33: iesve.EnergySource.misc_t
             34: iesve.EnergySource.misc_u
             35: iesve.EnergySource.misc_v
             36: iesve.EnergySource.misc_w
             37: iesve.EnergySource.misc_x
             38: iesve.EnergySource.misc_y
             39: iesve.EnergySource.misc_z
             41: iesve.EnergySource.district_heating
             40: iesve.EnergySource.grid_disp_elec_pv
            }
      
      .. py:property:: waste
         :classmethod:
         :type: iesve.EnergySource
      
         An instance of this class with:
         
         * a value of 11
         * a name of "waste".
      
   .. py:class:: EnergySources
   
      *Interface for energy sources*
   
      .. py:method:: get_all_energy_source_data
      
         *get_all_energy_source_data() -> list*
         
         *Get all energy source data as a list of dictionaries*
         *using averaged source and carbon factors if using monthly or hourly modes.*
         *Dictionary entries are name, carbon_emissions_factor, source_energy_factor, fuel_code and id.*
      
      .. py:method:: get_all_energy_source_data_non_averaged
      
         *get_all_energy_source_data_non_averaged() -> list*
         
         *Get all energy source data as a list of dictionaries*
         *using non-averaged source and carbon factors (assumes 8760 timesteps).*
         *Dictionary entries are name, carbon_emissions_factor, source_energy_factor, fuel_code and id.*
      
      .. py:method:: get_energy_meter
      
         *meter_id*
      
      .. py:method:: get_energy_source_data_by_id
      
         *id*
      
   .. py:class:: EnergyUse
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unspecified': iesve.EnergyUse.unspecified
             'prm_interior_lighting': iesve.EnergyUse.prm_interior_lighting
             'prm_exterior_lighting': iesve.EnergyUse.prm_exterior_lighting
             'prm_space_heating': iesve.EnergyUse.prm_space_heating
             'prm_space_cooling': iesve.EnergyUse.prm_space_cooling
             'prm_pumps': iesve.EnergyUse.prm_pumps
             'prm_heat_rejection': iesve.EnergyUse.prm_heat_rejection
             'prm_fans_interior_central': iesve.EnergyUse.prm_fans_interior_central
             'prm_fans_interior_local': iesve.EnergyUse.prm_fans_interior_local
             'prm_fans_garage': iesve.EnergyUse.prm_fans_garage
             'prm_fans_exhaust': iesve.EnergyUse.prm_fans_exhaust
             'prm_fans_process': iesve.EnergyUse.prm_fans_process
             'prm_services_water_heating': iesve.EnergyUse.prm_services_water_heating
             'prm_receptacle_equipment': iesve.EnergyUse.prm_receptacle_equipment
             'prm_interior_lighting_process': iesve.EnergyUse.prm_interior_lighting_process
             'prm_refrigeration': iesve.EnergyUse.prm_refrigeration
             'prm_data_center_equipment': iesve.EnergyUse.prm_data_center_equipment
             'prm_cooking': iesve.EnergyUse.prm_cooking
             'prm_elevators_escalators': iesve.EnergyUse.prm_elevators_escalators
             'prm_other_process': iesve.EnergyUse.prm_other_process
             'prm_humidification': iesve.EnergyUse.prm_humidification
             'prm_chp': iesve.EnergyUse.prm_chp
             'prm_elec_gen_chp': iesve.EnergyUse.prm_elec_gen_chp
             'prm_elec_gen_wind': iesve.EnergyUse.prm_elec_gen_wind
             'prm_elec_gen_pv': iesve.EnergyUse.prm_elec_gen_pv
             'prm_transformer': iesve.EnergyUse.prm_transformer
             'prm_motor': iesve.EnergyUse.prm_motor
             'prm_interior_lighting_unregulated': iesve.EnergyUse.prm_interior_lighting_unregulated
            }
      
      .. py:property:: prm_chp
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 21
         * a name of "prm_chp".
      
      .. py:property:: prm_cooking
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 17
         * a name of "prm_cooking".
      
      .. py:property:: prm_data_center_equipment
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 16
         * a name of "prm_data_center_equipment".
      
      .. py:property:: prm_elec_gen_chp
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 22
         * a name of "prm_elec_gen_chp".
      
      .. py:property:: prm_elec_gen_pv
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 24
         * a name of "prm_elec_gen_pv".
      
      .. py:property:: prm_elec_gen_wind
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 23
         * a name of "prm_elec_gen_wind".
      
      .. py:property:: prm_elevators_escalators
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 18
         * a name of "prm_elevators_escalators".
      
      .. py:property:: prm_exterior_lighting
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 2
         * a name of "prm_exterior_lighting".
      
      .. py:property:: prm_fans_exhaust
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 10
         * a name of "prm_fans_exhaust".
      
      .. py:property:: prm_fans_garage
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 9
         * a name of "prm_fans_garage".
      
      .. py:property:: prm_fans_interior_central
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 7
         * a name of "prm_fans_interior_central".
      
      .. py:property:: prm_fans_interior_local
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 8
         * a name of "prm_fans_interior_local".
      
      .. py:property:: prm_fans_process
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 11
         * a name of "prm_fans_process".
      
      .. py:property:: prm_heat_rejection
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 6
         * a name of "prm_heat_rejection".
      
      .. py:property:: prm_humidification
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 20
         * a name of "prm_humidification".
      
      .. py:property:: prm_interior_lighting
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 1
         * a name of "prm_interior_lighting".
      
      .. py:property:: prm_interior_lighting_process
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 14
         * a name of "prm_interior_lighting_process".
      
      .. py:property:: prm_interior_lighting_unregulated
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 27
         * a name of "prm_interior_lighting_unregulated".
      
      .. py:property:: prm_motor
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 26
         * a name of "prm_motor".
      
      .. py:property:: prm_other_process
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 19
         * a name of "prm_other_process".
      
      .. py:property:: prm_pumps
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 5
         * a name of "prm_pumps".
      
      .. py:property:: prm_receptacle_equipment
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 13
         * a name of "prm_receptacle_equipment".
      
      .. py:property:: prm_refrigeration
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 15
         * a name of "prm_refrigeration".
      
      .. py:property:: prm_services_water_heating
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 12
         * a name of "prm_services_water_heating".
      
      .. py:property:: prm_space_cooling
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 4
         * a name of "prm_space_cooling".
      
      .. py:property:: prm_space_heating
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 3
         * a name of "prm_space_heating".
      
      .. py:property:: prm_transformer
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 25
         * a name of "prm_transformer".
      
      .. py:property:: unspecified
         :classmethod:
         :type: iesve.EnergyUse
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unspecified".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.EnergyUse.unspecified
             1: iesve.EnergyUse.prm_interior_lighting
             2: iesve.EnergyUse.prm_exterior_lighting
             3: iesve.EnergyUse.prm_space_heating
             4: iesve.EnergyUse.prm_space_cooling
             5: iesve.EnergyUse.prm_pumps
             6: iesve.EnergyUse.prm_heat_rejection
             7: iesve.EnergyUse.prm_fans_interior_central
             8: iesve.EnergyUse.prm_fans_interior_local
             9: iesve.EnergyUse.prm_fans_garage
             10: iesve.EnergyUse.prm_fans_exhaust
             11: iesve.EnergyUse.prm_fans_process
             12: iesve.EnergyUse.prm_services_water_heating
             13: iesve.EnergyUse.prm_receptacle_equipment
             14: iesve.EnergyUse.prm_interior_lighting_process
             15: iesve.EnergyUse.prm_refrigeration
             16: iesve.EnergyUse.prm_data_center_equipment
             17: iesve.EnergyUse.prm_cooking
             18: iesve.EnergyUse.prm_elevators_escalators
             19: iesve.EnergyUse.prm_other_process
             20: iesve.EnergyUse.prm_humidification
             21: iesve.EnergyUse.prm_chp
             22: iesve.EnergyUse.prm_elec_gen_chp
             23: iesve.EnergyUse.prm_elec_gen_wind
             24: iesve.EnergyUse.prm_elec_gen_pv
             25: iesve.EnergyUse.prm_transformer
             26: iesve.EnergyUse.prm_motor
             27: iesve.EnergyUse.prm_interior_lighting_unregulated
            }
      
   .. py:class:: ExhaustMakeUpAirOption
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: make_up_air_includes_fixed_percentage_transfer_air
         :classmethod:
         :type: iesve.ExhaustMakeUpAirOption
      
         An instance of this class with:
         
         * a value of 3
         * a name of "make_up_air_includes_fixed_percentage_transfer_air".
      
      .. py:property:: make_up_air_is_hundred_percent_primary_air
         :classmethod:
         :type: iesve.ExhaustMakeUpAirOption
      
         An instance of this class with:
         
         * a value of 0
         * a name of "make_up_air_is_hundred_percent_primary_air".
      
      .. py:property:: make_up_air_is_hundred_percent_transfer_air
         :classmethod:
         :type: iesve.ExhaustMakeUpAirOption
      
         An instance of this class with:
         
         * a value of 1
         * a name of "make_up_air_is_hundred_percent_transfer_air".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'make_up_air_is_hundred_percent_primary_air': iesve.ExhaustMakeUpAirOption.make_up_air_is_hundred_percent_primary_air
             'make_up_air_is_hundred_percent_transfer_air': iesve.ExhaustMakeUpAirOption.make_up_air_is_hundred_percent_transfer_air
             'transfer_air_makes_up_difference': iesve.ExhaustMakeUpAirOption.transfer_air_makes_up_difference
             'make_up_air_includes_fixed_percentage_transfer_air': iesve.ExhaustMakeUpAirOption.make_up_air_includes_fixed_percentage_transfer_air
            }
      
      .. py:property:: transfer_air_makes_up_difference
         :classmethod:
         :type: iesve.ExhaustMakeUpAirOption
      
         An instance of this class with:
         
         * a value of 2
         * a name of "transfer_air_makes_up_difference".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ExhaustMakeUpAirOption.make_up_air_is_hundred_percent_primary_air
             1: iesve.ExhaustMakeUpAirOption.make_up_air_is_hundred_percent_transfer_air
             2: iesve.ExhaustMakeUpAirOption.transfer_air_makes_up_difference
             3: iesve.ExhaustMakeUpAirOption.make_up_air_includes_fixed_percentage_transfer_air
            }
      
   .. py:class:: FreeFormProfile
   
      *Free form profile.*
   
      .. py:method:: get_data
      
         *get_data() -> profile data*
         
         *Retrieve profile data.  The returned data depends on profile type. All returned*
         *data structures are compatible with the set_data() method.*
           *- Daily profile: a list of [ x, y, formula ] lists that represent the data for the profile.*
           *- Weekly profile: a list of daily profile IDs that make up the weekly profile.*
           *- Yearly profile: a list of lists: [ weekly profile ID, fromDay, toDay ],*
             *where fromDay = year day where the profile becomes active, toDay = last day of profile*
           *- Compact profile: a nested sets of lists, each list representing on/off time periods*
           *- Free form profile : list of lists: [ month, day, hour, minute, value ]*
      
      .. py:property:: id
      
         *(str) Profile ID.*
      
      .. py:method:: is_absolute
      
         *is_absolute() -> bool*
         
         *True if the profile is absolute, else False.*
      
      .. py:method:: is_compact
      
         *is_compact() -> bool*
         
         *True if the profile is a compact profile, else False.*
      
      .. py:method:: is_freeform
      
         *is_freeform() -> bool*
         
         *True if the profile is a free form profile, else False.*
      
      .. py:method:: is_graphable
      
         *is_graphable() -> bool*
         
         *True if the free form data was loaded successfully and contains no*
         *error. False otherwise.*
      
      .. py:method:: is_group
      
         *is_group() -> bool*
         
         *True if the profile is a group profile, False if a daily profile.*
      
      .. py:method:: is_modulating
      
         *is_modulating() -> bool*
         
         *True if the profile is modulating, else False.*
      
      .. py:method:: is_weekly
      
         *is_weekly() -> bool*
         
         *True if the profile is a weekly profile, else False.*
      
      .. py:method:: is_yearly
      
         *is_yearly() -> bool*
         
         *True if the profile is a yearly (annual) profile, else False.*
      
      .. py:method:: load_data
      
         *load_data(hide_ui)*
         
         *Load the free form profile data.  Note that this may take a long time.*
         *The optional bool parameter hide_ui (default: True) can be passed as*
         *False to show a wait indicator whilst loading.*
      
      .. py:property:: reference
      
         *(str) Profile reference (name).*
      
      .. py:method:: save_data
      
         *save_data() -> void*
         
         *Save the Free-form profile data to disk.*
      
      .. py:method:: set_data
      
         *set_data() -> bool*
         
         *Set profile data.  The data to be passed depends on profile type.*
         
         *Daily Profile:*
         *Data should represented by a list of [x,y,formula] lists*
         *[ [x,y,formula], [x,y,formula], ... ]*
         
         *Weekly Profile:*
         *Data should represented by a list of daily profile IDs*
         *[ ID1, ID2, ... ]*
         
         *Yearly Profile:*
          *Data should be represented by a list of [weekly profile ID(string), fromDay(int), toDay(int)] lists*
          *[ [ID1, from1, to1], [ID2, from2, to2], ... ]*
         
         *Compact Profile:*
         *Data should represented by a list of lists that contains compact profile data:*
         
         *The outer list is for the number of time periods*
         *Each time period is represented by a list of lists:*
                 *[ [toDay, toMonth], [entry], [entry], [entry], ... ]*
                 *Where an entry list is:*
                         *[description, firstTime, secondTime]*
                 *Where firstTime and secondTime are:*
                                 *[True, startHour, startMinute, endHour, endMinute]*
                                 *OR*
                                 *[False, 0, 0]  if time is not active*
                         *Description: "Label: DaysOfWeek" (eg. "Weekends: Sat, Sun")*
                         *StartHour, startMinute: 0-24, 0-59 for the start time*
                         *EndHour, endMinute: 0-24, 0-59 for the end time*
         
         *Free-form Profile:*
         *Set the free-form entries for this profile.*
         *Data should be a list of lists, where each entry in the outer list*
         *contains the month, day, hour, minute and value of that entry.*
         *Value is a double if no formula is set, and a string otherwise.*
         *First and last entries cannot be changed.*
         
         *[[month, day, hour, minute, value],...]*
         
         *month: 1-12*
         *day: 1-31*
         *hour: 0-23*
         *minute: 0-59*
      
   .. py:class:: GarageFanControlScheme
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: modulate_airflow
         :classmethod:
         :type: iesve.GarageFanControlScheme
      
         An instance of this class with:
         
         * a value of 4
         * a name of "modulate_airflow".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'on_occupied': iesve.GarageFanControlScheme.on_occupied
             'on_occupied_plus_extension': iesve.GarageFanControlScheme.on_occupied_plus_extension
             'on_continously': iesve.GarageFanControlScheme.on_continously
             'reduce_airflow_unoccupied': iesve.GarageFanControlScheme.reduce_airflow_unoccupied
             'modulate_airflow': iesve.GarageFanControlScheme.modulate_airflow
            }
      
      .. py:property:: on_continously
         :classmethod:
         :type: iesve.GarageFanControlScheme
      
         An instance of this class with:
         
         * a value of 2
         * a name of "on_continously".
      
      .. py:property:: on_occupied
         :classmethod:
         :type: iesve.GarageFanControlScheme
      
         An instance of this class with:
         
         * a value of 0
         * a name of "on_occupied".
      
      .. py:property:: on_occupied_plus_extension
         :classmethod:
         :type: iesve.GarageFanControlScheme
      
         An instance of this class with:
         
         * a value of 1
         * a name of "on_occupied_plus_extension".
      
      .. py:property:: reduce_airflow_unoccupied
         :classmethod:
         :type: iesve.GarageFanControlScheme
      
         An instance of this class with:
         
         * a value of 3
         * a name of "reduce_airflow_unoccupied".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.GarageFanControlScheme.on_occupied
             1: iesve.GarageFanControlScheme.on_occupied_plus_extension
             2: iesve.GarageFanControlScheme.on_continously
             3: iesve.GarageFanControlScheme.reduce_airflow_unoccupied
             4: iesve.GarageFanControlScheme.modulate_airflow
            }
      
   .. py:class:: GroupProfile
   
      *Weekly and Yearly group profiles.*
   
      .. py:method:: get_data
      
         *get_data() -> profile data*
         
         *Retrieve profile data.  The returned data depends on profile type. All returned*
         *data structures are compatible with the set_data() method.*
           *- Daily profile: a list of [ x, y, formula ] lists that represent the data for the profile.*
           *- Weekly profile: a list of daily profile IDs that make up the weekly profile.*
           *- Yearly profile: a list of lists: [ weekly profile ID, fromDay, toDay ],*
             *where fromDay = year day where the profile becomes active, toDay = last day of profile*
           *- Compact profile: a nested sets of lists, each list representing on/off time periods*
           *- Free form profile : list of lists: [ month, day, hour, minute, value ]*
      
      .. py:property:: id
      
         *(str) Profile ID.*
      
      .. py:method:: is_absolute
      
         *is_absolute() -> bool*
         
         *True if the profile is absolute, else False.*
      
      .. py:method:: is_compact
      
         *is_compact() -> bool*
         
         *True if the profile is a compact profile, else False.*
      
      .. py:method:: is_freeform
      
         *is_freeform() -> bool*
         
         *True if the profile is a free form profile, else False.*
      
      .. py:method:: is_group
      
         *is_group() -> bool*
         
         *True if the profile is a group profile, False if a daily profile.*
      
      .. py:method:: is_modulating
      
         *is_modulating() -> bool*
         
         *True if the profile is modulating, else False.*
      
      .. py:method:: is_weekly
      
         *is_weekly() -> bool*
         
         *True if the profile is a weekly profile, else False.*
      
      .. py:method:: is_yearly
      
         *is_yearly() -> bool*
         
         *True if the profile is a yearly (annual) profile, else False.*
      
      .. py:property:: reference
      
         *(str) Profile reference (name).*
      
      .. py:method:: set_data
      
         *set_data() -> bool*
         
         *Set profile data.  The data to be passed depends on profile type.*
         
         *Daily Profile:*
         *Data should represented by a list of [x,y,formula] lists*
         *[ [x,y,formula], [x,y,formula], ... ]*
         
         *Weekly Profile:*
         *Data should represented by a list of daily profile IDs*
         *[ ID1, ID2, ... ]*
         
         *Yearly Profile:*
          *Data should be represented by a list of [weekly profile ID(string), fromDay(int), toDay(int)] lists*
          *[ [ID1, from1, to1], [ID2, from2, to2], ... ]*
         
         *Compact Profile:*
         *Data should represented by a list of lists that contains compact profile data:*
         
         *The outer list is for the number of time periods*
         *Each time period is represented by a list of lists:*
                 *[ [toDay, toMonth], [entry], [entry], [entry], ... ]*
                 *Where an entry list is:*
                         *[description, firstTime, secondTime]*
                 *Where firstTime and secondTime are:*
                                 *[True, startHour, startMinute, endHour, endMinute]*
                                 *OR*
                                 *[False, 0, 0]  if time is not active*
                         *Description: "Label: DaysOfWeek" (eg. "Weekends: Sat, Sun")*
                         *StartHour, startMinute: 0-24, 0-59 for the start time*
                         *EndHour, endMinute: 0-24, 0-59 for the end time*
         
         *Free-form Profile:*
         *Set the free-form entries for this profile.*
         *Data should be a list of lists, where each entry in the outer list*
         *contains the month, day, hour, minute and value of that entry.*
         *Value is a double if no formula is set, and a string otherwise.*
         *First and last entries cannot be changed.*
         
         *[[month, day, hour, minute, value],...]*
         
         *month: 1-12*
         *day: 1-31*
         *hour: 0-23*
         *minute: 0-59*
      
   .. py:class:: HVACACCCalculationStatus
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: autocalc_complete
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 1
         * a name of "autocalc_complete".
      
      .. py:property:: autocalc_notposs_error9
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 11
         * a name of "autocalc_notposs_error9".
      
      .. py:property:: autocalc_notposs_error_unknown
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 12
         * a name of "autocalc_notposs_error_unknown".
      
      .. py:property:: autocalc_ready
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 0
         * a name of "autocalc_ready".
      
      .. py:property:: autocalc_warning8
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 10
         * a name of "autocalc_warning8".
      
      .. py:property:: mancalc_complete
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 31
         * a name of "mancalc_complete".
      
      .. py:property:: mancalc_notposs_error1
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 32
         * a name of "mancalc_notposs_error1".
      
      .. py:property:: mancalc_notposs_error10
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 41
         * a name of "mancalc_notposs_error10".
      
      .. py:property:: mancalc_notposs_error2
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 33
         * a name of "mancalc_notposs_error2".
      
      .. py:property:: mancalc_notposs_error3
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 34
         * a name of "mancalc_notposs_error3".
      
      .. py:property:: mancalc_notposs_error4
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 35
         * a name of "mancalc_notposs_error4".
      
      .. py:property:: mancalc_notposs_error5
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 36
         * a name of "mancalc_notposs_error5".
      
      .. py:property:: mancalc_notposs_error6
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 37
         * a name of "mancalc_notposs_error6".
      
      .. py:property:: mancalc_notposs_error7
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 38
         * a name of "mancalc_notposs_error7".
      
      .. py:property:: mancalc_notposs_error8
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 39
         * a name of "mancalc_notposs_error8".
      
      .. py:property:: mancalc_notposs_error9
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 40
         * a name of "mancalc_notposs_error9".
      
      .. py:property:: mancalc_notposs_error_unknown
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 42
         * a name of "mancalc_notposs_error_unknown".
      
      .. py:property:: mancalc_ready
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 30
         * a name of "mancalc_ready".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'autocalc_ready': iesve.HVACACCCalculationStatus.autocalc_ready
             'autocalc_complete': iesve.HVACACCCalculationStatus.autocalc_complete
             'notposs_contactfactor': iesve.HVACACCCalculationStatus.notposs_contactfactor
             'notposs_error1': iesve.HVACACCCalculationStatus.notposs_error1
             'notposs_error2': iesve.HVACACCCalculationStatus.notposs_error2
             'notposs_error3': iesve.HVACACCCalculationStatus.notposs_error3
             'notposs_error4': iesve.HVACACCCalculationStatus.notposs_error4
             'notposs_error5': iesve.HVACACCCalculationStatus.notposs_error5
             'notposs_error6': iesve.HVACACCCalculationStatus.notposs_error6
             'notposs_error7': iesve.HVACACCCalculationStatus.notposs_error7
             'autocalc_warning8': iesve.HVACACCCalculationStatus.autocalc_warning8
             'autocalc_notposs_error9': iesve.HVACACCCalculationStatus.autocalc_notposs_error9
             'autocalc_notposs_error_unknown': iesve.HVACACCCalculationStatus.autocalc_notposs_error_unknown
             'mancalc_ready': iesve.HVACACCCalculationStatus.mancalc_ready
             'mancalc_complete': iesve.HVACACCCalculationStatus.mancalc_complete
             'mancalc_notposs_error1': iesve.HVACACCCalculationStatus.mancalc_notposs_error1
             'mancalc_notposs_error2': iesve.HVACACCCalculationStatus.mancalc_notposs_error2
             'mancalc_notposs_error3': iesve.HVACACCCalculationStatus.mancalc_notposs_error3
             'mancalc_notposs_error4': iesve.HVACACCCalculationStatus.mancalc_notposs_error4
             'mancalc_notposs_error5': iesve.HVACACCCalculationStatus.mancalc_notposs_error5
             'mancalc_notposs_error6': iesve.HVACACCCalculationStatus.mancalc_notposs_error6
             'mancalc_notposs_error7': iesve.HVACACCCalculationStatus.mancalc_notposs_error7
             'mancalc_notposs_error8': iesve.HVACACCCalculationStatus.mancalc_notposs_error8
             'mancalc_notposs_error9': iesve.HVACACCCalculationStatus.mancalc_notposs_error9
             'mancalc_notposs_error10': iesve.HVACACCCalculationStatus.mancalc_notposs_error10
             'mancalc_notposs_error_unknown': iesve.HVACACCCalculationStatus.mancalc_notposs_error_unknown
            }
      
      .. py:property:: notposs_contactfactor
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 2
         * a name of "notposs_contactfactor".
      
      .. py:property:: notposs_error1
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 3
         * a name of "notposs_error1".
      
      .. py:property:: notposs_error2
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 4
         * a name of "notposs_error2".
      
      .. py:property:: notposs_error3
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 5
         * a name of "notposs_error3".
      
      .. py:property:: notposs_error4
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 6
         * a name of "notposs_error4".
      
      .. py:property:: notposs_error5
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 7
         * a name of "notposs_error5".
      
      .. py:property:: notposs_error6
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 8
         * a name of "notposs_error6".
      
      .. py:property:: notposs_error7
         :classmethod:
         :type: iesve.HVACACCCalculationStatus
      
         An instance of this class with:
         
         * a value of 9
         * a name of "notposs_error7".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACACCCalculationStatus.autocalc_ready
             1: iesve.HVACACCCalculationStatus.autocalc_complete
             2: iesve.HVACACCCalculationStatus.notposs_contactfactor
             3: iesve.HVACACCCalculationStatus.notposs_error1
             4: iesve.HVACACCCalculationStatus.notposs_error2
             5: iesve.HVACACCCalculationStatus.notposs_error3
             6: iesve.HVACACCCalculationStatus.notposs_error4
             7: iesve.HVACACCCalculationStatus.notposs_error5
             8: iesve.HVACACCCalculationStatus.notposs_error6
             9: iesve.HVACACCCalculationStatus.notposs_error7
             10: iesve.HVACACCCalculationStatus.autocalc_warning8
             11: iesve.HVACACCCalculationStatus.autocalc_notposs_error9
             12: iesve.HVACACCCalculationStatus.autocalc_notposs_error_unknown
             30: iesve.HVACACCCalculationStatus.mancalc_ready
             31: iesve.HVACACCCalculationStatus.mancalc_complete
             32: iesve.HVACACCCalculationStatus.mancalc_notposs_error1
             33: iesve.HVACACCCalculationStatus.mancalc_notposs_error2
             34: iesve.HVACACCCalculationStatus.mancalc_notposs_error3
             35: iesve.HVACACCCalculationStatus.mancalc_notposs_error4
             36: iesve.HVACACCCalculationStatus.mancalc_notposs_error5
             37: iesve.HVACACCCalculationStatus.mancalc_notposs_error6
             38: iesve.HVACACCCalculationStatus.mancalc_notposs_error7
             39: iesve.HVACACCCalculationStatus.mancalc_notposs_error8
             40: iesve.HVACACCCalculationStatus.mancalc_notposs_error9
             41: iesve.HVACACCCalculationStatus.mancalc_notposs_error10
             42: iesve.HVACACCCalculationStatus.mancalc_notposs_error_unknown
            }
      
   .. py:class:: HVACACCSizingMode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: autosizing
         :classmethod:
         :type: iesve.HVACACCSizingMode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "autosizing".
      
      .. py:property:: both
         :classmethod:
         :type: iesve.HVACACCSizingMode
      
         An instance of this class with:
         
         * a value of 2
         * a name of "both".
      
      .. py:property:: manual
         :classmethod:
         :type: iesve.HVACACCSizingMode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "manual".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'autosizing': iesve.HVACACCSizingMode.autosizing
             'manual': iesve.HVACACCSizingMode.manual
             'both': iesve.HVACACCSizingMode.both
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACACCSizingMode.autosizing
             1: iesve.HVACACCSizingMode.manual
             2: iesve.HVACACCSizingMode.both
            }
      
   .. py:class:: HVACAbstractBoiler
   
      *Interface for HVAC abstract boiler*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_losses
      
         *(float) Distribution losses*
      
      .. py:property:: electrical_circulation_power
      
         *(float) Electrical circulation power*
      
      .. py:property:: heating_plant_type
      
         *(int) Heating plant type*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_dhw_boiler
      
         *(bool) Whether it is a DHW boiler. True if so, False otherwise*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(int) Whether output capacity is sized. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model_type
      
         *(HVACBoilerType) Model type*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_part_load_entries
      
         *(int) Number of part load entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sequence_number
      
         *(int) Sequence number*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: uses_chp
      
         *(bool) Whether CHP is used. True if so, False otherwise.*
      
      .. py:property:: uses_water_source_chp
      
         *(bool) Whether water source CHP is used. True if so, False otherwise.*
      
   .. py:class:: HVACAbstractCHRHeatExchanger
   
      *Interface for HVAC heat exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: capacity
      
         *(float, W) Design capacity*
      
      .. py:method:: get_approach
      
         *get_approach( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_approach(type) -> float*
             **
             *Get the design approach*
      
      .. py:method:: get_effectiveness
      
         *get_effectiveness( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_effectiveness(type) -> float*
             **
             *Get the heat exchanger effectiveness*
      
      .. py:method:: get_load_side_entering_temperature
      
         *get_load_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_entering_temperature(type) -> float*
             **
             *Get the design load side entering temperature*
      
      .. py:method:: get_load_side_leaving_temperature
      
         *get_load_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_leaving_temperature(type) -> float*
             **
             *Get the design load leaving temperature*
      
      .. py:method:: get_source_flow_rate
      
         *get_source_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_flow_rate(type) -> float*
             **
             *Get the design source flow rate*
      
      .. py:method:: get_source_side_entering_temperature
      
         *get_source_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_entering_temperature(type) -> float*
             **
             *Get the design source side entering temperature*
      
      .. py:method:: get_source_side_leaving_temperature
      
         *get_source_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_leaving_temperature(type) -> float*
             **
             *Get the design source side leaving temperature*
      
      .. py:method:: get_supply_flow_rate
      
         *get_supply_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_supply_flow_rate(type) -> float*
             **
             *Get the design supply flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: inlet_temperature_delta_t
      
         *(float) Design inlet temperature delta T*
      
      .. py:method:: is_design_heat_rejection_autosized
      
         *is_design_heat_rejection_autosized( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *is_design_heat_rejection_autosized(type) -> bool*
             **
             *Check whether the design heat rejection is autosized for the given HVACWaterWaterHeatExchangerDataType.*
             *Returns True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractChiller
   
      *Interface for HVAC abstract chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractComponent
   
      *Interface for HVAC abstract component*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractController
   
      *Interface for HVAC abstract controller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACAbstractControllerWithSensor
   
      *Interface for HVAC abstract controller with sensor*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: deadband
      
         *(float) Deadband*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_active_set_point
      
         *(int) Whether there is an active set point. 1 if so, 0 otherwise.*
      
      .. py:property:: is_proportional_control
      
         *(int) Whether there is a proportional controller. 1 if so, 0 otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_change_per_time_step
      
         *(float) Maximum change per time step*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: midband
      
         *(float) Midband*
      
      .. py:property:: midband_mode
      
         *(int) Midband mode*
      
      .. py:property:: midband_point_profile_id
      
         *(string) Midband point profile ID*
      
      .. py:property:: min_control_signal_value
      
         *(float) Minimum control signal value*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: on_off_max_signal_mode
      
         *(int) On/off maximum signal mode*
      
      .. py:property:: on_off_max_signal_profile_id
      
         *(string) On/off max signal profile ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: prop_min_signal_profile_id
      
         *(string) Proportional minimum signal profile ID*
      
      .. py:property:: proportional_bandwidth
      
         *(float) Proportional bandwidth*
      
      .. py:property:: proportional_controller_id
      
         *(string) Proportional controller ID*
      
      .. py:property:: proportional_min_signal_mode
      
         *(int) Proportional minimum signal mode*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: set_point
      
         *(float) Set point*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACAbstractDXCoolingSystem
   
      *Interface for HVAC abstract DX cooling system*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: coefficient
      
         *(float) Coefficient*
      
      .. py:property:: coil_wet_bulb_temp
      
         *(float) Coil wet bulb temperature*
      
      .. py:property:: condenser_type
      
         *(HVACDXCoolingCondenserType) Condenser type*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outdoor_air_dry_bulb_temp
      
         *(float) Outdoor air dry bulb temperature*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractHeatPump
   
      *Interface for HVAC abstract heat pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: heat_pump_type
      
         *(HVACHeatPumpType) Heat pump type*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_source_temperature
      
         *(float) Minimum source temperature*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_cop_entries
      
         *(int) Number of COP entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: performance
      
         *(dict) HVAC heat pump performance data. Entries are:*
         
         *source_temperature, cop and max_output*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractWaterAirHeatPump
   
      *Interface for HVAC abstract water air heat pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: cop_cooling
      
         *(float) Coefficient of performance for cooling*
      
      .. py:property:: cop_heating
      
         *(float) Coefficient of performance for heating*
      
      .. py:property:: entering_coil_dry_bulb_temperature_heating
      
         *(float) Entering coil dry bulb temperature heating*
      
      .. py:property:: entering_coil_wet_bulb_temperature_cooling
      
         *(float) Entering coil wet bulb temperature cooling*
      
      .. py:property:: entering_water_temperature_cooling
      
         *(float) Entering water temperature cooling*
      
      .. py:property:: entering_water_temperature_heating
      
         *(float) Entering water temperature heating*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAbstractWaterWaterHeatExchanger
   
      *Interface for abstract HVAC water-water heat exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:method:: get_approach
      
         *get_approach( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_approach(type) -> float*
             **
             *Get the design approach*
      
      .. py:method:: get_effectiveness
      
         *get_effectiveness( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_effectiveness(type) -> float*
             **
             *Get the heat exchanger effectiveness*
      
      .. py:method:: get_load_side_entering_temperature
      
         *get_load_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_entering_temperature(type) -> float*
             **
             *Get the design load side entering temperature*
      
      .. py:method:: get_load_side_leaving_temperature
      
         *get_load_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_leaving_temperature(type) -> float*
             **
             *Get the design load leaving temperature*
      
      .. py:method:: get_source_flow_rate
      
         *get_source_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_flow_rate(type) -> float*
             **
             *Get the design source flow rate*
      
      .. py:method:: get_source_side_entering_temperature
      
         *get_source_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_entering_temperature(type) -> float*
             **
             *Get the design source side entering temperature*
      
      .. py:method:: get_source_side_leaving_temperature
      
         *get_source_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_leaving_temperature(type) -> float*
             **
             *Get the design source side leaving temperature*
      
      .. py:method:: get_supply_flow_rate
      
         *get_supply_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_supply_flow_rate(type) -> float*
             **
             *Get the design supply flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:method:: is_design_heat_rejection_autosized
      
         *is_design_heat_rejection_autosized( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *is_design_heat_rejection_autosized(type) -> bool*
             **
             *Check whether the design heat rejection is autosized for the given HVACWaterWaterHeatExchangerDataType.*
             *Returns True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAirFilter
   
      *Interface for HVAC air filter*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAirToAirHeatEnthalpyExchanger
   
      *Interface for HVAC air to air heat enthalpy exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: latent_heat_effectiveness
      
         *(float) Latent heat effectiveness*
      
      .. py:property:: motor_or_pump_power
      
         *(float) Motor or pump power*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sensible_heat_effectiveness
      
         *(float) Sensible heat effectiveness*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACAmbientHeatRejectionDevice
   
      *Interface for HVAC ambient heat rejection device*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_approach
      
         *(float) Design approach*
      
      .. py:property:: design_flow_rate
      
         *(float) Design flow rate*
      
      .. py:property:: design_heat_rejection
      
         *(float) Design heat rejection*
      
      .. py:property:: design_leaving_temperature
      
         *(float) Design leaving temperature*
      
      .. py:property:: design_range
      
         *(float) Design range*
      
      .. py:property:: design_supply_water_temperature
      
         *(float) Supply water temperature*
      
      .. py:property:: design_wet_bulb_temperature
      
         *(float) Design wet bulb temperature*
      
      .. py:property:: fan_control
      
         *(HVACDXFanControl) Fan control*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: fan_power
      
         *(float) Fan power*
      
      .. py:property:: hr_device_autosized
      
         *(bool) Whether the heat rejection device is autosized. True if so, False otherwise.*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: low_speed_fan_flow_fraction
      
         *(float) Low speed fan flow fraction*
      
      .. py:property:: low_speed_fan_power_fraction
      
         *(float) Low speed fan power fraction*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump_delta_t
      
         *(float) Pump delta T*
      
      .. py:property:: pump_efficiency
      
         *(float) Pump efficiency*
      
      .. py:property:: pump_heat_gain
      
         *(float) Pump heat gain*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: specific_pump_power
      
         *(float) Specific fan power*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACBoiler
   
      *Interface for HVAC boiler*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_losses
      
         *(float) Distribution losses*
      
      .. py:property:: electrical_circulation_power
      
         *(float) Electrical circulation power*
      
      .. py:property:: heating_plant_type
      
         *(int) Heating plant type*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_dhw_boiler
      
         *(bool) Whether it is a DHW boiler. True if so, False otherwise*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(int) Whether output capacity is sized. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model_type
      
         *(HVACBoilerType) Model type*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_part_load_entries
      
         *(int) Number of part load entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: part_load_performance
      
         *(list) List of dictionaries of part load performance data.*
         *Dictionary keys are:*
         
         *efficiency, load, pump_usage*
      
      .. py:property:: primary_meter
      
         *(VEEnergyMeter) Primary energy meter*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sequence_number
      
         *(int) Sequence number*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: uses_chp
      
         *(bool) Whether CHP is used. True if so, False otherwise.*
      
      .. py:property:: uses_water_source_chp
      
         *(bool) Whether water source CHP is used. True if so, False otherwise.*
      
   .. py:class:: HVACBoilerType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: hot_water_boiler
         :classmethod:
         :type: iesve.HVACBoilerType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "hot_water_boiler".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'hot_water_boiler': iesve.HVACBoilerType.hot_water_boiler
             'part_load_curve_boiler': iesve.HVACBoilerType.part_load_curve_boiler
            }
      
      .. py:property:: part_load_curve_boiler
         :classmethod:
         :type: iesve.HVACBoilerType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "part_load_curve_boiler".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.HVACBoilerType.hot_water_boiler
             0: iesve.HVACBoilerType.part_load_curve_boiler
            }
      
   .. py:class:: HVACChilledCeiling
   
      *Interface for HVAC chilled ceiling*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_pump_consumption
      
         *(float) Distribution pump consumption*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: material_index
      
         *(int) Material index*
      
      .. py:property:: max_cooling_from_chiller
      
         *(float) Maximum cooling from chiller*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: orientation
      
         *(int) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_at_ref_temp_difference
      
         *(float) Output at reference temperature difference*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_temp_difference
      
         *(float) Reference temperature difference*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: water_capacity
      
         *(float) Water capacity*
      
      .. py:property:: weight
      
         *(float) Weight*
      
   .. py:class:: HVACChilledCeilingRoom
   
      *Interface for HVAC chilled ceiling room*
   
      .. py:property:: autosize_mode
      
         *(int) Whether autosize mode is enabled. 1 if so, 0 otherwise.*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chilled_ceiling_id
      
         *(string) Chilled ceiling ID*
      
      .. py:property:: chiller_id
      
         *(string) Chiller ID*
      
      .. py:property:: cooling_source_id
      
         *(string) Cooling source ID*
      
      .. py:property:: cooling_source_type
      
         *(int) Cooling source type*
      
      .. py:property:: deadband_value
      
         *(float) Deadband value*
      
      .. py:property:: design_heating_cooling_load
      
         *(float) Design heating and cooling load*
      
      .. py:property:: design_room_air_temp
      
         *(float) Design room air temperature*
      
      .. py:property:: design_room_radiant_temp
      
         *(float) Design room radiant temperature*
      
      .. py:property:: design_water_delta_t
      
         *(float) Design water delta T*
      
      .. py:property:: error_code
      
         *(int) Error code*
      
      .. py:property:: flow_for_max_control_signal
      
         *(float) Flow for maximum control signal*
      
      .. py:property:: flow_for_min_control_signal
      
         *(float) Flow for minimum control signal*
      
      .. py:property:: flow_max_change_per_time_step
      
         *(float) Flow max change per time step*
      
      .. py:property:: flow_midband
      
         *(float) Flow midband*
      
      .. py:property:: flow_midband_mode
      
         *(int) Flow midband mode*
      
      .. py:property:: flow_midband_profile_id
      
         *(string) Flow midband profile ID*
      
      .. py:property:: flow_proportional_bandwidth
      
         *(float) Flow proportional bandwidth*
      
      .. py:property:: flow_proportional_control
      
         *(int) Whether it is flow proportional control. 1 if so, 0 otherwise.*
      
      .. py:property:: flow_proportional_controller_id
      
         *(string) Flow proportional controller ID*
      
      .. py:property:: flow_proportional_sensed_variable
      
         *(int) Flow proportional sensed variable*
      
      .. py:property:: flow_proportional_sensor_body_index
      
         *(int) Flow proportional sensor body index*
      
      .. py:property:: flow_proportional_sensor_location
      
         *(int) Flow proportional sensor location*
      
      .. py:property:: flow_proportional_sensor_room_id
      
         *(string) Flow proportional sensor room ID*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_setpoint_sensor_enabled
      
         *(int) Whether the set point sensor is enabled. 1 if so, 0 otherwise*
      
      .. py:property:: model_id
      
         *(string) Model ID*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: number_of_or_connections
      
         *(int) Number of OR connections*
      
      .. py:property:: number_of_units
      
         *(float) Number of units*
      
      .. py:property:: on_off_controller_id
      
         *(string) On/off controller ID*
      
      .. py:property:: on_off_sensor_body_index
      
         *(int) On/off sensor body index*
      
      .. py:property:: on_off_sensor_room_id
      
         *(string) On/off sensor room ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: prop_flow_orientation
      
         *(float) Proportional flow orientation*
      
      .. py:property:: prop_flow_radiant_fraction
      
         *(float) Proportional flow radiant fraction*
      
      .. py:property:: prop_flow_slope
      
         *(float) Proportional flow slope*
      
      .. py:property:: prop_temp_orientation
      
         *(float) Proportional temperature orientation*
      
      .. py:property:: prop_temp_radiant_fraction
      
         *(float) Proportional temperature radiant fraction*
      
      .. py:property:: prop_temp_slope
      
         *(float) Proportional temperature slope*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_location
      
         *(int) Sensor location*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: set_point_value
      
         *(float) Set-point value*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: temp_for_max_control_signal
      
         *(float) Temperature for maximum control signal*
      
      .. py:property:: temp_for_min_control_signal
      
         *(float) Temperature for minimum control signal*
      
      .. py:property:: temp_max_change_per_time_step
      
         *(float) Temperature maximum change per time step*
      
      .. py:property:: temp_midband
      
         *(float) Temperature midband*
      
      .. py:property:: temp_midband_mode
      
         *(int) Temperature midband mode*
      
      .. py:property:: temp_midband_profile_id
      
         *(string) Temperature midband profile ID*
      
      .. py:property:: temp_proportional_bandwidth
      
         *(float) Temperature proportional bandwidth*
      
      .. py:property:: temp_proportional_control
      
         *(int) Whether it is temperature proportional control. 1 is so, 0 otherwise.*
      
      .. py:property:: temp_proportional_controller_id
      
         *(string) Temperature proportional controller ID*
      
      .. py:property:: temp_proportional_sensed_variable
      
         *(int) Temperature proportional sensed variable*
      
      .. py:property:: temp_proportional_sensor_body_index
      
         *(int) Temperature proportional sensor body index*
      
      .. py:property:: temp_proportional_sensor_location
      
         *(int) Temperature proportional sensor location*
      
      .. py:property:: temp_proportional_sensor_room_id
      
         *(string) Temperature proportional sensor  ID*
      
      .. py:property:: thermal_source_id
      
         *(string) Thermal source ID*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
      .. py:property:: water_loop_supply_temperature_used
      
         *(int) Whether water loop supply temperature is used. 1 is so, 0 otherwise.*
      
   .. py:class:: HVACChilledWaterLoop
   
      *Interface for HVAC chilled water loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chillers
      
         *(list) Chillers (HVACChiller)*
      
      .. py:property:: condenser_water_loop
      
         *(HVACCondenserWaterLoop) Condenser water loop*
      
      .. py:property:: distribution_loss
      
         *(float) Distribution loss*
      
      .. py:method:: get_chiller_count_by_type
      
         *get_chiller_count_by_type( (HVACChilledWaterLoop)arg1, (object)arg2) -> object :*
             *get_chiller_count_by_type(chiller type) -> int*
             **
             *Get the number of chillers of a provided HVACChillerType*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_secondary_loop_enabled
      
         *(bool) Whether an independent secondary loop is enabled*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: primary_chilled_water_demand_side_load_fraction_high_threshold
      
         *(float) Higher threshold for primary chilled water demand side load fraction*
      
      .. py:property:: primary_chilled_water_demand_side_load_fraction_low_threshold
      
         *(float) Lower threshold for primary chilled water demand side load fraction*
      
      .. py:property:: primary_chilled_water_supply_temp_high_threshold
      
         *(float) Higher threshold for primary chilled water supply temperature*
      
      .. py:property:: primary_chilled_water_supply_temp_low_threshold
      
         *(float) Lower threshold  for primary chilled water supply temperature*
      
      .. py:property:: primary_chilled_water_supply_temp_reset_type
      
         *(int) Primary chilled water supply temperature reset type*
      
      .. py:property:: primary_chilled_water_supply_temperature
      
         *(float) Primary chilled water supply temperature*
      
      .. py:property:: primary_chilled_water_temperature_difference
      
         *(float) Primary chilled water temperature difference*
      
      .. py:property:: primary_circuit_using_dedicated_chiller_pumps
      
         *(float) Primary circuit using dedicated chiller pumps*
      
      .. py:property:: primary_outdoor_dew_point_temp_high_threshold
      
         *(float) Higher threshold for primary outdoor dew point temperature*
      
      .. py:property:: primary_outdoor_dew_point_temp_low_threshold
      
         *(float) Lower threshold for primary outdoor dew point temperature*
      
      .. py:property:: primary_outdoor_dry_bulb_temp_high_threshold
      
         *(float) Higher threshold for primary outdoor dry bulb temperature*
      
      .. py:property:: primary_outdoor_dry_bulb_temp_low_threshold
      
         *(float) Lower threshold for primary outdoor dry bulb temperature*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: secondary_chilled_water_demand_side_load_fraction_high_threshold
      
         *(float) Higher threshold for secondary chilled water demand side load fraction*
      
      .. py:property:: secondary_chilled_water_demand_side_load_fraction_low_threshold
      
         *(float) Lower threshold for secondary chilled water demand side load fraction*
      
      .. py:property:: secondary_chilled_water_supply_temp_high_threshold
      
         *(float) Secondary chilled water supply temp high threshold*
      
      .. py:property:: secondary_chilled_water_supply_temp_low_threshold
      
         *(float) Lower threshold for secondary chilled water supply temperature*
      
      .. py:property:: secondary_chilled_water_supply_temp_reset_type
      
         *(int) Secondary chilled water supply temperature reset type*
      
      .. py:property:: secondary_chilled_water_supply_temperature
      
         *(float) Secondary chilled water supply temperature*
      
      .. py:property:: secondary_chilled_water_temperature_difference
      
         *(float) Secondary chilled water temperature difference*
      
      .. py:property:: secondary_outdoor_dew_point_temp_high_threshold
      
         *(float) Higher threshold for secondary outdoor dew point temperature*
      
      .. py:property:: secondary_outdoor_dew_point_temp_low_threshold
      
         *(float) Lower threshold for secondary outdoor dew point temperature*
      
      .. py:property:: secondary_outdoor_dry_bulb_temp_high_threshold
      
         *(float) Higher threshold for secondary outdoor dry bulb temperature*
      
      .. py:property:: secondary_outdoor_dry_bulb_temp_low_threshold
      
         *(float) Lower threshold for secondary outdoor dry bulb temperature*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: thermal_storage_loop
      
         *(list) Thermal storage loops (HVACThermalStorageLoop)*
      
   .. py:class:: HVACChiller
   
      *Interface for HVAC chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACChillerType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: CoolingChiller
         :classmethod:
         :type: iesve.HVACChillerType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "CoolingChiller".
      
      .. py:property:: DischargeChiller
         :classmethod:
         :type: iesve.HVACChillerType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "DischargeChiller".
      
      .. py:property:: ElectricAirCooled
         :classmethod:
         :type: iesve.HVACChillerType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ElectricAirCooled".
      
      .. py:property:: ElectricWaterCooled
         :classmethod:
         :type: iesve.HVACChillerType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ElectricWaterCooled".
      
      .. py:property:: PartLoadCurve
         :classmethod:
         :type: iesve.HVACChillerType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "PartLoadCurve".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'PartLoadCurve': iesve.HVACChillerType.PartLoadCurve
             'ElectricWaterCooled': iesve.HVACChillerType.ElectricWaterCooled
             'ElectricAirCooled': iesve.HVACChillerType.ElectricAirCooled
             'DischargeChiller': iesve.HVACChillerType.DischargeChiller
             'CoolingChiller': iesve.HVACChillerType.CoolingChiller
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACChillerType.PartLoadCurve
             1: iesve.HVACChillerType.ElectricWaterCooled
             2: iesve.HVACChillerType.ElectricAirCooled
             3: iesve.HVACChillerType.DischargeChiller
             4: iesve.HVACChillerType.CoolingChiller
            }
      
   .. py:class:: HVACCombinedHeatAndPower
   
      *Interface for HVAC combined heat and power*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACComponent
   
      *Interface for HVAC component*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACCondenserWaterLoop
   
      *Interface for HVAC condenser water loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: condenser_water_loop_used
      
         *(bool) Whether a condenser water loop is used. True if so, False otherwise.*
      
      .. py:property:: cooling_tower
      
         *(HVACCoolingTower) Cooling tower or None*
      
      .. py:property:: design_condenser_entering_water_temp
      
         *(float) Condenser design entering water temperature*
      
      .. py:property:: design_condenser_loop_flow_rate
      
         *(float) Design condenser loop flow rate*
      
      .. py:property:: design_condenser_water_loop_supply_temp
      
         *(float) Condenser design water loop supply temperature*
      
      .. py:property:: design_outdoor_dry_bulb_temp
      
         *(float) Design outdoor dry bulb temperature*
      
      .. py:property:: design_outdoor_wet_bulb_temp
      
         *(float) Design outdoor wet bulb temperature*
      
      .. py:property:: design_temperature_diff
      
         *(float) Design temperature difference*
      
      .. py:property:: dry_fluid_cooler
      
         *(HVACDryFluidCooler) Dry fluid cooler or None*
      
      .. py:property:: entering_water_constant_value
      
         *(float) Entering water constant value*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: motor_efficiency_factor
      
         *(float) Motor efficiency factor*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: specific_pump_power
      
         *(float) Specific pump power*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACController
   
      *Interface for HVAC controller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACControllerWithDifferentialSensor
   
      *Interface for HVAC controller with differential sensor*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: deadband
      
         *(float) Deadband*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_active_set_point
      
         *(int) Whether there is an active set point. 1 if so, 0 otherwise.*
      
      .. py:property:: is_proportional_control
      
         *(int) Whether there is a proportional controller. 1 if so, 0 otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_change_per_time_step
      
         *(float) Maximum change per time step*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: midband
      
         *(float) Midband*
      
      .. py:property:: midband_mode
      
         *(int) Midband mode*
      
      .. py:property:: midband_point_profile_id
      
         *(string) Midband point profile ID*
      
      .. py:property:: min_control_signal_value
      
         *(float) Minimum control signal value*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: on_off_max_signal_mode
      
         *(int) On/off maximum signal mode*
      
      .. py:property:: on_off_max_signal_profile_id
      
         *(string) On/off max signal profile ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: prop_min_signal_profile_id
      
         *(string) Proportional minimum signal profile ID*
      
      .. py:property:: proportional_bandwidth
      
         *(float) Proportional bandwidth*
      
      .. py:property:: proportional_controller_id
      
         *(string) Proportional controller ID*
      
      .. py:property:: proportional_min_signal_mode
      
         *(int) Proportional minimum signal mode*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: set_point
      
         *(float) Set point*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACControllerWithSensor
   
      *Interface for HVAC controller with sensor*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: deadband
      
         *(float) Deadband*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_active_set_point
      
         *(int) Whether there is an active set point. 1 if so, 0 otherwise.*
      
      .. py:property:: is_proportional_control
      
         *(int) Whether there is a proportional controller. 1 if so, 0 otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_change_per_time_step
      
         *(float) Maximum change per time step*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: midband
      
         *(float) Midband*
      
      .. py:property:: midband_mode
      
         *(int) Midband mode*
      
      .. py:property:: midband_point_profile_id
      
         *(string) Midband point profile ID*
      
      .. py:property:: min_control_signal_value
      
         *(float) Minimum control signal value*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: on_off_max_signal_mode
      
         *(int) On/off maximum signal mode*
      
      .. py:property:: on_off_max_signal_profile_id
      
         *(string) On/off max signal profile ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: prop_min_signal_profile_id
      
         *(string) Proportional minimum signal profile ID*
      
      .. py:property:: proportional_bandwidth
      
         *(float) Proportional bandwidth*
      
      .. py:property:: proportional_controller_id
      
         *(string) Proportional controller ID*
      
      .. py:property:: proportional_min_signal_mode
      
         *(int) Proportional minimum signal mode*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: set_point
      
         *(float) Set point*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACCoolingCoil
   
      *Interface for HVAC cooling coil*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chilled_water_loop_circuit
      
         *(CoilLocationCircuit) Chilled water loop circuit if the coil is a chilled water loop. Throws TypeError exception otherwise.*
      
      .. py:property:: contact_factor
      
         *(float) Contact factor*
      
      .. py:property:: cool_source_ext_dry_bulb_temperature
      
         *(float) Cooling source external dry bulb temperature*
      
      .. py:property:: cool_source_ext_dry_bulb_temperature_sized
      
         *(bool) Whether the cooling source external dry bulb temperature is sized.*
         *True if so, False otherwise*
      
      .. py:property:: cool_source_ext_wet_bulb_temperature
      
         *(float) Cooling source external wet bulb temperature*
      
      .. py:property:: cool_source_total_capacity
      
         *(float) Cooling source total capacity*
      
      .. py:property:: cooling_source
      
         *(Varies) Cooling source or None*
      
      .. py:property:: design_capacity
      
         *(float) Design capacity*
      
      .. py:property:: design_cop
      
         *(float) Design coefficient of performance (COP)*
      
      .. py:property:: design_entering_coil_temp
      
         *(float) Design entering coil temperature*
      
      .. py:property:: design_outdoor_air_temp
      
         *(float) Design outdoor air temperature*
      
      .. py:property:: design_parameters
      
         *(dict) Design sizing parameters. Keys vary based on model and system type.*
         
         *Possible keys are:*
         *oversizing_factor, contact_factor, sizing_mode, air_flow_rate, entering_air_db_temperature,*
         *entering_air_wb_temperature, leaving_air_db_temperature, leaving_air_wb_temperature, chilled_water_supply_temp,*
         *chilled_water_loop_delta_t, chilled_water_flow_rate, status, rated_capacity, design_capacity, design_cop,*
         *design_outdoor_air_db_temperature, design_outdoor_air_wb_temperature, design_entering_coil_wb_temperature,*
         *source_type, design_entering_water_temperature*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model_type
      
         *(CoolingCoilModelType) Cooling coil model type*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: system_type
      
         *(HVACCoolingSourceSystemType) Cooling source system type*
      
   .. py:class:: HVACCoolingSourceSystemType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: chilled_water_loop
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "chilled_water_loop".
      
      .. py:property:: direct_expansion
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "direct_expansion".
      
      .. py:property:: generic_cooling_source
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 5
         * a name of "generic_cooling_source".
      
      .. py:property:: legacy
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of -1
         * a name of "legacy".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'legacy': iesve.HVACCoolingSourceSystemType.legacy
             'chilled_water_loop': iesve.HVACCoolingSourceSystemType.chilled_water_loop
             'unitary_cooling': iesve.HVACCoolingSourceSystemType.unitary_cooling
             'waterside_economizer': iesve.HVACCoolingSourceSystemType.waterside_economizer
             'direct_expansion': iesve.HVACCoolingSourceSystemType.direct_expansion
             'water_air_heat_pump': iesve.HVACCoolingSourceSystemType.water_air_heat_pump
             'generic_cooling_source': iesve.HVACCoolingSourceSystemType.generic_cooling_source
             'variable_refrigerant_flow': iesve.HVACCoolingSourceSystemType.variable_refrigerant_flow
            }
      
      .. py:property:: unitary_cooling
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "unitary_cooling".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.HVACCoolingSourceSystemType.legacy
             0: iesve.HVACCoolingSourceSystemType.chilled_water_loop
             1: iesve.HVACCoolingSourceSystemType.unitary_cooling
             2: iesve.HVACCoolingSourceSystemType.waterside_economizer
             3: iesve.HVACCoolingSourceSystemType.direct_expansion
             4: iesve.HVACCoolingSourceSystemType.water_air_heat_pump
             5: iesve.HVACCoolingSourceSystemType.generic_cooling_source
             6: iesve.HVACCoolingSourceSystemType.variable_refrigerant_flow
            }
      
      .. py:property:: variable_refrigerant_flow
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 6
         * a name of "variable_refrigerant_flow".
      
      .. py:property:: water_air_heat_pump
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "water_air_heat_pump".
      
      .. py:property:: waterside_economizer
         :classmethod:
         :type: iesve.HVACCoolingSourceSystemType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "waterside_economizer".
      
   .. py:class:: HVACCoolingTower
   
      *Interface for HVAC cooling tower*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_approach
      
         *(float) Design approach*
      
      .. py:property:: design_flow_rate
      
         *(float) Design flow rate*
      
      .. py:property:: design_heat_rejection
      
         *(float) Design heat rejection*
      
      .. py:property:: design_leaving_temperature
      
         *(float) Design leaving temperature*
      
      .. py:property:: design_range
      
         *(float) Design range*
      
      .. py:property:: design_supply_water_temperature
      
         *(float) Supply water temperature*
      
      .. py:property:: design_wet_bulb_temperature
      
         *(float) Design wet bulb temperature*
      
      .. py:property:: fan_control
      
         *(HVACDXFanControl) Fan control*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: fan_power
      
         *(float) Fan power*
      
      .. py:property:: hr_device_autosized
      
         *(bool) Whether the heat rejection device is autosized. True if so, False otherwise.*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: low_speed_fan_flow_fraction
      
         *(float) Low speed fan flow fraction*
      
      .. py:property:: low_speed_fan_power_fraction
      
         *(float) Low speed fan power fraction*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump_delta_t
      
         *(float) Pump delta T*
      
      .. py:property:: pump_efficiency
      
         *(float) Pump efficiency*
      
      .. py:property:: pump_heat_gain
      
         *(float) Pump heat gain*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: specific_pump_power
      
         *(float) Specific fan power*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDHWBranch
   
      *Interface for DHW Branch*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: delivery_efficiency
      
         *(float) DHW delivery efficiency if simple mode, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_profile
      
         *(string) DHW supply temperature set point profile ID if simple mode and setpoint type is profile, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_type
      
         *(HVACDHWTemperatureSetPointType) DHW supply temperature set point type if simple mode, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_value
      
         *(float) DHW supply temperature set point value if simple mode and setpoint type is constant, None otherwise*
      
      .. py:property:: dhw_location_on_hwl
      
         *(HVACHWLDemandLoop) DHW heat exchanger (HX) location on HWL if heat source is HWL, None otherwise*
      
      .. py:property:: hwl_dhw_heat_exchanger
      
         *(HVACHWLDHWHeatExchanger) DHW HWL heat exchanger (HX) if explicit mode, None otherwise*
      
      .. py:property:: hx_approach
      
         *(float) Heat exchanger approach if explicit mode, None otherwise*
      
      .. py:property:: hx_effectiveness
      
         *(float) Heat exchanger effectiveness if explicit mode, None otherwise*
      
      .. py:property:: hx_load_hwl_hx_capacity
      
         *(float, W) Heat exchanger load and HWL HX capacity if explicit mode, None otherwise*
      
      .. py:property:: hx_source_side_flow_rate
      
         *(float) Heat exchanger source-side flow rate if explicit mode, None otherwise*
      
      .. py:property:: hx_supply_flow_rate
      
         *(float) Heat exchanger DHW supply flow rate if explicit mode, None otherwise*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_pre_heat_using_solar_water_heater
      
         *(bool) Is DHW pre-heat using Solar Water Heater (SWH)? True or False if simple mode, None otherwise.*
      
      .. py:property:: is_pump_used
      
         *(bool) Is a DHW pump used? True or False if explicit mode, None otherwise.*
      
      .. py:property:: is_recirculation_percent_of_flow
      
         *(bool) Is this recirculation a percentage of the DHW design supply flow?*
         
         *True or False if recirculation is used, None otherwise.*
      
      .. py:property:: is_recirculation_scheduled
      
         *(bool) Is the recirculation scheduled? True or False if recirculation is used, None otherwise.*
      
      .. py:property:: is_recirculation_used
      
         *(bool) Is DHW recirculation used? True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_storage_tank_used
      
         *(bool) Is a DHW storage tank used? True if so, False otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump
      
         *(HVACPump) Pump component if a DHW pump is used, None otherwise*
      
      .. py:property:: pump_heat_gain_fraction
      
         *(float) Pump heat gain (fraction) if a DHW pump is used, None otherwise*
      
      .. py:property:: recirculation_flow_rate
      
         *(float) Recirculation flow rate if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_loop_length
      
         *(float) Recirculation loop length if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_losses
      
         *(float) Recirculation losses if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_percent_of_supply_flow_rate
      
         *(float) % of DHW design supply flow rate if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_profile_id
      
         *(string) Recirculation profile ID if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_pump_meter
      
         *(VEEnergyMeter) Recirculation pump meter if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_pump_power
      
         *(float) Recirculation pump power if recirculation is used, None otherwise*
      
      .. py:property:: recirculation_schedule_type
      
         *(HVACRecirculationScheduleType) Recirculation schedule type if recirculation is used, None otherwise*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: solar_water_heater
      
         *(HVACSolarWaterHeater) Solar water heater (SWH) if SWH is used for DHW pre-heat, None otherwise*
      
      .. py:property:: specific_pump_power_at_rated_speed
      
         *(float) Specific pump power at rated speed if a DHW pump is used, None otherwise*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: tank_heat_loss
      
         *(float) Storage tank heat loss if storage tank is used, None otherwise*
      
      .. py:property:: tank_insulation_thickness
      
         *(float) Tank insulation thickness if storage tank is used, None otherwise*
      
      .. py:property:: tank_insulation_type
      
         *(HVACDHWTankInsulationType) Tank insulation type if storage tank is used, None otherwise*
      
      .. py:property:: tank_storage_volume
      
         *(float) Tank storage volume if storage tank is used, None otherwise*
      
      .. py:property:: tank_type
      
         *(HVACDHWTankDetails) Storage tank type if storage tank is used, None otherwise*
      
   .. py:class:: HVACDHWCHRHeatExchanger
   
      *Interface for DHW CHR Heat Exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: capacity
      
         *(float, W) Design capacity*
      
      .. py:method:: get_approach
      
         *get_approach( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_approach(type) -> float*
             **
             *Get the design approach*
      
      .. py:method:: get_effectiveness
      
         *get_effectiveness( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_effectiveness(type) -> float*
             **
             *Get the heat exchanger effectiveness*
      
      .. py:method:: get_load_side_entering_temperature
      
         *get_load_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_entering_temperature(type) -> float*
             **
             *Get the design load side entering temperature*
      
      .. py:method:: get_load_side_leaving_temperature
      
         *get_load_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_leaving_temperature(type) -> float*
             **
             *Get the design load leaving temperature*
      
      .. py:method:: get_source_flow_rate
      
         *get_source_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_flow_rate(type) -> float*
             **
             *Get the design source flow rate*
      
      .. py:method:: get_source_side_entering_temperature
      
         *get_source_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_entering_temperature(type) -> float*
             **
             *Get the design source side entering temperature*
      
      .. py:method:: get_source_side_leaving_temperature
      
         *get_source_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_leaving_temperature(type) -> float*
             **
             *Get the design source side leaving temperature*
      
      .. py:method:: get_supply_flow_rate
      
         *get_supply_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_supply_flow_rate(type) -> float*
             **
             *Get the design supply flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: inlet_temperature_delta_t
      
         *(float) Design inlet temperature delta T*
      
      .. py:method:: is_design_heat_rejection_autosized
      
         *is_design_heat_rejection_autosized( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *is_design_heat_rejection_autosized(type) -> bool*
             **
             *Check whether the design heat rejection is autosized for the given HVACWaterWaterHeatExchangerDataType.*
             *Returns True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDHWModel
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: explicit
         :classmethod:
         :type: iesve.HVACDHWModel
      
         An instance of this class with:
         
         * a value of 0
         * a name of "explicit".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'explicit': iesve.HVACDHWModel.explicit
             'simple': iesve.HVACDHWModel.simple
            }
      
      .. py:property:: simple
         :classmethod:
         :type: iesve.HVACDHWModel
      
         An instance of this class with:
         
         * a value of 1
         * a name of "simple".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDHWModel.explicit
             1: iesve.HVACDHWModel.simple
            }
      
   .. py:class:: HVACDHWSystem
   
      *Interface for HVAC DHW system*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: branches
      
         *(list) DHW Branches*
      
      .. py:property:: cold_water_inlet_temperature_set_point_profile
      
         *(string) DHW cold water inlet temperature set point profile ID if setpoint type is profile, None otherwise*
      
      .. py:property:: cold_water_inlet_temperature_set_point_type
      
         *(HVACDHWTemperatureSetPointType) DHW cold water inlet temperature set point type*
      
      .. py:property:: cold_water_inlet_temperature_value
      
         *(float) DHW cold water inlet temperature set point value if setpoint type is constant, None otherwise*
      
      .. py:property:: condenser_heat_recovery
      
         *(DHWCHRHeatExchanger) Condenser heat recovery if CWL is used for DHW pre-heat, None otherwise*
      
      .. py:property:: condenser_heat_recovery_pre_heat_used
      
         *(bool) Whether a condenser heat recovery heat exchanger is used for DHW pre-heat. True or False if explicit mode, None otherwise.*
      
      .. py:property:: condenser_water_loop
      
         *(HVACCondenserWaterLoop) Condenser water loop (CWL) if CWL is used for DHW pre-heat, None otherwise*
      
      .. py:property:: design_cold_water_inlet_temperature
      
         *(float) DHW design cold water inlet temperature if explicit mode, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature
      
         *(float) DHW design supply temperature if explicit mode, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_profile
      
         *(string) DHW design supply temperature set point profile ID if explicit mode and setpoint type is profile, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_type
      
         *(HVACDHWTemperatureSetPointType) DHW design supply temperature set point type if explicit mode, None otherwise*
      
      .. py:property:: dhw_design_supply_temperature_set_point_value
      
         *(float) DHW design supply temperature set point value if explicit mode and setpoint type is constant, None otherwise*
      
      .. py:property:: dhw_model
      
         *(HVACDHWModel) DHW Model*
      
      .. py:method:: get_branch_by_id
      
         *get_branch_by_id( (HVACDHWSystem)arg1, (object)arg2) -> object :*
             *get_branch_by_id(id) -> HVACDHWBranch*
             **
             *Get a DHW branch by ID*
      
      .. py:property:: heat_source
      
         *(HVACHeatSource) Heat source*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_to_be_autosized
      
         *(bool) Whether the DHW flow rate is to be autosized. True or False if explicit mode, None otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: solar_water_heater
      
         *(HVACSolarWaterHeater) Solar water heater (SWH) if SWH is used for DHW pre-heat, None otherwise*
      
      .. py:property:: solar_water_heater_pre_heat_used
      
         *(bool) Whether a solar water heater is used for DHW pre-heat. True or False if explicit mode, None otherwise.*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDHWTankDetails
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: heat_loss
         :classmethod:
         :type: iesve.HVACDHWTankDetails
      
         An instance of this class with:
         
         * a value of 1
         * a name of "heat_loss".
      
      .. py:property:: insulation_details
         :classmethod:
         :type: iesve.HVACDHWTankDetails
      
         An instance of this class with:
         
         * a value of 0
         * a name of "insulation_details".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'insulation_details': iesve.HVACDHWTankDetails.insulation_details
             'heat_loss': iesve.HVACDHWTankDetails.heat_loss
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDHWTankDetails.insulation_details
             1: iesve.HVACDHWTankDetails.heat_loss
            }
      
   .. py:class:: HVACDHWTankInsulationType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: factory_insulated
         :classmethod:
         :type: iesve.HVACDHWTankInsulationType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "factory_insulated".
      
      .. py:property:: loose_jacket
         :classmethod:
         :type: iesve.HVACDHWTankInsulationType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "loose_jacket".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'uninsulated': iesve.HVACDHWTankInsulationType.uninsulated
             'loose_jacket': iesve.HVACDHWTankInsulationType.loose_jacket
             'factory_insulated': iesve.HVACDHWTankInsulationType.factory_insulated
            }
      
      .. py:property:: uninsulated
         :classmethod:
         :type: iesve.HVACDHWTankInsulationType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "uninsulated".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDHWTankInsulationType.uninsulated
             1: iesve.HVACDHWTankInsulationType.loose_jacket
             2: iesve.HVACDHWTankInsulationType.factory_insulated
            }
      
   .. py:class:: HVACDHWTemperatureSetPointType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant
         :classmethod:
         :type: iesve.HVACDHWTemperatureSetPointType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "constant".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'constant': iesve.HVACDHWTemperatureSetPointType.constant
             'profile': iesve.HVACDHWTemperatureSetPointType.profile
            }
      
      .. py:property:: profile
         :classmethod:
         :type: iesve.HVACDHWTemperatureSetPointType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "profile".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDHWTemperatureSetPointType.constant
             1: iesve.HVACDHWTemperatureSetPointType.profile
            }
      
   .. py:class:: HVACDXCoolingCondenserType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_cooled
         :classmethod:
         :type: iesve.HVACDXCoolingCondenserType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_cooled".
      
      .. py:property:: evaporative_cooled
         :classmethod:
         :type: iesve.HVACDXCoolingCondenserType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "evaporative_cooled".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_cooled': iesve.HVACDXCoolingCondenserType.air_cooled
             'evaporative_cooled': iesve.HVACDXCoolingCondenserType.evaporative_cooled
             'number_of_types': iesve.HVACDXCoolingCondenserType.number_of_types
            }
      
      .. py:property:: number_of_types
         :classmethod:
         :type: iesve.HVACDXCoolingCondenserType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "number_of_types".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDXCoolingCondenserType.air_cooled
             1: iesve.HVACDXCoolingCondenserType.evaporative_cooled
             2: iesve.HVACDXCoolingCondenserType.number_of_types
            }
      
   .. py:class:: HVACDXCoolingInstance
   
      *Interface for HVAC DX cooling instance*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: coefficient
      
         *(float) Coefficient*
      
      .. py:property:: coil_wet_bulb_temp
      
         *(float) Coil wet bulb temperature*
      
      .. py:property:: condenser_type
      
         *(HVACDXCoolingCondenserType) Condenser type*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outdoor_air_dry_bulb_temp
      
         *(float) Outdoor air dry bulb temperature*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDXCoolingSystem
   
      *Interface for HVAC DX cooling system*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: coefficient
      
         *(float) Coefficient*
      
      .. py:property:: coil_wet_bulb_temp
      
         *(float) Coil wet bulb temperature*
      
      .. py:property:: condenser_type
      
         *(HVACDXCoolingCondenserType) Condenser type*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outdoor_air_dry_bulb_temp
      
         *(float) Outdoor air dry bulb temperature*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDXFanControl
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'one_speed_fan': iesve.HVACDXFanControl.one_speed_fan
             'two_speed_fan': iesve.HVACDXFanControl.two_speed_fan
             'vsd_fan': iesve.HVACDXFanControl.vsd_fan
            }
      
      .. py:property:: one_speed_fan
         :classmethod:
         :type: iesve.HVACDXFanControl
      
         An instance of this class with:
         
         * a value of 0
         * a name of "one_speed_fan".
      
      .. py:property:: two_speed_fan
         :classmethod:
         :type: iesve.HVACDXFanControl
      
         An instance of this class with:
         
         * a value of 1
         * a name of "two_speed_fan".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDXFanControl.one_speed_fan
             1: iesve.HVACDXFanControl.two_speed_fan
             2: iesve.HVACDXFanControl.vsd_fan
            }
      
      .. py:property:: vsd_fan
         :classmethod:
         :type: iesve.HVACDXFanControl
      
         An instance of this class with:
         
         * a value of 2
         * a name of "vsd_fan".
      
   .. py:class:: HVACDamper
   
      *Interface for HVAC damper*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: mid_node
      
         *(int) Mid node*
      
      .. py:property:: minimum_flow
      
         *(float) Minimum flow*
      
      .. py:property:: modulating_profile_profile_id
      
         *(string) The profile ID of the modulating profile*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDamperSplitter
   
      *Interface for HVAC damper splitter*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDedicatedWatersideEconomizer
   
      *Interface for HVAC dedicated waterside economizer*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: back_up_chilled_water_loop_id
      
         *(string) Back-up chilled water loop ID*
      
      .. py:property:: cooling_coil_design_water_delta_t
      
         *(float) Cooling coil design water delta T*
      
      .. py:property:: cooling_tower_design_fan_power
      
         *(float) Cooling tower design fan power*
      
      .. py:property:: design_cooling_tower_approach
      
         *(float) Design cooling tower approach*
      
      .. py:property:: design_cooling_tower_load
      
         *(float) Design cooling tower load*
      
      .. py:property:: design_cooling_tower_range
      
         *(float) Design cooling tower range*
      
      .. py:property:: design_outside_wet_bulb_temperature
      
         *(float) Design outside wet bulb temperature*
      
      .. py:property:: design_pump_power
      
         *(float) Design pump power*
      
      .. py:property:: fan_control
      
         *(int) Fan control*
      
      .. py:property:: heat_exchanger_effectiveness
      
         *(float) Heat exchanger effectiveness*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: low_speed_fan_flow_fraction
      
         *(float) Low speed fan flow fraction*
      
      .. py:property:: low_speed_fan_power_fraction
      
         *(float) Low speed fan power fraction*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: operates_only_when_it_can_meet_the_coil_load_in_full
      
         *(int) Whether it operates only when it can meet the coil load in full*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: use_back_up_chilled_water_loop_cooling_tower_and_pump_params
      
         *(bool) Whether back-up chilled water loop cooling tower and pump parameters are used.*
         *True if so, False otherwise.*
      
   .. py:class:: HVACDefrostControl
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'on_demand': iesve.HVACDefrostControl.on_demand
             'timed': iesve.HVACDefrostControl.timed
            }
      
      .. py:property:: on_demand
         :classmethod:
         :type: iesve.HVACDefrostControl
      
         An instance of this class with:
         
         * a value of 1
         * a name of "on_demand".
      
      .. py:property:: timed
         :classmethod:
         :type: iesve.HVACDefrostControl
      
         An instance of this class with:
         
         * a value of 0
         * a name of "timed".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.HVACDefrostControl.on_demand
             0: iesve.HVACDefrostControl.timed
            }
      
   .. py:class:: HVACDefrostStrategy
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'resistive': iesve.HVACDefrostStrategy.resistive
             'reverse_cycle': iesve.HVACDefrostStrategy.reverse_cycle
            }
      
      .. py:property:: resistive
         :classmethod:
         :type: iesve.HVACDefrostStrategy
      
         An instance of this class with:
         
         * a value of 1
         * a name of "resistive".
      
      .. py:property:: reverse_cycle
         :classmethod:
         :type: iesve.HVACDefrostStrategy
      
         An instance of this class with:
         
         * a value of 0
         * a name of "reverse_cycle".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.HVACDefrostStrategy.resistive
             0: iesve.HVACDefrostStrategy.reverse_cycle
            }
      
   .. py:class:: HVACDirectActingHeater
   
      *Interface for HVAC direct acting heater*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: efficiency
      
         *(float) efficiency*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sequence_number
      
         *(int) Sequence number*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: uses_chp
      
         *(bool) Whether CHP is used. True if so, False otherwise.*
      
   .. py:class:: HVACDirectActingHeaterRoom
   
      *Interface for direct acting heater room*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: direct_acting_heater_id
      
         *(string) Direct acting heater ID*
      
      .. py:property:: heat_output_for_max_control_signal
      
         *(float) Heat output for maximum control signal*
      
      .. py:property:: heat_output_for_min_control_signal
      
         *(float) Heat output for minimum control signal*
      
      .. py:property:: heat_output_max_change_per_time_step
      
         *(float) Heat output maximum change per time step*
      
      .. py:property:: heat_output_midband
      
         *(float) Heat output midband*
      
      .. py:property:: heat_output_midband_mode
      
         *(int) Heat output midband mode*
      
      .. py:property:: heat_output_midband_profile_id
      
         *(string) Heat output midband profile ID*
      
      .. py:property:: heat_output_proportional_bandwidth
      
         *(float) Heat output proportional bandwidth*
      
      .. py:property:: heat_output_proportional_control
      
         *(int) Whether there is heat output proportional control*
         
         *1 if so, 0 otherwise.*
      
      .. py:property:: heat_output_proportional_controller_id
      
         *(string) Heat output proportional controller ID*
      
      .. py:property:: heat_output_proportional_sensed_variable
      
         *(int) Heat output proportional sensed variable*
      
      .. py:property:: heat_output_proportional_sensor_body_index
      
         *(int) Heat output proportional sensor body index*
      
      .. py:property:: heat_output_proportional_sensor_location
      
         *(int) Heat output proportional sensor location*
      
      .. py:property:: heat_output_proportional_sensor_room_id
      
         *(string) Heat output proportional sensor room ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: prop_heat_output_orientation
      
         *(float) Proportional heat output orientation*
      
      .. py:property:: prop_heat_output_radiant_fraction
      
         *(float) Proportional heat output radiant fraction*
      
      .. py:property:: prop_heat_output_slope
      
         *(float) Proportional heat output slope*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDryFluidCooler
   
      *Interface for HVAC dry fluid cooler*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_approach
      
         *(float) Design approach*
      
      .. py:property:: design_dry_bulb_temperature
      
         *(float) Design dry bulb temperature*
      
      .. py:property:: design_flow_rate
      
         *(float) Design flow rate*
      
      .. py:property:: design_heat_rejection
      
         *(float) Design heat rejection*
      
      .. py:property:: design_leaving_temperature
      
         *(float) Design leaving temperature*
      
      .. py:property:: design_range
      
         *(float) Design range*
      
      .. py:property:: design_supply_water_temperature
      
         *(float) Supply water temperature*
      
      .. py:property:: design_wet_bulb_delta_t
      
         *(float) Design wet bulb delta T*
      
      .. py:property:: design_wet_bulb_temperature
      
         *(float) Design wet bulb temperature*
      
      .. py:property:: fan_control
      
         *(HVACDXFanControl) Fan control*
      
      .. py:property:: fan_electric_input_ratio
      
         *(float) Fan electric input ratio*
      
      .. py:property:: fan_power
      
         *(float) Fan power*
      
      .. py:property:: fluid_cooler_mode
      
         *(HVACDryFluidCoolerMode) Fluid cooler mode*
      
      .. py:property:: hr_device_autosized
      
         *(bool) Whether the heat rejection device is autosized. True if so, False otherwise.*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: low_speed_fan_flow_fraction
      
         *(float) Low speed fan flow fraction*
      
      .. py:property:: low_speed_fan_power_fraction
      
         *(float) Low speed fan power fraction*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump_delta_t
      
         *(float) Pump delta T*
      
      .. py:property:: pump_efficiency
      
         *(float) Pump efficiency*
      
      .. py:property:: pump_heat_gain
      
         *(float) Pump heat gain*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: specific_pump_power
      
         *(float) Specific fan power*
      
      .. py:property:: spray_pump_electric_input_ratio
      
         *(float) Spray pump electric input ratio*
      
      .. py:property:: spray_pump_power
      
         *(float) Spray pump power*
      
      .. py:property:: switch_temperature
      
         *(float) Switch temperature*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACDryFluidCoolerMode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: dry_mode
         :classmethod:
         :type: iesve.HVACDryFluidCoolerMode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "dry_mode".
      
      .. py:property:: dual_mode
         :classmethod:
         :type: iesve.HVACDryFluidCoolerMode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "dual_mode".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'dual_mode': iesve.HVACDryFluidCoolerMode.dual_mode
             'dry_mode': iesve.HVACDryFluidCoolerMode.dry_mode
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACDryFluidCoolerMode.dual_mode
             1: iesve.HVACDryFluidCoolerMode.dry_mode
            }
      
   .. py:class:: HVACDuct
   
      *Interface for HVAC Duct*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACEACChiller
   
      *Interface for HVAC EAC chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: compressor_heat_gain_to_condenser_loop
      
         *(float) Compressor heat gain to condenser loop fraction*
      
      .. py:property:: condenser_fan_eir
      
         *(float) Condenser fan EIR*
      
      .. py:property:: condenser_fan_power
      
         *(float) Condenser fan power*
      
      .. py:property:: cop
      
         *(float) Design coefficient of performance (COP)*
      
      .. py:property:: curve_type_names
      
         *(list) Curve type names (string)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: iplv
      
         *(float) Integrated part load value*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_outdoor_dry_bulb_temperature_autosized
      
         *(bool) Whether outdoor dry bulb temperature is autosized.*
         *True if so, False otherwise*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACEWCChiller
   
      *Interface for HVAC EWC chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: compressor_heat_gain_to_condenser_loop
      
         *(float) Compressor heat gain to condenser loop fraction*
      
      .. py:property:: cop
      
         *(float) Design coefficient of performance (COP)*
      
      .. py:property:: curve_type_names
      
         *(list) Curve type names (string)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: iplv
      
         *(float) Integrated part load value*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACElectricChiller
   
      *Interface for HVAC electric chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: compressor_heat_gain_to_condenser_loop
      
         *(float) Compressor heat gain to condenser loop fraction*
      
      .. py:property:: cop
      
         *(float) Design coefficient of performance (COP)*
      
      .. py:property:: curve_type_names
      
         *(list) Curve type names (string)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: iplv
      
         *(float) Integrated part load value*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_part_load_ratio
      
         *(float) Minimum part load ratio*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACEnhancedBoiler
   
      *Interface for HVAC enhanced boiler*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_losses
      
         *(float) Distribution losses*
      
      .. py:property:: electrical_circulation_power
      
         *(float) Electrical circulation power*
      
      .. py:property:: heating_plant_type
      
         *(int) Heating plant type*
      
      .. py:property:: hot_water_pump_factor
      
         *(float) Hot water pump factor*
      
      .. py:property:: hot_water_pump_power
      
         *(float) Hot water pump power*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_dhw_boiler
      
         *(bool) Whether it is a DHW boiler. True if so, False otherwise*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(int) Whether output capacity is sized. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_two_identical_boiler
      
         *(bool) Whether it forms a pair of identical boilers.*
         *True if so, False otherwise.*
      
      .. py:property:: max_parasitic_power
      
         *(float) Maximum parasitic power*
      
      .. py:property:: model_type
      
         *(HVACBoilerType) Model type*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_part_load_entries
      
         *(int) Number of part load entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: parasitic_power
      
         *(float) Parasitic power*
      
      .. py:property:: parasitic_ratio
      
         *(float) Parasitic ratio*
      
      .. py:property:: percentage_of_combined_capacity
      
         *(float) Percentage of combined capacity*
      
      .. py:property:: primary_meter
      
         *(VEEnergyMeter) Primary energy meter*
      
      .. py:property:: rated_condition
      
         *(dict) Dictionary of rated condition data. Keys are:*
         
         *efficiency*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sequence_number
      
         *(int) Sequence number*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: uses_chp
      
         *(bool) Whether CHP is used. True if so, False otherwise.*
      
      .. py:property:: uses_water_source_chp
      
         *(bool) Whether water source CHP is used. True if so, False otherwise.*
      
   .. py:class:: HVACFan
   
      *Interface for HVAC fan*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_fan_power
      
         *(float) Design fan power*
      
      .. py:property:: design_flow_rate
      
         *(float) Design flow rate*
      
      .. py:property:: design_total_pressure
      
         *(float) Design total pressure*
      
      .. py:property:: fan_efficiency_at_design_flow_rate
      
         *(float) Fan efficiency at the design flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_autosizable
      
         *(bool) Whether the fan is autosizable. True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_variable_air_volume
      
         *(bool) Whether the fan has variable air volume. True if so, False otherwise.*
      
      .. py:property:: motor_airstream_heat_pickup_factor
      
         *(float) Motor airstream pickup factor*
      
      .. py:property:: motor_efficiency_at_design_flow_rate
      
         *(float) Motor efficiency at the design flow rate*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACGenericCoolingSource
   
      *Interface for HVAC generic cooling source*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_losses
      
         *(float) Distribution losses*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether output capacity is sized. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: plc_chiller
      
         *(HVACPLCChiller) PLC chiller*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACGenericHeatSource
   
      *Interface for HVAC generic heat source*
   
      .. py:property:: autosize_air_source_heat_pump
      
         *(bool) Whether the air source heat pump is autosized. True if so, false otherwise.*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_heating_capacity
      
         *(float) Capacity*
      
      .. py:property:: equipment
      
         *(list) Equipment (HVACAbstractBoiler)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: percentage_of_heat_source_capacity
      
         *(float) Percentage of heat source capacity*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: use_air_source_heat_pump
      
         *(bool) Whether an air source heat pump is used. True if so, False otherwise.*
      
   .. py:class:: HVACHWLDHWHeatExchanger
   
      *Interface for HVAC DHW HWL heat exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:method:: get_approach
      
         *get_approach( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_approach(type) -> float*
             **
             *Get the design approach*
      
      .. py:method:: get_effectiveness
      
         *get_effectiveness( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_effectiveness(type) -> float*
             **
             *Get the heat exchanger effectiveness*
      
      .. py:method:: get_load_side_entering_temperature
      
         *get_load_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_entering_temperature(type) -> float*
             **
             *Get the design load side entering temperature*
      
      .. py:method:: get_load_side_leaving_temperature
      
         *get_load_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_leaving_temperature(type) -> float*
             **
             *Get the design load leaving temperature*
      
      .. py:method:: get_source_flow_rate
      
         *get_source_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_flow_rate(type) -> float*
             **
             *Get the design source flow rate*
      
      .. py:method:: get_source_side_entering_temperature
      
         *get_source_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_entering_temperature(type) -> float*
             **
             *Get the design source side entering temperature*
      
      .. py:method:: get_source_side_leaving_temperature
      
         *get_source_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_leaving_temperature(type) -> float*
             **
             *Get the design source side leaving temperature*
      
      .. py:method:: get_supply_flow_rate
      
         *get_supply_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_supply_flow_rate(type) -> float*
             **
             *Get the design supply flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: inlet_temperature_delta_t
      
         *(float) Inlet temperature delta T*
      
      .. py:method:: is_design_heat_rejection_autosized
      
         *is_design_heat_rejection_autosized( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *is_design_heat_rejection_autosized(type) -> bool*
             **
             *Check whether the design heat rejection is autosized for the given HVACWaterWaterHeatExchangerDataType.*
             *Returns True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHWLDemandLoop
   
      *Interface for HVAC HWL demand loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHeatPump
   
      *Interface for HVAC heat pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: heat_pump_type
      
         *(HVACHeatPumpType) Heat pump type*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_source_temperature
      
         *(float) Minimum source temperature*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_cop_entries
      
         *(int) Number of COP entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: performance
      
         *(dict) HVAC heat pump performance data. Entries are:*
         
         *source_temperature, cop and max_output*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHeatPumpInstance
   
      *Interface HVAC heat pump instance*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: heat_pump_type
      
         *(HVACHeatPumpType) Heat pump type*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: min_source_temperature
      
         *(float) Minimum source temperature*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_cop_entries
      
         *(int) Number of COP entries*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: performance
      
         *(dict) HVAC heat pump performance data. Entries are:*
         
         *source_temperature, cop and max_output*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHeatPumpType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_air_heat_pump
         :classmethod:
         :type: iesve.HVACHeatPumpType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "air_air_heat_pump".
      
      .. py:property:: air_source_heat_pump
         :classmethod:
         :type: iesve.HVACHeatPumpType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_source_heat_pump".
      
      .. py:property:: air_water_heat_pump
         :classmethod:
         :type: iesve.HVACHeatPumpType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "air_water_heat_pump".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_source_heat_pump': iesve.HVACHeatPumpType.air_source_heat_pump
             'air_water_heat_pump': iesve.HVACHeatPumpType.air_water_heat_pump
             'air_air_heat_pump': iesve.HVACHeatPumpType.air_air_heat_pump
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACHeatPumpType.air_source_heat_pump
             1: iesve.HVACHeatPumpType.air_water_heat_pump
             2: iesve.HVACHeatPumpType.air_air_heat_pump
            }
      
   .. py:class:: HVACHeatRecoveryModel
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: basic
         :classmethod:
         :type: iesve.HVACHeatRecoveryModel
      
         An instance of this class with:
         
         * a value of 0
         * a name of "basic".
      
      .. py:property:: explicit
         :classmethod:
         :type: iesve.HVACHeatRecoveryModel
      
         An instance of this class with:
         
         * a value of 2
         * a name of "explicit".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'basic': iesve.HVACHeatRecoveryModel.basic
             'percentage_hr': iesve.HVACHeatRecoveryModel.percentage_hr
             'explicit': iesve.HVACHeatRecoveryModel.explicit
            }
      
      .. py:property:: percentage_hr
         :classmethod:
         :type: iesve.HVACHeatRecoveryModel
      
         An instance of this class with:
         
         * a value of 1
         * a name of "percentage_hr".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACHeatRecoveryModel.basic
             1: iesve.HVACHeatRecoveryModel.percentage_hr
             2: iesve.HVACHeatRecoveryModel.explicit
            }
      
   .. py:class:: HVACHeatSource
   
      *Interface for HVAC heat source*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_heating_capacity
      
         *(float) Capacity*
      
      .. py:property:: equipment
      
         *(list) Equipment (HVACAbstractBoiler)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHeatTransferLoop
   
      *Interface for HVAC heat transfer loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACHeatingCoil
   
      *Interface for HVAC heating coil*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_capacity
      
      .. py:property:: design_cop
      
      .. py:property:: design_parameters
      
         *(dict) Design sizing parameters. Keys vary based on model and system type.*
         
         *Possible keys are:*
         *oversizing_factor, design_capacity, air_flow_rate, entering_air_db_temperature, leaving_air_db_temperature,*
         *rated_capacity, hot_water_supply_temp, hot_water_loop_delta_t, hot_water_flow_rate,*
         *design_cop, design_entering_coil_db_temperature, design_outdoor_air_wb_temperature, meter, design_entering_water_temperature*
      
      .. py:property:: entering_coil_temp
      
      .. py:property:: entering_water_temp
      
      .. py:property:: heat_source
      
         *(Varies) Heat source or 'None' if not applicable*
      
      .. py:property:: hot_water_loop_circuit
      
         *(HVACHWLDemandLoop) Hot water loop circuit if system type is 'heating_system_hot_water_loop', 'None' otherwise.*
      
      .. py:property:: htl
      
         *(HVACHeatTransferLoop) Heat transfer loop or 'None' if not applicable*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model_type
      
         *(HVACHeatingCoilModelType) Model type*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: system_type
      
         *(HVACHeatingSourceSystemType) System type*
      
   .. py:class:: HVACHotWaterLoop
   
      *Interface for HVAC hot water loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_heating_capacity
      
         *(float) Capacity*
      
      .. py:property:: equipment
      
         *(list) Equipment (HVACAbstractBoiler)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_pre_heat_using_solar_water_heater
      
         *(bool) is Hot Water Loop using solar water heater preheat*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: solar_water_heater
      
         *(HVACSolarWaterHeater) Solar water heater*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACInlet
   
      *Interface for HVAC inlet*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACJunction
   
      *Interface for HVAC Junction*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACLARIData
   
   
      .. py:method:: GetRoomData
      
         *GetRoomData( (HVACLARIData)arg1, (str)arg2) -> list*
      
      .. py:property:: chilledWaterLoopsData
      
      .. py:method:: get_multiple_room_data
      
         *get_multiple_room_data( (HVACLARIData)arg1, (list)arg2) -> dict*
      
      .. py:property:: heatTransferLoopsData
      
      .. py:property:: hotWaterLoopsData
      
      .. py:property:: isUpdatedPostSizing
      
      .. py:property:: systemData
      
      .. py:property:: systemSummaryData
      
   .. py:class:: HVACLocation
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: duct_contained_within_ra_plenum
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 3
         * a name of "duct_contained_within_ra_plenum".
      
      .. py:property:: duct_contained_within_room
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 1
         * a name of "duct_contained_within_room".
      
      .. py:property:: duct_contained_within_sa_plenum
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 4
         * a name of "duct_contained_within_sa_plenum".
      
      .. py:property:: duct_contained_within_void
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 2
         * a name of "duct_contained_within_void".
      
      .. py:property:: duct_contained_within_zone
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 5
         * a name of "duct_contained_within_zone".
      
      .. py:property:: duct_ext_to_building
         :classmethod:
         :type: iesve.HVACLocation
      
         An instance of this class with:
         
         * a value of 0
         * a name of "duct_ext_to_building".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'duct_ext_to_building': iesve.HVACLocation.duct_ext_to_building
             'duct_contained_within_room': iesve.HVACLocation.duct_contained_within_room
             'duct_contained_within_void': iesve.HVACLocation.duct_contained_within_void
             'duct_contained_within_ra_plenum': iesve.HVACLocation.duct_contained_within_ra_plenum
             'duct_contained_within_sa_plenum': iesve.HVACLocation.duct_contained_within_sa_plenum
             'duct_contained_within_zone': iesve.HVACLocation.duct_contained_within_zone
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACLocation.duct_ext_to_building
             1: iesve.HVACLocation.duct_contained_within_room
             2: iesve.HVACLocation.duct_contained_within_void
             3: iesve.HVACLocation.duct_contained_within_ra_plenum
             4: iesve.HVACLocation.duct_contained_within_sa_plenum
             5: iesve.HVACLocation.duct_contained_within_zone
            }
      
   .. py:class:: HVACMultiplex
   
      *Interface for HVAC multiplex*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: layer_editing_mode
      
         *(HVACMultiplexLayerEditingMode) Multiplex layer editing mode*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_layers
      
         *(int) Number of layers in the multiplex*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACMultiplexLayerEditingMode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: all_selected
         :classmethod:
         :type: iesve.HVACMultiplexLayerEditingMode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "all_selected".
      
      .. py:property:: current
         :classmethod:
         :type: iesve.HVACMultiplexLayerEditingMode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "current".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'current': iesve.HVACMultiplexLayerEditingMode.current
             'all_selected': iesve.HVACMultiplexLayerEditingMode.all_selected
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACMultiplexLayerEditingMode.current
             1: iesve.HVACMultiplexLayerEditingMode.all_selected
            }
      
   .. py:class:: HVACNetwork
   
      *Interface for HVAC network*
   
      .. py:property:: LARIData
      
      .. py:property:: chilled_water_loop_ids
      
         *(list) Chilled water loop IDs (string) in the network*
      
      .. py:property:: chilled_water_loops
      
         *(list) Chilled water loops (HVACChilledWaterLoop) in the network*
      
      .. py:property:: components
      
         *(list) Components (HVACComponent) in the network*
      
      .. py:property:: controllers
      
         *(list) Controllers (HVACController) in the network*
      
      .. py:property:: dhw_systems
      
         *(list) Domestic Hot Water (DHW) systems (HVACDHWSystem) in the network*
      
      .. py:property:: generic_heat_sources
      
         *(list) Generic heat sources (HVACGenericHeatSource) in the network*
      
      .. py:method:: get_component_by_id
      
         *get_component_by_id( (HVACNetwork)arg1, (str)arg2) -> object :*
             *get_component_by_id(id) -> HVACComponent*
             **
             *Get component by ID*
      
      .. py:method:: get_controller_by_id
      
         *get_controller_by_id( (HVACNetwork)arg1, (str)arg2) -> object :*
             *get_controller_by_id(id) -> HVACController*
             **
             *Get controller by ID*
      
      .. py:method:: get_multiplex_by_id
      
         *get_multiplex_by_id( (HVACNetwork)arg1, (str)arg2) -> object :*
             *get_multiplex_by_id(multiplex id) -> HVACMultiplex*
             **
             *Get multiplex by its ID*
      
      .. py:method:: get_multiplex_on_prototype_system
      
         *get_multiplex_on_prototype_system( (HVACNetwork)arg1, (str)arg2) -> object :*
             *get_multiplex_on_prototype_system(system id) -> HVACMultiplex*
             **
             *Get multiplex by system ID*
      
      .. py:method:: get_system_by_id
      
         *get_system_by_id( (HVACNetwork)arg1, (str)arg2) -> object :*
             *get_system_by_id(system id) -> HVACPrototypeSystem*
             **
             *Get system by ID*
      
      .. py:method:: has_t24_non_compliant_systems
      
         *has_t24_non_compliant_systems( (HVACNetwork)arg1 [, (object)sys_classification=-1]) -> bool :*
             *has_t24_non_compliant_systems(HVACSysClassification sys_classification) -> bool*
             **
             *Whether the network has Title 24 non-compliant systems.*
             *True if so, False otherwise.*
      
      .. py:property:: hot_water_loop_ids
      
         *(list) Hot water loop IDs (string) in the network*
      
      .. py:property:: hot_water_loops
      
         *(list) Hot water loops (HVACHotWaterLoop) in the network*
      
      .. py:method:: load_network
      
         *load_network( (str)arg1) -> object :*
             *load_network(network name) -> HVACNetwork*
             **
             *Load the given HVAC network*
      
      .. py:property:: multiplexes
      
         *(list) Multiplexes (HVACMultiplex) in the network*
      
      .. py:property:: name
      
         *(string) Network name*
      
      .. py:property:: non_master_rooms
      
         *(list) Non Master rooms in HVAC Zones in the network*
      
      .. py:property:: path
      
         *(string) Network path*
      
      .. py:property:: systems
      
         *(list) Systems (HVACPrototypeSystem) in the network*
      
      .. py:property:: systems_dict
      
         *(dict) Systems (HVACPrototypeSystem) in the network,*
         *keyed by system ID*
      
      .. py:property:: vrf_systems
      
         *(list) VRF Systems (HVACVRFSystem) in the network*
      
   .. py:class:: HVACNetworkObject
   
      *Interface for HVAC network object*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACNetworkObjectType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: component
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "component".
      
      .. py:property:: controller
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "controller".
      
      .. py:property:: generic
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "generic".
      
      .. py:property:: multiplex
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "multiplex".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_set': iesve.HVACNetworkObjectType.not_set
             'generic': iesve.HVACNetworkObjectType.generic
             'component': iesve.HVACNetworkObjectType.component
             'controller': iesve.HVACNetworkObjectType.controller
             'multiplex': iesve.HVACNetworkObjectType.multiplex
             'prototype_system': iesve.HVACNetworkObjectType.prototype_system
             'waterside_container': iesve.HVACNetworkObjectType.waterside_container
            }
      
      .. py:property:: not_set
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_set".
      
      .. py:property:: prototype_system
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 5
         * a name of "prototype_system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACNetworkObjectType.not_set
             1: iesve.HVACNetworkObjectType.generic
             2: iesve.HVACNetworkObjectType.component
             3: iesve.HVACNetworkObjectType.controller
             4: iesve.HVACNetworkObjectType.multiplex
             5: iesve.HVACNetworkObjectType.prototype_system
             6: iesve.HVACNetworkObjectType.waterside_container
            }
      
      .. py:property:: waterside_container
         :classmethod:
         :type: iesve.HVACNetworkObjectType
      
         An instance of this class with:
         
         * a value of 6
         * a name of "waterside_container".
      
   .. py:class:: HVACOutdoorUnitControl
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: load_priority
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 0
         * a name of "load_priority".
      
      .. py:property:: load_priority_with_compressor_power
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 1
         * a name of "load_priority_with_compressor_power".
      
      .. py:property:: master_thermostat_priority
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 3
         * a name of "master_thermostat_priority".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'load_priority': iesve.HVACOutdoorUnitControl.load_priority
             'load_priority_with_compressor_power': iesve.HVACOutdoorUnitControl.load_priority_with_compressor_power
             'zone_priority': iesve.HVACOutdoorUnitControl.zone_priority
             'master_thermostat_priority': iesve.HVACOutdoorUnitControl.master_thermostat_priority
             'thermostat_offeset_priority': iesve.HVACOutdoorUnitControl.thermostat_offeset_priority
             'profile': iesve.HVACOutdoorUnitControl.profile
            }
      
      .. py:property:: profile
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 5
         * a name of "profile".
      
      .. py:property:: thermostat_offeset_priority
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 4
         * a name of "thermostat_offeset_priority".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACOutdoorUnitControl.load_priority
             1: iesve.HVACOutdoorUnitControl.load_priority_with_compressor_power
             2: iesve.HVACOutdoorUnitControl.zone_priority
             3: iesve.HVACOutdoorUnitControl.master_thermostat_priority
             4: iesve.HVACOutdoorUnitControl.thermostat_offeset_priority
             5: iesve.HVACOutdoorUnitControl.profile
            }
      
      .. py:property:: zone_priority
         :classmethod:
         :type: iesve.HVACOutdoorUnitControl
      
         An instance of this class with:
         
         * a value of 2
         * a name of "zone_priority".
      
   .. py:class:: HVACOutlet
   
      *Interface for HVAC outlet*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACPCMBattery
   
      *Interface for HVAC PCM battery*
   
      .. py:property:: attached_room_id
      
         *(string) Room ID*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model_id
      
         *(string) Model ID*
      
      .. py:property:: model_not_found
      
         *(bool) Whether the model is not found.*
         
         *True if the model is not found, False otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_units
      
         *(int) Number of units*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACPLCChiller
   
      *Interface for HVAC PLC chiller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chiller_pumps_power
      
         *(float) Power of the chiller pumps*
      
      .. py:property:: chiller_type
      
         *(HVACChillerType) Chiller type*
      
      .. py:property:: chr_recipient_id
      
         *(string) CHR recipient ID*
      
      .. py:property:: condenser_water_pump_power
      
         *(float) Condenser water pump power*
      
      .. py:property:: cooling_tower_fan_power
      
         *(float) Cooling tower fan power*
      
      .. py:property:: deprecated_chr_percentage
      
         *(float) Deprecated CHR percentage*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_absorption_chiller
      
         *(bool) Whether it is an absorption chiller. True if so, False otherwise.*
      
      .. py:property:: is_chr_recipient_set
      
         *(bool) Whether the CHR recipient is set. True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_output_capacity_sized
      
         *(bool) Whether the output capacity is sized. True if so, False otherwise*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_part_load_entries
      
         *(int) Number of part load entries*
      
      .. py:property:: number_of_temperature_dependent_cops
      
         *(int) Number of temperature dependent COPs*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_capacity
      
         *(float) Output capacity*
      
      .. py:property:: outside_temp_for_cop_data
      
         *(int) Outside temperature for COP data*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACPlenum
   
      *Interface for HVAC plenum*
   
      .. py:property:: attached_room_id
      
         *(string) Attached room ID*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACPreCoolingLoop
   
      *Interface for HVAC pre-cooling loop*
   
      .. py:property:: autosizable
      
         *(bool) Whether it is autosizable. True if so, False otherwise.*
      
      .. py:property:: autosize_value
      
         *(float) Autosize value*
      
      .. py:property:: autosized
      
         *(bool) Whether it is autosized. True if so, False otherwise.*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: capacity
      
         *(float) Capacity*
      
      .. py:property:: cooling_tower_autosizable
      
         *(bool) Whether the cooling tower is autosizable. True if so, False otherwise.*
      
      .. py:property:: deprecated_heat_recovery
      
         *(float) Deprecated heat recovery*
      
      .. py:property:: dry_fluid_cooler_autosizable
      
         *(bool) Whether the dry fluid cooler is autosizable. True if so, False otherwise.*
      
      .. py:property:: heat_recovery_recipient_id
      
         *(string) Heat recovery recipient ID*
      
      .. py:property:: heat_recovery_recipient_set
      
         *(bool) Whether a heat recovery recipient is set. True if so, False otherwise.*
      
      .. py:property:: heat_recovery_used
      
         *(bool) Whether heat recovery is used. True if so, False otherwise.*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: water_source_loop_autosizable
      
         *(bool) Whether the water source loop is autosizable. True if so, False otherwise.*
      
      .. py:property:: water_source_loop_autosize_value
      
         *(float) Water source loop autosize value.*
      
      .. py:property:: water_source_loop_used
      
         *(bool) Whether a water source loop is used. True if so, False otherwise.*
      
   .. py:class:: HVACPrototypeSystem
   
      *Interface for HVAC Prototype system*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: components
      
         *(list) Components (HVACComponent) in the system*
      
      .. py:property:: controllers
      
         *(list) Controllers (HVACController) in the system*
      
      .. py:method:: get_cooling_design_load
      
         *get_cooling_design_load( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_cooling_design_load(layer number) -> float*
             **
             *Gets the cooling design load*
      
      .. py:method:: get_cooling_design_load_per_area
      
         *get_cooling_design_load_per_area( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_cooling_design_load_per_area(layer number) -> float*
             **
             *Gets the cooling design load per area*
      
      .. py:method:: get_cooling_design_load_per_area_inversed
      
         *get_cooling_design_load_per_area_inversed( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_cooling_design_load_per_area_inversed(layer number) -> float*
             **
             *Gets the cooling design load per area inversed*
      
      .. py:method:: get_cooling_max_primary_airflow
      
         *get_cooling_max_primary_airflow( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_cooling_max_primary_airflow(layer number) -> float*
             **
             *Gets the cooling maximum primary airflow*
      
      .. py:method:: get_heating_design_load
      
         *get_heating_design_load( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_heating_design_load(layer number) -> float*
             **
             *Gets the heating design load*
      
      .. py:method:: get_heating_design_load_per_area
      
         *get_heating_design_load_per_area( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_heating_design_load_per_area(layer number) -> float*
             **
             *Gets the heating design load per area*
      
      .. py:method:: get_heating_design_load_per_area_inversed
      
         *get_heating_design_load_per_area_inversed( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_heating_design_load_per_area_inversed(layer number) -> float*
             **
             *Gets the heating design load per area inversed*
      
      .. py:method:: get_heating_max_primary_airflow
      
         *get_heating_max_primary_airflow( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_heating_max_primary_airflow(layer number) -> float*
             **
             *Gets the heating maximum primary airflow*
      
      .. py:method:: get_oa_percentage_of_max_cooling_primary_sa
      
         *get_oa_percentage_of_max_cooling_primary_sa( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_oa_percentage_of_max_cooling_primary_sa(layer number) -> float*
             **
             *Gets the outdoor airflow of maximum cooling primary supply air percentage*
      
      .. py:method:: get_oa_percentage_of_max_heating_primary_sa
      
         *get_oa_percentage_of_max_heating_primary_sa( (HVACPrototypeSystem)arg1, (object)arg2) -> float :*
             *get_oa_percentage_of_max_heating_primary_sa(layer number) -> float*
             **
             *Gets the outdoor airflow of maximum heating primary supply air percentage*
      
      .. py:method:: get_room_cooling_peak_month
      
         *get_room_cooling_peak_month( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_room_cooling_peak_month(layer number) -> string*
             **
             *Gets the room cooling peak month*
      
      .. py:method:: get_room_cooling_peak_time
      
         *get_room_cooling_peak_time( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_room_cooling_peak_time(layer number) -> string*
             **
             *Gets the room cooling peak time*
      
      .. py:method:: get_room_heating_peak_month
      
         *get_room_heating_peak_month( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_room_heating_peak_month(layer number) -> string*
             **
             *Gets the room heating peak month*
      
      .. py:method:: get_room_heating_peak_time
      
         *get_room_heating_peak_time( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_room_heating_peak_time(layer number) -> string*
             **
             *Gets the room heating peak time*
      
      .. py:method:: get_room_id_for_umlh
      
         *get_room_id_for_umlh( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_room_id_for_umlh(layer number) -> string*
             **
             *Gets the room ID for UMLH*
      
      .. py:method:: get_space_id
      
         *get_space_id( (HVACPrototypeSystem)arg1, (object)arg2) -> str :*
             *get_space_id(layer number) -> string*
             **
             *Gets the ID of the assigned space for the specified multiplex layer. This is the ID of the assigned HVAC zone if the prototype system uses HVAC zones, or the room ID if the prototype system uses rooms.*
      
      .. py:method:: get_space_ids
      
         *get_space_ids( (HVACPrototypeSystem)arg1, (object)arg2) -> list :*
             *get_space_ids(layer number) -> list*
             **
             *Gets a list of IDs for the assigned space for the specified multiplex layer. This is the IDs of the zoned rooms if the prototype system uses HVAC zones, or a single room ID if the prototype system uses rooms.*
      
      .. py:method:: get_system_parameters
      
         *get_system_parameters( (HVACPrototypeSystem)arg1) -> SystemParameters :*
             *get_system_parameters() -> SystemParameters*
             **
             *Gets the system parameters for this system*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_sizing_enabled
      
         *(bool) Whether or not sizing is enabled. True if so, False otherwise*
      
      .. py:property:: is_valid
      
         *(bool) Whether or not the system is valid. True if so, False otherwise*
      
      .. py:property:: multiplex
      
         *(HVACMultiplex) The system multiplex*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_layers
      
         *(int) Number of layers in the system*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: standard
      
         *(string) Standard*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: system_type
      
         *(HVACPrototypeSystemType) System type*
      
   .. py:class:: HVACPrototypeSystemType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: actimass_system
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 97
         * a name of "actimass_system".
      
      .. py:property:: cool_phase_system
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 99
         * a name of "cool_phase_system".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'prm_system_1': iesve.HVACPrototypeSystemType.prm_system_1
             'prm_system_2': iesve.HVACPrototypeSystemType.prm_system_2
             'prm_system_3': iesve.HVACPrototypeSystemType.prm_system_3
             'prm_system_4': iesve.HVACPrototypeSystemType.prm_system_4
             'prm_system_5': iesve.HVACPrototypeSystemType.prm_system_5
             'prm_system_6': iesve.HVACPrototypeSystemType.prm_system_6
             'prm_system_7': iesve.HVACPrototypeSystemType.prm_system_7
             'prm_system_8': iesve.HVACPrototypeSystemType.prm_system_8
             'prm_system_9': iesve.HVACPrototypeSystemType.prm_system_9
             'prm_system_10': iesve.HVACPrototypeSystemType.prm_system_10
             'actimass_system': iesve.HVACPrototypeSystemType.actimass_system
             'tata_renew_sc_system': iesve.HVACPrototypeSystemType.tata_renew_sc_system
             'cool_phase_system': iesve.HVACPrototypeSystemType.cool_phase_system
            }
      
      .. py:property:: prm_system_1
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "prm_system_1".
      
      .. py:property:: prm_system_10
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 10
         * a name of "prm_system_10".
      
      .. py:property:: prm_system_2
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "prm_system_2".
      
      .. py:property:: prm_system_3
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "prm_system_3".
      
      .. py:property:: prm_system_4
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "prm_system_4".
      
      .. py:property:: prm_system_5
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 5
         * a name of "prm_system_5".
      
      .. py:property:: prm_system_6
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 6
         * a name of "prm_system_6".
      
      .. py:property:: prm_system_7
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 7
         * a name of "prm_system_7".
      
      .. py:property:: prm_system_8
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 8
         * a name of "prm_system_8".
      
      .. py:property:: prm_system_9
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 9
         * a name of "prm_system_9".
      
      .. py:property:: tata_renew_sc_system
         :classmethod:
         :type: iesve.HVACPrototypeSystemType
      
         An instance of this class with:
         
         * a value of 98
         * a name of "tata_renew_sc_system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.HVACPrototypeSystemType.prm_system_1
             2: iesve.HVACPrototypeSystemType.prm_system_2
             3: iesve.HVACPrototypeSystemType.prm_system_3
             4: iesve.HVACPrototypeSystemType.prm_system_4
             5: iesve.HVACPrototypeSystemType.prm_system_5
             6: iesve.HVACPrototypeSystemType.prm_system_6
             7: iesve.HVACPrototypeSystemType.prm_system_7
             8: iesve.HVACPrototypeSystemType.prm_system_8
             9: iesve.HVACPrototypeSystemType.prm_system_9
             10: iesve.HVACPrototypeSystemType.prm_system_10
             97: iesve.HVACPrototypeSystemType.actimass_system
             98: iesve.HVACPrototypeSystemType.tata_renew_sc_system
             99: iesve.HVACPrototypeSystemType.cool_phase_system
            }
      
   .. py:class:: HVACPump
   
      *Interface for HVAC pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: efficiency_factor
      
         *(float) Efficiency factor*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: meter
      
         *(VEEnergyMeter) Pump meter*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: power_curve
      
         *(HVACSystemCurve) System (power) curve*
      
      .. py:property:: pump_power
      
         *(float) Pump power*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACRadiator
   
      *Interface for HVAC radiator*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: distribution_pump_consumption
      
         *(float) Distribution pump consumption*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: material_index
      
         *(int) Material index*
      
      .. py:property:: max_input_from_boiler
      
         *(float) Maximum input from boiler*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: orientation
      
         *(int) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: output_at_ref_temp_difference
      
         *(float) Output at reference temperature difference*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_temp_difference
      
         *(float) Reference temperature difference*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: water_capacity
      
         *(float) Water capacity*
      
      .. py:property:: weight
      
         *(float) Weight*
      
   .. py:class:: HVACRadiatorRoom
   
      *Interface for HVAC radiator room*
   
      .. py:property:: autosize_mode
      
         *(int) Whether autosize mode is enabled. 1 if so, 0 otherwise.*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: deadband_value
      
         *(float) Deadband value*
      
      .. py:property:: design_heating_cooling_load
      
         *(float) Design heating and cooling load*
      
      .. py:property:: design_room_air_temp
      
         *(float) Design room air temperature*
      
      .. py:property:: design_room_radiant_temp
      
         *(float) Design room radiant temperature*
      
      .. py:property:: design_water_delta_t
      
         *(float) Design water delta T*
      
      .. py:property:: error_code
      
         *(int) Error code*
      
      .. py:property:: flow_for_max_control_signal
      
         *(float) Flow for maximum control signal*
      
      .. py:property:: flow_for_min_control_signal
      
         *(float) Flow for minimum control signal*
      
      .. py:property:: flow_max_change_per_time_step
      
         *(float) Flow max change per time step*
      
      .. py:property:: flow_midband
      
         *(float) Flow midband*
      
      .. py:property:: flow_midband_mode
      
         *(int) Flow midband mode*
      
      .. py:property:: flow_midband_profile_id
      
         *(string) Flow midband profile ID*
      
      .. py:property:: flow_proportional_bandwidth
      
         *(float) Flow proportional bandwidth*
      
      .. py:property:: flow_proportional_control
      
         *(int) Whether it is flow proportional control. 1 if so, 0 otherwise.*
      
      .. py:property:: flow_proportional_controller_id
      
         *(string) Flow proportional controller ID*
      
      .. py:property:: flow_proportional_sensed_variable
      
         *(int) Flow proportional sensed variable*
      
      .. py:property:: flow_proportional_sensor_body_index
      
         *(int) Flow proportional sensor body index*
      
      .. py:property:: flow_proportional_sensor_location
      
         *(int) Flow proportional sensor location*
      
      .. py:property:: flow_proportional_sensor_room_id
      
         *(string) Flow proportional sensor room ID*
      
      .. py:property:: get_heat_source_type
      
         *(int) Heat source type*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_setpoint_sensor_enabled
      
         *(int) Whether the set point sensor is enabled. 1 if so, 0 otherwise*
      
      .. py:property:: model_id
      
         *(string) Model ID*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: number_of_or_connections
      
         *(int) Number of OR connections*
      
      .. py:property:: number_of_units
      
         *(float) Number of units*
      
      .. py:property:: on_off_controller_id
      
         *(string) On/off controller ID*
      
      .. py:property:: on_off_sensor_body_index
      
         *(int) On/off sensor body index*
      
      .. py:property:: on_off_sensor_room_id
      
         *(string) On/off sensor room ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: prop_flow_orientation
      
         *(float) Proportional flow orientation*
      
      .. py:property:: prop_flow_radiant_fraction
      
         *(float) Proportional flow radiant fraction*
      
      .. py:property:: prop_flow_slope
      
         *(float) Proportional flow slope*
      
      .. py:property:: prop_temp_orientation
      
         *(float) Proportional temperature orientation*
      
      .. py:property:: prop_temp_radiant_fraction
      
         *(float) Proportional temperature radiant fraction*
      
      .. py:property:: prop_temp_slope
      
         *(float) Proportional temperature slope*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: radiator_id
      
         *(string) Radiator ID*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_location
      
         *(int) Sensor location*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: set_point_value
      
         *(float) Set-point value*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: temp_for_max_control_signal
      
         *(float) Temperature for maximum control signal*
      
      .. py:property:: temp_for_min_control_signal
      
         *(float) Temperature for minimum control signal*
      
      .. py:property:: temp_max_change_per_time_step
      
         *(float) Temperature maximum change per time step*
      
      .. py:property:: temp_midband
      
         *(float) Temperature midband*
      
      .. py:property:: temp_midband_mode
      
         *(int) Temperature midband mode*
      
      .. py:property:: temp_midband_profile_id
      
         *(string) Temperature midband profile ID*
      
      .. py:property:: temp_proportional_bandwidth
      
         *(float) Temperature proportional bandwidth*
      
      .. py:property:: temp_proportional_control
      
         *(int) Whether it is temperature proportional control. 1 is so, 0 otherwise.*
      
      .. py:property:: temp_proportional_controller_id
      
         *(string) Temperature proportional controller ID*
      
      .. py:property:: temp_proportional_sensed_variable
      
         *(int) Temperature proportional sensed variable*
      
      .. py:property:: temp_proportional_sensor_body_index
      
         *(int) Temperature proportional sensor body index*
      
      .. py:property:: temp_proportional_sensor_location
      
         *(int) Temperature proportional sensor location*
      
      .. py:property:: temp_proportional_sensor_room_id
      
         *(string) Temperature proportional sensor  ID*
      
      .. py:property:: thermal_source_id
      
         *(string) Thermal source ID*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
      .. py:property:: water_loop_supply_temperature_used
      
         *(int) Whether water loop supply temperature is used. 1 is so, 0 otherwise.*
      
   .. py:class:: HVACRecirculationScheduleType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'space_occupancy': iesve.HVACRecirculationScheduleType.space_occupancy
             'time_switch_profile': iesve.HVACRecirculationScheduleType.time_switch_profile
            }
      
      .. py:property:: space_occupancy
         :classmethod:
         :type: iesve.HVACRecirculationScheduleType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "space_occupancy".
      
      .. py:property:: time_switch_profile
         :classmethod:
         :type: iesve.HVACRecirculationScheduleType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "time_switch_profile".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACRecirculationScheduleType.space_occupancy
             1: iesve.HVACRecirculationScheduleType.time_switch_profile
            }
      
   .. py:class:: HVACRoom
   
      *Interface for HVAC room*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chilled_ceiling_room_units
      
         *(list) Chilled ceiling room units (HVACChilledCeilingRoom)*
      
      .. py:property:: direct_acting_heater_room_units
      
         *(list) Direct acting heater room units (HVACDirectActingHeaterRoom)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_disconnected_room
      
         *(bool) Whether the room is disconnected. True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_principal
      
         *(bool) Whether it is a principal room. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: radiator_units
      
         *(list) Radiator units (HVACRadiatorRoom)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACRoomUnit
   
      *Interface for HVAC room unit*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: deadband_value
      
         *(float) Deadband value*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_setpoint_sensor_enabled
      
         *(int) Whether the set point sensor is enabled. 1 if so, 0 otherwise*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: number_of_or_connections
      
         *(int) Number of OR connections*
      
      .. py:property:: on_off_controller_id
      
         *(string) On/off controller ID*
      
      .. py:property:: on_off_sensor_body_index
      
         *(int) On/off sensor body index*
      
      .. py:property:: on_off_sensor_room_id
      
         *(string) On/off sensor room ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_location
      
         *(int) Sensor location*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: set_point_value
      
         *(float) Set-point value*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACSHWPanelType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: flat_panel
         :classmethod:
         :type: iesve.HVACSHWPanelType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "flat_panel".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'flat_panel': iesve.HVACSHWPanelType.flat_panel
             'parabolic_panel': iesve.HVACSHWPanelType.parabolic_panel
            }
      
      .. py:property:: parabolic_panel
         :classmethod:
         :type: iesve.HVACSHWPanelType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "parabolic_panel".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACSHWPanelType.flat_panel
             1: iesve.HVACSHWPanelType.parabolic_panel
            }
      
   .. py:class:: HVACSolarAirCollectorBIST
   
      *Interface for solar air collector BIST*
   
      .. py:property:: attached_room_id
      
         *(string) Attached room ID*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACSolarWaterHeater
   
      *Interface for HVAC solar water heater*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: flat_solar_panel_data
      
         *(dict) Flat PV data (float)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_waterside_component
      
         *(bool) Whether it is a waterside component. True if so, False otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: panel_type
      
         *(HVACSHWPanelType) Panel type*
      
      .. py:property:: parabolic_solar_panel_data
      
         *(dict) Parabolic PV data (float)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACSourceDependentRoom
   
      *Interface for HVAC source dependent room component*
   
      .. py:property:: autosize_mode
      
         *(int) Whether autosize mode is enabled. 1 if so, 0 otherwise.*
      
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: deadband_value
      
         *(float) Deadband value*
      
      .. py:property:: design_heating_cooling_load
      
         *(float) Design heating and cooling load*
      
      .. py:property:: design_room_air_temp
      
         *(float) Design room air temperature*
      
      .. py:property:: design_room_radiant_temp
      
         *(float) Design room radiant temperature*
      
      .. py:property:: design_water_delta_t
      
         *(float) Design water delta T*
      
      .. py:property:: error_code
      
         *(int) Error code*
      
      .. py:property:: flow_for_max_control_signal
      
         *(float) Flow for maximum control signal*
      
      .. py:property:: flow_for_min_control_signal
      
         *(float) Flow for minimum control signal*
      
      .. py:property:: flow_max_change_per_time_step
      
         *(float) Flow max change per time step*
      
      .. py:property:: flow_midband
      
         *(float) Flow midband*
      
      .. py:property:: flow_midband_mode
      
         *(int) Flow midband mode*
      
      .. py:property:: flow_midband_profile_id
      
         *(string) Flow midband profile ID*
      
      .. py:property:: flow_proportional_bandwidth
      
         *(float) Flow proportional bandwidth*
      
      .. py:property:: flow_proportional_control
      
         *(int) Whether it is flow proportional control. 1 if so, 0 otherwise.*
      
      .. py:property:: flow_proportional_controller_id
      
         *(string) Flow proportional controller ID*
      
      .. py:property:: flow_proportional_sensed_variable
      
         *(int) Flow proportional sensed variable*
      
      .. py:property:: flow_proportional_sensor_body_index
      
         *(int) Flow proportional sensor body index*
      
      .. py:property:: flow_proportional_sensor_location
      
         *(int) Flow proportional sensor location*
      
      .. py:property:: flow_proportional_sensor_room_id
      
         *(string) Flow proportional sensor room ID*
      
      .. py:property:: high_sensor_input
      
         *(int) High sensor input*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: is_setpoint_sensor_enabled
      
         *(int) Whether the set point sensor is enabled. 1 if so, 0 otherwise*
      
      .. py:property:: model_id
      
         *(string) Model ID*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: number_of_or_connections
      
         *(int) Number of OR connections*
      
      .. py:property:: number_of_units
      
         *(float) Number of units*
      
      .. py:property:: on_off_controller_id
      
         *(string) On/off controller ID*
      
      .. py:property:: on_off_sensor_body_index
      
         *(int) On/off sensor body index*
      
      .. py:property:: on_off_sensor_room_id
      
         *(string) On/off sensor room ID*
      
      .. py:property:: orientation
      
         *(float) Orientation*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: oversizing_factor
      
         *(float) Oversizing factor*
      
      .. py:property:: prop_flow_orientation
      
         *(float) Proportional flow orientation*
      
      .. py:property:: prop_flow_radiant_fraction
      
         *(float) Proportional flow radiant fraction*
      
      .. py:property:: prop_flow_slope
      
         *(float) Proportional flow slope*
      
      .. py:property:: prop_temp_orientation
      
         *(float) Proportional temperature orientation*
      
      .. py:property:: prop_temp_radiant_fraction
      
         *(float) Proportional temperature radiant fraction*
      
      .. py:property:: prop_temp_slope
      
         *(float) Proportional temperature slope*
      
      .. py:property:: radiant_fraction
      
         *(float) Radiant fraction*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: sensed_variable
      
         *(int) Sensed variable*
      
      .. py:property:: sensor_location
      
         *(int) Sensor location*
      
      .. py:property:: set_point_mode
      
         *(int) Set point mode*
      
      .. py:property:: set_point_profile_id
      
         *(string) Set point profile ID*
      
      .. py:property:: set_point_value
      
         *(float) Set-point value*
      
      .. py:property:: slope
      
         *(float) Slope*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: temp_for_max_control_signal
      
         *(float) Temperature for maximum control signal*
      
      .. py:property:: temp_for_min_control_signal
      
         *(float) Temperature for minimum control signal*
      
      .. py:property:: temp_max_change_per_time_step
      
         *(float) Temperature maximum change per time step*
      
      .. py:property:: temp_midband
      
         *(float) Temperature midband*
      
      .. py:property:: temp_midband_mode
      
         *(int) Temperature midband mode*
      
      .. py:property:: temp_midband_profile_id
      
         *(string) Temperature midband profile ID*
      
      .. py:property:: temp_proportional_bandwidth
      
         *(float) Temperature proportional bandwidth*
      
      .. py:property:: temp_proportional_control
      
         *(int) Whether it is temperature proportional control. 1 is so, 0 otherwise.*
      
      .. py:property:: temp_proportional_controller_id
      
         *(string) Temperature proportional controller ID*
      
      .. py:property:: temp_proportional_sensed_variable
      
         *(int) Temperature proportional sensed variable*
      
      .. py:property:: temp_proportional_sensor_body_index
      
         *(int) Temperature proportional sensor body index*
      
      .. py:property:: temp_proportional_sensor_location
      
         *(int) Temperature proportional sensor location*
      
      .. py:property:: temp_proportional_sensor_room_id
      
         *(string) Temperature proportional sensor  ID*
      
      .. py:property:: thermal_source_id
      
         *(string) Thermal source ID*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
      .. py:property:: water_loop_supply_temperature_used
      
         *(int) Whether water loop supply temperature is used. 1 is so, 0 otherwise.*
      
   .. py:class:: HVACSprayChamber
   
      *Interface for HVAC spray chamber*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: circulation_pump_power
      
         *Interface for HVAC spray chamber*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: spray_efficiency
      
         *(float) Spray efficiency*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACSteamHumidifier
   
      *Interface for HVAC steam humidifier*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: boiler_supply_flag
      
         *(int) Boiler supply flag*
      
      .. py:property:: heat_source_id
      
         *(string) Heat source ID*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: maximum_output
      
         *(float) Maximum output*
      
      .. py:property:: maximum_relative_humidity
      
         *(float) Maximum relative humidity*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: total_efficiency
      
         *(float) Total efficiency*
      
   .. py:class:: HVACSysClassification
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ecb_2010_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 8
         * a name of "ecb_2010_compliance_system".
      
      .. py:property:: ecb_2013_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 9
         * a name of "ecb_2013_compliance_system".
      
      .. py:property:: iecc_2012_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 11
         * a name of "iecc_2012_compliance_system".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_classification': iesve.HVACSysClassification.no_classification
             'standard_design_system': iesve.HVACSysClassification.standard_design_system
             't24_design_system': iesve.HVACSysClassification.t24_design_system
             't24_standard_design_system': iesve.HVACSysClassification.t24_standard_design_system
             'ncm_design_system': iesve.HVACSysClassification.ncm_design_system
             'prm_2004_compliance_system': iesve.HVACSysClassification.prm_2004_compliance_system
             'prm_2007_compliance_system': iesve.HVACSysClassification.prm_2007_compliance_system
             'prm_2010_compliance_system': iesve.HVACSysClassification.prm_2010_compliance_system
             'prm_2013_compliance_system': iesve.HVACSysClassification.prm_2013_compliance_system
             'prm_2016_compliance_system': iesve.HVACSysClassification.prm_2016_compliance_system
             'prm_2019_compliance_system': iesve.HVACSysClassification.prm_2019_compliance_system
             'ecb_2010_compliance_system': iesve.HVACSysClassification.ecb_2010_compliance_system
             'ecb_2013_compliance_system': iesve.HVACSysClassification.ecb_2013_compliance_system
             'necb_2011_compliance_system': iesve.HVACSysClassification.necb_2011_compliance_system
             'necb_2017_compliance_system': iesve.HVACSysClassification.necb_2017_compliance_system
             'iecc_2012_compliance_system': iesve.HVACSysClassification.iecc_2012_compliance_system
            }
      
      .. py:property:: ncm_design_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 3
         * a name of "ncm_design_system".
      
      .. py:property:: necb_2011_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 10
         * a name of "necb_2011_compliance_system".
      
      .. py:property:: necb_2017_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 13
         * a name of "necb_2017_compliance_system".
      
      .. py:property:: no_classification
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of -1
         * a name of "no_classification".
      
      .. py:property:: prm_2004_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 4
         * a name of "prm_2004_compliance_system".
      
      .. py:property:: prm_2007_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 5
         * a name of "prm_2007_compliance_system".
      
      .. py:property:: prm_2010_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 6
         * a name of "prm_2010_compliance_system".
      
      .. py:property:: prm_2013_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 7
         * a name of "prm_2013_compliance_system".
      
      .. py:property:: prm_2016_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 12
         * a name of "prm_2016_compliance_system".
      
      .. py:property:: prm_2019_compliance_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 14
         * a name of "prm_2019_compliance_system".
      
      .. py:property:: standard_design_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 0
         * a name of "standard_design_system".
      
      .. py:property:: t24_design_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 1
         * a name of "t24_design_system".
      
      .. py:property:: t24_standard_design_system
         :classmethod:
         :type: iesve.HVACSysClassification
      
         An instance of this class with:
         
         * a value of 2
         * a name of "t24_standard_design_system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.HVACSysClassification.no_classification
             0: iesve.HVACSysClassification.standard_design_system
             1: iesve.HVACSysClassification.t24_design_system
             2: iesve.HVACSysClassification.t24_standard_design_system
             3: iesve.HVACSysClassification.ncm_design_system
             4: iesve.HVACSysClassification.prm_2004_compliance_system
             5: iesve.HVACSysClassification.prm_2007_compliance_system
             6: iesve.HVACSysClassification.prm_2010_compliance_system
             7: iesve.HVACSysClassification.prm_2013_compliance_system
             12: iesve.HVACSysClassification.prm_2016_compliance_system
             14: iesve.HVACSysClassification.prm_2019_compliance_system
             8: iesve.HVACSysClassification.ecb_2010_compliance_system
             9: iesve.HVACSysClassification.ecb_2013_compliance_system
             10: iesve.HVACSysClassification.necb_2011_compliance_system
             13: iesve.HVACSysClassification.necb_2017_compliance_system
             11: iesve.HVACSysClassification.iecc_2012_compliance_system
            }
      
   .. py:class:: HVACSystemCurve
   
      *Interface for HVAC system curve*
   
      .. py:property:: curve_description
      
         *(str) Curve description*
      
      .. py:property:: curve_name
      
         *(str) Curve name*
      
      .. py:property:: curve_role
      
         *(HVACSystemCurveRole) Curve role*
      
      .. py:property:: curve_role_string
      
         *(str) Curve role*
      
      .. py:property:: curve_type
      
         *(HVACSystemCurveType) Curve type*
      
   .. py:class:: HVACSystemCurveRole
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: AAHPC_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 21
         * a name of "AAHPC_FCAPTT".
      
      .. py:property:: AAHPC_FEIRP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 23
         * a name of "AAHPC_FEIRP".
      
      .. py:property:: AAHPC_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 22
         * a name of "AAHPC_FEIRTT".
      
      .. py:property:: AAHPH_FCAPT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 17
         * a name of "AAHPH_FCAPT".
      
      .. py:property:: AAHPH_FDEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 20
         * a name of "AAHPH_FDEIRTT".
      
      .. py:property:: AAHPH_FEIRP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 19
         * a name of "AAHPH_FEIRP".
      
      .. py:property:: AAHPH_FEIRT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 18
         * a name of "AAHPH_FEIRT".
      
      .. py:property:: BOIL_FEPT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 4
         * a name of "BOIL_FEPT".
      
      .. py:property:: CHILL_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 0
         * a name of "CHILL_FCAPTT".
      
      .. py:property:: CHILL_FEIRPT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 2
         * a name of "CHILL_FEIRPT".
      
      .. py:property:: CHILL_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 1
         * a name of "CHILL_FEIRTT".
      
      .. py:property:: CPHPC_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 28
         * a name of "CPHPC_FCAPTT".
      
      .. py:property:: CPHPC_FCOPP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 34
         * a name of "CPHPC_FCOPP".
      
      .. py:property:: CPHPC_FCOPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 33
         * a name of "CPHPC_FCOPTT".
      
      .. py:property:: CPHPC_FEIRP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 30
         * a name of "CPHPC_FEIRP".
      
      .. py:property:: CPHPC_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 29
         * a name of "CPHPC_FEIRTT".
      
      .. py:property:: CPHPH_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 24
         * a name of "CPHPH_FCAPTT".
      
      .. py:property:: CPHPH_FCOPP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 32
         * a name of "CPHPH_FCOPP".
      
      .. py:property:: CPHPH_FCOPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 31
         * a name of "CPHPH_FCOPTT".
      
      .. py:property:: CPHPH_FDEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 27
         * a name of "CPHPH_FDEIRTT".
      
      .. py:property:: CPHPH_FEIRP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 26
         * a name of "CPHPH_FEIRP".
      
      .. py:property:: CPHPH_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 25
         * a name of "CPHPH_FEIRTT".
      
      .. py:property:: DX_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 8
         * a name of "DX_FCAPTT".
      
      .. py:property:: DX_FEIRP
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 10
         * a name of "DX_FEIRP".
      
      .. py:property:: DX_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 9
         * a name of "DX_FEIRTT".
      
      .. py:property:: EAC_FCAPTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 5
         * a name of "EAC_FCAPTT".
      
      .. py:property:: EAC_FEIRPT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 7
         * a name of "EAC_FEIRPT".
      
      .. py:property:: EAC_FEIRTT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 6
         * a name of "EAC_FEIRTT".
      
      .. py:property:: PUMP_PWRV
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 3
         * a name of "PUMP_PWRV".
      
      .. py:property:: WAHP_FCAPTT_COOL
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 14
         * a name of "WAHP_FCAPTT_COOL".
      
      .. py:property:: WAHP_FCAPTT_HEAT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 11
         * a name of "WAHP_FCAPTT_HEAT".
      
      .. py:property:: WAHP_FEIRP_COOL
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 16
         * a name of "WAHP_FEIRP_COOL".
      
      .. py:property:: WAHP_FEIRP_HEAT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 13
         * a name of "WAHP_FEIRP_HEAT".
      
      .. py:property:: WAHP_FEIRTT_COOL
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 15
         * a name of "WAHP_FEIRTT_COOL".
      
      .. py:property:: WAHP_FEIRTT_HEAT
         :classmethod:
         :type: iesve.HVACSystemCurveRole
      
         An instance of this class with:
         
         * a value of 12
         * a name of "WAHP_FEIRTT_HEAT".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'CHILL_FCAPTT': iesve.HVACSystemCurveRole.CHILL_FCAPTT
             'CHILL_FEIRTT': iesve.HVACSystemCurveRole.CHILL_FEIRTT
             'CHILL_FEIRPT': iesve.HVACSystemCurveRole.CHILL_FEIRPT
             'PUMP_PWRV': iesve.HVACSystemCurveRole.PUMP_PWRV
             'BOIL_FEPT': iesve.HVACSystemCurveRole.BOIL_FEPT
             'EAC_FCAPTT': iesve.HVACSystemCurveRole.EAC_FCAPTT
             'EAC_FEIRTT': iesve.HVACSystemCurveRole.EAC_FEIRTT
             'EAC_FEIRPT': iesve.HVACSystemCurveRole.EAC_FEIRPT
             'DX_FCAPTT': iesve.HVACSystemCurveRole.DX_FCAPTT
             'DX_FEIRTT': iesve.HVACSystemCurveRole.DX_FEIRTT
             'DX_FEIRP': iesve.HVACSystemCurveRole.DX_FEIRP
             'WAHP_FCAPTT_HEAT': iesve.HVACSystemCurveRole.WAHP_FCAPTT_HEAT
             'WAHP_FEIRTT_HEAT': iesve.HVACSystemCurveRole.WAHP_FEIRTT_HEAT
             'WAHP_FEIRP_HEAT': iesve.HVACSystemCurveRole.WAHP_FEIRP_HEAT
             'WAHP_FCAPTT_COOL': iesve.HVACSystemCurveRole.WAHP_FCAPTT_COOL
             'WAHP_FEIRTT_COOL': iesve.HVACSystemCurveRole.WAHP_FEIRTT_COOL
             'WAHP_FEIRP_COOL': iesve.HVACSystemCurveRole.WAHP_FEIRP_COOL
             'AAHPH_FCAPT': iesve.HVACSystemCurveRole.AAHPH_FCAPT
             'AAHPH_FEIRT': iesve.HVACSystemCurveRole.AAHPH_FEIRT
             'AAHPH_FEIRP': iesve.HVACSystemCurveRole.AAHPH_FEIRP
             'AAHPH_FDEIRTT': iesve.HVACSystemCurveRole.AAHPH_FDEIRTT
             'AAHPC_FCAPTT': iesve.HVACSystemCurveRole.AAHPC_FCAPTT
             'AAHPC_FEIRTT': iesve.HVACSystemCurveRole.AAHPC_FEIRTT
             'AAHPC_FEIRP': iesve.HVACSystemCurveRole.AAHPC_FEIRP
             'CPHPH_FCAPTT': iesve.HVACSystemCurveRole.CPHPH_FCAPTT
             'CPHPH_FEIRTT': iesve.HVACSystemCurveRole.CPHPH_FEIRTT
             'CPHPH_FEIRP': iesve.HVACSystemCurveRole.CPHPH_FEIRP
             'CPHPH_FDEIRTT': iesve.HVACSystemCurveRole.CPHPH_FDEIRTT
             'CPHPC_FCAPTT': iesve.HVACSystemCurveRole.CPHPC_FCAPTT
             'CPHPC_FEIRTT': iesve.HVACSystemCurveRole.CPHPC_FEIRTT
             'CPHPC_FEIRP': iesve.HVACSystemCurveRole.CPHPC_FEIRP
             'CPHPH_FCOPTT': iesve.HVACSystemCurveRole.CPHPH_FCOPTT
             'CPHPH_FCOPP': iesve.HVACSystemCurveRole.CPHPH_FCOPP
             'CPHPC_FCOPTT': iesve.HVACSystemCurveRole.CPHPC_FCOPTT
             'CPHPC_FCOPP': iesve.HVACSystemCurveRole.CPHPC_FCOPP
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACSystemCurveRole.CHILL_FCAPTT
             1: iesve.HVACSystemCurveRole.CHILL_FEIRTT
             2: iesve.HVACSystemCurveRole.CHILL_FEIRPT
             3: iesve.HVACSystemCurveRole.PUMP_PWRV
             4: iesve.HVACSystemCurveRole.BOIL_FEPT
             5: iesve.HVACSystemCurveRole.EAC_FCAPTT
             6: iesve.HVACSystemCurveRole.EAC_FEIRTT
             7: iesve.HVACSystemCurveRole.EAC_FEIRPT
             8: iesve.HVACSystemCurveRole.DX_FCAPTT
             9: iesve.HVACSystemCurveRole.DX_FEIRTT
             10: iesve.HVACSystemCurveRole.DX_FEIRP
             11: iesve.HVACSystemCurveRole.WAHP_FCAPTT_HEAT
             12: iesve.HVACSystemCurveRole.WAHP_FEIRTT_HEAT
             13: iesve.HVACSystemCurveRole.WAHP_FEIRP_HEAT
             14: iesve.HVACSystemCurveRole.WAHP_FCAPTT_COOL
             15: iesve.HVACSystemCurveRole.WAHP_FEIRTT_COOL
             16: iesve.HVACSystemCurveRole.WAHP_FEIRP_COOL
             17: iesve.HVACSystemCurveRole.AAHPH_FCAPT
             18: iesve.HVACSystemCurveRole.AAHPH_FEIRT
             19: iesve.HVACSystemCurveRole.AAHPH_FEIRP
             20: iesve.HVACSystemCurveRole.AAHPH_FDEIRTT
             21: iesve.HVACSystemCurveRole.AAHPC_FCAPTT
             22: iesve.HVACSystemCurveRole.AAHPC_FEIRTT
             23: iesve.HVACSystemCurveRole.AAHPC_FEIRP
             24: iesve.HVACSystemCurveRole.CPHPH_FCAPTT
             25: iesve.HVACSystemCurveRole.CPHPH_FEIRTT
             26: iesve.HVACSystemCurveRole.CPHPH_FEIRP
             27: iesve.HVACSystemCurveRole.CPHPH_FDEIRTT
             28: iesve.HVACSystemCurveRole.CPHPC_FCAPTT
             29: iesve.HVACSystemCurveRole.CPHPC_FEIRTT
             30: iesve.HVACSystemCurveRole.CPHPC_FEIRP
             31: iesve.HVACSystemCurveRole.CPHPH_FCOPTT
             32: iesve.HVACSystemCurveRole.CPHPH_FCOPP
             33: iesve.HVACSystemCurveRole.CPHPC_FCOPTT
             34: iesve.HVACSystemCurveRole.CPHPC_FCOPP
            }
      
   .. py:class:: HVACSystemCurveType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: centrifugal
         :classmethod:
         :type: iesve.HVACSystemCurveType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "centrifugal".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'centrifugal': iesve.HVACSystemCurveType.centrifugal
             'reciprocating': iesve.HVACSystemCurveType.reciprocating
             'screw': iesve.HVACSystemCurveType.screw
             'scroll': iesve.HVACSystemCurveType.scroll
             'other': iesve.HVACSystemCurveType.other
            }
      
      .. py:property:: other
         :classmethod:
         :type: iesve.HVACSystemCurveType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "other".
      
      .. py:property:: reciprocating
         :classmethod:
         :type: iesve.HVACSystemCurveType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "reciprocating".
      
      .. py:property:: screw
         :classmethod:
         :type: iesve.HVACSystemCurveType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "screw".
      
      .. py:property:: scroll
         :classmethod:
         :type: iesve.HVACSystemCurveType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "scroll".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACSystemCurveType.centrifugal
             1: iesve.HVACSystemCurveType.reciprocating
             2: iesve.HVACSystemCurveType.screw
             3: iesve.HVACSystemCurveType.scroll
             4: iesve.HVACSystemCurveType.other
            }
      
   .. py:class:: HVACSystemLink
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ACT_BEAM_IU_INDUCED_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2010
         * a name of "ACT_BEAM_IU_INDUCED_AIRFLOW".
      
      .. py:property:: ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2008
         * a name of "ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOL".
      
      .. py:property:: ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOLING_ONLY
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2108
         * a name of "ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOLING_ONLY".
      
      .. py:property:: ACT_BM_IU_PRIMARY_AIR_CAV_VAV_HEAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2009
         * a name of "ACT_BM_IU_PRIMARY_AIR_CAV_VAV_HEAT".
      
      .. py:property:: ADJACENT_SPACE_WITH_EA_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 504
         * a name of "ADJACENT_SPACE_WITH_EA_FAN".
      
      .. py:property:: AHU_COOLING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 700
         * a name of "AHU_COOLING_COIL".
      
      .. py:property:: AHU_HEATING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 601
         * a name of "AHU_HEATING_COIL".
      
      .. py:property:: AHU_PRE_HEAT_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 600
         * a name of "AHU_PRE_HEAT_COIL".
      
      .. py:property:: AIRFLOW_ON_IF_NV_INSUF_COOL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2027
         * a name of "AIRFLOW_ON_IF_NV_INSUF_COOL".
      
      .. py:property:: AIRFLOW_ON_IF_NV_INSUF_VENT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2028
         * a name of "AIRFLOW_ON_IF_NV_INSUF_VENT".
      
      .. py:property:: CAV_AIRFLOW_NIGHTTIME_SETBACK
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2020
         * a name of "CAV_AIRFLOW_NIGHTTIME_SETBACK".
      
      .. py:property:: CAV_AIRFLOW_OCCUPIED_HOURS
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2019
         * a name of "CAV_AIRFLOW_OCCUPIED_HOURS".
      
      .. py:property:: COOLING_AIRFLOW_VAV_CAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2000
         * a name of "COOLING_AIRFLOW_VAV_CAV".
      
      .. py:property:: COOLING_COIL_AHU_COOL_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2066
         * a name of "COOLING_COIL_AHU_COOL_LAT".
      
      .. py:property:: COOLING_COIL_AHU_DEHUM_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2067
         * a name of "COOLING_COIL_AHU_DEHUM_LAT".
      
      .. py:property:: COOLING_COIL_AHU_EXTEND_DEHUM_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2068
         * a name of "COOLING_COIL_AHU_EXTEND_DEHUM_LAT".
      
      .. py:property:: COOLING_COIL_AHU_LOWTEMP_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2099
         * a name of "COOLING_COIL_AHU_LOWTEMP_LAT".
      
      .. py:property:: COOLING_COIL_AHU_SUPPLY_AIR_DPT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2069
         * a name of "COOLING_COIL_AHU_SUPPLY_AIR_DPT".
      
      .. py:property:: COOLING_COIL_COIL_LEAVING_DPT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2070
         * a name of "COOLING_COIL_COIL_LEAVING_DPT".
      
      .. py:property:: COOLING_COIL_DOAS_DEHUM
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2097
         * a name of "COOLING_COIL_DOAS_DEHUM".
      
      .. py:property:: COOLING_COIL_DOAS_FIXED_TEMP
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2096
         * a name of "COOLING_COIL_DOAS_FIXED_TEMP".
      
      .. py:property:: COOLING_COIL_DOAS_TEMPERING
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2073
         * a name of "COOLING_COIL_DOAS_TEMPERING".
      
      .. py:property:: COOLING_COIL_FULL_COOLING_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2075
         * a name of "COOLING_COIL_FULL_COOLING_LAT_BAND".
      
      .. py:property:: COOLING_COIL_FULL_DEHUM_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2076
         * a name of "COOLING_COIL_FULL_DEHUM_LAT_BAND".
      
      .. py:property:: COOLING_COIL_FULL_H_C_DEHUM_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2079
         * a name of "COOLING_COIL_FULL_H_C_DEHUM_LAT".
      
      .. py:property:: COOLING_COIL_FULL_H_C_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2078
         * a name of "COOLING_COIL_FULL_H_C_LAT_BAND".
      
      .. py:property:: COOLING_COIL_ZONE_FIXED_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2083
         * a name of "COOLING_COIL_ZONE_FIXED_LAT".
      
      .. py:property:: COOLING_COIL_ZONE_VARIABLE_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2081
         * a name of "COOLING_COIL_ZONE_VARIABLE_LAT".
      
      .. py:property:: COOLING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2100
         * a name of "COOLING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET".
      
      .. py:property:: COOLING_ONLY_SYS_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2017
         * a name of "COOLING_ONLY_SYS_AIRFLOW".
      
      .. py:property:: COOLING_THERMOSTAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2104
         * a name of "COOLING_THERMOSTAT".
      
      .. py:property:: DCV_MIN_OUTSIDE_AIR_ECON
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 110
         * a name of "DCV_MIN_OUTSIDE_AIR_ECON".
      
      .. py:property:: DEDICATED_OA_VENT_COOLING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 704
         * a name of "DEDICATED_OA_VENT_COOLING_COIL".
      
      .. py:property:: DEDICATED_OA_VENT_HEATING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 606
         * a name of "DEDICATED_OA_VENT_HEATING_COIL".
      
      .. py:property:: DELIMITER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of -1
         * a name of "DELIMITER".
      
      .. py:property:: DIRECT_ACTING_HEATER_COOLER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2089
         * a name of "DIRECT_ACTING_HEATER_COOLER".
      
      .. py:property:: DIRECT_EVAP_COOLING
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2059
         * a name of "DIRECT_EVAP_COOLING".
      
      .. py:property:: DIRECT_EVAP_SPRAY
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 1001
         * a name of "DIRECT_EVAP_SPRAY".
      
      .. py:property:: DOAS_AHU_COOLING_DEVICE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 800
         * a name of "DOAS_AHU_COOLING_DEVICE".
      
      .. py:property:: DOAS_PTAC_PTHP_COOLING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2094
         * a name of "DOAS_PTAC_PTHP_COOLING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: DOAS_PTAC_PTHP_HEATING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2095
         * a name of "DOAS_PTAC_PTHP_HEATING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: DOAS_VENT_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2002
         * a name of "DOAS_VENT_AIRFLOW".
      
      .. py:property:: DOAS_VENT_AIRFLOW_CAV_DCV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2003
         * a name of "DOAS_VENT_AIRFLOW_CAV_DCV".
      
      .. py:property:: DUAL_FAN_DUAL_DUCT_ZN_HEAT_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2011
         * a name of "DUAL_FAN_DUAL_DUCT_ZN_HEAT_AIRFLOW".
      
      .. py:property:: DUAL_FAN_DUAL_DUCT_ZONE_COOL_AIRFLOW_AND_OA_VENT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2107
         * a name of "DUAL_FAN_DUAL_DUCT_ZONE_COOL_AIRFLOW_AND_OA_VENT".
      
      .. py:property:: EA_PERCENT_AVAILABLE_TO_ER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2032
         * a name of "EA_PERCENT_AVAILABLE_TO_ER".
      
      .. py:property:: EA_PERCENT_VS_RETURN_OR_TRANSFER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2031
         * a name of "EA_PERCENT_VS_RETURN_OR_TRANSFER".
      
      .. py:property:: ELEC_HEAT_COIL_2ND_STAGE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 605
         * a name of "ELEC_HEAT_COIL_2ND_STAGE".
      
      .. py:property:: ENERGY_RECOVERY_BYPASS_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 104
         * a name of "ENERGY_RECOVERY_BYPASS_DAMPER".
      
      .. py:property:: ENERGY_RECOVERY_BYPASS_LEGACY_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 108
         * a name of "ENERGY_RECOVERY_BYPASS_LEGACY_DAMPER".
      
      .. py:property:: ENERGY_RECOVERY_HX_WHEEL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 900
         * a name of "ENERGY_RECOVERY_HX_WHEEL".
      
      .. py:property:: ER_BYPASS_TEMP_TARGET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2047
         * a name of "ER_BYPASS_TEMP_TARGET".
      
      .. py:property:: ER_BYPASS_TEMP_TARGET_LEGACY_CONFIG
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2091
         * a name of "ER_BYPASS_TEMP_TARGET_LEGACY_CONFIG".
      
      .. py:property:: ER_BYPASS_TEMP_TARGET_PSZ
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2051
         * a name of "ER_BYPASS_TEMP_TARGET_PSZ".
      
      .. py:property:: ER_BYPASS_TEMP_TARGET_PSZ_LEGACY
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2092
         * a name of "ER_BYPASS_TEMP_TARGET_PSZ_LEGACY".
      
      .. py:property:: ER_TARGET_COOL_MODE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2048
         * a name of "ER_TARGET_COOL_MODE".
      
      .. py:property:: ER_TARGET_HEAT_MODE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2049
         * a name of "ER_TARGET_HEAT_MODE".
      
      .. py:property:: ER_TARGET_PSZ_HEAT_COOL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2050
         * a name of "ER_TARGET_PSZ_HEAT_COOL".
      
      .. py:property:: EVAP_SPRAY_HUMID_PER_ZN_RH
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2061
         * a name of "EVAP_SPRAY_HUMID_PER_ZN_RH".
      
      .. py:property:: EVAP_SPRAY_HUMID_SA_RH
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2062
         * a name of "EVAP_SPRAY_HUMID_SA_RH".
      
      .. py:property:: EXHAUST_CV_HOOD_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2026
         * a name of "EXHAUST_CV_HOOD_AIRFLOW".
      
      .. py:property:: EXHAUST_DRIVEN_VENTILATION_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2090
         * a name of "EXHAUST_DRIVEN_VENTILATION_AIRFLOW".
      
      .. py:property:: EXHAUST_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 203
         * a name of "EXHAUST_FAN".
      
      .. py:property:: FCU_ACT_BEAM_COOL_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 701
         * a name of "FCU_ACT_BEAM_COOL_COIL".
      
      .. py:property:: FCU_ACT_BEAM_HEAT_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 603
         * a name of "FCU_ACT_BEAM_HEAT_COIL".
      
      .. py:property:: FCU_COOLING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2004
         * a name of "FCU_COOLING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: FCU_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 204
         * a name of "FCU_FAN".
      
      .. py:property:: FCU_HEATING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2005
         * a name of "FCU_HEATING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: FILTER_PRESSURE_AND_CHANGE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 300
         * a name of "FILTER_PRESSURE_AND_CHANGE".
      
      .. py:property:: FPB_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 205
         * a name of "FPB_FAN".
      
      .. py:property:: FPB_PRIMARY_AIRFLOW_CAV_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2006
         * a name of "FPB_PRIMARY_AIRFLOW_CAV_VAV".
      
      .. py:property:: FPB_SECONDARY_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2007
         * a name of "FPB_SECONDARY_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: HEATED_COOLED_SLAB_ZONE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 505
         * a name of "HEATED_COOLED_SLAB_ZONE".
      
      .. py:property:: HEATING_AIRFLOW_VAV_CAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2001
         * a name of "HEATING_AIRFLOW_VAV_CAV".
      
      .. py:property:: HEATING_COIL_AHU_MIN_SAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2071
         * a name of "HEATING_COIL_AHU_MIN_SAT".
      
      .. py:property:: HEATING_COIL_DOAS_TEMPERING
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2074
         * a name of "HEATING_COIL_DOAS_TEMPERING".
      
      .. py:property:: HEATING_COIL_FULL_HEATING_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2077
         * a name of "HEATING_COIL_FULL_HEATING_LAT_BAND".
      
      .. py:property:: HEATING_COIL_FULL_H_C_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2080
         * a name of "HEATING_COIL_FULL_H_C_LAT_BAND".
      
      .. py:property:: HEATING_COIL_MIN_SAT_WITH_RESET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2072
         * a name of "HEATING_COIL_MIN_SAT_WITH_RESET".
      
      .. py:property:: HEATING_COIL_ZN_FIX_LAT_STAGE_1
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2085
         * a name of "HEATING_COIL_ZN_FIX_LAT_STAGE_1".
      
      .. py:property:: HEATING_COIL_ZN_FIX_LAT_STAGE_2
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2086
         * a name of "HEATING_COIL_ZN_FIX_LAT_STAGE_2".
      
      .. py:property:: HEATING_COIL_ZONE_FIXED_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2084
         * a name of "HEATING_COIL_ZONE_FIXED_LAT".
      
      .. py:property:: HEATING_COIL_ZONE_VARIABLE_LAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2082
         * a name of "HEATING_COIL_ZONE_VARIABLE_LAT".
      
      .. py:property:: HEATING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2101
         * a name of "HEATING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET".
      
      .. py:property:: HEATING_ONLY_SYS_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2018
         * a name of "HEATING_ONLY_SYS_AIRFLOW".
      
      .. py:property:: HEATING_THERMOSTAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2105
         * a name of "HEATING_THERMOSTAT".
      
      .. py:property:: HEAT_PIPE_RR_WHL_BYPASS_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 105
         * a name of "HEAT_PIPE_RR_WHL_BYPASS_DAMPER".
      
      .. py:property:: HEAT_PIPE_RUN_RND_WHEEL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 901
         * a name of "HEAT_PIPE_RUN_RND_WHEEL".
      
      .. py:property:: HP_RRCOIL_WHL_BYPASS_TEMP
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2052
         * a name of "HP_RRCOIL_WHL_BYPASS_TEMP".
      
      .. py:property:: HP_RR_WHL_BYPASS_TEMP_DIFF
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2053
         * a name of "HP_RR_WHL_BYPASS_TEMP_DIFF".
      
      .. py:property:: INDIRECT_EVAP_COOLING
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2058
         * a name of "INDIRECT_EVAP_COOLING".
      
      .. py:property:: INDIRECT_EVAP_SPRAY
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 1002
         * a name of "INDIRECT_EVAP_SPRAY".
      
      .. py:property:: MIN_FAN_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2021
         * a name of "MIN_FAN_AIRFLOW".
      
      .. py:property:: MIXED_MODE_DISABLE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2029
         * a name of "MIXED_MODE_DISABLE".
      
      .. py:property:: MIXED_MODE_TOUT_TZN_DELTA
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2030
         * a name of "MIXED_MODE_TOUT_TZN_DELTA".
      
      .. py:property:: MODULATION_BY_LOAD
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2106
         * a name of "MODULATION_BY_LOAD".
      
      .. py:property:: NONE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 0
         * a name of "NONE".
      
      .. py:property:: OA_ECON_DBT_HIGH_LIMIT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2109
         * a name of "OA_ECON_DBT_HIGH_LIMIT".
      
      .. py:property:: OA_ECON_DIFF_ENTHALPY
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2040
         * a name of "OA_ECON_DIFF_ENTHALPY".
      
      .. py:property:: OA_ECON_DPT_LIMIT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2039
         * a name of "OA_ECON_DPT_LIMIT".
      
      .. py:property:: OA_ECON_TARGET_AND_DBT_LIMIT_DEPRECATED
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2034
         * a name of "OA_ECON_TARGET_AND_DBT_LIMIT_DEPRECATED".
      
      .. py:property:: OA_ECON_TARGET_FULL_COOLING_LAT_BAND
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2110
         * a name of "OA_ECON_TARGET_FULL_COOLING_LAT_BAND".
      
      .. py:property:: OA_ECON_TARGET_PER_RA_TEMP
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2093
         * a name of "OA_ECON_TARGET_PER_RA_TEMP".
      
      .. py:property:: OA_ECON_TARGET_RESET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2035
         * a name of "OA_ECON_TARGET_RESET".
      
      .. py:property:: OA_ECON_ZN_TEMP_LOW_LIMIT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2036
         * a name of "OA_ECON_ZN_TEMP_LOW_LIMIT".
      
      .. py:property:: OA_FIXED_PERCENTAGE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2038
         * a name of "OA_FIXED_PERCENTAGE".
      
      .. py:property:: OA_MIN_RESET_OCCUPIED_ZONE_CO2
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2043
         * a name of "OA_MIN_RESET_OCCUPIED_ZONE_CO2".
      
      .. py:property:: OA_MIN_RESET_OCCUPIED_ZONE_VAV_FLOW_PERCENT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2045
         * a name of "OA_MIN_RESET_OCCUPIED_ZONE_VAV_FLOW_PERCENT".
      
      .. py:property:: OA_MIN_RESET_UNOCCUPIED_ZN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2044
         * a name of "OA_MIN_RESET_UNOCCUPIED_ZN".
      
      .. py:property:: OA_MIN_RESET_UNOCCUPIED_ZN_VAV_FLOW_PERCENT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2046
         * a name of "OA_MIN_RESET_UNOCCUPIED_ZN_VAV_FLOW_PERCENT".
      
      .. py:property:: OA_MIN_RESET_ZN_VAV_FLOW_PERCENT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2042
         * a name of "OA_MIN_RESET_ZN_VAV_FLOW_PERCENT".
      
      .. py:property:: OA_MIN_RESET_ZONE_CO2
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2041
         * a name of "OA_MIN_RESET_ZONE_CO2".
      
      .. py:property:: OA_VARIABLE_MIN_PERCENTAGE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2037
         * a name of "OA_VARIABLE_MIN_PERCENTAGE".
      
      .. py:property:: OCCUPIED_ZONE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 500
         * a name of "OCCUPIED_ZONE".
      
      .. py:property:: ON_IF_TEMP_BELOW_MIN_SAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2111
         * a name of "ON_IF_TEMP_BELOW_MIN_SAT".
      
      .. py:property:: OUTSIDE_AIR_FIXED_MIN_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 103
         * a name of "OUTSIDE_AIR_FIXED_MIN_DAMPER".
      
      .. py:property:: OUTSIDE_AIR_MIN_ECON_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 100
         * a name of "OUTSIDE_AIR_MIN_ECON_DAMPER".
      
      .. py:property:: OUTSIDE_AIR_NO_MIN_ECON_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 101
         * a name of "OUTSIDE_AIR_NO_MIN_ECON_DAMPER".
      
      .. py:property:: OUTSIDE_AIR_VARIABLE_MIN_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 102
         * a name of "OUTSIDE_AIR_VARIABLE_MIN_DAMPER".
      
      .. py:property:: PACKAGE_TERMINAL_UNIT_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 206
         * a name of "PACKAGE_TERMINAL_UNIT_FAN".
      
      .. py:property:: PARKING_GARAGE_EXHAUST
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2098
         * a name of "PARKING_GARAGE_EXHAUST".
      
      .. py:property:: PRE_HEAT_COIL_AHU_MIN_EAT
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2065
         * a name of "PRE_HEAT_COIL_AHU_MIN_EAT".
      
      .. py:property:: PSZ_COOLING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2012
         * a name of "PSZ_COOLING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: PSZ_HEATING_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2013
         * a name of "PSZ_HEATING_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: PTAC_PTHP_COOLING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 702
         * a name of "PTAC_PTHP_COOLING_COIL".
      
      .. py:property:: PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2014
         * a name of "PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2102
         * a name of "PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV_NO_OFFSET".
      
      .. py:property:: PTAC_PTHP_HEATING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 604
         * a name of "PTAC_PTHP_HEATING_COIL".
      
      .. py:property:: PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2015
         * a name of "PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV".
      
      .. py:property:: PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2103
         * a name of "PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV_NO_OFFSET".
      
      .. py:property:: RAD_CONV_COOL_DEVICE_PANEL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2088
         * a name of "RAD_CONV_COOL_DEVICE_PANEL".
      
      .. py:property:: RAD_CONV_HEAT_DEVICE_PANEL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2087
         * a name of "RAD_CONV_HEAT_DEVICE_PANEL".
      
      .. py:property:: RA_BYPASS_MIXED_AIR_TARGET_TEMP
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2054
         * a name of "RA_BYPASS_MIXED_AIR_TARGET_TEMP".
      
      .. py:property:: RA_DUCT_HEAT_LOSS_GAIN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 401
         * a name of "RA_DUCT_HEAT_LOSS_GAIN".
      
      .. py:property:: RA_PERCENT_TO_ALT_PATH_OR_ZONE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2033
         * a name of "RA_PERCENT_TO_ALT_PATH_OR_ZONE".
      
      .. py:property:: RA_PLENUM
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 503
         * a name of "RA_PLENUM".
      
      .. py:property:: RETURN_AIR_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 107
         * a name of "RETURN_AIR_DAMPER".
      
      .. py:property:: RETURN_RELIEF_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 202
         * a name of "RETURN_RELIEF_FAN".
      
      .. py:property:: SA_DUCT_HEAT_LOSS_GAIN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 400
         * a name of "SA_DUCT_HEAT_LOSS_GAIN".
      
      .. py:property:: SA_UFAD_PLENUM
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 502
         * a name of "SA_UFAD_PLENUM".
      
      .. py:property:: SERIES_FPB_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 109
         * a name of "SERIES_FPB_DAMPER".
      
      .. py:property:: STEAM_HUMIDIFIER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 1000
         * a name of "STEAM_HUMIDIFIER".
      
      .. py:property:: STEAM_HUMID_PER_ZN_RH
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2063
         * a name of "STEAM_HUMID_PER_ZN_RH".
      
      .. py:property:: STEAM_HUMID_SA_RH
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2064
         * a name of "STEAM_HUMID_SA_RH".
      
      .. py:property:: STRATIFIED_ZN_REMIX_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2024
         * a name of "STRATIFIED_ZN_REMIX_AIRFLOW".
      
      .. py:property:: SUPPLY_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 200
         * a name of "SUPPLY_FAN".
      
      .. py:property:: SUPPLY_FAN_TSP_ADDITION
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 201
         * a name of "SUPPLY_FAN_TSP_ADDITION".
      
      .. py:property:: THERMALLY_STRATIFIED_ZONE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 501
         * a name of "THERMALLY_STRATIFIED_ZONE".
      
      .. py:property:: UCS_COOLING_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2016
         * a name of "UCS_COOLING_AIRFLOW".
      
      .. py:property:: UCS_COOLING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 703
         * a name of "UCS_COOLING_COIL".
      
      .. py:property:: UNIT_HEATER_FAN
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 207
         * a name of "UNIT_HEATER_FAN".
      
      .. py:property:: VOID_SPACE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 506
         * a name of "VOID_SPACE".
      
      .. py:property:: ZONE_AIRFLOW_DETECTION
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2023
         * a name of "ZONE_AIRFLOW_DETECTION".
      
      .. py:property:: ZONE_COOLING_DEVICE
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 801
         * a name of "ZONE_COOLING_DEVICE".
      
      .. py:property:: ZONE_DCV_STAGE1_VAV_CTRL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2022
         * a name of "ZONE_DCV_STAGE1_VAV_CTRL".
      
      .. py:property:: ZONE_MIXING_BOX_DAMPER
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 106
         * a name of "ZONE_MIXING_BOX_DAMPER".
      
      .. py:property:: ZONE_MIXING_FIXED_DBT_DAMPER_TARGET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2057
         * a name of "ZONE_MIXING_FIXED_DBT_DAMPER_TARGET".
      
      .. py:property:: ZONE_MIXING_PERCENT_PRIMARY_AIR
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2056
         * a name of "ZONE_MIXING_PERCENT_PRIMARY_AIR".
      
      .. py:property:: ZONE_MIXING_VARIABLE_DBT_TARGET
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2055
         * a name of "ZONE_MIXING_VARIABLE_DBT_TARGET".
      
      .. py:property:: ZONE_RA_TRANSFER_AIRFLOW
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2025
         * a name of "ZONE_RA_TRANSFER_AIRFLOW".
      
      .. py:property:: ZONE_REHEAT_HEATING_COIL
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 602
         * a name of "ZONE_REHEAT_HEATING_COIL".
      
      .. py:property:: ZONE_RH_HIGH_LIMIT_FOR_DEC
         :classmethod:
         :type: iesve.HVACSystemLink
      
         An instance of this class with:
         
         * a value of 2060
         * a name of "ZONE_RH_HIGH_LIMIT_FOR_DEC".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'DELIMITER': iesve.HVACSystemLink.DELIMITER
             'NONE': iesve.HVACSystemLink.NONE
             'OUTSIDE_AIR_MIN_ECON_DAMPER': iesve.HVACSystemLink.OUTSIDE_AIR_MIN_ECON_DAMPER
             'OUTSIDE_AIR_NO_MIN_ECON_DAMPER': iesve.HVACSystemLink.OUTSIDE_AIR_NO_MIN_ECON_DAMPER
             'OUTSIDE_AIR_VARIABLE_MIN_DAMPER': iesve.HVACSystemLink.OUTSIDE_AIR_VARIABLE_MIN_DAMPER
             'OUTSIDE_AIR_FIXED_MIN_DAMPER': iesve.HVACSystemLink.OUTSIDE_AIR_FIXED_MIN_DAMPER
             'ENERGY_RECOVERY_BYPASS_DAMPER': iesve.HVACSystemLink.ENERGY_RECOVERY_BYPASS_DAMPER
             'HEAT_PIPE_RR_WHL_BYPASS_DAMPER': iesve.HVACSystemLink.HEAT_PIPE_RR_WHL_BYPASS_DAMPER
             'ZONE_MIXING_BOX_DAMPER': iesve.HVACSystemLink.ZONE_MIXING_BOX_DAMPER
             'RETURN_AIR_DAMPER': iesve.HVACSystemLink.RETURN_AIR_DAMPER
             'ENERGY_RECOVERY_BYPASS_LEGACY_DAMPER': iesve.HVACSystemLink.ENERGY_RECOVERY_BYPASS_LEGACY_DAMPER
             'SERIES_FPB_DAMPER': iesve.HVACSystemLink.SERIES_FPB_DAMPER
             'DCV_MIN_OUTSIDE_AIR_ECON': iesve.HVACSystemLink.DCV_MIN_OUTSIDE_AIR_ECON
             'SUPPLY_FAN': iesve.HVACSystemLink.SUPPLY_FAN
             'SUPPLY_FAN_TSP_ADDITION': iesve.HVACSystemLink.SUPPLY_FAN_TSP_ADDITION
             'RETURN_RELIEF_FAN': iesve.HVACSystemLink.RETURN_RELIEF_FAN
             'EXHAUST_FAN': iesve.HVACSystemLink.EXHAUST_FAN
             'FCU_FAN': iesve.HVACSystemLink.FCU_FAN
             'FPB_FAN': iesve.HVACSystemLink.FPB_FAN
             'PACKAGE_TERMINAL_UNIT_FAN': iesve.HVACSystemLink.PACKAGE_TERMINAL_UNIT_FAN
             'UNIT_HEATER_FAN': iesve.HVACSystemLink.UNIT_HEATER_FAN
             'FILTER_PRESSURE_AND_CHANGE': iesve.HVACSystemLink.FILTER_PRESSURE_AND_CHANGE
             'SA_DUCT_HEAT_LOSS_GAIN': iesve.HVACSystemLink.SA_DUCT_HEAT_LOSS_GAIN
             'RA_DUCT_HEAT_LOSS_GAIN': iesve.HVACSystemLink.RA_DUCT_HEAT_LOSS_GAIN
             'OCCUPIED_ZONE': iesve.HVACSystemLink.OCCUPIED_ZONE
             'THERMALLY_STRATIFIED_ZONE': iesve.HVACSystemLink.THERMALLY_STRATIFIED_ZONE
             'SA_UFAD_PLENUM': iesve.HVACSystemLink.SA_UFAD_PLENUM
             'RA_PLENUM': iesve.HVACSystemLink.RA_PLENUM
             'ADJACENT_SPACE_WITH_EA_FAN': iesve.HVACSystemLink.ADJACENT_SPACE_WITH_EA_FAN
             'HEATED_COOLED_SLAB_ZONE': iesve.HVACSystemLink.HEATED_COOLED_SLAB_ZONE
             'VOID_SPACE': iesve.HVACSystemLink.VOID_SPACE
             'AHU_PRE_HEAT_COIL': iesve.HVACSystemLink.AHU_PRE_HEAT_COIL
             'AHU_HEATING_COIL': iesve.HVACSystemLink.AHU_HEATING_COIL
             'ZONE_REHEAT_HEATING_COIL': iesve.HVACSystemLink.ZONE_REHEAT_HEATING_COIL
             'FCU_ACT_BEAM_HEAT_COIL': iesve.HVACSystemLink.FCU_ACT_BEAM_HEAT_COIL
             'PTAC_PTHP_HEATING_COIL': iesve.HVACSystemLink.PTAC_PTHP_HEATING_COIL
             'ELEC_HEAT_COIL_2ND_STAGE': iesve.HVACSystemLink.ELEC_HEAT_COIL_2ND_STAGE
             'DEDICATED_OA_VENT_HEATING_COIL': iesve.HVACSystemLink.DEDICATED_OA_VENT_HEATING_COIL
             'AHU_COOLING_COIL': iesve.HVACSystemLink.AHU_COOLING_COIL
             'FCU_ACT_BEAM_COOL_COIL': iesve.HVACSystemLink.FCU_ACT_BEAM_COOL_COIL
             'PTAC_PTHP_COOLING_COIL': iesve.HVACSystemLink.PTAC_PTHP_COOLING_COIL
             'UCS_COOLING_COIL': iesve.HVACSystemLink.UCS_COOLING_COIL
             'DEDICATED_OA_VENT_COOLING_COIL': iesve.HVACSystemLink.DEDICATED_OA_VENT_COOLING_COIL
             'DOAS_AHU_COOLING_DEVICE': iesve.HVACSystemLink.DOAS_AHU_COOLING_DEVICE
             'ZONE_COOLING_DEVICE': iesve.HVACSystemLink.ZONE_COOLING_DEVICE
             'ENERGY_RECOVERY_HX_WHEEL': iesve.HVACSystemLink.ENERGY_RECOVERY_HX_WHEEL
             'HEAT_PIPE_RUN_RND_WHEEL': iesve.HVACSystemLink.HEAT_PIPE_RUN_RND_WHEEL
             'STEAM_HUMIDIFIER': iesve.HVACSystemLink.STEAM_HUMIDIFIER
             'DIRECT_EVAP_SPRAY': iesve.HVACSystemLink.DIRECT_EVAP_SPRAY
             'INDIRECT_EVAP_SPRAY': iesve.HVACSystemLink.INDIRECT_EVAP_SPRAY
             'COOLING_AIRFLOW_VAV_CAV': iesve.HVACSystemLink.COOLING_AIRFLOW_VAV_CAV
             'HEATING_AIRFLOW_VAV_CAV': iesve.HVACSystemLink.HEATING_AIRFLOW_VAV_CAV
             'DOAS_VENT_AIRFLOW': iesve.HVACSystemLink.DOAS_VENT_AIRFLOW
             'DOAS_VENT_AIRFLOW_CAV_DCV': iesve.HVACSystemLink.DOAS_VENT_AIRFLOW_CAV_DCV
             'FCU_COOLING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.FCU_COOLING_AIRFLOW_CAV_2SP_VAV
             'FCU_HEATING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.FCU_HEATING_AIRFLOW_CAV_2SP_VAV
             'FPB_PRIMARY_AIRFLOW_CAV_VAV': iesve.HVACSystemLink.FPB_PRIMARY_AIRFLOW_CAV_VAV
             'FPB_SECONDARY_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.FPB_SECONDARY_AIRFLOW_CAV_2SP_VAV
             'ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOL': iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOL
             'ACT_BM_IU_PRIMARY_AIR_CAV_VAV_HEAT': iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_HEAT
             'ACT_BEAM_IU_INDUCED_AIRFLOW': iesve.HVACSystemLink.ACT_BEAM_IU_INDUCED_AIRFLOW
             'DUAL_FAN_DUAL_DUCT_ZN_HEAT_AIRFLOW': iesve.HVACSystemLink.DUAL_FAN_DUAL_DUCT_ZN_HEAT_AIRFLOW
             'PSZ_COOLING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.PSZ_COOLING_AIRFLOW_CAV_2SP_VAV
             'PSZ_HEATING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.PSZ_HEATING_AIRFLOW_CAV_2SP_VAV
             'PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV
             'PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV
             'UCS_COOLING_AIRFLOW': iesve.HVACSystemLink.UCS_COOLING_AIRFLOW
             'COOLING_ONLY_SYS_AIRFLOW': iesve.HVACSystemLink.COOLING_ONLY_SYS_AIRFLOW
             'HEATING_ONLY_SYS_AIRFLOW': iesve.HVACSystemLink.HEATING_ONLY_SYS_AIRFLOW
             'CAV_AIRFLOW_OCCUPIED_HOURS': iesve.HVACSystemLink.CAV_AIRFLOW_OCCUPIED_HOURS
             'CAV_AIRFLOW_NIGHTTIME_SETBACK': iesve.HVACSystemLink.CAV_AIRFLOW_NIGHTTIME_SETBACK
             'MIN_FAN_AIRFLOW': iesve.HVACSystemLink.MIN_FAN_AIRFLOW
             'ZONE_DCV_STAGE1_VAV_CTRL': iesve.HVACSystemLink.ZONE_DCV_STAGE1_VAV_CTRL
             'ZONE_AIRFLOW_DETECTION': iesve.HVACSystemLink.ZONE_AIRFLOW_DETECTION
             'STRATIFIED_ZN_REMIX_AIRFLOW': iesve.HVACSystemLink.STRATIFIED_ZN_REMIX_AIRFLOW
             'ZONE_RA_TRANSFER_AIRFLOW': iesve.HVACSystemLink.ZONE_RA_TRANSFER_AIRFLOW
             'EXHAUST_CV_HOOD_AIRFLOW': iesve.HVACSystemLink.EXHAUST_CV_HOOD_AIRFLOW
             'AIRFLOW_ON_IF_NV_INSUF_COOL': iesve.HVACSystemLink.AIRFLOW_ON_IF_NV_INSUF_COOL
             'AIRFLOW_ON_IF_NV_INSUF_VENT': iesve.HVACSystemLink.AIRFLOW_ON_IF_NV_INSUF_VENT
             'MIXED_MODE_DISABLE': iesve.HVACSystemLink.MIXED_MODE_DISABLE
             'MIXED_MODE_TOUT_TZN_DELTA': iesve.HVACSystemLink.MIXED_MODE_TOUT_TZN_DELTA
             'EA_PERCENT_VS_RETURN_OR_TRANSFER': iesve.HVACSystemLink.EA_PERCENT_VS_RETURN_OR_TRANSFER
             'EA_PERCENT_AVAILABLE_TO_ER': iesve.HVACSystemLink.EA_PERCENT_AVAILABLE_TO_ER
             'RA_PERCENT_TO_ALT_PATH_OR_ZONE': iesve.HVACSystemLink.RA_PERCENT_TO_ALT_PATH_OR_ZONE
             'OA_ECON_TARGET_AND_DBT_LIMIT_DEPRECATED': iesve.HVACSystemLink.OA_ECON_TARGET_AND_DBT_LIMIT_DEPRECATED
             'OA_ECON_TARGET_RESET': iesve.HVACSystemLink.OA_ECON_TARGET_RESET
             'OA_ECON_ZN_TEMP_LOW_LIMIT': iesve.HVACSystemLink.OA_ECON_ZN_TEMP_LOW_LIMIT
             'OA_VARIABLE_MIN_PERCENTAGE': iesve.HVACSystemLink.OA_VARIABLE_MIN_PERCENTAGE
             'OA_FIXED_PERCENTAGE': iesve.HVACSystemLink.OA_FIXED_PERCENTAGE
             'OA_ECON_DPT_LIMIT': iesve.HVACSystemLink.OA_ECON_DPT_LIMIT
             'OA_ECON_DIFF_ENTHALPY': iesve.HVACSystemLink.OA_ECON_DIFF_ENTHALPY
             'OA_MIN_RESET_ZONE_CO2': iesve.HVACSystemLink.OA_MIN_RESET_ZONE_CO2
             'OA_MIN_RESET_ZN_VAV_FLOW_PERCENT': iesve.HVACSystemLink.OA_MIN_RESET_ZN_VAV_FLOW_PERCENT
             'OA_MIN_RESET_OCCUPIED_ZONE_CO2': iesve.HVACSystemLink.OA_MIN_RESET_OCCUPIED_ZONE_CO2
             'OA_MIN_RESET_UNOCCUPIED_ZN': iesve.HVACSystemLink.OA_MIN_RESET_UNOCCUPIED_ZN
             'OA_MIN_RESET_OCCUPIED_ZONE_VAV_FLOW_PERCENT': iesve.HVACSystemLink.OA_MIN_RESET_OCCUPIED_ZONE_VAV_FLOW_PERCENT
             'OA_MIN_RESET_UNOCCUPIED_ZN_VAV_FLOW_PERCENT': iesve.HVACSystemLink.OA_MIN_RESET_UNOCCUPIED_ZN_VAV_FLOW_PERCENT
             'ER_BYPASS_TEMP_TARGET': iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET
             'ER_TARGET_COOL_MODE': iesve.HVACSystemLink.ER_TARGET_COOL_MODE
             'ER_TARGET_HEAT_MODE': iesve.HVACSystemLink.ER_TARGET_HEAT_MODE
             'ER_TARGET_PSZ_HEAT_COOL': iesve.HVACSystemLink.ER_TARGET_PSZ_HEAT_COOL
             'ER_BYPASS_TEMP_TARGET_PSZ': iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_PSZ
             'HP_RRCOIL_WHL_BYPASS_TEMP': iesve.HVACSystemLink.HP_RRCOIL_WHL_BYPASS_TEMP
             'HP_RR_WHL_BYPASS_TEMP_DIFF': iesve.HVACSystemLink.HP_RR_WHL_BYPASS_TEMP_DIFF
             'RA_BYPASS_MIXED_AIR_TARGET_TEMP': iesve.HVACSystemLink.RA_BYPASS_MIXED_AIR_TARGET_TEMP
             'ZONE_MIXING_VARIABLE_DBT_TARGET': iesve.HVACSystemLink.ZONE_MIXING_VARIABLE_DBT_TARGET
             'ZONE_MIXING_PERCENT_PRIMARY_AIR': iesve.HVACSystemLink.ZONE_MIXING_PERCENT_PRIMARY_AIR
             'ZONE_MIXING_FIXED_DBT_DAMPER_TARGET': iesve.HVACSystemLink.ZONE_MIXING_FIXED_DBT_DAMPER_TARGET
             'INDIRECT_EVAP_COOLING': iesve.HVACSystemLink.INDIRECT_EVAP_COOLING
             'DIRECT_EVAP_COOLING': iesve.HVACSystemLink.DIRECT_EVAP_COOLING
             'ZONE_RH_HIGH_LIMIT_FOR_DEC': iesve.HVACSystemLink.ZONE_RH_HIGH_LIMIT_FOR_DEC
             'EVAP_SPRAY_HUMID_PER_ZN_RH': iesve.HVACSystemLink.EVAP_SPRAY_HUMID_PER_ZN_RH
             'EVAP_SPRAY_HUMID_SA_RH': iesve.HVACSystemLink.EVAP_SPRAY_HUMID_SA_RH
             'STEAM_HUMID_PER_ZN_RH': iesve.HVACSystemLink.STEAM_HUMID_PER_ZN_RH
             'STEAM_HUMID_SA_RH': iesve.HVACSystemLink.STEAM_HUMID_SA_RH
             'PRE_HEAT_COIL_AHU_MIN_EAT': iesve.HVACSystemLink.PRE_HEAT_COIL_AHU_MIN_EAT
             'COOLING_COIL_AHU_COOL_LAT': iesve.HVACSystemLink.COOLING_COIL_AHU_COOL_LAT
             'COOLING_COIL_AHU_DEHUM_LAT': iesve.HVACSystemLink.COOLING_COIL_AHU_DEHUM_LAT
             'COOLING_COIL_AHU_EXTEND_DEHUM_LAT': iesve.HVACSystemLink.COOLING_COIL_AHU_EXTEND_DEHUM_LAT
             'COOLING_COIL_AHU_SUPPLY_AIR_DPT': iesve.HVACSystemLink.COOLING_COIL_AHU_SUPPLY_AIR_DPT
             'COOLING_COIL_COIL_LEAVING_DPT': iesve.HVACSystemLink.COOLING_COIL_COIL_LEAVING_DPT
             'HEATING_COIL_AHU_MIN_SAT': iesve.HVACSystemLink.HEATING_COIL_AHU_MIN_SAT
             'HEATING_COIL_MIN_SAT_WITH_RESET': iesve.HVACSystemLink.HEATING_COIL_MIN_SAT_WITH_RESET
             'COOLING_COIL_DOAS_TEMPERING': iesve.HVACSystemLink.COOLING_COIL_DOAS_TEMPERING
             'HEATING_COIL_DOAS_TEMPERING': iesve.HVACSystemLink.HEATING_COIL_DOAS_TEMPERING
             'COOLING_COIL_FULL_COOLING_LAT_BAND': iesve.HVACSystemLink.COOLING_COIL_FULL_COOLING_LAT_BAND
             'COOLING_COIL_FULL_DEHUM_LAT_BAND': iesve.HVACSystemLink.COOLING_COIL_FULL_DEHUM_LAT_BAND
             'HEATING_COIL_FULL_HEATING_LAT_BAND': iesve.HVACSystemLink.HEATING_COIL_FULL_HEATING_LAT_BAND
             'COOLING_COIL_FULL_H_C_LAT_BAND': iesve.HVACSystemLink.COOLING_COIL_FULL_H_C_LAT_BAND
             'COOLING_COIL_FULL_H_C_DEHUM_LAT': iesve.HVACSystemLink.COOLING_COIL_FULL_H_C_DEHUM_LAT
             'HEATING_COIL_FULL_H_C_LAT_BAND': iesve.HVACSystemLink.HEATING_COIL_FULL_H_C_LAT_BAND
             'COOLING_COIL_ZONE_VARIABLE_LAT': iesve.HVACSystemLink.COOLING_COIL_ZONE_VARIABLE_LAT
             'HEATING_COIL_ZONE_VARIABLE_LAT': iesve.HVACSystemLink.HEATING_COIL_ZONE_VARIABLE_LAT
             'COOLING_COIL_ZONE_FIXED_LAT': iesve.HVACSystemLink.COOLING_COIL_ZONE_FIXED_LAT
             'HEATING_COIL_ZONE_FIXED_LAT': iesve.HVACSystemLink.HEATING_COIL_ZONE_FIXED_LAT
             'HEATING_COIL_ZN_FIX_LAT_STAGE_1': iesve.HVACSystemLink.HEATING_COIL_ZN_FIX_LAT_STAGE_1
             'HEATING_COIL_ZN_FIX_LAT_STAGE_2': iesve.HVACSystemLink.HEATING_COIL_ZN_FIX_LAT_STAGE_2
             'RAD_CONV_HEAT_DEVICE_PANEL': iesve.HVACSystemLink.RAD_CONV_HEAT_DEVICE_PANEL
             'RAD_CONV_COOL_DEVICE_PANEL': iesve.HVACSystemLink.RAD_CONV_COOL_DEVICE_PANEL
             'DIRECT_ACTING_HEATER_COOLER': iesve.HVACSystemLink.DIRECT_ACTING_HEATER_COOLER
             'EXHAUST_DRIVEN_VENTILATION_AIRFLOW': iesve.HVACSystemLink.EXHAUST_DRIVEN_VENTILATION_AIRFLOW
             'ER_BYPASS_TEMP_TARGET_LEGACY_CONFIG': iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_LEGACY_CONFIG
             'ER_BYPASS_TEMP_TARGET_PSZ_LEGACY': iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_PSZ_LEGACY
             'OA_ECON_TARGET_PER_RA_TEMP': iesve.HVACSystemLink.OA_ECON_TARGET_PER_RA_TEMP
             'DOAS_PTAC_PTHP_COOLING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.DOAS_PTAC_PTHP_COOLING_AIRFLOW_CAV_2SP_VAV
             'DOAS_PTAC_PTHP_HEATING_AIRFLOW_CAV_2SP_VAV': iesve.HVACSystemLink.DOAS_PTAC_PTHP_HEATING_AIRFLOW_CAV_2SP_VAV
             'COOLING_COIL_DOAS_FIXED_TEMP': iesve.HVACSystemLink.COOLING_COIL_DOAS_FIXED_TEMP
             'COOLING_COIL_DOAS_DEHUM': iesve.HVACSystemLink.COOLING_COIL_DOAS_DEHUM
             'PARKING_GARAGE_EXHAUST': iesve.HVACSystemLink.PARKING_GARAGE_EXHAUST
             'COOLING_COIL_AHU_LOWTEMP_LAT': iesve.HVACSystemLink.COOLING_COIL_AHU_LOWTEMP_LAT
             'COOLING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET': iesve.HVACSystemLink.COOLING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
             'HEATING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET': iesve.HVACSystemLink.HEATING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
             'PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV_NO_OFFSET': iesve.HVACSystemLink.PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
             'PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV_NO_OFFSET': iesve.HVACSystemLink.PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
             'COOLING_THERMOSTAT': iesve.HVACSystemLink.COOLING_THERMOSTAT
             'HEATING_THERMOSTAT': iesve.HVACSystemLink.HEATING_THERMOSTAT
             'MODULATION_BY_LOAD': iesve.HVACSystemLink.MODULATION_BY_LOAD
             'DUAL_FAN_DUAL_DUCT_ZONE_COOL_AIRFLOW_AND_OA_VENT': iesve.HVACSystemLink.DUAL_FAN_DUAL_DUCT_ZONE_COOL_AIRFLOW_AND_OA_VENT
             'ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOLING_ONLY': iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOLING_ONLY
             'OA_ECON_DBT_HIGH_LIMIT': iesve.HVACSystemLink.OA_ECON_DBT_HIGH_LIMIT
             'OA_ECON_TARGET_FULL_COOLING_LAT_BAND': iesve.HVACSystemLink.OA_ECON_TARGET_FULL_COOLING_LAT_BAND
             'ON_IF_TEMP_BELOW_MIN_SAT': iesve.HVACSystemLink.ON_IF_TEMP_BELOW_MIN_SAT
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.HVACSystemLink.DELIMITER
             0: iesve.HVACSystemLink.NONE
             100: iesve.HVACSystemLink.OUTSIDE_AIR_MIN_ECON_DAMPER
             101: iesve.HVACSystemLink.OUTSIDE_AIR_NO_MIN_ECON_DAMPER
             102: iesve.HVACSystemLink.OUTSIDE_AIR_VARIABLE_MIN_DAMPER
             103: iesve.HVACSystemLink.OUTSIDE_AIR_FIXED_MIN_DAMPER
             104: iesve.HVACSystemLink.ENERGY_RECOVERY_BYPASS_DAMPER
             105: iesve.HVACSystemLink.HEAT_PIPE_RR_WHL_BYPASS_DAMPER
             106: iesve.HVACSystemLink.ZONE_MIXING_BOX_DAMPER
             107: iesve.HVACSystemLink.RETURN_AIR_DAMPER
             108: iesve.HVACSystemLink.ENERGY_RECOVERY_BYPASS_LEGACY_DAMPER
             109: iesve.HVACSystemLink.SERIES_FPB_DAMPER
             110: iesve.HVACSystemLink.DCV_MIN_OUTSIDE_AIR_ECON
             200: iesve.HVACSystemLink.SUPPLY_FAN
             201: iesve.HVACSystemLink.SUPPLY_FAN_TSP_ADDITION
             202: iesve.HVACSystemLink.RETURN_RELIEF_FAN
             203: iesve.HVACSystemLink.EXHAUST_FAN
             204: iesve.HVACSystemLink.FCU_FAN
             205: iesve.HVACSystemLink.FPB_FAN
             206: iesve.HVACSystemLink.PACKAGE_TERMINAL_UNIT_FAN
             207: iesve.HVACSystemLink.UNIT_HEATER_FAN
             300: iesve.HVACSystemLink.FILTER_PRESSURE_AND_CHANGE
             400: iesve.HVACSystemLink.SA_DUCT_HEAT_LOSS_GAIN
             401: iesve.HVACSystemLink.RA_DUCT_HEAT_LOSS_GAIN
             500: iesve.HVACSystemLink.OCCUPIED_ZONE
             501: iesve.HVACSystemLink.THERMALLY_STRATIFIED_ZONE
             502: iesve.HVACSystemLink.SA_UFAD_PLENUM
             503: iesve.HVACSystemLink.RA_PLENUM
             504: iesve.HVACSystemLink.ADJACENT_SPACE_WITH_EA_FAN
             505: iesve.HVACSystemLink.HEATED_COOLED_SLAB_ZONE
             506: iesve.HVACSystemLink.VOID_SPACE
             600: iesve.HVACSystemLink.AHU_PRE_HEAT_COIL
             601: iesve.HVACSystemLink.AHU_HEATING_COIL
             602: iesve.HVACSystemLink.ZONE_REHEAT_HEATING_COIL
             603: iesve.HVACSystemLink.FCU_ACT_BEAM_HEAT_COIL
             604: iesve.HVACSystemLink.PTAC_PTHP_HEATING_COIL
             605: iesve.HVACSystemLink.ELEC_HEAT_COIL_2ND_STAGE
             606: iesve.HVACSystemLink.DEDICATED_OA_VENT_HEATING_COIL
             700: iesve.HVACSystemLink.AHU_COOLING_COIL
             701: iesve.HVACSystemLink.FCU_ACT_BEAM_COOL_COIL
             702: iesve.HVACSystemLink.PTAC_PTHP_COOLING_COIL
             703: iesve.HVACSystemLink.UCS_COOLING_COIL
             704: iesve.HVACSystemLink.DEDICATED_OA_VENT_COOLING_COIL
             800: iesve.HVACSystemLink.DOAS_AHU_COOLING_DEVICE
             801: iesve.HVACSystemLink.ZONE_COOLING_DEVICE
             900: iesve.HVACSystemLink.ENERGY_RECOVERY_HX_WHEEL
             901: iesve.HVACSystemLink.HEAT_PIPE_RUN_RND_WHEEL
             1000: iesve.HVACSystemLink.STEAM_HUMIDIFIER
             1001: iesve.HVACSystemLink.DIRECT_EVAP_SPRAY
             1002: iesve.HVACSystemLink.INDIRECT_EVAP_SPRAY
             2000: iesve.HVACSystemLink.COOLING_AIRFLOW_VAV_CAV
             2001: iesve.HVACSystemLink.HEATING_AIRFLOW_VAV_CAV
             2002: iesve.HVACSystemLink.DOAS_VENT_AIRFLOW
             2003: iesve.HVACSystemLink.DOAS_VENT_AIRFLOW_CAV_DCV
             2004: iesve.HVACSystemLink.FCU_COOLING_AIRFLOW_CAV_2SP_VAV
             2005: iesve.HVACSystemLink.FCU_HEATING_AIRFLOW_CAV_2SP_VAV
             2006: iesve.HVACSystemLink.FPB_PRIMARY_AIRFLOW_CAV_VAV
             2007: iesve.HVACSystemLink.FPB_SECONDARY_AIRFLOW_CAV_2SP_VAV
             2008: iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOL
             2009: iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_HEAT
             2010: iesve.HVACSystemLink.ACT_BEAM_IU_INDUCED_AIRFLOW
             2011: iesve.HVACSystemLink.DUAL_FAN_DUAL_DUCT_ZN_HEAT_AIRFLOW
             2012: iesve.HVACSystemLink.PSZ_COOLING_AIRFLOW_CAV_2SP_VAV
             2013: iesve.HVACSystemLink.PSZ_HEATING_AIRFLOW_CAV_2SP_VAV
             2014: iesve.HVACSystemLink.PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV
             2015: iesve.HVACSystemLink.PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV
             2016: iesve.HVACSystemLink.UCS_COOLING_AIRFLOW
             2017: iesve.HVACSystemLink.COOLING_ONLY_SYS_AIRFLOW
             2018: iesve.HVACSystemLink.HEATING_ONLY_SYS_AIRFLOW
             2019: iesve.HVACSystemLink.CAV_AIRFLOW_OCCUPIED_HOURS
             2020: iesve.HVACSystemLink.CAV_AIRFLOW_NIGHTTIME_SETBACK
             2021: iesve.HVACSystemLink.MIN_FAN_AIRFLOW
             2022: iesve.HVACSystemLink.ZONE_DCV_STAGE1_VAV_CTRL
             2023: iesve.HVACSystemLink.ZONE_AIRFLOW_DETECTION
             2024: iesve.HVACSystemLink.STRATIFIED_ZN_REMIX_AIRFLOW
             2025: iesve.HVACSystemLink.ZONE_RA_TRANSFER_AIRFLOW
             2026: iesve.HVACSystemLink.EXHAUST_CV_HOOD_AIRFLOW
             2027: iesve.HVACSystemLink.AIRFLOW_ON_IF_NV_INSUF_COOL
             2028: iesve.HVACSystemLink.AIRFLOW_ON_IF_NV_INSUF_VENT
             2029: iesve.HVACSystemLink.MIXED_MODE_DISABLE
             2030: iesve.HVACSystemLink.MIXED_MODE_TOUT_TZN_DELTA
             2031: iesve.HVACSystemLink.EA_PERCENT_VS_RETURN_OR_TRANSFER
             2032: iesve.HVACSystemLink.EA_PERCENT_AVAILABLE_TO_ER
             2033: iesve.HVACSystemLink.RA_PERCENT_TO_ALT_PATH_OR_ZONE
             2034: iesve.HVACSystemLink.OA_ECON_TARGET_AND_DBT_LIMIT_DEPRECATED
             2035: iesve.HVACSystemLink.OA_ECON_TARGET_RESET
             2036: iesve.HVACSystemLink.OA_ECON_ZN_TEMP_LOW_LIMIT
             2037: iesve.HVACSystemLink.OA_VARIABLE_MIN_PERCENTAGE
             2038: iesve.HVACSystemLink.OA_FIXED_PERCENTAGE
             2039: iesve.HVACSystemLink.OA_ECON_DPT_LIMIT
             2040: iesve.HVACSystemLink.OA_ECON_DIFF_ENTHALPY
             2041: iesve.HVACSystemLink.OA_MIN_RESET_ZONE_CO2
             2042: iesve.HVACSystemLink.OA_MIN_RESET_ZN_VAV_FLOW_PERCENT
             2043: iesve.HVACSystemLink.OA_MIN_RESET_OCCUPIED_ZONE_CO2
             2044: iesve.HVACSystemLink.OA_MIN_RESET_UNOCCUPIED_ZN
             2045: iesve.HVACSystemLink.OA_MIN_RESET_OCCUPIED_ZONE_VAV_FLOW_PERCENT
             2046: iesve.HVACSystemLink.OA_MIN_RESET_UNOCCUPIED_ZN_VAV_FLOW_PERCENT
             2047: iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET
             2048: iesve.HVACSystemLink.ER_TARGET_COOL_MODE
             2049: iesve.HVACSystemLink.ER_TARGET_HEAT_MODE
             2050: iesve.HVACSystemLink.ER_TARGET_PSZ_HEAT_COOL
             2051: iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_PSZ
             2052: iesve.HVACSystemLink.HP_RRCOIL_WHL_BYPASS_TEMP
             2053: iesve.HVACSystemLink.HP_RR_WHL_BYPASS_TEMP_DIFF
             2054: iesve.HVACSystemLink.RA_BYPASS_MIXED_AIR_TARGET_TEMP
             2055: iesve.HVACSystemLink.ZONE_MIXING_VARIABLE_DBT_TARGET
             2056: iesve.HVACSystemLink.ZONE_MIXING_PERCENT_PRIMARY_AIR
             2057: iesve.HVACSystemLink.ZONE_MIXING_FIXED_DBT_DAMPER_TARGET
             2058: iesve.HVACSystemLink.INDIRECT_EVAP_COOLING
             2059: iesve.HVACSystemLink.DIRECT_EVAP_COOLING
             2060: iesve.HVACSystemLink.ZONE_RH_HIGH_LIMIT_FOR_DEC
             2061: iesve.HVACSystemLink.EVAP_SPRAY_HUMID_PER_ZN_RH
             2062: iesve.HVACSystemLink.EVAP_SPRAY_HUMID_SA_RH
             2063: iesve.HVACSystemLink.STEAM_HUMID_PER_ZN_RH
             2064: iesve.HVACSystemLink.STEAM_HUMID_SA_RH
             2065: iesve.HVACSystemLink.PRE_HEAT_COIL_AHU_MIN_EAT
             2066: iesve.HVACSystemLink.COOLING_COIL_AHU_COOL_LAT
             2067: iesve.HVACSystemLink.COOLING_COIL_AHU_DEHUM_LAT
             2068: iesve.HVACSystemLink.COOLING_COIL_AHU_EXTEND_DEHUM_LAT
             2069: iesve.HVACSystemLink.COOLING_COIL_AHU_SUPPLY_AIR_DPT
             2070: iesve.HVACSystemLink.COOLING_COIL_COIL_LEAVING_DPT
             2071: iesve.HVACSystemLink.HEATING_COIL_AHU_MIN_SAT
             2072: iesve.HVACSystemLink.HEATING_COIL_MIN_SAT_WITH_RESET
             2073: iesve.HVACSystemLink.COOLING_COIL_DOAS_TEMPERING
             2074: iesve.HVACSystemLink.HEATING_COIL_DOAS_TEMPERING
             2075: iesve.HVACSystemLink.COOLING_COIL_FULL_COOLING_LAT_BAND
             2076: iesve.HVACSystemLink.COOLING_COIL_FULL_DEHUM_LAT_BAND
             2077: iesve.HVACSystemLink.HEATING_COIL_FULL_HEATING_LAT_BAND
             2078: iesve.HVACSystemLink.COOLING_COIL_FULL_H_C_LAT_BAND
             2079: iesve.HVACSystemLink.COOLING_COIL_FULL_H_C_DEHUM_LAT
             2080: iesve.HVACSystemLink.HEATING_COIL_FULL_H_C_LAT_BAND
             2081: iesve.HVACSystemLink.COOLING_COIL_ZONE_VARIABLE_LAT
             2082: iesve.HVACSystemLink.HEATING_COIL_ZONE_VARIABLE_LAT
             2083: iesve.HVACSystemLink.COOLING_COIL_ZONE_FIXED_LAT
             2084: iesve.HVACSystemLink.HEATING_COIL_ZONE_FIXED_LAT
             2085: iesve.HVACSystemLink.HEATING_COIL_ZN_FIX_LAT_STAGE_1
             2086: iesve.HVACSystemLink.HEATING_COIL_ZN_FIX_LAT_STAGE_2
             2087: iesve.HVACSystemLink.RAD_CONV_HEAT_DEVICE_PANEL
             2088: iesve.HVACSystemLink.RAD_CONV_COOL_DEVICE_PANEL
             2089: iesve.HVACSystemLink.DIRECT_ACTING_HEATER_COOLER
             2090: iesve.HVACSystemLink.EXHAUST_DRIVEN_VENTILATION_AIRFLOW
             2091: iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_LEGACY_CONFIG
             2092: iesve.HVACSystemLink.ER_BYPASS_TEMP_TARGET_PSZ_LEGACY
             2093: iesve.HVACSystemLink.OA_ECON_TARGET_PER_RA_TEMP
             2094: iesve.HVACSystemLink.DOAS_PTAC_PTHP_COOLING_AIRFLOW_CAV_2SP_VAV
             2095: iesve.HVACSystemLink.DOAS_PTAC_PTHP_HEATING_AIRFLOW_CAV_2SP_VAV
             2096: iesve.HVACSystemLink.COOLING_COIL_DOAS_FIXED_TEMP
             2097: iesve.HVACSystemLink.COOLING_COIL_DOAS_DEHUM
             2098: iesve.HVACSystemLink.PARKING_GARAGE_EXHAUST
             2099: iesve.HVACSystemLink.COOLING_COIL_AHU_LOWTEMP_LAT
             2100: iesve.HVACSystemLink.COOLING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
             2101: iesve.HVACSystemLink.HEATING_COIL_ZONE_VARIABLE_LAT_NO_OFFSET
             2102: iesve.HVACSystemLink.PTAC_PTHP_COOL_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
             2103: iesve.HVACSystemLink.PTAC_PTHP_HEAT_AIRFLOW_CAV_2SP_VAV_NO_OFFSET
             2104: iesve.HVACSystemLink.COOLING_THERMOSTAT
             2105: iesve.HVACSystemLink.HEATING_THERMOSTAT
             2106: iesve.HVACSystemLink.MODULATION_BY_LOAD
             2107: iesve.HVACSystemLink.DUAL_FAN_DUAL_DUCT_ZONE_COOL_AIRFLOW_AND_OA_VENT
             2108: iesve.HVACSystemLink.ACT_BM_IU_PRIMARY_AIR_CAV_VAV_COOLING_ONLY
             2109: iesve.HVACSystemLink.OA_ECON_DBT_HIGH_LIMIT
             2110: iesve.HVACSystemLink.OA_ECON_TARGET_FULL_COOLING_LAT_BAND
             2111: iesve.HVACSystemLink.ON_IF_TEMP_BELOW_MIN_SAT
            }
      
   .. py:class:: HVACThermalDuctProperties
   
      *HVAC thermal duct properties*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: body_index
      
         *(int) Body index*
      
      .. py:property:: duct_location
      
         *(int) Duct location (HVACLocation)*
      
      .. py:property:: duct_surface_area
      
         *(float) Duct surface area*
      
      .. py:property:: duct_u_value
      
         *(float) Duct U-value*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: space_id
      
         *(string) Space ID*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACThermalStorageLoop
   
      *Interface for HVAC thermal storage loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: chillers
      
         *(list) Chillers (HVACChiller)*
      
      .. py:property:: condenser_water_loop
      
         *(HVACCondenserWaterLoop) Condenser water loop*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump
      
         *(HVACPump) Pump*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: tank
      
         *(HVACThermalStorageTank) Tank*
      
   .. py:class:: HVACThermalStorageTank
   
      *Interface for HVAC thermal storage tank*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACTimeSwitchController
   
      *Interface for HVAC time switch controller*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: control_line_orientation
      
         *(int) Control line orientation*
      
      .. py:property:: control_node
      
         *(int) Control node*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: independent_mode
      
         *(int) Independent mode*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: max_control_signal_value
      
         *(float) Maximum control signal value*
      
      .. py:property:: max_signal_variation_mode
      
         *(int) Maximum signal variation mode*
      
      .. py:property:: max_signal_variation_profile_id
      
         *(string) Maximum signal variation profile ID*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: number_of_and_connections
      
         *(int) Number of AND connections*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_line_orientation
      
         *(int) Reference line orientation*
      
      .. py:property:: reference_node
      
         *(int) Reference node*
      
      .. py:property:: sensor_line_orientation
      
         *(int) Sensor line orientation*
      
      .. py:property:: sensor_node
      
         *(int) Sensor node*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: time_switch_profile_id
      
         *(string) Time switch profile ID*
      
   .. py:class:: HVACUnitaryCoolingSystem
   
      *Interface for HVAC Unitary cooling system*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_air_flow_rate
      
         *(float) Design air flow rate*
      
      .. py:property:: design_airflow_autosized
      
         *(int) Design airflow autosized*
      
      .. py:property:: extrapolate_performance_data
      
         *(int) Extrapolate performance data*
      
      .. py:property:: heat_rejection_fan_power
      
         *(float) Heat rejection fan power*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: low_load_copr_degradation_factor
      
         *(float) Low-load COPR degradation factor*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: scale_performance_parameters_with_design_air_flow_rate
      
         *(int) Scale performance parameters with design air flow rate*
      
      .. py:property:: supply_fan_power
      
         *(float) Supply fan power*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACVRFSourceType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_source
         :classmethod:
         :type: iesve.HVACVRFSourceType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_source".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_source': iesve.HVACVRFSourceType.air_source
             'water_source': iesve.HVACVRFSourceType.water_source
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACVRFSourceType.air_source
             1: iesve.HVACVRFSourceType.water_source
            }
      
      .. py:property:: water_source
         :classmethod:
         :type: iesve.HVACVRFSourceType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "water_source".
      
   .. py:class:: HVACVRFSystem
   
      *Interface for HVAC VRF System*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: design_condition_outdoor_unit_data
      
         *(dict) Dictionary of design condition outdoor unit data. Possible dictionary entries are:*
         
         *cooling_capacity, cooling_cop, cooling_combination_ratio, cooling_average_indoor_wb_temperature, cooling_outdoor_db_temperature,*
         *heating_capacity, heating_cop, heating_combination_ratio, heating_average_indoor_db_temperature,*
         *heating_average_indoor_wb_temperature, heating_outdoor_wb_temperature, heating_outdoor_db_temperature,*
         *cooling_entering_source_loop_temperature, heating_entering_source_loop_temperature*
      
      .. py:property:: design_parameters
      
         *(dict) Dictionary of design parameters. Possible dictionary entries are:*
         
         *performance_curve_set_description, is_autosize_outdoor_unit, oversizing_factor, performance_curve_set_name*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: reference_condition_indoor_unit_data
      
         *(dict) Dictionary of reference indoor unit data. Possible dictionary entries are:*
         
         *cooling_entering_coil_wb_temperature, cooling_outdoor_air_db_temperature, use_same_cooling_temperature_as_outdoor,*
         *heating_entering_coil_db_temperature, heating_outdoor_air_wb_temperature, use_same_heating_temperature_as_outdoor,*
         *cooling_entering_water_temperature, heating_entering_water_temperature*
      
      .. py:property:: reference_condition_outdoor_unit_data
      
         *(dict) Dictionary of reference condition outdoor unit data. Possible dictionary entries are:*
         
         *cooling_capacity, cooling_cop, cooling_combination_ratio, cooling_average_indoor_wb_temperature, cooling_outdoor_db_temperature,*
         *use_same_cooling_temperature_as_indoor, heating_capacity, heating_cop, heating_combination_ratio,*
         *heating_average_indoor_db_temperature, heating_average_indoor_wb_temperature, heating_outdoor_wb_temperature,*
         *heating_outdoor_db_temperature, use_same_heating_temperature_as_indoor, cooling_entering_source_loop_temperature,*
         *heating_entering_source_loop_temperature*
      
      .. py:property:: system_data
      
         *(dict) Dictionary of VRF System data. Possible dictionary entries are:*
         
         *unit_control_profile, source_type, min_part_load_ratio, unit_control, source_water_loop_id,*
         *master_thermostat_location_space_id, heat_recovery_mode, is_seperate_piping_values,*
         *equivalent_piping_length_cooling, equivalent_piping_length_heating, piping_level_difference_cooling,*
         *piping_level_difference_heating, use_crankcase_heater, crankcase_heater_power,*
         *max_outdoor_temp_for_crankcase_heater_operation, use_electric_resistance_backup_heat,*
         *backup_cooling_source_cop, backup_heating_source_efficiency, outdoor_temp_operation_range_cooling_minimum,*
         *outdoor_temp_operation_range_cooling_maximum, outdoor_temp_operation_range_heating_minimum,*
         *outdoor_temp_operation_range_heating_maximum, fan_eir, defrost_strategy, resistive_defrost_heater_capacity,*
         *defrost_control, defrost_time_fraction, max_outdoor_temp_for_defrost_operation, cooling_heating_meter,*
         *crankcase_heater_meter, electric_resistance_backup_heat_meter, backup_cooling_source_meter,*
         *backup_heating_source_meter, fan_meter, defrost_meter*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterAirHeatPump
   
      *Interface for HVAC water air heat pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: cop_cooling
      
         *(float) Coefficient of performance for cooling*
      
      .. py:property:: cop_heating
      
         *(float) Coefficient of performance for heating*
      
      .. py:property:: entering_coil_dry_bulb_temperature_heating
      
         *(float) Entering coil dry bulb temperature heating*
      
      .. py:property:: entering_coil_wet_bulb_temperature_cooling
      
         *(float) Entering coil wet bulb temperature cooling*
      
      .. py:property:: entering_water_temperature_cooling
      
         *(float) Entering water temperature cooling*
      
      .. py:property:: entering_water_temperature_heating
      
         *(float) Entering water temperature heating*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterAirHeatPumpInstance
   
      *Interface for HVAC water air heat pump instance*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: cop_cooling
      
         *(float) Coefficient of performance for cooling*
      
      .. py:property:: cop_heating
      
         *(float) Coefficient of performance for heating*
      
      .. py:property:: entering_coil_dry_bulb_temperature_heating
      
         *(float) Entering coil dry bulb temperature heating*
      
      .. py:property:: entering_coil_wet_bulb_temperature_cooling
      
         *(float) Entering coil wet bulb temperature cooling*
      
      .. py:property:: entering_water_temperature_cooling
      
         *(float) Entering water temperature cooling*
      
      .. py:property:: entering_water_temperature_heating
      
         *(float) Entering water temperature heating*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterLoopHeatRecovery
   
      *(HVACHeatRecoveryModel) Model*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: model
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterSourceLoop
   
      *Interface for HVAC water source loop*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: pump_delta_t
      
         *(float) Pump delta T*
      
      .. py:property:: pump_efficiency
      
         *(float) Pump efficiency*
      
      .. py:property:: pump_heat_gain
      
         *(float) Pump heat gain*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: specific_pump_power
      
         *(float) Specific pump power*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterWaterHeatExchanger
   
      *Interface for HVAC water-water heat exchanger*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:method:: get_approach
      
         *get_approach( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_approach(type) -> float*
             **
             *Get the design approach*
      
      .. py:method:: get_effectiveness
      
         *get_effectiveness( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_effectiveness(type) -> float*
             **
             *Get the heat exchanger effectiveness*
      
      .. py:method:: get_load_side_entering_temperature
      
         *get_load_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_entering_temperature(type) -> float*
             **
             *Get the design load side entering temperature*
      
      .. py:method:: get_load_side_leaving_temperature
      
         *get_load_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_load_side_leaving_temperature(type) -> float*
             **
             *Get the design load leaving temperature*
      
      .. py:method:: get_source_flow_rate
      
         *get_source_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_flow_rate(type) -> float*
             **
             *Get the design source flow rate*
      
      .. py:method:: get_source_side_entering_temperature
      
         *get_source_side_entering_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_entering_temperature(type) -> float*
             **
             *Get the design source side entering temperature*
      
      .. py:method:: get_source_side_leaving_temperature
      
         *get_source_side_leaving_temperature( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_source_side_leaving_temperature(type) -> float*
             **
             *Get the design source side leaving temperature*
      
      .. py:method:: get_supply_flow_rate
      
         *get_supply_flow_rate( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *get_supply_flow_rate(type) -> float*
             **
             *Get the design supply flow rate*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:method:: is_design_heat_rejection_autosized
      
         *is_design_heat_rejection_autosized( (HVACAbstractWaterWaterHeatExchanger)arg1, (object)arg2) -> object :*
             *is_design_heat_rejection_autosized(type) -> bool*
             **
             *Check whether the design heat rejection is autosized for the given HVACWaterWaterHeatExchangerDataType.*
             *Returns True if so, False otherwise.*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACWaterWaterHeatExchangerDataType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: cooling
         :classmethod:
         :type: iesve.HVACWaterWaterHeatExchangerDataType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "cooling".
      
      .. py:property:: heating
         :classmethod:
         :type: iesve.HVACWaterWaterHeatExchangerDataType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "heating".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'cooling': iesve.HVACWaterWaterHeatExchangerDataType.cooling
             'heating': iesve.HVACWaterWaterHeatExchangerDataType.heating
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HVACWaterWaterHeatExchangerDataType.cooling
             1: iesve.HVACWaterWaterHeatExchangerDataType.heating
            }
      
   .. py:class:: HVACWaterWaterHeatPump
   
      *Interface for HVAC water-water heat pump*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
   .. py:class:: HVACZone
   
      *Interface for HVAC zone*
   
      .. py:property:: available_system_links
      
         *(list) Available system links (HVACSystemLink)*
      
      .. py:property:: id
      
         *(string) ID of the network*
      
      .. py:property:: inlet_nodes
      
         *(list) Inlet node numbers (int)*
      
      .. py:property:: is_duct
      
         *(bool) Whether the component is a duct. True if so, False otherwise.*
      
      .. py:property:: is_selected
      
         *(bool) Whether the network is selected. True if so, false otherwise.*
      
      .. py:property:: multiplex_id
      
         *(string) Multiplex ID*
      
      .. py:property:: multiplex_layer_number
      
         *(int) Multiplex layer number*
      
      .. py:property:: network
      
         *(HVACNetwork) Network*
      
      .. py:property:: network_object_type
      
         *(HVACNetworkObjectType) Network object type*
      
      .. py:property:: outlet_nodes
      
         *(list) Outlet node numbers (int)*
      
      .. py:property:: reference
      
         *(string) Reference of the network*
      
      .. py:property:: room_ids
      
         *(list) List of room IDs*
      
      .. py:property:: system_id
      
         *(string) System ID*
      
      .. py:property:: system_link
      
         *(HVACSystemLink) System link*
      
      .. py:property:: zone_id
      
         *(string) Zone ID*
      
   .. py:class:: HeatingCoilModelType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: advanced_heating_coil
         :classmethod:
         :type: iesve.HeatingCoilModelType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "advanced_heating_coil".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'simple_heating_coil': iesve.HeatingCoilModelType.simple_heating_coil
             'advanced_heating_coil': iesve.HeatingCoilModelType.advanced_heating_coil
            }
      
      .. py:property:: simple_heating_coil
         :classmethod:
         :type: iesve.HeatingCoilModelType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "simple_heating_coil".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HeatingCoilModelType.simple_heating_coil
             1: iesve.HeatingCoilModelType.advanced_heating_coil
            }
      
   .. py:class:: HeatingSourceSystemType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: heating_system_aa_heat_pump
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "heating_system_aa_heat_pump".
      
      .. py:property:: heating_system_electric
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 5
         * a name of "heating_system_electric".
      
      .. py:property:: heating_system_generic
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "heating_system_generic".
      
      .. py:property:: heating_system_heat_transfer_loop
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "heating_system_heat_transfer_loop".
      
      .. py:property:: heating_system_hot_water_loop
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "heating_system_hot_water_loop".
      
      .. py:property:: heating_system_vrf
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 6
         * a name of "heating_system_vrf".
      
      .. py:property:: heating_system_wa_heat_pump
         :classmethod:
         :type: iesve.HeatingSourceSystemType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "heating_system_wa_heat_pump".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'heating_system_generic': iesve.HeatingSourceSystemType.heating_system_generic
             'heating_system_hot_water_loop': iesve.HeatingSourceSystemType.heating_system_hot_water_loop
             'heating_system_aa_heat_pump': iesve.HeatingSourceSystemType.heating_system_aa_heat_pump
             'heating_system_wa_heat_pump': iesve.HeatingSourceSystemType.heating_system_wa_heat_pump
             'heating_system_heat_transfer_loop': iesve.HeatingSourceSystemType.heating_system_heat_transfer_loop
             'heating_system_electric': iesve.HeatingSourceSystemType.heating_system_electric
             'heating_system_vrf': iesve.HeatingSourceSystemType.heating_system_vrf
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HeatingSourceSystemType.heating_system_generic
             1: iesve.HeatingSourceSystemType.heating_system_hot_water_loop
             2: iesve.HeatingSourceSystemType.heating_system_aa_heat_pump
             3: iesve.HeatingSourceSystemType.heating_system_wa_heat_pump
             4: iesve.HeatingSourceSystemType.heating_system_heat_transfer_loop
             5: iesve.HeatingSourceSystemType.heating_system_electric
             6: iesve.HeatingSourceSystemType.heating_system_vrf
            }
      
   .. py:class:: HumidificationControlOption
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'per_system_level_relative_humidity_control_only': iesve.HumidificationControlOption.per_system_level_relative_humidity_control_only
             'system_supply_air_humidified_per_zone_relative_humidity_sensors': iesve.HumidificationControlOption.system_supply_air_humidified_per_zone_relative_humidity_sensors
            }
      
      .. py:property:: per_system_level_relative_humidity_control_only
         :classmethod:
         :type: iesve.HumidificationControlOption
      
         An instance of this class with:
         
         * a value of 0
         * a name of "per_system_level_relative_humidity_control_only".
      
      .. py:property:: system_supply_air_humidified_per_zone_relative_humidity_sensors
         :classmethod:
         :type: iesve.HumidificationControlOption
      
         An instance of this class with:
         
         * a value of 1
         * a name of "system_supply_air_humidified_per_zone_relative_humidity_sensors".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.HumidificationControlOption.per_system_level_relative_humidity_control_only
             1: iesve.HumidificationControlOption.system_supply_air_humidified_per_zone_relative_humidity_sensors
            }
      
   .. py:class:: IECC
   
      *Interface for IECC*
   
      .. py:method:: get_designer_contractor
      
         *get_designer_contractor() -> Dictionary*
         
         *Get a dictionary of designer and contractor data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_owner_agent
      
         *get_owner_agent() -> Dictionary*
         
         *Get a dictionary of owner and agent data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_site_permit_software
      
         *get_site_permit_software() -> Dictionary*
         
         *Get a dictionary of site, permit and software data from project details*
         *The dictionary contains the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
      .. py:method:: set_designer_contractor
      
         *set_designer_contractor(data)*
         
         *Set designer and contractor entries for project details from a dictionary*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
         
         *set_designer_contractor(data)*
         
         *Set designer and contractor entries for project details from a dictionary*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_owner_agent
      
         *set_owner_agent(data)*
         
         *Set owner and agent entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
         
         *set_owner_agent(data)*
         
         *Set owner and agent entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_site_permit_software
      
         *set_site_permit_software(data)*
         
         *Set site, permit and software entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
         
         *set_site_permit_software(data)*
         
         *Set site, permit and software entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
   .. py:class:: ImportGBXML
   
      *Interface for GBXML import*
   
      .. py:method:: import_file
      
         *cap_height*
      
   .. py:class:: Insulation_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: factory_insulated
         :classmethod:
         :type: iesve.Insulation_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "factory_insulated".
      
      .. py:property:: loose_jacket
         :classmethod:
         :type: iesve.Insulation_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "loose_jacket".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'uninsulated': iesve.Insulation_type.uninsulated
             'loose_jacket': iesve.Insulation_type.loose_jacket
             'factory_insulated': iesve.Insulation_type.factory_insulated
            }
      
      .. py:property:: uninsulated
         :classmethod:
         :type: iesve.Insulation_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "uninsulated".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.Insulation_type.uninsulated
             2: iesve.Insulation_type.loose_jacket
             3: iesve.Insulation_type.factory_insulated
            }
      
   .. py:class:: LARISpaceData
   
   
      .. py:method:: get_average_ceiling_height_room
      
         *get_average_ceiling_height_room( (LARISpaceData)arg1, (str)arg2) -> object*
      
      .. py:method:: get_average_ceiling_height_zone
      
         *get_average_ceiling_height_zone( (LARISpaceData)arg1, (str)arg2) -> object*
      
      .. py:method:: get_u_values_room
      
         *get_u_values_room( (LARISpaceData)arg1, (str)arg2) -> dict*
      
      .. py:method:: get_u_values_zone
      
         *get_u_values_zone( (LARISpaceData)arg1, (str)arg2) -> dict*
      
      .. py:method:: get_zones
      
         *get_zones( (LARISpaceData)arg1) -> list*
      
   .. py:class:: LightingGain
   
      *Casual Gain data.*
   
      .. py:method:: get
      
         *get() -> Dictionary*
         
         *Returns a Dictionary containing the data for the internal gain.*
      
      .. py:property:: name
      
         *(str) Descriptive string*
      
   .. py:class:: LightingGain_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: display
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "display".
      
      .. py:property:: fluorescent
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "fluorescent".
      
      .. py:property:: general
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "general".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'fluorescent': iesve.LightingGain_type.fluorescent
             'tungsten': iesve.LightingGain_type.tungsten
             'general': iesve.LightingGain_type.general
             'task': iesve.LightingGain_type.task
             'display': iesve.LightingGain_type.display
             'process': iesve.LightingGain_type.process
            }
      
      .. py:property:: process
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "process".
      
      .. py:property:: task
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "task".
      
      .. py:property:: tungsten
         :classmethod:
         :type: iesve.LightingGain_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "tungsten".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.LightingGain_type.fluorescent
             2: iesve.LightingGain_type.tungsten
             3: iesve.LightingGain_type.general
             4: iesve.LightingGain_type.task
             5: iesve.LightingGain_type.display
             6: iesve.LightingGain_type.process
            }
      
   .. py:class:: LightingStandard
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: IECC2012
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 3
         * a name of "IECC2012".
      
      .. py:property:: NECB2011
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 4
         * a name of "NECB2011".
      
      .. py:property:: NECB2017
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 6
         * a name of "NECB2017".
      
      .. py:property:: PRM2007
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 0
         * a name of "PRM2007".
      
      .. py:property:: PRM2010
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 1
         * a name of "PRM2010".
      
      .. py:property:: PRM2013
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 2
         * a name of "PRM2013".
      
      .. py:property:: PRM2016
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 5
         * a name of "PRM2016".
      
      .. py:property:: PRM2019
         :classmethod:
         :type: iesve.LightingStandard
      
         An instance of this class with:
         
         * a value of 7
         * a name of "PRM2019".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'PRM2007': iesve.LightingStandard.PRM2007
             'PRM2010': iesve.LightingStandard.PRM2010
             'PRM2013': iesve.LightingStandard.PRM2013
             'IECC2012': iesve.LightingStandard.IECC2012
             'NECB2011': iesve.LightingStandard.NECB2011
             'PRM2016': iesve.LightingStandard.PRM2016
             'NECB2017': iesve.LightingStandard.NECB2017
             'PRM2019': iesve.LightingStandard.PRM2019
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.LightingStandard.PRM2007
             1: iesve.LightingStandard.PRM2010
             2: iesve.LightingStandard.PRM2013
             3: iesve.LightingStandard.IECC2012
             4: iesve.LightingStandard.NECB2011
             5: iesve.LightingStandard.PRM2016
             6: iesve.LightingStandard.NECB2017
             7: iesve.LightingStandard.PRM2019
            }
      
   .. py:class:: Mv2
   
      *Interface for Model Viewer 2*
   
      .. py:method:: take_snapshot
      
         *take_snapshot(file_name, path, view_mode, components)*
         
         *Takes a snapshot of the model, using model viewer 2, and saves it to disk.  All*
         *parameters are optional.*
         *An empty string as path (default value) means current project folder.*
         
         *Valid view modes:*
             *shaded, textured, hidden_line, xray, component*
         *Default Parameter Values:*
         *file_name = 'Snapshot' | path = '' | view_mode = shaded | components = False*
         *If a path or filename are specified, the caller is responsible for making sure they are valid.*
      
      .. py:method:: take_snapshot_or_create_blank_image
      
         *take_snapshot_or_blank_image(file_name, path, view_mode, components)*
         
         *Takes a snapshot of the model or gets a blank image, depending on what the user preference isfor compliance report image settings.*
      
   .. py:class:: NECB
   
      *Interface for NECB. Supports 2017 only.*
   
      .. py:method:: get_designer_contractor
      
         *get_designer_contractor() -> Dictionary*
         
         *Get a dictionary of designer and contractor data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_owner_agent
      
         *get_owner_agent() -> Dictionary*
         
         *Get a dictionary of owner and agent data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_site_permit_software
      
         *get_site_permit_software() -> Dictionary*
         
         *Get a dictionary of site, permit and software data from project details*
         *The dictionary contains the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
      .. py:method:: set_designer_contractor
      
         *set_designer_contractor(data)*
         
         *Set designer and contractor entries for project details from a dictionary*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
         
         *set_designer_contractor(data)*
         
         *Set designer and contractor entries for project details from a dictionary*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_owner_agent
      
         *set_owner_agent(data)*
         
         *Set owner and agent entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
         
         *set_owner_agent(data)*
         
         *Set owner and agent entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_site_permit_software
      
         *set_site_permit_software(data)*
         
         *Set site, permit and software entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
         
         *set_site_permit_software(data)*
         
         *Set site, permit and software entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
   .. py:class:: OccupantDiversity
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae621_time_averaging
         :classmethod:
         :type: iesve.OccupantDiversity
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae621_time_averaging".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'room_data_diversity_factors': iesve.OccupantDiversity.room_data_diversity_factors
             'specify_independently': iesve.OccupantDiversity.specify_independently
             'ashrae621_time_averaging': iesve.OccupantDiversity.ashrae621_time_averaging
            }
      
      .. py:property:: room_data_diversity_factors
         :classmethod:
         :type: iesve.OccupantDiversity
      
         An instance of this class with:
         
         * a value of 0
         * a name of "room_data_diversity_factors".
      
      .. py:property:: specify_independently
         :classmethod:
         :type: iesve.OccupantDiversity
      
         An instance of this class with:
         
         * a value of 1
         * a name of "specify_independently".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.OccupantDiversity.room_data_diversity_factors
             1: iesve.OccupantDiversity.specify_independently
             2: iesve.OccupantDiversity.ashrae621_time_averaging
            }
      
   .. py:class:: OutdoorAirRequirementLinkage
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: linked
         :classmethod:
         :type: iesve.OutdoorAirRequirementLinkage
      
         An instance of this class with:
         
         * a value of 0
         * a name of "linked".
      
      .. py:property:: maximum
         :classmethod:
         :type: iesve.OutdoorAirRequirementLinkage
      
         An instance of this class with:
         
         * a value of 1
         * a name of "maximum".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'linked': iesve.OutdoorAirRequirementLinkage.linked
             'maximum': iesve.OutdoorAirRequirementLinkage.maximum
             'sum': iesve.OutdoorAirRequirementLinkage.sum
            }
      
      .. py:property:: sum
         :classmethod:
         :type: iesve.OutdoorAirRequirementLinkage
      
         An instance of this class with:
         
         * a value of 2
         * a name of "sum".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.OutdoorAirRequirementLinkage.linked
             1: iesve.OutdoorAirRequirementLinkage.maximum
             2: iesve.OutdoorAirRequirementLinkage.sum
            }
      
   .. py:class:: PRM
   
      *Interface for PRM*
   
      .. py:method:: get_designer_contractor
      
         *get_designer_contractor() -> Dictionary*
         
         *Get a dictionary of designer and contractor data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_florida
      
         *get_florida() - > Dictionary*
         
         *Get a dictionary of Florida data*
         *The dictionary contains the following entries:*
         
         *description, jurisdiction, class, building_floor_area, num_stories*
      
      .. py:method:: get_florida_certifications
      
         *get_florida_certifications() - > Dictionary*
         
         *Get a dictionary of Florida certifications data*
         *The dictionary contains the following entries:*
         
         *preparer, preparer_date, building_official, building_official_date, owner_agent,*
         *owner_agent_date, architect, architect_reg, electrical_designer,*
         *electrical_designer_reg, lighting_designer, lighting_designer_reg,*
         *mechanical_designer, mechanical_designer_reg, plumbing_designer, plumbing_designer_reg*
      
      .. py:method:: get_owner_agent
      
         *get_owner_agent() -> Dictionary*
         
         *Get a dictionary of owner and agent data from project details*
         *The dictionary contains the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: get_site_permit_software
      
         *get_site_permit_software() -> Dictionary*
         
         *Get a dictionary of site, permit and software data from project details*
         *The dictionary contains the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
      .. py:method:: get_thermal_comfort_room_categories_data
      
         *get_thermal_comfort_room_categories_data() -> list*
         
         *Returns a list of dictionaries for each space.*
         *The dictionary contains the following entries:*
         
         *id, name, activity, analyse*
      
      .. py:method:: get_unmet_load_hour_parameters
      
         *get_unmet_load_hour_parameters() -> dictionary*
         
         *Get unmet load hour parameters.*
         *Returns a dictionary containing 'cooling_tolerance', 'heating_tolerance' and*
         *'override_hvac_throttling_ranges' and 'exclude_nonmaster_rooms'.*
      
      .. py:method:: set_designer_contractor
      
         *set_designer_contractor(data)*
         
         *Set designer and contractor entries for project details from a dictionary*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_florida
      
         *set_florida(data)*
         
         *Set Florida data from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *description, jurisdiction, class, building_floor_area, num_stories*
      
      .. py:method:: set_florida_certifications
      
         *set_florida_certifications(data)*
         
         *Set Florida certifications data from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *preparer, preparer_date, building_official, building_official_date, owner_agent,*
         *owner_agent_date, architect, architect_reg, electrical_designer,*
         *electrical_designer_reg, lighting_designer, lighting_designer_reg,*
         *mechanical_designer, mechanical_designer_reg, plumbing_designer, plumbing_designer_reg*
      
      .. py:method:: set_owner_agent
      
         *set_owner_agent(data)*
         
         *Set owner and agent entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *first_name, last_name, company, address_1, address_2, city, state, zip_code, phone_number, email*
      
      .. py:method:: set_site_permit_software
      
         *set_site_permit_software(data)*
         
         *Set site, permit and software entries for project details from a dictionary.*
         *The dictionary can contain the following entries:*
         
         *title, address_1, address_2, city, state, zip_code, permit_no, permit_date*
      
      .. py:method:: set_thermal_comfort_room_categories_data
      
         *set_thermal_comfort_room_categories_data(data)*
         
         *Set thermal comfort room categories data from a list of dictionaries.*
         *The number of entries in the list must match the number of spaces.*
         *The dictionary must contain the following entries:*
         
         *id, name, activity, analyse*
      
      .. py:method:: set_unmet_load_hour_parameters
      
         *set_unmet_load_hour_parameters(data)*
         
         *Set unmet load hour parameters with the dictionary of data.*
         *The dictionary must contain 'cooling_tolerance', 'heating_tolerance' and*
         *'override_hvac_throttling_ranges' and 'exclude_nonmaster_rooms'.*
      
   .. py:class:: PeopleGain
   
      *Casual Gain data.*
   
      .. py:method:: get
      
         *get() -> Dictionary*
         
         *Returns a Dictionary containing the data for the internal gain.*
      
      .. py:property:: name
      
         *(str) Descriptive string*
      
   .. py:class:: PeopleGain_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'people': iesve.PeopleGain_type.people
            }
      
      .. py:property:: people
         :classmethod:
         :type: iesve.PeopleGain_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "people".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.PeopleGain_type.people
            }
      
   .. py:class:: ProfileUnits
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: imperial
         :classmethod:
         :type: iesve.ProfileUnits
      
         An instance of this class with:
         
         * a value of 1
         * a name of "imperial".
      
      .. py:property:: metric
         :classmethod:
         :type: iesve.ProfileUnits
      
         An instance of this class with:
         
         * a value of 0
         * a name of "metric".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'metric': iesve.ProfileUnits.metric
             'imperial': iesve.ProfileUnits.imperial
             'none': iesve.ProfileUnits.none
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.ProfileUnits
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ProfileUnits.metric
             1: iesve.ProfileUnits.imperial
             -1: iesve.ProfileUnits.none
            }
      
   .. py:class:: ProfileVariation
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant
         :classmethod:
         :type: iesve.ProfileVariation
      
         An instance of this class with:
         
         * a value of 0
         * a name of "constant".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'constant': iesve.ProfileVariation.constant
             'profile': iesve.ProfileVariation.profile
             'two_values': iesve.ProfileVariation.two_values
             'relative_to_zone_room': iesve.ProfileVariation.relative_to_zone_room
            }
      
      .. py:property:: profile
         :classmethod:
         :type: iesve.ProfileVariation
      
         An instance of this class with:
         
         * a value of 1
         * a name of "profile".
      
      .. py:property:: relative_to_zone_room
         :classmethod:
         :type: iesve.ProfileVariation
      
         An instance of this class with:
         
         * a value of 3
         * a name of "relative_to_zone_room".
      
      .. py:property:: two_values
         :classmethod:
         :type: iesve.ProfileVariation
      
         An instance of this class with:
         
         * a value of 2
         * a name of "two_values".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ProfileVariation.constant
             1: iesve.ProfileVariation.profile
             2: iesve.ProfileVariation.two_values
             3: iesve.ProfileVariation.relative_to_zone_room
            }
      
   .. py:class:: ProjectInfo
   
      *Interface for project information*
   
      .. py:method:: get
      
         *get() -> dictionary*
         
         *Get project information.*
         *Returns a dictionary with the following keys:*
         *project_name, building_owner, address, design_team, energy_analyst,*
         *conditioned_floor_area*
      
      .. py:method:: set
      
         *set(data)*
         
         *Set project information using a dictionary of data.*
         *Dictionary can contain the following keys:*
         *project_name, building_owner, address, design_team, energy_analyst,*
         *conditioned_floor_area*
      
   .. py:class:: RefModelUserEdits
   
      *Interface for reference model user edits*
   
      .. py:method:: get
      
         *get() -> dictionary*
         
         *Get reference model user edits.*
         *Returns a dictionary with the following keys:*
         *geometry, spaces, envelope, interior_lighting, hvac_systems, service_hot_water,*
         *miscellaneous*
      
      .. py:method:: set
      
         *set(data)*
         
         *Set reference model user edits using a dictionary of data.*
         *Dictionary can contain the following keys:*
         *geometry, spaces, envelope, interior_lighting, hvac_systems, service_hot_water,*
         *miscellaneous*
      
   .. py:class:: ResultsReader
   
      *Support for reading simulation result files (APS files).*
      *Basic usage:*
      
      *f = iesve.ResultsReader()*
      *f.open_aps_data(filename)*
      *x = f.get_results('Total electricity', 'e')*
      *f.close()*
      
      *or*
      
      *f = iesve.ResultsReader.open(filename)*
      *x = f.get_results('Total electricity', 'e')*
      *f.close()*
   
      .. py:method:: close
      
         *close() -> None*
         
         *Close the results file, and releases all resources associated with the*
         *file.  It is recommended to close files as soon as possible to save resources.*
      
      .. py:property:: first_day
      
         *(int) The first simulation day that has results.*
      
      .. py:property:: first_weekday_plot_year
      
         *(int) The day-of-week (Sun = 1..) of Jan 1 in plot year.*
      
      .. py:method:: get_all_apache_system_results
      
         *get_all_apache_system_results(system_id, aps_var, var_level, [start_day], [end_day]) ->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the results for specified system + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_all_component_process_results
      
         *get_all_component_process_results(room_id, index_in_room, aps_var, var_level, [start_day], [end_day]) ->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Read the results for specified process variable.  See get_results for*
         *start_day and end_day details.*
      
      .. py:method:: get_all_opening_results
      
         *get_all_opening_results(room_id, surface_index, opening_index, aps_var, [start_day], [end_day]->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the results for specified opening + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_all_process_results
      
         *get_all_process_results(process_name, aps_var [start_day], [end_day]) ->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Read the results for specified process variable.  See get_results for*
         *start_day and end_day details.*
      
      .. py:method:: get_all_results
      
         *get_all_results(aps_var, var_level, [start_day], [end_day]) ->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the model-level results for specified variable.*
         *See units spreadsheet for information on variable + level*
         *If start_day and\or end_day are omitted, all available results will be*
         *returned.  start_day = 1 means January 1, end_day = 365 is December 31st.*
         *Check APS file firstday and lastday properties for valid range for file.*
         
         *Note: results are always returned in metric units*
      
      .. py:method:: get_all_room_results
      
         *get_all_room_results(room_id, aps_var, var_level, [start_day], [end_day]) ->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the results for specified room + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_all_surface_results
      
         *get_all_surface_results(room_id, aps_handle, aps_var, [start_day], [end_day]->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the results for specified surface + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_all_weather_results
      
         *get_all_weather_results(aps_var, [start_day], [end_day]->*
             *Dictionary of numpy array of floats, keyed by variable display name*
         
         *Get the results for a weather variable.  See units spreadsheet for*
         *available variables.  See get_results for start_day and end_day details.*
      
      .. py:method:: get_apache_system_results
      
         *get_apache_system_results(system_id, aps_var, vista_var, var_level, [start_day], [end_day]) ->*
             *Numpy array of floats*
         
         *Get the results for specified system + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_apache_systems
      
         *get_apache_systems() -> [(system name, system ID)]*
         
         *Get list of Apache Systems in the results file.*
      
      .. py:method:: get_component_objects
      
         *get_component_objects() ->*
         *[(room ID, index in room, component name, [(variable name, variable unit, variable level)])]*
         
         *Return the list of process component objects for this results file.*
      
      .. py:method:: get_component_process_results
      
         *get_component_process_results(room_id, index_in_room, aps_var, vista_var, var_level, [start_day], [end_day]) ->*
             *Numpy array of floats*
         
         *Read the results for specified process variable.  See get_results for*
         *start_day and end_day details.*
      
      .. py:method:: get_conditioned_sizes
      
         *get_conditioned_sizes()->*
             *tuple of floats*
         
         *Get a tuple of the conditioned area, volume*
          *and number of conditioned rooms as recorded in the results file.*
      
      .. py:method:: get_data_file_details
      
         *get_data_file_details(filename, date_time_format) ->*
             *Dictionary of file details*
         
         *Get file details. Dictionary keys are name, calculated, profile_month_start, profile_month_end*
      
      .. py:method:: get_energy_meters
      
         *get_energy_meters( used_only=True ) -> dictionary*
         
         *Returns a dictionary of all (or only the used) energy meters in the file by id.*
         *Each item is a dictionary containing information about a specific energy meter.*
         *Dictionary fields include:*
             *id : the meter id (iesve.EnergyMeter)*
             *name : the meter name (string)*
             *parent_id : the id of the parent meter this meter belongs to, if any (iesve.EnergyMeter)*
             *source_id : the id of the source the meter is assigned to (iesve.EnergySource)*
             *has_subs : whether or not the meter has any child (sub) meters (bool)*
             *used : whether or not the meter has any aps results (bool)*
      
      .. py:method:: get_energy_results
      
         *get_energy_results( use_id=unspecified, source_id=unspecified, meter_id=unspecified,*
                              *type='e', add_subs=-1, start_day=-1, end_day=-1) ->*
             *Numpy array of floats, or None*
         
         *Returns the specified energy results given the use id, source id, meter id and type.*
         *Setting type to 'e' or 'c' determines whether or not energy (W) or carbon (kgC) results are returned.*
         *Setting add_subs to 1 or 0 determines whether or not parent meter results include or do not include child (sub) meter results.*
         *When add_subs is -1 the option is ignored and the default behaviour will be applied.*
         *See get_results for start_day and end_day details.*
         *Example usage:*
             *get_energy_results() -> 'Total Energy'*
             *get_energy_results( source_id=elec ) -> 'Electricity'*
             *get_energy_results( source_id=elec, meter_id=1 ) -> 'Electricity: Meter 1'*
             *get_energy_results( use_id=prm_pumps ) -> 'Pumps'*
             *get_energy_results( use_id=prm_pumps, source_id=elec ) -> 'Pumps - Electricity'*
             *get_energy_results( use_id=prm_pumps, source_id=elec, meter_id=1 ) -> 'Pumps - Electricity: Meter 1'*
      
      .. py:method:: get_energy_results_ex
      
         *get_energy_results_ex( use_ids, source_ids, type='e', start_day=-1, end_day=-1) ->*
             *Numpy array of floats, or None*
         
         *Returns the aggregated energy results for the specified use(s) and/or source(s).*
         *The use_ids argument can be None, a single use id, or a list of use ids.*
         *The source_ids argument can be None, a single source id, or a list of source ids.*
         *At least one use or one source must be specified.*
         *Setting type to 'e' or 'c' determines whether or not energy (W) or carbon (kgC) results are returned.*
         *See get_results for start_day and end_day details.*
      
      .. py:method:: get_energy_sources
      
         *get_energy_sources( used_only=True ) -> dictionary*
         
         *Returns a dictionary of all (or only the used) energy sources in the file by id.*
         *Each item is a dictionary containing information about a specific energy source.*
         *Dictionary fields include:*
             *id : the source id (iesve.EnergySource)*
             *name : the source name (string)*
             *cef : the carbon emission factor of the source, used to convert kgC to kgCO2 (float)*
             *used : whether or not the source has any aps results (bool)*
      
      .. py:method:: get_energy_uses
      
         *get_energy_uses( used_only=True ) -> dictionary*
         
         *Returns a dictionary of all (or only the used) energy uses in the file by id.*
         *Each item is a dictionary containing information about a specific energy use.*
         *Dictionary fields include:*
             *id : the use id (iesve.EnergyUse)*
             *name : the use name (string)*
             *tied_source_id : the id of the source the use is fixed to, if any (iesve.EnergySource)*
             *used : whether or not the use has any aps results (bool)*
      
      .. py:method:: get_hvac_component_results
      
         *get_hvac_component_results(component_id, component_type, var_name, [start_day], [end_day]->*
             *Numpy array of floats*
         
         *Get the results for HVAC Component ID + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details. Note the follow component types are defined:*
           *1: HVAC_TYPE_ROOM*
           *2: HVAC_TYPE_SIMPLE_HEATING_COIL*
           *3: HVAC_TYPE_SIMPLE_COOLING_COIL*
           *4: VAC_TYPE_SPRAY_HUMIDIFIER*
           *5: HVAC_TYPE_STEAM_HUMIDIFIER*
           *6: HVAC_TYPE_TEMP_FLOW_CTRL*
           *7: HVAC_TYPE_JUNCTION*
           *8: HVAC_TYPE_DUCT*
           *9: HVAC_TYPE_EQUIP_HEAT_GAIN*
          *10: HVAC_TYPE_HEAT_RECOV*
          *11: HVAC_TYPE_TERMINAL_REHEAT*
          *12: HVAC_TYPE_TERMINAL_RECOOL*
          *13: HVAC_TYPE_BOILER*
          *14: HVAC_TYPE_CHILLER*
          *15: HVAC_TYPE_FAN*
          *16: HVAC_TYPE_DAMPER*
          *17: HVAC_TYPE_VERSATEMP*
          *18: HVAC_TYPE_UNITARY_COOLING*
          *19: HVAC_TYPE_WATERSIDE_ECON*
          *20: HVAC_TYPE_EWC_CHILLER*
          *21: HVAC_TYPE_HWB_BOILER*
          *22: HVAC_TYPE_ADIABATIC_DUCT*
          *23: HVAC_TYPE_EAC_CHILLER*
          *24: HVAC_TYPE_DX_COOLING*
          *25: HVAC_TYPE_ADVANCED_COOLING_COIL*
          *26: HVAC_TYPE_CHILLED_WATER_LOOP*
          *27: HVAC_TYPE_ADVANCED_HEATING_COIL*
          *28: HVAC_TYPE_HOT_WATER_LOOP*
          *29: HVAC_TYPE_GENERIC_HEAT_SOURCE*
          *30: HVAC_TYPE_AWHP*
          *31: HVAC_TYPE_AAHP*
          *32: HVAC_TYPE_SOLAR_WATER_HEATER*
          *33: HVAC_TYPE_HEAT_TRANSFER_LOOP*
          *34: HVAC_TYPE_WAHP*
          *35: HVAC_TYPE_GENERIC_COOLING_SOURCE*
          *36: HVAC_TYPE_ROOM_RADIATOR*
          *37: HVAC_TYPE_ROOM_CHILLED_CEILING*
          *38: HVAC_TYPE_CONDENSER_WATER_LOOP*
          *39: HVAC_TYPE_COOLING_TOWER*
          *40: HVAC_TYPE_FLUID_COOLER*
          *41: HVAC_TYPE_PRE_COOLING*
          *42: HVAC_TYPE_WATER_SOURCE_LOOP*
          *43: HVAC_TYPE_WATER_WATER_HX*
          *44: HVAC_TYPE_PCM_THERMAL_BATTERY*
          *45: HVAC_TYPE_PUMP*
          *46: HVAC_TYPE_VRF_INDOOR_HEAT*
          *47: HVAC_TYPE_VRF_INDOOR_COOL*
          *48: HVAC_TYPE_VRF_INDOOR_TYPE*
          *49: HVAC_TYPE_VRF_OUTDOOR*
          *50: HVAC_TYPE_SOLAR_AIRCOLLECTOR_BIST*
          *51: HVAC_TYPE_AIRFILTER*
          *52: HVAC_TYPE_PLENUM*
          *53: HVAC_TYPE_THERMAL_STORAGE_LOOP*
          *54: HVAC_TYPE_THERMAL_STORAGE_TANK*
          *55: HVAC_TYPE_TSD_VIRTUAL_CHILLER*
          *56: HVAC_TYPE_TSC_VIRTUAL_CHILLER*
          *62: HVAC_TYPE_EAHP*
          *63: HVAC_TYPE_EAHP_HEATING_INSTACNE*
          *64: HVAC_TYPE_EAHP_COOLING_INSTANCE*
          *67: HVAC_TYPE_HEAT_RECOVERY_LOOP*
          *68: HVAC_TYPE_DRAIN_WATER_HEAT_RECOVERY_HX*
          *69: HVAC_TYPE_CENTRAL_PLANT_HEAT_PUMP*
      
      .. py:method:: get_hvac_node_results
      
         *get_hvac_node_results(node_nr, [layer_nr], var_name, [start_day], [end_day]->*
             *Numpy array of floats*
         
         *Get the results for HVAC Node.  Use layer_nr to specify multiplex*
         *layer, or -1 for plant-side node.  See units spreadsheet for available*
         *variables and matching level.  See get_results for start_day and*
         *end_day details.*
      
      .. py:method:: get_opening_results
      
         *get_opening_results(room_id, surface_index, opening_index, aps_var, vista_var, [start_day], [end_day]->*
             *Numpy array of floats*
         
         *Get the results for specified opening + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_peak_results
      
         *variables*
      
      .. py:method:: get_process_list
      
         *get_process_list() -> [process category]*
         
         *Return the list of process categories for this results file.*
      
      .. py:method:: get_process_results
      
         *get_process_results(process_name, aps_var, vista_var [start_day], [end_day]) ->*
             *Numpy array of floats*
         
         *Read the results for specified process variable.  See get_results for*
         *start_day and end_day details.*
      
      .. py:method:: get_process_variables
      
         *get_process_variables(process) -> [(name, units)]*
         
         *For the process specified (one of the return values from GetProcessList),*
         *return the available process variables.*
      
      .. py:method:: get_results
      
         *get_results(aps_var, vista_var, var_level, [start_day], [end_day]) ->*
             *Numpy array of floats*
         
         *Get the model-level results for specified variable.*
         *See units spreadsheet for information on variable + level*
         *If start_day and\or end_day are omitted, all available results will be*
         *returned.  start_day = 1 means January 1, end_day = 365 is December 31st.*
         *Check APS file firstday and lastday properties for valid range for file.*
         
         *Note: results are always returned in metric units*
      
      .. py:method:: get_room_geometry_details
      
         *get_room_geometry_details([room ID]) -> [{details}]*
         *get_room_geometry_details(roomID) -> {details}*
         
         *Returns a list of dictionaries for all requested room IDs.  You may also*
         *pass a single room ID string, in which case a single dictionary is returned.*
         *Dictionary entries are:*
             *opaque, glazed, internal_wall, external_wall, internal_glazed,*
             *num_open, num_surf, external_glazed, rooflight, door, floor,*
             *ground_floor, ceiling, roof.*
      
      .. py:method:: get_room_ids
      
         *get_room_ids() -> [roomID]*
         
         *Returns a list of room IDs for all rooms in the results file.*
      
      .. py:method:: get_room_list
      
         *get_room_list() -> [(room name, room ID, room area, room volume)]*
         
         *Returns a list of (room ID, room name, room area, room volume) for all rooms in the results file.*
      
      .. py:method:: get_room_results
      
         *get_room_results(room_id, aps_var, vista_var, var_level, [start_day], [end_day]) ->*
             *Numpy array of floats*
         
         *Get the results for specified room + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_surface_results
      
         *get_surface_results(room_id, aps_handle, aps_var, vista_var [start_day], [end_day]->*
             *Numpy array of floats*
         
         *Get the results for specified surface + variable.  See units spreadsheet*
         *for available variables and matching level.  See get_results for start_day*
         *and end_day details.*
      
      .. py:method:: get_units
      
         *get_units( ) -> { units data }*
         
         *Get the list of results file units that are applicable to the loaded*
         *file.  The return value is a dictionary of dictionaries with all relevant*
         *units data.  The main dictionary is keyed on unit type (units_type).*
         *The available unit data fields (in IP and Metric variants) are:*
             *divisor, offset, display_name.*
      
      .. py:method:: get_unmet_hours
      
         *get_unmet_hours()->*
             *Dictionary*
         
         *Get unmet load hours data.*
      
      .. py:method:: get_variables
      
         *get_variables( ) -> [ variable data ]*
         
         *Get the list of results file variables that are applicable to the loaded*
         *file.  The return value is a list of dictionaries with all relevant*
         *variable data.  The available data fields are:*
             *category, display_name, aps_varname, units_type, units_category,*
             *combine_flag, model_level, post_process, color, color_rgb, subtype,*
             *line_style, order, polarity.*
      
      .. py:method:: get_weather_results
      
         *get_weather_results(aps_var, vista_var, [start_day], [end_day]->*
             *Numpy array of floats*
         
         *Get the results for a weather variable.  See units spreadsheet for*
         *available variables.  See get_results for start_day and end_day details.*
      
      .. py:property:: hvac_file
      
         *(str) The HVAC network used for simulation.*
      
      .. py:property:: last_day
      
         *(int) The last simulation day that has results.*
      
      .. py:method:: open
      
         *open(filename) -> iesve.ResultsReader*
         
         *Open an APS file and return a ResultsReader instance. Throws exception*
         *on error.*
      
      .. py:method:: open_aps_data
      
         *open_aps_data(filename) -> int*
         
         *Open an APS file, returns 1 on success, throws exception on file not found.*
      
      .. py:property:: plot_data_offset_secs
      
         *(int) The plot data offset in seconds.*
      
      .. py:property:: plot_year
      
         *(int) The plot year.*
      
      .. py:property:: results_per_day
      
         *(int) The number of results per 24 hour period.*
      
      .. py:property:: simulation_year
      
         *(int) The simulation year.*
      
      .. py:property:: weather_file
      
         *(str) The weatherfile used for simulation.*
      
      .. py:property:: year
      
         *(int) The plot year. WARNING: DEPRECATED, use plot_year instead.*
      
   .. py:class:: RoomAirExchange
   
      *Interface for RoomAirExchange object.*
   
      .. py:method:: get
      
         *Gets the air exchange data.*
         *Returns:*
             *Dictionary with the following information, including whether values are*
             *from template:*
             *- Infiltration type and name, the maximum flow (including converted*
               *values) and the variation profile ID.*
             *- Adjacent condition, with offset temperature or temperature profile ID if*
               *relevant.*
      
   .. py:class:: RoomGroups
   
      *Interface for Room Groups*
   
      .. py:method:: assign_rooms_to_group
      
         *assign_rooms_to_group(scheme handle, group handle, [room IDs])*
         
         *Assigns the rooms specified by room IDs list to the specified group.*
         *The room IDs list can be either a list of strings or a list of VEBody objects.*
      
      .. py:method:: assign_rooms_to_zone
      
         *assign_rooms_to_zone(zone ID)*
         
         *Assigns all rooms to the specified zone*
      
      .. py:method:: create_grouping_scheme
      
         *create_grouping_scheme(name) -> int*
         
         *Creates a room grouping scheme with the given name*
         *Returns the handle of the new grouping scheme*
      
      .. py:method:: create_room_group
      
         *create_room_group(scheme handle, new group name, colour) -> int*
         
         *Creates a room group with the given name and colour in the provided grouping scheme.*
         *Colour is expressed as a tuple of (R,G,B) and is optional, will default to black*
         *Returns the handle of the new room group*
      
      .. py:method:: create_zone
      
         *create_zone(zone group ID, zone name) -> ID of created zone*
         
         *Creates a zone with the given name in the provided zone group*
         *Returns the ID of the newly added zone*
      
      .. py:method:: create_zone_group
      
         *create_zone_group(name) -> string*
         
         *Creates a zone group with the given name*
         *Returns the ID of the new zone group*
      
      .. py:method:: get_grouping_schemes
      
         *get_grouping_schemes( ) -> List of dictionaries*
         
         *Get a list of room grouping schemes stored as dictionaries*
         *Dictionary entries are:*
         *handle, name*
      
      .. py:method:: get_room_groups
      
         *get_room_groups(grouping scheme handle) -> List of dictionaries*
         
         *Get a list of room groups (stored as dictionaries) for a grouping scheme*
         
         *Dictionary entries are:*
         *RGB colour, handle, name, rooms*
      
      .. py:method:: get_zone_groups
      
         *get_zone_groups() -> List of dictionaries*
         
         *Get a list of zone groups (stored as dictionaries)*
         
         *Dictionary entries are:*
         *name, id*
      
      .. py:method:: get_zones
      
         *get_zones(zone group ID) -> List of dictionaries*
         
         *Get a list of zones (stored as dictionaries) for a given zone group*
         
         *Dictionary entries are:*
         *name, id, rooms (list of IDs), master_room*
      
   .. py:class:: RoomInternalGain
   
      *Interface for RoomInternalGain object.*
   
      .. py:method:: get
      
         *Gets the internal gain data.*
         *Returns:*
             *Dictionary with the following information, including whether values are from*
             *template:*
             *- Name and type, variation profile ID and diversity factor.*
             *Lighting gains also include:*
             *- Maximum sensible gain, maximum power consumption and power units*
               *(with converted values)*
             *- Radiant fraction, fuel, dimming profile ID and ballast/driver fraction.*
             *- When the lighting units are Lux there is also maximum illuminance*
               *(lux) and installed power density (W/m^2 per 100 lux)*
             *Power gains also include:*
             *- Units, maximum sensible gain and maximum power consumption (with*
               *converted values)*
             *- Maximum latent gain (except for computers)*
             *- Radiant fraction and fuel.*
             *People gains also include:*
             *- Occupancy unit and value (with converted values)*
             *- Maximum sensible gain, maximum latent gain and power units (with*
               *converted values).*
      
   .. py:class:: RoomLightingGain
   
      *Interface for RoomInternalGain object.*
   
      .. py:method:: get
      
         *Gets the internal gain data.*
         *Returns:*
             *Dictionary with the following information, including whether values are from*
             *template:*
             *- Name and type, variation profile ID and diversity factor.*
             *Lighting gains also include:*
             *- Maximum sensible gain, maximum power consumption and power units*
               *(with converted values)*
             *- Radiant fraction, fuel, dimming profile ID and ballast/driver fraction.*
             *- When the lighting units are Lux there is also maximum illuminance*
               *(lux) and installed power density (W/m^2 per 100 lux)*
             *Power gains also include:*
             *- Units, maximum sensible gain and maximum power consumption (with*
               *converted values)*
             *- Maximum latent gain (except for computers)*
             *- Radiant fraction and fuel.*
             *People gains also include:*
             *- Occupancy unit and value (with converted values)*
             *- Maximum sensible gain, maximum latent gain and power units (with*
               *converted values).*
      
   .. py:class:: RoomPeopleGain
   
      *Interface for RoomInternalGain object.*
   
      .. py:method:: get
      
         *Gets the internal gain data.*
         *Returns:*
             *Dictionary with the following information, including whether values are from*
             *template:*
             *- Name and type, variation profile ID and diversity factor.*
             *Lighting gains also include:*
             *- Maximum sensible gain, maximum power consumption and power units*
               *(with converted values)*
             *- Radiant fraction, fuel, dimming profile ID and ballast/driver fraction.*
             *- When the lighting units are Lux there is also maximum illuminance*
               *(lux) and installed power density (W/m^2 per 100 lux)*
             *Power gains also include:*
             *- Units, maximum sensible gain and maximum power consumption (with*
               *converted values)*
             *- Maximum latent gain (except for computers)*
             *- Radiant fraction and fuel.*
             *People gains also include:*
             *- Occupancy unit and value (with converted values)*
             *- Maximum sensible gain, maximum latent gain and power units (with*
               *converted values).*
      
   .. py:class:: RoomPowerGain
   
      *Interface for RoomInternalGain object.*
   
      .. py:method:: get
      
         *Gets the internal gain data.*
         *Returns:*
             *Dictionary with the following information, including whether values are from*
             *template:*
             *- Name and type, variation profile ID and diversity factor.*
             *Lighting gains also include:*
             *- Maximum sensible gain, maximum power consumption and power units*
               *(with converted values)*
             *- Radiant fraction, fuel, dimming profile ID and ballast/driver fraction.*
             *- When the lighting units are Lux there is also maximum illuminance*
               *(lux) and installed power density (W/m^2 per 100 lux)*
             *Power gains also include:*
             *- Units, maximum sensible gain and maximum power consumption (with*
               *converted values)*
             *- Maximum latent gain (except for computers)*
             *- Radiant fraction and fuel.*
             *People gains also include:*
             *- Occupancy unit and value (with converted values)*
             *- Maximum sensible gain, maximum latent gain and power units (with*
               *converted values).*
      
   .. py:class:: SolarHeating_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: flat
         :classmethod:
         :type: iesve.SolarHeating_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "flat".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.SolarHeating_type.none
             'flat': iesve.SolarHeating_type.flat
             'parabolic': iesve.SolarHeating_type.parabolic
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.SolarHeating_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "none".
      
      .. py:property:: parabolic
         :classmethod:
         :type: iesve.SolarHeating_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "parabolic".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.SolarHeating_type.none
             1: iesve.SolarHeating_type.flat
             2: iesve.SolarHeating_type.parabolic
            }
      
   .. py:class:: SpaceOutdoorAirRequirementBasis
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae_170
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae_170".
      
      .. py:property:: ashrae_621
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 0
         * a name of "ashrae_621".
      
      .. py:property:: maximum
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 3
         * a name of "maximum".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'ashrae_621': iesve.SpaceOutdoorAirRequirementBasis.ashrae_621
             'outdoor_requirement': iesve.SpaceOutdoorAirRequirementBasis.outdoor_requirement
             'ashrae_170': iesve.SpaceOutdoorAirRequirementBasis.ashrae_170
             'maximum': iesve.SpaceOutdoorAirRequirementBasis.maximum
             'sum': iesve.SpaceOutdoorAirRequirementBasis.sum
             'title_24': iesve.SpaceOutdoorAirRequirementBasis.title_24
            }
      
      .. py:property:: outdoor_requirement
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 1
         * a name of "outdoor_requirement".
      
      .. py:property:: sum
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 4
         * a name of "sum".
      
      .. py:property:: title_24
         :classmethod:
         :type: iesve.SpaceOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 5
         * a name of "title_24".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.SpaceOutdoorAirRequirementBasis.ashrae_621
             1: iesve.SpaceOutdoorAirRequirementBasis.outdoor_requirement
             2: iesve.SpaceOutdoorAirRequirementBasis.ashrae_170
             3: iesve.SpaceOutdoorAirRequirementBasis.maximum
             4: iesve.SpaceOutdoorAirRequirementBasis.sum
             5: iesve.SpaceOutdoorAirRequirementBasis.title_24
            }
      
   .. py:class:: StrategyOutsideAirVentilationMinReq
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: all_hours
         :classmethod:
         :type: iesve.StrategyOutsideAirVentilationMinReq
      
         An instance of this class with:
         
         * a value of 2
         * a name of "all_hours".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'occupied_opening_hours_only': iesve.StrategyOutsideAirVentilationMinReq.occupied_opening_hours_only
             'occupied_extension_hours': iesve.StrategyOutsideAirVentilationMinReq.occupied_extension_hours
             'all_hours': iesve.StrategyOutsideAirVentilationMinReq.all_hours
            }
      
      .. py:property:: occupied_extension_hours
         :classmethod:
         :type: iesve.StrategyOutsideAirVentilationMinReq
      
         An instance of this class with:
         
         * a value of 1
         * a name of "occupied_extension_hours".
      
      .. py:property:: occupied_opening_hours_only
         :classmethod:
         :type: iesve.StrategyOutsideAirVentilationMinReq
      
         An instance of this class with:
         
         * a value of 0
         * a name of "occupied_opening_hours_only".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.StrategyOutsideAirVentilationMinReq.occupied_opening_hours_only
             1: iesve.StrategyOutsideAirVentilationMinReq.occupied_extension_hours
             2: iesve.StrategyOutsideAirVentilationMinReq.all_hours
            }
      
   .. py:class:: StrategySystemFanOperation
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: any_strategy
         :classmethod:
         :type: iesve.StrategySystemFanOperation
      
         An instance of this class with:
         
         * a value of 3
         * a name of "any_strategy".
      
      .. py:property:: cycling
         :classmethod:
         :type: iesve.StrategySystemFanOperation
      
         An instance of this class with:
         
         * a value of 1
         * a name of "cycling".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'on_continously': iesve.StrategySystemFanOperation.on_continously
             'cycling': iesve.StrategySystemFanOperation.cycling
             'off_continously': iesve.StrategySystemFanOperation.off_continously
             'any_strategy': iesve.StrategySystemFanOperation.any_strategy
            }
      
      .. py:property:: off_continously
         :classmethod:
         :type: iesve.StrategySystemFanOperation
      
         An instance of this class with:
         
         * a value of 2
         * a name of "off_continously".
      
      .. py:property:: on_continously
         :classmethod:
         :type: iesve.StrategySystemFanOperation
      
         An instance of this class with:
         
         * a value of 0
         * a name of "on_continously".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.StrategySystemFanOperation.on_continously
             1: iesve.StrategySystemFanOperation.cycling
             2: iesve.StrategySystemFanOperation.off_continously
             3: iesve.StrategySystemFanOperation.any_strategy
            }
      
   .. py:class:: SystemOutdoorAirRequirementBasis
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae_621
         :classmethod:
         :type: iesve.SystemOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 0
         * a name of "ashrae_621".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'ashrae_621': iesve.SystemOutdoorAirRequirementBasis.ashrae_621
             'sum_of_zone_outdoor_air_requirements': iesve.SystemOutdoorAirRequirementBasis.sum_of_zone_outdoor_air_requirements
            }
      
      .. py:property:: sum_of_zone_outdoor_air_requirements
         :classmethod:
         :type: iesve.SystemOutdoorAirRequirementBasis
      
         An instance of this class with:
         
         * a value of 1
         * a name of "sum_of_zone_outdoor_air_requirements".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.SystemOutdoorAirRequirementBasis.ashrae_621
             1: iesve.SystemOutdoorAirRequirementBasis.sum_of_zone_outdoor_air_requirements
            }
      
   .. py:class:: SystemParameters
   
      *Interface for HVAC system parameters*
   
      .. py:method:: get_schedules
      
         *get_schedules() -> dictionary*
         
         *Get a dictionary of schedules data.*
         *Possible dictionary entries:*
         *is_optimal_start, morning_startup_time, after_hours_operation,*
         *system_occupancy_schedule, is_link_operation_and_availability_profiles,*
         *system_operation_schedule, system_availability_schedule,*
         *minimum_outside_air_ventilation, exhaust_fan_operation,*
         *hvac_system_fan_operation_occupied_hours_and_extension_periods,*
         *hvac_system_fan_operation_closed_periods,*
         *zone_recirculation_fan_operation_occupied_hours_and_extension_periods,*
         *zone_recirculation_fan_operation_closed_periods, control_scheme,*
         *design_max_flow_rate, percent_flow_during_unoccupied_hours,*
         *contaminant_schedule_profile, system_availability*
      
      .. py:method:: get_system_parameters
      
         *layer_number*
      
      .. py:method:: get_zone_airflows_turndown_engineering
      
         *layer_number*
      
      .. py:method:: get_zone_loads_airflows
      
         *layer_number*
      
      .. py:method:: get_zone_temperature_humidity_equipment
      
         *layer_number*
      
      .. py:method:: get_zone_ventilation_exhaust
      
         *layer_number*
      
   .. py:class:: SystemSizingBypassOption
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: bypass_system_sizing
         :classmethod:
         :type: iesve.SystemSizingBypassOption
      
         An instance of this class with:
         
         * a value of 0
         * a name of "bypass_system_sizing".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'bypass_system_sizing': iesve.SystemSizingBypassOption.bypass_system_sizing
             'system_sizing_on': iesve.SystemSizingBypassOption.system_sizing_on
            }
      
      .. py:property:: system_sizing_on
         :classmethod:
         :type: iesve.SystemSizingBypassOption
      
         An instance of this class with:
         
         * a value of 1
         * a name of "system_sizing_on".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.SystemSizingBypassOption.bypass_system_sizing
             1: iesve.SystemSizingBypassOption.system_sizing_on
            }
      
   .. py:class:: T24
   
      *Interface for Title 24*
   
      .. py:method:: get
      
         *get() -> dictionary*
         
         *Get Title 24 data.*
         *Returns a dictionary with the following keys:*
         *project_name, building_address, doc_author_name, doc_author_company,*
         *doc_author_phone and building_city*
      
      .. py:method:: get_pv_designer
      
         *get_pv_designer() -> dict*
         
         *Gets data on PV designer if present in project data dialog.*
         *Checks for scope of PV then PV and Battery.*
      
      .. py:method:: get_room_ids_excluded_from_verification
      
         *get_room_ids_excluded_from_verification() -> list*
         
         *Gets a list of room IDs excluded from verification.*
      
      .. py:method:: get_solar_assessment_pv_data
      
         *get_solar_assessment_pv_data() -> list[dict]*
         
         *Return a list of PV panel data from solar assessment*
         *dict keys are:*
         *array, id, panel_area, azimuth, pitch, annual_solar_access*
      
      .. py:method:: get_unmet_hours
      
         *get_unmet_hours(aps_path, network_path) -> dict*
         
         *Get a dictionary of unmet load hours data for Title 24. Keys are:*
         *heating, cooling*
      
      .. py:method:: is_residential_model
      
         *is_residential_model() -> bool*
         
         *True if the model is residential, False otherwise*
      
   .. py:class:: T24EndUseData
   
      *Interface for Title 24 End Use Data Aggregator object*
      
      *Initialise with (enum eAshraeStandard,*
      
         *bool isResidential, string application_path)*
   
      .. py:method:: get_all_compliance_use_totals
      
         *Gets all compliance end use data total for*
         
         *proposed and standard*
      
      .. py:method:: get_all_use_totals
      
         *Gets all end use data total for*
         
         *proposed and standard*
      
      .. py:method:: get_efficiency_use_totals
      
         *Gets efficiency end use data total for*
         
         *proposed and standard*
      
      .. py:method:: get_end_use_data
      
         *Gets End Use data for proposed and standard*
         
          *for given end use enum*
      
      .. py:method:: get_flexibility_use_totals
      
         *Gets flexibility end use data total for*
         
         *proposed and standard*
      
      .. py:method:: get_non_regulated_use_totals
      
         *Gets non-regulated end use data total for*
         
         *proposed and standard*
      
   .. py:class:: T24ProposedBatterySimData
   
      *Interface for Title 24 Proposed Battery Simulation Data object*
      
      *Initialise with constructor method*
   
      .. py:property:: battery_control_type
      
         *enum BatteryControlType: Battery control type*
      
      .. py:property:: battery_schedule
      
         *string: Battery schedule*
      
      .. py:property:: battery_sim_was_run
      
         *bool: Battery simulation was run*
      
      .. py:property:: charge_loss_factor
      
         *float: Charge loss factor*
      
      .. py:property:: discharge_loss_factor
      
         *float: Discharge loss factor*
      
      .. py:property:: initial_charge_kwh
      
         *float: Initial charge in kWh*
      
      .. py:method:: load
      
         *Load proposed battery simulation data to model settings file.*
         
         *Load it run on initialisation so should normally be required*
      
      .. py:property:: max_charge_rate_kw
      
         *float: Max charge rate in kW*
      
      .. py:property:: max_discharge_rate_kw
      
         *float: Max discharge rate in kW*
      
      .. py:method:: save
      
         *Save proposed battery simulation data to model settings file*
      
      .. py:property:: standby_24h_loss_factor
      
         *float: Standby 24h loss factor*
      
      .. py:property:: tdv_file
      
         *string: TDV file*
      
      .. py:property:: usable_capacity_kwh
      
         *float: Usable capacity in kWh*
      
   .. py:class:: T24ReportEndUse
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: battery
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 14
         * a name of "battery".
      
      .. py:property:: domestic_hot_water
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 6
         * a name of "domestic_hot_water".
      
      .. py:property:: flexibility
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 8
         * a name of "flexibility".
      
      .. py:property:: heat_rejection
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 4
         * a name of "heat_rejection".
      
      .. py:property:: indoor_fans
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 3
         * a name of "indoor_fans".
      
      .. py:property:: indoor_lighting
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 7
         * a name of "indoor_lighting".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unspecified': iesve.T24ReportEndUse.unspecified
             'space_heating': iesve.T24ReportEndUse.space_heating
             'space_cooling': iesve.T24ReportEndUse.space_cooling
             'indoor_fans': iesve.T24ReportEndUse.indoor_fans
             'heat_rejection': iesve.T24ReportEndUse.heat_rejection
             'pumps_misc': iesve.T24ReportEndUse.pumps_misc
             'domestic_hot_water': iesve.T24ReportEndUse.domestic_hot_water
             'indoor_lighting': iesve.T24ReportEndUse.indoor_lighting
             'flexibility': iesve.T24ReportEndUse.flexibility
             'receptacle': iesve.T24ReportEndUse.receptacle
             'process': iesve.T24ReportEndUse.process
             'other_lighting': iesve.T24ReportEndUse.other_lighting
             'process_motor': iesve.T24ReportEndUse.process_motor
             'pv': iesve.T24ReportEndUse.pv
             'battery': iesve.T24ReportEndUse.battery
            }
      
      .. py:property:: other_lighting
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 11
         * a name of "other_lighting".
      
      .. py:property:: process
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 10
         * a name of "process".
      
      .. py:property:: process_motor
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 12
         * a name of "process_motor".
      
      .. py:property:: pumps_misc
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 5
         * a name of "pumps_misc".
      
      .. py:property:: pv
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 13
         * a name of "pv".
      
      .. py:property:: receptacle
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 9
         * a name of "receptacle".
      
      .. py:property:: space_cooling
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 2
         * a name of "space_cooling".
      
      .. py:property:: space_heating
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 1
         * a name of "space_heating".
      
      .. py:property:: unspecified
         :classmethod:
         :type: iesve.T24ReportEndUse
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unspecified".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.T24ReportEndUse.unspecified
             1: iesve.T24ReportEndUse.space_heating
             2: iesve.T24ReportEndUse.space_cooling
             3: iesve.T24ReportEndUse.indoor_fans
             4: iesve.T24ReportEndUse.heat_rejection
             5: iesve.T24ReportEndUse.pumps_misc
             6: iesve.T24ReportEndUse.domestic_hot_water
             7: iesve.T24ReportEndUse.indoor_lighting
             8: iesve.T24ReportEndUse.flexibility
             9: iesve.T24ReportEndUse.receptacle
             10: iesve.T24ReportEndUse.process
             11: iesve.T24ReportEndUse.other_lighting
             12: iesve.T24ReportEndUse.process_motor
             13: iesve.T24ReportEndUse.pv
             14: iesve.T24ReportEndUse.battery
            }
      
   .. py:class:: T24ResponsiblePerson
   
      *object*
      
      *Object containing information about the responsible person.*
   
      .. py:property:: address
      
         *address -> string*
         
         *Gets address of responsible person.*
      
      .. py:property:: city
      
         *city -> string*
         
         *Gets city of responsible person.*
      
      .. py:property:: license
      
         *license -> string*
         
         *Gets license of responsible person.*
      
      .. py:property:: name
      
         *name -> string*
         
         *Gets name of responsible person.*
      
      .. py:property:: organization
      
         *organization -> string*
         
         *Gets organization of responsible person.*
      
      .. py:property:: phone
      
         *phone -> string*
         
         *Gets phone number of responsible person.*
      
      .. py:property:: state
      
         *state -> string*
         
         *Gets state of responsible person.*
      
      .. py:property:: zip
      
         *zip -> int*
         
         *Gets zip of responsible person as an int.*
      
   .. py:class:: TDVCalculator
   
      *Interface for TDVCalculator object*
      
      *Initialise with (string aps_path,enum eAshraeStandard , enum Title24Climatezone,*
      
         *bool isResidential, string application_path)*
   
      .. py:method:: get_elec_tdv
      
         *get_elec_tdv() -> numpy array*
         
         *Gets TDV factors for Electricity in kBtu/kWh*
      
      .. py:method:: get_nat_gas_tdv
      
         *get_nat_gas_tdv() -> numpy array*
         
         *Gets TDV factors for Natural Gas in kBtu/kWh (already converted from kBtu/therm in data)*
      
      .. py:method:: get_propane_tdv
      
         *get_propane_tdv() -> numpy array*
         
         *Gets TDV factors for Propane in kBtu/kWh (already converted from kBtu/therm in data)*
         
         *Note: factors apply to additional sources not just propane*
      
   .. py:class:: TariffsEngine
   
      *Support for tariffs engine.*
      
      *Parameters:*
      
        *char *pcProjectFolder  -  MIT project folder ending by '' or not.*
          *I.e: C:\My project\*
      
        *char *pcAPSFile  -  APS file with path. I.e: C:\My project\vista\test.aps*
      
        *char *pcAPSBenchmarkFiles  -  2 options for MODE_NORMAL and*
          *MODE_UPDATE_XML_FILE_TARIFFS_NODE:*
      
          ** Files separated by ? used to compare no matter the energy dataset.*
      
              *I.e: File1?File2?File3*
      
          ** Empty string. Files depending on the energy data will be used to*
            *compare (see eEnergyDataset).*
      
          *Ignored for MODE_CHECK_UTILITIES_VARIABLES.*
      
        *boost::python::object oStrInfoMessage [out]  -  Non error message to*
          *show after initialization. If not nullptr, it has a message and*
          *has to be deleted.*
      
        *boost:python::object oStrError [out]  -  error message if any.*
      
        *const EUnitsSystem eUnitsSystem  -*
      
          ** iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_METRIC (default)*
      
          ** iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_IP*
      
        *const ETEModes eMode  -  TariffsEngine engine mode.*
      
          ** iesve.TariffsEngine.EModes.MODE_NORMAL  -  normal usage (computing,*
            *getting/setting data...) (default)*
      
          ** iesve.TariffsEngine.EModes.MODE_UPDATE_XML_FILE_TARIFFS_NODE =*
            *mode for updating <Tariffs> node in an XML file.*
      
          ** iesve.TariffsEngine.EModes.MODE_CHECK_UTILITIES_VARIABLES = Checks*
            *whether the utilities variables exist or not. Call only Init() and*
            *DemandVariablesExists()*
      
        *const EEnergyDataset eEnergyDataset  -  dataset to compare to*
      
          ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_LOAD_STORED =*
            *the energy dataset will be loaded from the tariffs files.*
      
          ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_ASHRAE =*
            *baselines files b[nnn]_... if pcAPSFile is proposed (p_...)*
      
          ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_GENERIC =*
            *file(s) specified in pcAPSBenchmarkFiles, if not empty. (default)*
      
          ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_UK_PART_L2 =*
            *files n_...and r_... if pcAPSFile is actual (a_...)*
      
          ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_REFERENCE =*
            *reference file r_... if pcAPSFile is proposed (p_...)*
      
        *const ETEComputeCosts bComputeCosts  -  compute utilities or not.*
      
          ** COMPUTE_COSTS_NO = don't compute utilities.*
      
          ** COMPUTE_COSTS_YES = compute utilities. (default)*
      
      *Return Value:*
              *bool  -  TRUE if success.*
                 *FALSE if fail. See oStrError.*
      
      *Code sample:*
      
        *import iesve*
      
        *strProjectFolder = 'C:\MyProject'*
        *strAPSFile = 'C:\MyProject\vista\a_tariff analysis.aps'*
        *strAPSBenchmarkFiles = 'C:\MyProject\vista\prb.aps'*
        *strInfoMessage = iesve.TariffsEngine.String()*
        *strError = iesve.TariffsEngine.String()*
        *eUnitsSystem = iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_METRIC (default)*
                       *iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_IP*
        *eMode = iesve.TariffsEngine.EModes.MODE_NORMAL (default)*
                *iesve.TariffsEngine.EModes.MODE_UPDATE_XML_FILE_TARIFFS_NODE*
                *iesve.TariffsEngine.EModes.MODE_CHECK_UTILITIES_VARIABLES*
        *eEnergyDataset  =  iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_LOAD_STORED*
                           *iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_ASHRAE*
                           *iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_GENERIC (default)*
                           *iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_UK_PART_L2*
                           *iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_REFERENCE*
        *eComputeCosts = iesve.TariffsEngine.EComputeCosts.COMPUTE_COSTS_NO*
                        *iesve.TariffsEngine.EComputeCosts.COMPUTE_COSTS_YES (default)*
      
        *te = iesve.TariffsEngine(strProjectFolder, strAPSFile, strAPSBenchmarkFiles, strInfoMessage, strError, eUnitsSystem, eMode, eEnergyDataset, eComputeCosts)*
      
        *if (strError.Empty() == False) :*
          *print(strError.GetString())*
        *else:*
          *print("Init ok")*
      
          *if (strInfoMessage.Empty() == False) :*
          *print(strInfoMessage.GetString())*
   
      .. py:method:: AcceptChanges
      
         *Accepts changes done. It will save the results, selected tariffs...*
         
         *Parameters:*
           *void  -*
         
         *Return Value:*
           *string  -  Error message if any.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *error = te.AcceptChanges()*
         
           *if error:*
             *print(error)*
      
      .. py:method:: ComputeWithFlatRate
      
           *Computes the utility's costs using the flat rate.*
         
         *Parameters:*
            *const int iUtilityId  -*
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
            *const double dbFlatRate  -  flat rate to use to compute.*
              *If <0, the current utility's flat rate will be used.*
         
         *Return Value:*
           *void  -*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *te.ComputeWithFlatRate(iesve.TariffsEngine.EUtilities.COAL, .075)*
      
      .. py:method:: ComputeWithTariff
      
           *Computes the utility iUtilityId using supplier iSupplierId and*
         *tariff iTariffId.*
         
         *Parameters:*
            *const int iUtilityId  -*
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
           *const int iSupplierId  -  supplier id to be set. If not found,*
             *a Python exception is thrown.*
         
           *const int iTariffId  -  tariff id to be set. If not found or*
             *doesn't belong to iSupplierId, a Python exception is thrown.*
         
         *Return Value:*
           *void  -*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *te.ComputeWithTariff(iesve.TariffsEngine.EUtilities.OIL, 1, 3)*
      
      .. py:method:: GetBenchmarkNetCost
      
         *Returns the benchmark cost for a utility or total.*
         
         *Parameters:*
            *const int iUtilityId  -*
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
              *If -1, the total cost of all of the utilities summed up will be*
              *returned.*
         
         *Return Value:*
           *double  -  benchmark total cost.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *print(te.GetBenchmarkNetCost(iesve.TariffsEngine.EUtilities.GAS))*
      
      .. py:method:: GetDesignNetCost
      
         *Returns the design cost for a utility or total.*
         
         *Parameters:*
            *const int iUtilityId  -*
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
              *If -1, the total cost of all of the utilities summed up will be*
              *returned.*
         
         *Return Value:*
           *double  -  design total cost.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *print(te.GetDesignNetCost(iesve.TariffsEngine.EUtilities.GAS))*
      
      .. py:method:: GetEndUseCost
      
         *Returns the cost of an individual end use.*
         
         *Parameters:*
           *int filetype  -  0 if design, 1 if benchmark*
           *int iUtilityId  -*
             ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
             ** iesve.TariffsEngine.EUtilities.GAS for gas.*
             ** iesve.TariffsEngine.EUtilities.OIL for oil.*
             ** iesve.TariffsEngine.EUtilities.COAL for coal.*
             ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
             ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
           *iesve.EnergyUse use  -  The end use to obtain data for.*
         
         *Code sample:*
         
           *cost = te.GetEndUseCost(0, iesve.TariffsEngine.EUtilities.ELECTRICITY, iesve.EnergyUse.prm_interior_lighting)*
      
      .. py:method:: GetEndUseCosts
      
         *Returns the cost of multiple end uses.*
         
         *Parameters:*
           *int filetype  -  0 if design, 1 if benchmark*
           *int iUtilityId  -*
             ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
             ** iesve.TariffsEngine.EUtilities.GAS for gas.*
             ** iesve.TariffsEngine.EUtilities.OIL for oil.*
             ** iesve.TariffsEngine.EUtilities.COAL for coal.*
             ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
             ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
           *list[iesve.EnergyUse] use  -  The end uses to obtain data for.*
         
         *Code sample:*
         
           *cost = te.GetEndUseCosts(0, iesve.TariffsEngine.EUtilities.ELECTRICITY, [iesve.EnergyUse.prm_interior_lighting, iesve.EnergyUse.prm_space_heating])*
      
      .. py:method:: GetRatesTimeSeries
      
         *Returns a numpy object with the rates applied per time*
         *gap from iFirstDay to iLastDay for utility iUtility, that has*
         *previously to have been computed.*
         
         *Parameters:*
            *const int iUtility  -*
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
           *const int iFirstDay  -  First day whose rates per time gap*
             *will be stored: 1,...365, 366...*
             *If -1, it will be taken from the APS.*
             *Default value = -1*
             *iFirstDay<=iLastDay*
         
           *const int iLastDay  -  Last day whose rates per time gap*
             *will be stored: 1,...365, 366...*
             *If -1, it will be taken from the APS.*
             *Default value = -1*
             *iFirstDay<=iLastDay*
         
           *Return Value:*
             *boost::python::object  -  numpy object with the design demand*
               *cost per time gap.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *costsPerGap = te.GetRatesTimeSeries(iesve.TariffsEngine.EUtilities.OIL, 1, 365)*
         
           *print(str(costsPerGap.size) + " values retrieved")*
         
           *if costsPerGap.size>0:*
             *print(costsPerGap[0])*
      
      .. py:method:: GetSelectedCurrency
      
         *Gets a tuple with the selected currency data.*
         
         *Parameters:*
         
           *void  -*
         
         *Return Value:*
           *TTuple = tuple with the selected currency.*
             *I.e: ['Polish zloty', 'PLN', 'Poland', 'PLN']*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *currency = te.GetSelectedCurrency()*
         
           *print(currency)*
      
      .. py:method:: GetSuppliersForUtility
      
         *Gets a tuples list with the suppliers belonging to a utility.*
         
         *Parameters:*
         
           *const int iUtilityId  -  ETEUtility value:*
         
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
              ** iesve.TariffsEngine.EUtilities.MISCELLANEOUS for miscellaneous.*
              ** iesve.TariffsEngine.EUtilities.RENEWABLES for renewables.*
         
         *Return Value:*
           *TListString  -  tuples list with the suppliers belonging to the*
                           *utility iUtilityId. Each tuple has utility name*
                           *and id, that can be used for other functions.*
         
                           *I.e: [['Electricity Commercial Supplier', 1],*
                                 *['Electricity Domestic Supplier', 4]*
                                *]*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *suppliers = te.SuppliersForUtility(te.ETEUtility.GAS)*
         
           *print(suppliers)*
      
      .. py:method:: GetTariffCurrencyUnits
      
         *Returns a text with the symbol of the selected currency divided by*
         *the unit of the tariff whose id is iTariffId. I.e: $/T*
         
         *Parameters:*
           *const int iUtilityId  -  utility the tariff belongs to:*
         
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
         
            *It's not possible miscellaneous nor renewables.*
         
           *const int & iTariffId  -  tariff's id.*
         
         *Return Value:*
           *string  -  A text with the symbol of the selected currency divided*
             *by the unit of the tariff whose id is iTariffId. I.e: $/T*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *currencyUnits = te.GetTariffCurrencyUnits(iesve.TariffsEngine.EUtilities.ELECTRICITY, 4)*
         
           *print(currencyUnits)*
      
      .. py:method:: GetTariffName
      
         *Retrieves the name of the tariff whose id is iTariffId and belongs*
         *to the utility iUtilityId.*
         
         *Parameters:*
           *const int iUtilityId  -  ETEUtility value:*
         
              ** iesve.TariffsEngine.EUtilities.ELECTRICITY for electricity.*
              ** iesve.TariffsEngine.EUtilities.GAS for gas.*
              ** iesve.TariffsEngine.EUtilities.OIL for oil.*
              ** iesve.TariffsEngine.EUtilities.COAL for coal.*
         
            *It's not possible miscellaneous nor renewables.*
         
           *const int iTariffId  -  Tariff's id to check.*
         
         *Return Value:*
           *string = tariff name or "" if not found.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *name = te.GetTariffName(iesve.TariffsEngine.EUtilities.ELECTRICITY, 4)*
         
           *print(name)*
      
      .. py:method:: GetTariffsForSupplier
      
         *Gets a tuple with the tariffs belonging to a supplier and,*
         *optionally, a currency.*
         
         *Parameters:*
           *const int iSupplierId  -  supplier id whose tariffs will be retrieved.*
         
           *const string & strCurrencyId  -  currency id the tariffs will have*
             *to have in order to be retrieved. If "", no currency checking will*
             *be carried out. Default "".*
         
         *Return Value:*
           *TListString  -  tuples list with the tariffs belonging to the*
             *supplier whose id is strSupplierId and using the currency if*
             *specified.*
         
                           *I.e: [['Unrestricted Tariff (£ GBP)', 12],*
                                 *['Two Rate Tariff (£ GBP)', 13],*
                                 *['Economy-7 Tariff (£ GBP)', 21],*
                                 *['Unrestricted Tariff ($ USD)', 23],*
                                 *['Two Rate Tariff ($ USD)', 24],*
                                 *['Economy-7 Tariff ($ USD)', 28]*
                                *]*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *tariffs = te.GetTariffsForSupplier(2)*
         
           *print(tariffs)*
      
      .. py:method:: GetUtilitiesNamesAndIds
      
         *Gets a tuple with the utilities names and its ids.*
         
         *Parameters:*
         
           *void  -*
         
         *Return Value:*
           *TListString  -  list with the utilities.*
         
             *I.e: [['Electricity', 0], ['Gas', 1], ['Oil', 2], ['Coal', 3],*
                   *['Miscellaneous', 4], ['Renewables', 5]]*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *utilities = te.GetUtilitiesNamesAndIds()*
         
           *print(utilities)*
      
      .. py:property:: Improvement
      
         *Read only property containing the % of improvement.*
         
         *Parameters:*
           *void  -*
         
         *Return Value:*
           *double  -  % improvement.*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *print(te.Improvement)*
      
      .. py:method:: Init
      
         *Init the tariffs engine.*
         
         *Parameters:*
         
           *char *pcProjectFolder  -  MIT project folder ending by '' or not.*
             *I.e: C:\My project\*
         
           *char *pcAPSFile  -  APS file with path. I.e: C:\My project\vista\test.aps*
         
           *char *pcAPSBenchmarkFiles  -  2 options for MODE_NORMAL and*
             *MODE_UPDATE_XML_FILE_TARIFFS_NODE:*
         
             ** Files separated by ? used to compare no matter the energy dataset.*
         
                 *I.e: File1?File2?File3*
         
             ** Empty string. Files depending on the energy data will be used to*
               *compare (see eEnergyDataset).*
         
             *Ignored for MODE_CHECK_UTILITIES_VARIABLES.*
         
           *boost::python::object oStrInfoMessage [out]  -  Non error message to*
             *show after initialization. If not nullptr, it has a message and*
             *has to be deleted.*
         
           *boost:python::object oStrError [out]  -  error message if any.*
         
           *const EUnitsSystem eUnitsSystem  -*
         
             ** iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_METRIC (default)*
         
             ** iesve.TariffsEngine.EUnitsSystem.UNITS_SYSTEM_IP*
         
           *const ETEModes eMode  -  TariffsEngine engine mode.*
         
             ** iesve.TariffsEngine.EModes.MODE_NORMAL  -  normal usage (computing,*
               *getting/setting data...) (default)*
         
             ** iesve.TariffsEngine.EModes.MODE_UPDATE_XML_FILE_TARIFFS_NODE =*
               *mode for updating <Tariffs> node in an XML file.*
         
             ** iesve.TariffsEngine.EModes.MODE_CHECK_UTILITIES_VARIABLES = Checks*
               *whether the utilities variables exist or not. Call only Init() and*
               *DemandVariablesExists()*
         
           *const EEnergyDataset eEnergyDataset  -  dataset to compare to*
         
             ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_LOAD_STORED =*
               *the energy dataset will be loaded from the tariffs files.*
         
             ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_ASHRAE =*
               *baselines files b[nnn]_... if pcAPSFile is proposed (p_...)*
         
             ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_GENERIC =*
               *file(s) specified in pcAPSBenchmarkFiles, if not empty. (default)*
         
             ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_UK_PART_L2 =*
               *files n_...and r_... if pcAPSFile is actual (a_...)*
         
             ** iesve.TariffsEngine.EEnergyDataset.ENERGY_DATASET_REFERENCE =*
               *reference file r_... if pcAPSFile is proposed (p_...)*
         
           *const ETEComputeCosts bComputeCosts  -  compute utilities or not.*
         
             ** COMPUTE_COSTS_NO = don't compute utilities.*
         
             ** COMPUTE_COSTS_YES = compute utilities. (default)*
         
         *Return Value:*
                 *bool  -  TRUE if success.*
                    *FALSE if fail. See oStrError.*
         
         *Code sample:*
         
           *import iesve*
         
           *strProjectFolder = 'C:\MyProject'*
           *strAPSFile = 'C:\MyProject\vista\a_tariff analysis.aps'*
           *strAPSBenchmarkFiles = 'C:\MyProject\vista\prb.aps'*
           *strInfoMessage = iesve.TariffsEngine.String()*
           *strError = iesve.TariffsEngine.String()*
         
           *te = iesve.TariffsEngine()*
         
           *if (not te.Init(strProjectFolder, strAPSFile, strAPSBenchmarkFiles, strInfoMessage, strError)) :*
             *print(strError.GetString())*
           *else:*
             *print("Init ok")*
         
             *if (strInfoMessage.Empty() == False) :*
               *print(strInfoMessage.GetString())*
      
      .. py:method:: SetBenchmarkProfile
      
         *Sets the file(s) to compare with.*
         
         *Parameters:*
         
           *char *pcFiles  -  string with the files separated by ? or empty.*
             *I.e: "File1?File2?File3"*
         
         *Return Value:*
           *void  -*
         
         *Code sample:*
         
           *te = iesve.TariffsEngine(...)*
         
           *te.SetBenchmarkProfile("prb.aps?prb2.aps")*
      
   .. py:class:: TerminalUnitFanControl
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant_fan_control
         :classmethod:
         :type: iesve.TerminalUnitFanControl
      
         An instance of this class with:
         
         * a value of 0
         * a name of "constant_fan_control".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'constant_fan_control': iesve.TerminalUnitFanControl.constant_fan_control
             'two_speed_fan_control': iesve.TerminalUnitFanControl.two_speed_fan_control
             'variable_fan_control': iesve.TerminalUnitFanControl.variable_fan_control
            }
      
      .. py:property:: two_speed_fan_control
         :classmethod:
         :type: iesve.TerminalUnitFanControl
      
         An instance of this class with:
         
         * a value of 1
         * a name of "two_speed_fan_control".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.TerminalUnitFanControl.constant_fan_control
             1: iesve.TerminalUnitFanControl.two_speed_fan_control
             2: iesve.TerminalUnitFanControl.variable_fan_control
            }
      
      .. py:property:: variable_fan_control
         :classmethod:
         :type: iesve.TerminalUnitFanControl
      
         An instance of this class with:
         
         * a value of 2
         * a name of "variable_fan_control".
      
   .. py:class:: Title24ClimateZones
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'zone_1': iesve.Title24ClimateZones.zone_1
             'zone_2': iesve.Title24ClimateZones.zone_2
             'zone_3': iesve.Title24ClimateZones.zone_3
             'zone_4': iesve.Title24ClimateZones.zone_4
             'zone_5': iesve.Title24ClimateZones.zone_5
             'zone_6': iesve.Title24ClimateZones.zone_6
             'zone_7': iesve.Title24ClimateZones.zone_7
             'zone_8': iesve.Title24ClimateZones.zone_8
             'zone_9': iesve.Title24ClimateZones.zone_9
             'zone_10': iesve.Title24ClimateZones.zone_10
             'zone_11': iesve.Title24ClimateZones.zone_11
             'zone_12': iesve.Title24ClimateZones.zone_12
             'zone_13': iesve.Title24ClimateZones.zone_13
             'zone_14': iesve.Title24ClimateZones.zone_14
             'zone_15': iesve.Title24ClimateZones.zone_15
             'zone_16': iesve.Title24ClimateZones.zone_16
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.Title24ClimateZones.zone_1
             1: iesve.Title24ClimateZones.zone_2
             2: iesve.Title24ClimateZones.zone_3
             3: iesve.Title24ClimateZones.zone_4
             4: iesve.Title24ClimateZones.zone_5
             5: iesve.Title24ClimateZones.zone_6
             6: iesve.Title24ClimateZones.zone_7
             7: iesve.Title24ClimateZones.zone_8
             8: iesve.Title24ClimateZones.zone_9
             9: iesve.Title24ClimateZones.zone_10
             10: iesve.Title24ClimateZones.zone_11
             11: iesve.Title24ClimateZones.zone_12
             12: iesve.Title24ClimateZones.zone_13
             13: iesve.Title24ClimateZones.zone_14
             14: iesve.Title24ClimateZones.zone_15
             15: iesve.Title24ClimateZones.zone_16
            }
      
      .. py:property:: zone_1
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 0
         * a name of "zone_1".
      
      .. py:property:: zone_10
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 9
         * a name of "zone_10".
      
      .. py:property:: zone_11
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 10
         * a name of "zone_11".
      
      .. py:property:: zone_12
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 11
         * a name of "zone_12".
      
      .. py:property:: zone_13
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 12
         * a name of "zone_13".
      
      .. py:property:: zone_14
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 13
         * a name of "zone_14".
      
      .. py:property:: zone_15
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 14
         * a name of "zone_15".
      
      .. py:property:: zone_16
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 15
         * a name of "zone_16".
      
      .. py:property:: zone_2
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 1
         * a name of "zone_2".
      
      .. py:property:: zone_3
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 2
         * a name of "zone_3".
      
      .. py:property:: zone_4
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 3
         * a name of "zone_4".
      
      .. py:property:: zone_5
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 4
         * a name of "zone_5".
      
      .. py:property:: zone_6
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 5
         * a name of "zone_6".
      
      .. py:property:: zone_7
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 6
         * a name of "zone_7".
      
      .. py:property:: zone_8
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 7
         * a name of "zone_8".
      
      .. py:property:: zone_9
         :classmethod:
         :type: iesve.Title24ClimateZones
      
         An instance of this class with:
         
         * a value of 8
         * a name of "zone_9".
      
   .. py:class:: TransformerLosses
   
      *Interface for transformer losses data*
   
      .. py:method:: get_adjustment_factor
      
         *get_adjustment_factor() -> float*
         
         *Gets adjustment factor for electrical sources, based on efficiency.*
      
      .. py:method:: get_efficiency
      
         *get_efficiency() -> float*
         
         *Gets user defined transformer efficiency.*
      
      .. py:method:: is_set
      
         *get_adjustment_factor() -> float*
         
         *Gets adjustment factor for electrical sources, based on efficiency.*
      
   .. py:class:: UMLH
   
      *Interface for Unmet load hours*
   
      .. py:method:: get_unmet_hours
      
         *bool*
      
   .. py:class:: UnitType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: area_cm2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 129
         * a name of "area_cm2".
      
      .. py:property:: area_heating_cooling_power
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 127
         * a name of "area_heating_cooling_power".
      
      .. py:property:: area_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 10
         * a name of "area_m2".
      
      .. py:property:: circulation_loss
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 75
         * a name of "circulation_loss".
      
      .. py:property:: condensation
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 44
         * a name of "condensation".
      
      .. py:property:: condensation_rate
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 43
         * a name of "condensation_rate".
      
      .. py:property:: condensation_rate_kg_m2_second
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 117
         * a name of "condensation_rate_kg_m2_second".
      
      .. py:property:: conductance
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 33
         * a name of "conductance".
      
      .. py:property:: conductivity
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 30
         * a name of "conductivity".
      
      .. py:property:: coordinates
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 9
         * a name of "coordinates".
      
      .. py:property:: cost_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 60
         * a name of "cost_area".
      
      .. py:property:: crack_flow
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 51
         * a name of "crack_flow".
      
      .. py:property:: degrees
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 109
         * a name of "degrees".
      
      .. py:property:: density
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 28
         * a name of "density".
      
      .. py:property:: dhw_consumption_hour_per_person_uk
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 64
         * a name of "dhw_consumption_hour_per_person_uk".
      
      .. py:property:: dhw_consumption_hour_per_person_us
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 65
         * a name of "dhw_consumption_hour_per_person_us".
      
      .. py:property:: dhw_consumption_per_hour_us
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 98
         * a name of "dhw_consumption_per_hour_us".
      
      .. py:property:: distance_cm
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "distance_cm".
      
      .. py:property:: distance_km
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "distance_km".
      
      .. py:property:: distance_m
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "distance_m".
      
      .. py:property:: distance_mm
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "distance_mm".
      
      .. py:property:: electrical_power_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 35
         * a name of "electrical_power_area".
      
      .. py:property:: electrical_power_length
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 99
         * a name of "electrical_power_length".
      
      .. py:property:: energy_consumption_per_hour
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 85
         * a name of "energy_consumption_per_hour".
      
      .. py:property:: energy_joules
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 22
         * a name of "energy_joules".
      
      .. py:property:: enthalpy
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 27
         * a name of "enthalpy".
      
      .. py:property:: enthalpy_difference
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 91
         * a name of "enthalpy_difference".
      
      .. py:property:: enthalpy_kj
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 50
         * a name of "enthalpy_kj".
      
      .. py:property:: flow_gpm_kbtu_per_hour
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 94
         * a name of "flow_gpm_kbtu_per_hour".
      
      .. py:property:: flow_litres_per_second_gpm
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 86
         * a name of "flow_litres_per_second_gpm".
      
      .. py:property:: flow_per_km
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 87
         * a name of "flow_per_km".
      
      .. py:property:: flow_per_person
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 97
         * a name of "flow_per_person".
      
      .. py:property:: formatting_only
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 61
         * a name of "formatting_only".
      
      .. py:property:: gigajoules_ton_hours
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 119
         * a name of "gigajoules_ton_hours".
      
      .. py:property:: gigajoules_ton_kwh
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 120
         * a name of "gigajoules_ton_kwh".
      
      .. py:property:: heat_transfer_coefficient
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 32
         * a name of "heat_transfer_coefficient".
      
      .. py:property:: heatflux_w
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 8
         * a name of "heatflux_w".
      
      .. py:property:: heatflux_watts
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 66
         * a name of "heatflux_watts".
      
      .. py:property:: heatflux_wm2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 7
         * a name of "heatflux_wm2".
      
      .. py:property:: heating_cooling_power_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 39
         * a name of "heating_cooling_power_area".
      
      .. py:property:: heating_cooling_power_kw
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 36
         * a name of "heating_cooling_power_kw".
      
      .. py:property:: heating_cooling_power_kw_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 126
         * a name of "heating_cooling_power_kw_area".
      
      .. py:property:: heating_cooling_power_per_person
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 13
         * a name of "heating_cooling_power_per_person".
      
      .. py:property:: heating_cooling_power_per_person_short
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 14
         * a name of "heating_cooling_power_per_person_short".
      
      .. py:property:: heating_cooling_power_person
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 38
         * a name of "heating_cooling_power_person".
      
      .. py:property:: heating_cooling_power_w
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 37
         * a name of "heating_cooling_power_w".
      
      .. py:property:: heating_cooling_power_w_display_kw
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 62
         * a name of "heating_cooling_power_w_display_kw".
      
      .. py:property:: hourly_volumetric_flow
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 78
         * a name of "hourly_volumetric_flow".
      
      .. py:property:: humidity_ratio
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 23
         * a name of "humidity_ratio".
      
      .. py:property:: inverse_area_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 102
         * a name of "inverse_area_m2".
      
      .. py:property:: inverse_k
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 89
         * a name of "inverse_k".
      
      .. py:property:: inverse_k2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 90
         * a name of "inverse_k2".
      
      .. py:property:: inverse_k3
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 95
         * a name of "inverse_k3".
      
      .. py:property:: inverse_length
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 80
         * a name of "inverse_length".
      
      .. py:property:: inverse_per_energy_consumption_kwh
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 103
         * a name of "inverse_per_energy_consumption_kwh".
      
      .. py:property:: joules_ton_hours
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 118
         * a name of "joules_ton_hours".
      
      .. py:property:: kwh_m2_to_kbtu_ft2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 101
         * a name of "kwh_m2_to_kbtu_ft2".
      
      .. py:property:: land_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 112
         * a name of "land_area".
      
      .. py:property:: land_density
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 113
         * a name of "land_density".
      
      .. py:property:: layer_thick
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 16
         * a name of "layer_thick".
      
      .. py:property:: length_m_display_mm
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 104
         * a name of "length_m_display_mm".
      
      .. py:property:: length_m_to_in
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 58
         * a name of "length_m_to_in".
      
      .. py:property:: line_loss
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 69
         * a name of "line_loss".
      
      .. py:property:: linear_heat_transfer_coefficient
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 93
         * a name of "linear_heat_transfer_coefficient".
      
      .. py:property:: lumens
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 45
         * a name of "lumens".
      
      .. py:property:: luminance
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 49
         * a name of "luminance".
      
      .. py:property:: luminous_efficacy_watt
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 57
         * a name of "luminous_efficacy_watt".
      
      .. py:property:: luminous_intensity
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 48
         * a name of "luminous_intensity".
      
      .. py:property:: luminous_power_density
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 56
         * a name of "luminous_power_density".
      
      .. py:property:: lux_lumens_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 46
         * a name of "lux_lumens_m2".
      
      .. py:property:: mass_flow
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 26
         * a name of "mass_flow".
      
      .. py:property:: mass_flow_per_hour
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 84
         * a name of "mass_flow_per_hour".
      
      .. py:property:: mass_kg
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 19
         * a name of "mass_kg".
      
      .. py:property:: mass_kg_per_m
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 114
         * a name of "mass_kg_per_m".
      
      .. py:property:: mass_tonne_short_ton
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 105
         * a name of "mass_tonne_short_ton".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_conversion': iesve.UnitType.no_conversion
             'distance_km': iesve.UnitType.distance_km
             'distance_m': iesve.UnitType.distance_m
             'distance_cm': iesve.UnitType.distance_cm
             'distance_mm': iesve.UnitType.distance_mm
             'volume_flow_rate_m3_per_person': iesve.UnitType.volume_flow_rate_m3_per_person
             'volume_flow_rate_litres_per_person': iesve.UnitType.volume_flow_rate_litres_per_person
             'temperature': iesve.UnitType.temperature
             'heatflux_wm2': iesve.UnitType.heatflux_wm2
             'heatflux_w': iesve.UnitType.heatflux_w
             'coordinates': iesve.UnitType.coordinates
             'area_m2': iesve.UnitType.area_m2
             'volume_m3': iesve.UnitType.volume_m3
             'heating_cooling_power_kw': iesve.UnitType.heating_cooling_power_kw
             'heating_cooling_power_per_person': iesve.UnitType.heating_cooling_power_per_person
             'heating_cooling_power_per_person_short': iesve.UnitType.heating_cooling_power_per_person_short
             'volume_flow_rate_litres_per_person_m2': iesve.UnitType.volume_flow_rate_litres_per_person_m2
             'layer_thick': iesve.UnitType.layer_thick
             'volume_litres': iesve.UnitType.volume_litres
             'speed_metres_per_second': iesve.UnitType.speed_metres_per_second
             'mass_kg': iesve.UnitType.mass_kg
             'temperature_difference_positive': iesve.UnitType.temperature_difference_positive
             'temperature_difference_positive_negative': iesve.UnitType.temperature_difference_positive_negative
             'energy_joules': iesve.UnitType.energy_joules
             'humidity_ratio': iesve.UnitType.humidity_ratio
             'pressure': iesve.UnitType.pressure
             'volume_flow': iesve.UnitType.volume_flow
             'mass_flow': iesve.UnitType.mass_flow
             'enthalpy': iesve.UnitType.enthalpy
             'density': iesve.UnitType.density
             'specific_heat_capacity': iesve.UnitType.specific_heat_capacity
             'conductivity': iesve.UnitType.conductivity
             'heat_transfer_coefficient': iesve.UnitType.heat_transfer_coefficient
             'conductance': iesve.UnitType.conductance
             'resistance': iesve.UnitType.resistance
             'electrical_power_area': iesve.UnitType.electrical_power_area
             'heating_cooling_power_w': iesve.UnitType.heating_cooling_power_w
             'heating_cooling_power_person': iesve.UnitType.heating_cooling_power_person
             'heating_cooling_power_area': iesve.UnitType.heating_cooling_power_area
             'solar_flux': iesve.UnitType.solar_flux
             'occupancy_density': iesve.UnitType.occupancy_density
             'volume_flow_area': iesve.UnitType.volume_flow_area
             'condensation_rate': iesve.UnitType.condensation_rate
             'condensation': iesve.UnitType.condensation
             'lumens': iesve.UnitType.lumens
             'lux_lumens_m2': iesve.UnitType.lux_lumens_m2
             'viscosity': iesve.UnitType.viscosity
             'luminous_intensity': iesve.UnitType.luminous_intensity
             'luminance': iesve.UnitType.luminance
             'enthalpy_kj': iesve.UnitType.enthalpy_kj
             'crack_flow': iesve.UnitType.crack_flow
             'pressure_in_mercury': iesve.UnitType.pressure_in_mercury
             'pressure_in_water': iesve.UnitType.pressure_in_water
             'vapour_permeability': iesve.UnitType.vapour_permeability
             'vapour_permeance': iesve.UnitType.vapour_permeance
             'luminous_power_density': iesve.UnitType.luminous_power_density
             'luminous_efficacy_watt': iesve.UnitType.luminous_efficacy_watt
             'length_m_to_in': iesve.UnitType.length_m_to_in
             'volume_flow_rate_m3_per_person_cfm': iesve.UnitType.volume_flow_rate_m3_per_person_cfm
             'cost_area': iesve.UnitType.cost_area
             'formatting_only': iesve.UnitType.formatting_only
             'heating_cooling_power_w_display_kw': iesve.UnitType.heating_cooling_power_w_display_kw
             'specific_fan_power': iesve.UnitType.specific_fan_power
             'dhw_consumption_hour_per_person_uk': iesve.UnitType.dhw_consumption_hour_per_person_uk
             'dhw_consumption_hour_per_person_us': iesve.UnitType.dhw_consumption_hour_per_person_us
             'heatflux_watts': iesve.UnitType.heatflux_watts
             'thermal_capacity_kjm2k': iesve.UnitType.thermal_capacity_kjm2k
             'tank_loss': iesve.UnitType.tank_loss
             'line_loss': iesve.UnitType.line_loss
             'second_order_heat_loss': iesve.UnitType.second_order_heat_loss
             'volume_flow_rate_litres_per_hour_m2': iesve.UnitType.volume_flow_rate_litres_per_hour_m2
             'temperature_coefficient': iesve.UnitType.temperature_coefficient
             'volume_litres_uk_gallons': iesve.UnitType.volume_litres_uk_gallons
             'volume_flow_rate_litres_per_hour_gallon': iesve.UnitType.volume_flow_rate_litres_per_hour_gallon
             'circulation_loss': iesve.UnitType.circulation_loss
             'storage_loss_us_gallon': iesve.UnitType.storage_loss_us_gallon
             'volume_litres_per_us_gallons': iesve.UnitType.volume_litres_per_us_gallons
             'hourly_volumetric_flow': iesve.UnitType.hourly_volumetric_flow
             'parts_per_million': iesve.UnitType.parts_per_million
             'inverse_length': iesve.UnitType.inverse_length
             'pressure_velocity_1': iesve.UnitType.pressure_velocity_1
             'pressure_velocity_2': iesve.UnitType.pressure_velocity_2
             'pressure_velocity_3': iesve.UnitType.pressure_velocity_3
             'mass_flow_per_hour': iesve.UnitType.mass_flow_per_hour
             'energy_consumption_per_hour': iesve.UnitType.energy_consumption_per_hour
             'flow_litres_per_second_gpm': iesve.UnitType.flow_litres_per_second_gpm
             'flow_per_km': iesve.UnitType.flow_per_km
             'watts_per_flow': iesve.UnitType.watts_per_flow
             'inverse_k': iesve.UnitType.inverse_k
             'inverse_k2': iesve.UnitType.inverse_k2
             'enthalpy_difference': iesve.UnitType.enthalpy_difference
             'volume_m3_us_gallon': iesve.UnitType.volume_m3_us_gallon
             'linear_heat_transfer_coefficient': iesve.UnitType.linear_heat_transfer_coefficient
             'flow_gpm_kbtu_per_hour': iesve.UnitType.flow_gpm_kbtu_per_hour
             'inverse_k3': iesve.UnitType.inverse_k3
             'sbem_heat_transfer_rate': iesve.UnitType.sbem_heat_transfer_rate
             'flow_per_person': iesve.UnitType.flow_per_person
             'dhw_consumption_per_hour_us': iesve.UnitType.dhw_consumption_per_hour_us
             'electrical_power_length': iesve.UnitType.electrical_power_length
             'volume_flow_rate_litres_per_second_m2_facade': iesve.UnitType.volume_flow_rate_litres_per_second_m2_facade
             'kwh_m2_to_kbtu_ft2': iesve.UnitType.kwh_m2_to_kbtu_ft2
             'inverse_area_m2': iesve.UnitType.inverse_area_m2
             'inverse_per_energy_consumption_kwh': iesve.UnitType.inverse_per_energy_consumption_kwh
             'length_m_display_mm': iesve.UnitType.length_m_display_mm
             'mass_tonne_short_ton': iesve.UnitType.mass_tonne_short_ton
             'wind_speed': iesve.UnitType.wind_speed
             'volume_flow_ach': iesve.UnitType.volume_flow_ach
             'occupancy_people': iesve.UnitType.occupancy_people
             'degrees': iesve.UnitType.degrees
             'percent': iesve.UnitType.percent
             'volume_flow_air_changes_per_hour_short': iesve.UnitType.volume_flow_air_changes_per_hour_short
             'land_area': iesve.UnitType.land_area
             'land_density': iesve.UnitType.land_density
             'mass_kg_per_m': iesve.UnitType.mass_kg_per_m
             'volume_flow_m3_per_hour_per_m2_of_envelope': iesve.UnitType.volume_flow_m3_per_hour_per_m2_of_envelope
             'pressure_inches_of_water_column': iesve.UnitType.pressure_inches_of_water_column
             'condensation_rate_kg_m2_second': iesve.UnitType.condensation_rate_kg_m2_second
             'joules_ton_hours': iesve.UnitType.joules_ton_hours
             'gigajoules_ton_hours': iesve.UnitType.gigajoules_ton_hours
             'gigajoules_ton_kwh': iesve.UnitType.gigajoules_ton_kwh
             'occupany_people_per_100_m2': iesve.UnitType.occupany_people_per_100_m2
             'volume_flow_per_unit': iesve.UnitType.volume_flow_per_unit
             'volume_flow_equals_supply_air': iesve.UnitType.volume_flow_equals_supply_air
             'volume_flow_greater_than_supply_air': iesve.UnitType.volume_flow_greater_than_supply_air
             'volume_flow_percentage_above_supply_air': iesve.UnitType.volume_flow_percentage_above_supply_air
             'heating_cooling_power_kw_area': iesve.UnitType.heating_cooling_power_kw_area
             'area_heating_cooling_power': iesve.UnitType.area_heating_cooling_power
             'suspended_solid': iesve.UnitType.suspended_solid
             'area_cm2': iesve.UnitType.area_cm2
             'temperature_half_ip': iesve.UnitType.temperature_half_ip
            }
      
      .. py:property:: no_conversion
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of -1
         * a name of "no_conversion".
      
      .. py:property:: occupancy_density
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 41
         * a name of "occupancy_density".
      
      .. py:property:: occupancy_people
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 108
         * a name of "occupancy_people".
      
      .. py:property:: occupany_people_per_100_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 121
         * a name of "occupany_people_per_100_m2".
      
      .. py:property:: parts_per_million
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 79
         * a name of "parts_per_million".
      
      .. py:property:: percent
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 110
         * a name of "percent".
      
      .. py:property:: pressure
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 24
         * a name of "pressure".
      
      .. py:property:: pressure_in_mercury
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 52
         * a name of "pressure_in_mercury".
      
      .. py:property:: pressure_in_water
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 53
         * a name of "pressure_in_water".
      
      .. py:property:: pressure_inches_of_water_column
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 116
         * a name of "pressure_inches_of_water_column".
      
      .. py:property:: pressure_velocity_1
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 81
         * a name of "pressure_velocity_1".
      
      .. py:property:: pressure_velocity_2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 82
         * a name of "pressure_velocity_2".
      
      .. py:property:: pressure_velocity_3
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 83
         * a name of "pressure_velocity_3".
      
      .. py:property:: resistance
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 34
         * a name of "resistance".
      
      .. py:property:: sbem_heat_transfer_rate
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 96
         * a name of "sbem_heat_transfer_rate".
      
      .. py:property:: second_order_heat_loss
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 70
         * a name of "second_order_heat_loss".
      
      .. py:property:: solar_flux
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 40
         * a name of "solar_flux".
      
      .. py:property:: specific_fan_power
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 63
         * a name of "specific_fan_power".
      
      .. py:property:: specific_heat_capacity
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 29
         * a name of "specific_heat_capacity".
      
      .. py:property:: speed_metres_per_second
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 18
         * a name of "speed_metres_per_second".
      
      .. py:property:: storage_loss_us_gallon
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 76
         * a name of "storage_loss_us_gallon".
      
      .. py:property:: suspended_solid
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 128
         * a name of "suspended_solid".
      
      .. py:property:: tank_loss
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 68
         * a name of "tank_loss".
      
      .. py:property:: temperature
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 6
         * a name of "temperature".
      
      .. py:property:: temperature_coefficient
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 72
         * a name of "temperature_coefficient".
      
      .. py:property:: temperature_difference_positive
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 20
         * a name of "temperature_difference_positive".
      
      .. py:property:: temperature_difference_positive_negative
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 21
         * a name of "temperature_difference_positive_negative".
      
      .. py:property:: temperature_half_ip
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 130
         * a name of "temperature_half_ip".
      
      .. py:property:: thermal_capacity_kjm2k
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 67
         * a name of "thermal_capacity_kjm2k".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.UnitType.no_conversion
             0: iesve.UnitType.distance_km
             1: iesve.UnitType.distance_m
             2: iesve.UnitType.distance_cm
             3: iesve.UnitType.distance_mm
             4: iesve.UnitType.volume_flow_rate_m3_per_person
             5: iesve.UnitType.volume_flow_rate_litres_per_person
             6: iesve.UnitType.temperature
             7: iesve.UnitType.heatflux_wm2
             8: iesve.UnitType.heatflux_w
             9: iesve.UnitType.coordinates
             10: iesve.UnitType.area_m2
             11: iesve.UnitType.volume_m3
             12: iesve.UnitType.heating_cooling_power_kw
             13: iesve.UnitType.heating_cooling_power_per_person
             14: iesve.UnitType.heating_cooling_power_per_person_short
             15: iesve.UnitType.volume_flow_rate_litres_per_person_m2
             16: iesve.UnitType.layer_thick
             17: iesve.UnitType.volume_litres
             18: iesve.UnitType.speed_metres_per_second
             19: iesve.UnitType.mass_kg
             20: iesve.UnitType.temperature_difference_positive
             21: iesve.UnitType.temperature_difference_positive_negative
             22: iesve.UnitType.energy_joules
             23: iesve.UnitType.humidity_ratio
             24: iesve.UnitType.pressure
             25: iesve.UnitType.volume_flow
             26: iesve.UnitType.mass_flow
             27: iesve.UnitType.enthalpy
             28: iesve.UnitType.density
             29: iesve.UnitType.specific_heat_capacity
             30: iesve.UnitType.conductivity
             32: iesve.UnitType.heat_transfer_coefficient
             33: iesve.UnitType.conductance
             34: iesve.UnitType.resistance
             35: iesve.UnitType.electrical_power_area
             36: iesve.UnitType.heating_cooling_power_kw
             37: iesve.UnitType.heating_cooling_power_w
             38: iesve.UnitType.heating_cooling_power_person
             39: iesve.UnitType.heating_cooling_power_area
             40: iesve.UnitType.solar_flux
             41: iesve.UnitType.occupancy_density
             42: iesve.UnitType.volume_flow_area
             43: iesve.UnitType.condensation_rate
             44: iesve.UnitType.condensation
             45: iesve.UnitType.lumens
             46: iesve.UnitType.lux_lumens_m2
             47: iesve.UnitType.viscosity
             48: iesve.UnitType.luminous_intensity
             49: iesve.UnitType.luminance
             50: iesve.UnitType.enthalpy_kj
             51: iesve.UnitType.crack_flow
             52: iesve.UnitType.pressure_in_mercury
             53: iesve.UnitType.pressure_in_water
             54: iesve.UnitType.vapour_permeability
             55: iesve.UnitType.vapour_permeance
             56: iesve.UnitType.luminous_power_density
             57: iesve.UnitType.luminous_efficacy_watt
             58: iesve.UnitType.length_m_to_in
             59: iesve.UnitType.volume_flow_rate_m3_per_person_cfm
             60: iesve.UnitType.cost_area
             61: iesve.UnitType.formatting_only
             62: iesve.UnitType.heating_cooling_power_w_display_kw
             63: iesve.UnitType.specific_fan_power
             64: iesve.UnitType.dhw_consumption_hour_per_person_uk
             65: iesve.UnitType.dhw_consumption_hour_per_person_us
             66: iesve.UnitType.heatflux_watts
             67: iesve.UnitType.thermal_capacity_kjm2k
             68: iesve.UnitType.tank_loss
             69: iesve.UnitType.line_loss
             70: iesve.UnitType.second_order_heat_loss
             71: iesve.UnitType.volume_flow_rate_litres_per_hour_m2
             72: iesve.UnitType.temperature_coefficient
             73: iesve.UnitType.volume_litres_uk_gallons
             74: iesve.UnitType.volume_flow_rate_litres_per_hour_gallon
             75: iesve.UnitType.circulation_loss
             76: iesve.UnitType.storage_loss_us_gallon
             77: iesve.UnitType.volume_litres_per_us_gallons
             78: iesve.UnitType.hourly_volumetric_flow
             79: iesve.UnitType.parts_per_million
             80: iesve.UnitType.inverse_length
             81: iesve.UnitType.pressure_velocity_1
             82: iesve.UnitType.pressure_velocity_2
             83: iesve.UnitType.pressure_velocity_3
             84: iesve.UnitType.mass_flow_per_hour
             85: iesve.UnitType.energy_consumption_per_hour
             86: iesve.UnitType.flow_litres_per_second_gpm
             87: iesve.UnitType.flow_per_km
             88: iesve.UnitType.watts_per_flow
             89: iesve.UnitType.inverse_k
             90: iesve.UnitType.inverse_k2
             91: iesve.UnitType.enthalpy_difference
             92: iesve.UnitType.volume_m3_us_gallon
             93: iesve.UnitType.linear_heat_transfer_coefficient
             94: iesve.UnitType.flow_gpm_kbtu_per_hour
             95: iesve.UnitType.inverse_k3
             96: iesve.UnitType.sbem_heat_transfer_rate
             97: iesve.UnitType.flow_per_person
             98: iesve.UnitType.dhw_consumption_per_hour_us
             99: iesve.UnitType.electrical_power_length
             100: iesve.UnitType.volume_flow_rate_litres_per_second_m2_facade
             101: iesve.UnitType.kwh_m2_to_kbtu_ft2
             102: iesve.UnitType.inverse_area_m2
             103: iesve.UnitType.inverse_per_energy_consumption_kwh
             104: iesve.UnitType.length_m_display_mm
             105: iesve.UnitType.mass_tonne_short_ton
             106: iesve.UnitType.wind_speed
             107: iesve.UnitType.volume_flow_ach
             108: iesve.UnitType.occupancy_people
             109: iesve.UnitType.degrees
             110: iesve.UnitType.percent
             111: iesve.UnitType.volume_flow_air_changes_per_hour_short
             112: iesve.UnitType.land_area
             113: iesve.UnitType.land_density
             114: iesve.UnitType.mass_kg_per_m
             115: iesve.UnitType.volume_flow_m3_per_hour_per_m2_of_envelope
             116: iesve.UnitType.pressure_inches_of_water_column
             117: iesve.UnitType.condensation_rate_kg_m2_second
             118: iesve.UnitType.joules_ton_hours
             119: iesve.UnitType.gigajoules_ton_hours
             120: iesve.UnitType.gigajoules_ton_kwh
             121: iesve.UnitType.occupany_people_per_100_m2
             122: iesve.UnitType.volume_flow_per_unit
             123: iesve.UnitType.volume_flow_equals_supply_air
             124: iesve.UnitType.volume_flow_greater_than_supply_air
             125: iesve.UnitType.volume_flow_percentage_above_supply_air
             126: iesve.UnitType.heating_cooling_power_kw_area
             127: iesve.UnitType.area_heating_cooling_power
             128: iesve.UnitType.suspended_solid
             129: iesve.UnitType.area_cm2
             130: iesve.UnitType.temperature_half_ip
            }
      
      .. py:property:: vapour_permeability
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 54
         * a name of "vapour_permeability".
      
      .. py:property:: vapour_permeance
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 55
         * a name of "vapour_permeance".
      
      .. py:property:: viscosity
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 47
         * a name of "viscosity".
      
      .. py:property:: volume_flow
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 25
         * a name of "volume_flow".
      
      .. py:property:: volume_flow_ach
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 107
         * a name of "volume_flow_ach".
      
      .. py:property:: volume_flow_air_changes_per_hour_short
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 111
         * a name of "volume_flow_air_changes_per_hour_short".
      
      .. py:property:: volume_flow_area
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 42
         * a name of "volume_flow_area".
      
      .. py:property:: volume_flow_equals_supply_air
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 123
         * a name of "volume_flow_equals_supply_air".
      
      .. py:property:: volume_flow_greater_than_supply_air
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 124
         * a name of "volume_flow_greater_than_supply_air".
      
      .. py:property:: volume_flow_m3_per_hour_per_m2_of_envelope
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 115
         * a name of "volume_flow_m3_per_hour_per_m2_of_envelope".
      
      .. py:property:: volume_flow_per_unit
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 122
         * a name of "volume_flow_per_unit".
      
      .. py:property:: volume_flow_percentage_above_supply_air
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 125
         * a name of "volume_flow_percentage_above_supply_air".
      
      .. py:property:: volume_flow_rate_litres_per_hour_gallon
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 74
         * a name of "volume_flow_rate_litres_per_hour_gallon".
      
      .. py:property:: volume_flow_rate_litres_per_hour_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 71
         * a name of "volume_flow_rate_litres_per_hour_m2".
      
      .. py:property:: volume_flow_rate_litres_per_person
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 5
         * a name of "volume_flow_rate_litres_per_person".
      
      .. py:property:: volume_flow_rate_litres_per_person_m2
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 15
         * a name of "volume_flow_rate_litres_per_person_m2".
      
      .. py:property:: volume_flow_rate_litres_per_second_m2_facade
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 100
         * a name of "volume_flow_rate_litres_per_second_m2_facade".
      
      .. py:property:: volume_flow_rate_m3_per_person
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 4
         * a name of "volume_flow_rate_m3_per_person".
      
      .. py:property:: volume_flow_rate_m3_per_person_cfm
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 59
         * a name of "volume_flow_rate_m3_per_person_cfm".
      
      .. py:property:: volume_litres
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 17
         * a name of "volume_litres".
      
      .. py:property:: volume_litres_per_us_gallons
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 77
         * a name of "volume_litres_per_us_gallons".
      
      .. py:property:: volume_litres_uk_gallons
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 73
         * a name of "volume_litres_uk_gallons".
      
      .. py:property:: volume_m3
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 11
         * a name of "volume_m3".
      
      .. py:property:: volume_m3_us_gallon
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 92
         * a name of "volume_m3_us_gallon".
      
      .. py:property:: watts_per_flow
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 88
         * a name of "watts_per_flow".
      
      .. py:property:: wind_speed
         :classmethod:
         :type: iesve.UnitType
      
         An instance of this class with:
         
         * a value of 106
         * a name of "wind_speed".
      
   .. py:class:: VEAdjacency
   
      *Adjacency.Section of internal wall that joins two rooms.*
      *Resides inside (parented by) a surface (a single surface can have*
      *multiple adjacencies if it sits between multiple rooms.*
   
      .. py:method:: get_construction
      
         *get_construction( (VEAdjacency)arg1) -> str :*
             *get_construction()  ->  constructionId*
             **
             *Returns the construction ID (string) used in the adjacency*
      
      .. py:method:: get_properties
      
         *get_properties( (VEAdjacency)arg1) -> dict :*
             *get_properties()  ->  Dictionary (property)*
             **
             *Returns assorted properties of the adjacency*
              *- surface_index (int, id) the index of the surface in the adjacent room*
              *- aps_handle (int, id) the aps handle used by the results reader*
              *- body_id (string, id) the ID of the room on the other side of adjacency*
              *- distance (meters) the distance between the two rooms.*
             *The following area related properties are also returned:*
              *- gross (m2) gross area including all openings*
              *- window (m2) total glazed opening area in adjacency*
              *- hole (m2) total hole opening area*
              *- door (m2) total door area in adjacency.*
      
   .. py:class:: VEApacheSystem
   
      *Apache System object.*
   
      .. py:method:: air_supply
      
         *Air supply data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"condition":            supply condition*
                 *"profile" (optional):   profile ID*
                 *"OA_max_flow":          maximum outside air supply flow rate (l/s)*
                 *"temperature_difference": air supply temperature difference (0 for no sizing) (K)*
                 *"cooling_max_flow":     maximum cooling air supply flow rate (l/s)*
      
      .. py:method:: apply_ncm
      
         *apply_ncm()*
         
         *Applies NCM wizard data to the system.*
         *Call this after setting NCM wizard data to update the system itself.*
         *If you do not call this, changes will be made only in the wizard and not the system.*
      
      .. py:method:: auxiliary_energy
      
         *Auxiliary energy data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"method":               Auxiliary energy method*
                 *"SFP" (optional):       Specific fan power (SFP) (W/l/s)*
                 *"AEV":                  Energy value (W/m^2)*
                 *"equivalent_energy":    Equivalent energy in kWh/m^2/y, for 3255hrs operation*
                 *"fan_fraction":         Auxiliary energy fan fraction*
                 *"off_schedule_AEV":     Off-schedule heating/cooling AEV (W/m^2)*
                 *"air_supply_mechanism" (optional):      Air supply mechanism*
      
      .. py:method:: bivalent_systems_ncm
      
         *Bivalent systems NCM data for the Apache system.*
         *Returns:*
                  *Dictionary with the following keys:*
                 *"load_for_primary_system":              % Load for the primary system*
                 *"overall_seasonal_efficiency":          Overall seasonal efficiency*
                 *"systems":              List of dictionaries of system data (one for each system)*
         
                  *System data dictionary contains the following keys:*
                 *"heat_source":          Heat source*
                 *"meter":                Energy meter*
                 *"gen_seff":             GEN SEFF (fraction)*
                 *"load":         % Load*
      
      .. py:method:: control
      
         *Control data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"master_zone": master zone (room ID)*
      
      .. py:method:: cooling
      
         *Cooling data for the Apache system.*
         *Parameters:*
         *show_ncm (optional): Whether to show NCM specific data in the output*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"cool_vent_mechanism":  Cooling/ventilation mechanism*
                 *"fuel" (optional):      Fuel*
                 *"meter_branch" (optional): Meter branch*
                 *"SEER":                 Seasonal energy efficiency ratio (kW/kW)*
                 *"del_eff":              Delivery efficiency*
                 *"SSEER":                Seasonal system energy efficiency ratio (kW/kW)*
                 *"gen_size":             Generator size (kW)*
                 *"has_absorption_chiller": Whether the system has an absorption chiller*
                 *"pump_and_fan_power_perc": Pump & fan power (% of rejected heat)*
                 *"nominal_eer": (Optional) Nominal EER (kW/kW)*
                 *"free_cooling": (Optional) Changeover mixed mode free cooling*
      
      .. py:method:: cooling_ncm
      
         *Cooling NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"type":         Cooling type*
                 *"power":                Cooling power*
                 *"chiller_meter":                Chiller meter*
                 *"generator_seasonal_eer_known":         Do you know the generator seasonal EER?*
                 *"generator_seasonal_eer":               Seasonal EER*
                 *"default_generator_seasonal_eer":               Default seasonal EER value*
                 *"qualify_for_eca":              Does it qualify for ECAs?*
                 *"generator_nominal_eer_known":          Do you know the generator nominal EER?*
                 *"generator_nominal_eer":                Nominal EER*
                 *"default_generator_nominal_eer":                Default nominal EER value*
                 *"mixed_mode":           Mixed mode operation strategy (SBEM only)*
      
      .. py:method:: default
      
         *ID of the default Apache system.*
      
      .. py:method:: fuel_name
      
         *fuel_name(fuel_id) -> string*
         
         *Gets the fuel name for the input fuel ID.*
         *Args:*
                 *fuel_id (int): the ID of the fuel*
         *Returns:*
                 *Name of fuel*
         *Raises:*
                 *ValueError: if no name is found for the input fuel ID*
                 *RuntimeError: in the case of an internal data handling error*
      
      .. py:method:: general_ncm
      
         *General NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"is_proxy_for_hvac":            Whether it is a proxy for an ApacheHVAC system*
                 *"ncm_system_type":              NCM system type*
      
      .. py:method:: heating
      
         *Heating data for the Apache system.*
         *Parameters:*
         *show_ncm (optional): Whether to show NCM specific data in the output*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"fuel":                 generator fuel*
                 *"meter_branch"          generator meter branch*
                 *"gen_seasonal_eff":     seasonal efficiency of the generator*
                 *"del_eff":              delivery efficiency of the generator*
                 *"SCoP":                 seasonal coefficient of performance (kW/kW)*
                 *"gen_size":             generator size (kW)*
                 *"HR_effectiveness":     ventilation heat recovery effectiveness*
                 *"HR_return_temp":       ventilation heat recovery return air temperature (C)*
                 *"used_with_CHP":        whether the heat source is used in conjunction with CHP*
                 *"CHP_ranking" (optional): ranking of heat source after the CHP plant*
                 *"CHP_heat_output" (optional): CHP Heat Output (kW)*
                 *"is_heat_pump" (optional): Is it a heat pump?*
                 *"meter_cef" (optional): Meter CEF kgCO2/kWh*
                 *"meter_pef" (optional): Meter PEF kgCO2/kWh*
      
      .. py:method:: heating_ncm
      
         *Heating NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"heat_source":          Heat source*
                 *"meter":                Energy meter*
                 *"qualify_for_ecas":             Does it qualify for ECAs?*
                 *"uses_chp":             Whether this system also uses CHP*
                 *"installed_after_98":           Whether this system was installed on or after 1998*
                 *"existing_district_heating":            Whether this system is an existing district heating system*
                 *"generator_seasonal_efficiency_known":          Do you know the generator seasonal efficiency?*
                 *"generator_seasonal_efficiency":                Generator seasonal efficiency*
                 *"default_generator_seasonal_efficiency":                Default generator seasonal efficiency*
                 *"convectors_have_fans":         Whether convectors have fans*
                 *"fan_power_ratio_known":                Whether the fan power ratio is known*
                 *"fan_power_ratio":              Fan power ratio*
                 *"default_fan_power_ratio":              Default fan power ratio*
                 *"generator_radiant_efficiency_known":           Whether the generator radiant efficiency is known*
                 *"generator_radiant_efficiency":         Generator radiant efficiency*
                 *"default_generator_radiant_efficiency":         Default generator radiant efficiency*
                 *"boiler_over_15_years_old":             Whether the boiler is over 15 years old*
      
      .. py:method:: hot_water
      
         *Hot water data for the Apache system.*
         *Parameters:*
         *show_ncm (optional): Whether to show NCM specific data in the output*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"has_ApHVAC_boiler":    whether the system is served by an ApacheHVAC boiler*
                 *"del_eff":              DHW delivery efficiency*
                 *"cold_water_inlet_temp": mean cold water inlet temperature (C)*
                 *"supply_temp":          hot water supply temperature (C)*
                 *"is_storage_system":    whether the system is a storage system*
                 *"storage_volume" (optional):    storage volume (l)*
                 *"insulation_type" (optional):   type of insulation*
                 *"insulation_thickness" (optional): insulation thickness (mm)*
                 *"storage_losses" (optional):    storage losses (kWh/l/day)*
                 *"has_secondary_circulation":    whether the system has secondary circulation*
                 *"circulation_losses" (optional): circulation losses (W/m)*
                 *"pump_power" (optional):        pump power (kW)*
                 *"pump_meter" (optional):        Pump meter*
                 *"loop_length" (optional):       loop length (m)*
                 *"has_time_switch" (optional):   Whether or not there is a time switch*
                 *"generator_type" (optional):    Generator type*
                 *"later_than_1998" (optional):   Later than 1998?*
                 *"existing_district_heating" (optional): Existing district heating system?*
                 *"generator_meter" (optional):   Generator meter*
                 *"use_default_generator_seaonal_efficiency" (optional):  Do you know the generator seasonal efficiency?*
                 *"default_generator_seaonal_efficiency" (optional):      Default generator seasonal efficiency*
                 *"generator_seasonal_efficiency" (optional):     Seasonal generator efficiency*
      
      .. py:property:: id
      
         *(str) Apache system's ID.*
      
      .. py:method:: meter_name
      
         *meter_name(fuel_id, meter_branch) -> string*
         
         *Gets the meter name for the input meter ID.*
         *Args:*
                 *fuel_id (int): the ID of the fuel that the meter belongs to*
                 *meter_branch (tuple of int): the branch of the meter*
         *Returns:*
                 *Name of meter*
         *Raises:*
                 *ValueError: if no name is found for the meter ID*
                 *RuntimeError: in the case of an internal data handling error*
      
      .. py:method:: metering_provision_ncm
      
         *Metering provision NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"provision_for_metering":               Does the system have provisioning for metering?*
                 *"warns":                Does the metering warn 'out of range' values?*
                 *"control_correction":           Control correction*
      
      .. py:property:: name
      
         *(str) Apache system's name.*
      
      .. py:method:: set_air_supply
      
         *set_air_supply(air_supply_data)*
         
         *Set air supply data from the supplied dictionary*
         *Dictionary keys are:*
           *condition, profile, OA_max_flow, temperature_difference, cooling_max_flow*
         
         *set_air_supply(air_supply_data)*
         
         *Set air supply data from the supplied dictionary*
         *Dictionary keys are:*
           *condition, profile, OA_max_flow, temperature_difference, cooling_max_flow*
      
      .. py:method:: set_auxiliary_energy
      
         *set_auxiliary_energy(aux_data)*
         
         *Set auxiliary energy data from the supplied dictionary*
         *Dictionary keys are:*
           *method, SFP, AEV, off_schedule_AEV, fan_fraction, air_supply_mechanism*
         
         *set_auxiliary_energy(aux_data)*
         
         *Set auxiliary energy data from the supplied dictionary*
         *Dictionary keys are:*
           *method, SFP, AEV, off_schedule_AEV, fan_fraction, air_supply_mechanism*
      
      .. py:method:: set_bivalent_systems_ncm
      
         *set_bivalent_systems_ncm(data)*
         
         *Set bivalent systems from the supplied list of dictionaries.*
         *Each dictionary requires the following keys:*
           *heat_source, meter, gen_seff, load*
      
      .. py:method:: set_control
      
         *set_control(control_id)*
         
         *Set the master zone control.*
      
      .. py:method:: set_cooling
      
         *set_cooling(cooling_data)*
         
         *Set cooling data from the supplied dictionary.*
         *Dictionary keys are:*
           *cool_vent_mechanism, has_absorption_chiller, fuel, SEER, del_eff, SSEER,*
           *gen_size, pump_and_fan_power_perc, nominal_eer, free_cooling*
         
         *set_cooling(cooling_data)*
         
         *Set cooling data from the supplied dictionary.*
         *Dictionary keys are:*
           *cool_vent_mechanism, has_absorption_chiller, fuel, SEER, del_eff, SSEER,*
           *gen_size, pump_and_fan_power_perc, nominal_eer, free_cooling*
      
      .. py:method:: set_cooling_ncm
      
         *set_cooling_ncm(data)*
         
         *Set cooling NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *type, power, chiller_meter, generator_seasonal_eer_known,*
           *generator_seasonal_eer, qualify_for_eca, generator_nominal_eer_known,*
           *generator_nominal_eer, mixed_mode*
         
         *set_cooling_ncm(data)*
         
         *Set cooling NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *type, power, chiller_meter, generator_seasonal_eer_known,*
           *generator_seasonal_eer, qualify_for_eca, generator_nominal_eer_known,*
           *generator_nominal_eer, mixed_mode*
      
      .. py:method:: set_default
      
         *set_default(system_id)*
         
         *Set the default system ID.*
      
      .. py:method:: set_general_ncm
      
         *set_general_ncm(data)*
         
         *Set general NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *is_proxy_for_hvac, ncm_system_type*
         
         *set_general_ncm(data)*
         
         *Set general NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *is_proxy_for_hvac, ncm_system_type*
      
      .. py:method:: set_heating
      
         *set_heating(heating_data)*
         
         *Set heating data from the supplied dictionary.*
         *Dictionary keys are:*
           *fuel, gen_seasonal_eff, SCoP, gen_size, HR_effectiveness, HR_return_temp,*
           *used_with_CHP, CHP_ranking, CHP_heat_output, is_heat_pump, meter_cef, meter_pef*
         
         *set_heating(heating_data)*
         
         *Set heating data from the supplied dictionary.*
         *Dictionary keys are:*
           *fuel, gen_seasonal_eff, SCoP, gen_size, HR_effectiveness, HR_return_temp,*
           *used_with_CHP, CHP_ranking, CHP_heat_output, is_heat_pump, meter_cef, meter_pef*
      
      .. py:method:: set_heating_ncm
      
         *set_heating_ncm(data)*
         
         *Set heating NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *heat_source, meter, qualify_for_ecas, uses_chp, installed_after_98,*
           *generator_seasonal_efficiency_known, generator_seasonal_efficiency,*
           *default_generator_seasonal_efficiency, convectors_have_fans,*
           *fan_power_ratio_known, fan_power_ratio, default_fan_power_ratio,*
           *generator_radiant_efficiency_known, generator_radiant_efficiency,*
           *default_generator_radiant_efficiency, boiler_over_15_years_old*
         
         *set_heating_ncm(data)*
         
         *Set heating NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *heat_source, meter, qualify_for_ecas, uses_chp, installed_after_98,*
           *generator_seasonal_efficiency_known, generator_seasonal_efficiency,*
           *default_generator_seasonal_efficiency, convectors_have_fans,*
           *fan_power_ratio_known, fan_power_ratio, default_fan_power_ratio,*
           *generator_radiant_efficiency_known, generator_radiant_efficiency,*
           *default_generator_radiant_efficiency, boiler_over_15_years_old*
      
      .. py:method:: set_hot_water
      
         *set_hot_water(hot_water_data)*
         
         *Set hot water data from the supplied dictionary.*
         *Dictionary keys are:*
           *has_ApHVAC_boiler, del_eff, cold_water_inlet_temp, supply_temp, is_storage_system,*
           *storage_volume, insulation_type, insulation_thickness, storage_losses,*
           *has_secondary_circulation, circulation_losses, pump_power, loop_length,*
           *has_time_switch, generator_type, later_than_1998, existing_district_heating,*
           *generator_meter, use_default_generator_seaonal_efficiency, generator_seasonal_efficiency*
         
         *set_hot_water(hot_water_data)*
         
         *Set hot water data from the supplied dictionary.*
         *Dictionary keys are:*
           *has_ApHVAC_boiler, del_eff, cold_water_inlet_temp, supply_temp, is_storage_system,*
           *storage_volume, insulation_type, insulation_thickness, storage_losses,*
           *has_secondary_circulation, circulation_losses, pump_power, loop_length,*
           *has_time_switch, generator_type, later_than_1998, existing_district_heating,*
           *generator_meter, use_default_generator_seaonal_efficiency, generator_seasonal_efficiency*
      
      .. py:method:: set_metering_provision_ncm
      
         *set_metering_provision_ncm(data)*
         
         *Set metering provision NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *provision_for_metering, warns*
         
         *set_metering_provision_ncm(data)*
         
         *Set metering provision NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *provision_for_metering, warns*
      
      .. py:method:: set_name
      
         *set_name(name)*
         
         *Set the system name.*
      
      .. py:method:: set_solar_water_heating
      
         *set_solar_water_heating(sol_water_data)*
         
         *Set solar hot water heating data from the supplied dictionary.*
         *Dictionary keys are:*
           *type, area, azimuth, tilt, shading_factor, degradation_factor,*
           *conversion_eff, coeff_a1, coeff_a2, flow_rate, pump_fuel, volume,*
           *storage_loss, refl_length, refl_width, refl_focal_length, units_per_row, num_rows,*
           *tube_extension, intercept_factor, abso_radius, abso_absorptance,*
           *mirror_reflectance, cover_trans, fluid_flow, pump_power, heat_capacity,*
           *HX_effectiveness, tank_volume, tank_heat_loss, coeff_c1, coeff_c2,*
           *has_space_or_process_heating, supply_temp, return_temp*
         
         *set_solar_water_heating(sol_water_data)*
         
         *Set solar hot water heating data from the supplied dictionary.*
         *Dictionary keys are:*
           *type, area, azimuth, tilt, shading_factor, degradation_factor,*
           *conversion_eff, coeff_a1, coeff_a2, flow_rate, pump_fuel, volume,*
           *storage_loss, refl_length, refl_width, refl_focal_length, units_per_row, num_rows,*
           *tube_extension, intercept_factor, abso_radius, abso_absorptance,*
           *mirror_reflectance, cover_trans, fluid_flow, pump_power, heat_capacity,*
           *HX_effectiveness, tank_volume, tank_heat_loss, coeff_c1, coeff_c2,*
           *has_space_or_process_heating, supply_temp, return_temp*
      
      .. py:method:: set_solar_water_heating_ncm
      
         *set_solar_water_heating_ncm(data)*
         
         *Set solar hot water heating NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *is_solar_heating, panel_area, panel_azimuth, panel_tilt,*
           *performance_parameters_known, performance_parameters, sigma_0,*
           *a1, a2, iam, volume, preheating_type, insulation_thickness,*
           *insulation_type, is_heat_exchanger, heat_transfer_rate, overall_heat_loss_coeff*
           *pipes_insulated, circulation_system, nominal_pump_power*
         
         *set_solar_water_heating_ncm(data)*
         
         *Set solar hot water heating NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *is_solar_heating, panel_area, panel_azimuth, panel_tilt,*
           *performance_parameters_known, performance_parameters, sigma_0,*
           *a1, a2, iam, volume, preheating_type, insulation_thickness,*
           *insulation_type, is_heat_exchanger, heat_transfer_rate, overall_heat_loss_coeff*
           *pipes_insulated, circulation_system, nominal_pump_power*
      
      .. py:method:: set_system_adjustment_ncm
      
         *set_system_adjustment_ncm(data)*
         
         *Set system adjustment NCM data from the supplied dictionary.*
         *Dictionary keys are:*
          *ductwork_leakage_test_done, ductwork_leakage_test, ahu_meets_standards,*
          *cen_class, specific_fan_power_known, specific_fan_power, pump_type*
         
         *set_system_adjustment_ncm(data)*
         
         *Set system adjustment NCM data from the supplied dictionary.*
         *Dictionary keys are:*
          *ductwork_leakage_test_done, ductwork_leakage_test, ahu_meets_standards,*
          *cen_class, specific_fan_power_known, specific_fan_power, pump_type*
      
      .. py:method:: set_system_controls_ncm
      
         *set_system_controls_ncm(data)*
         
         *Set system controls NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *central_time_control, optimum_start_stop_control, local_time_control,*
           *local_temperature_control, weather_compensation_control*
         
         *set_system_controls_ncm(data)*
         
         *Set system controls NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *central_time_control, optimum_start_stop_control, local_time_control,*
           *local_temperature_control, weather_compensation_control*
      
      .. py:method:: set_ventilation_ncm
      
         *set_ventilation_ncm(data)*
         
         *Set ventilation NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *air_supply_mechanism, heat_recovery_type, heat_recovery_efficiency_known,*
           *heat_recovery_efficiency, variable_heat_recovery*
         
         *set_ventilation_ncm(data)*
         
         *Set ventilation NCM data from the supplied dictionary.*
         *Dictionary keys are:*
           *air_supply_mechanism, heat_recovery_type, heat_recovery_efficiency_known,*
           *heat_recovery_efficiency, variable_heat_recovery*
      
      .. py:method:: solar_water_heating
      
         *Solar water heating data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"type":                 collector type*
                 *Flat collectors also have the following keys:*
                 *"area":                 area (m^2)*
                 *"azimuth":              azimuth (degrees clockwise from North)*
                 *"tilt":                 tilt (degrees from horizontal)*
                 *"shading_factor":       shading factor*
                 *"degradation_factor":   degradation factor*
                 *"conversion_eff":       conversion efficiency at ambient temperature*
                 *"coeff_a1":             first order heat loss coefficient (a1) (W/m^2/K)*
                 *"coeff_a2":             second order heat loss coefficient (a2) (W/m^2/K)*
                 *"flow_rate":            flow rate (l/h/m^2)*
                 *"pump_power":           pump's power (kW)*
                 *"pump_fuel":            pump's fuel*
                 *"pump_meter_branch":    pump's meter branch*
                 *"HX_effectiveness":     heat exchanger effectiveness*
                 *"volume":               volume (l)*
                 *"storage_loss":         storage loss at max. temperature (kWh/l/day)*
                 *Parabolic collectors also have the following keys:*
                 *"azimuth":              Angle of collector tube (degrees from North)*
                 *"refl_length":          Length of one reflector collector unit (m)*
                 *"refl_width":           Width of one reflector collector unit (m)*
                 *"refl_focal_length":    Focal length of one reflector collector unit (m)*
                 *"units_per_row":        Collector units per row (in series)*
                 *"num_rows":             Number of rows (in parallel)*
                 *"tube_extension":       Extension of tube beyond a single unit (m)*
                 *"intercept_factor":     Fraction of beam radiation intercepted by receiver*
                 *"abso_radius":          Radius of absorber tube (m)*
                 *"abso_absorptance":     Absorptance of absorber tube*
                 *"mirror_reflectance":   Reflectance of the mirror*
                 *"cover_trans":          Transmittance of cover tube*
                 *"fluid_flow":           Total fluid flow (l/h/m^2)*
                 *"pump_power":           Pump power (kW)*
                 *"heat_capacity":        Fluid specific heat capacity(J/kg/K)*
                 *"HX_effectiveness":     Heat exchanger effectiveness*
                 *"tank_volume":          Tank volume (l)*
                 *"tank_heat_loss":       Design tank heat loss (kWh/l/day)*
                 *"pump_fuel":            pump's fuel*
                 *"pump_meter_branch":    pump's meter branch*
                 *"coeff_c1":             First order loss coefficient per unit aperture area*
                 *"coeff_c2":             Second order loss coefficient per unit aperture area*
                 *Flat and parabolic collectors also have the following keys:*
                 *"has_space_or_process_heating": Whether there is space or process heating*
                 *"supply_temp" (optional): Water loop design supply temperature (C)*
                 *"return_temp" (optional): Water loop design return temperature (C)*
      
      .. py:method:: solar_water_heating_derived
      
         *Derived solar water heating data for the Apache system.*
         *Returns:*
                 *Empty dictionary for flat/none, or dictionary with the following keys for parabolic:*
                 *"aperture_area":        Total aperture area (m^2)*
                 *"refl_rim_angle":       Reflector rim angle (degrees)*
                 *"conc_ratio":           Ratio of aperture area to projected absorber tube area*
                 *"ref_collector_eff":    Reference optical efficiency of collector*
                 *"fluid_flow_rate":      Total fluid flow rate (l/h)*
                 *"coeff_k1":             First order loss coefficient per unit tube length*
                 *"coeff_k2":             Second order loss coefficient per unit tube length*
      
      .. py:method:: solar_water_heating_ncm
      
         *Solar water heating data for NCM mode.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"is_solar_heating":                     Is there a solar heating system?*
                 *"panel_area":                   Solar panel area (m^2)*
                 *"panel_azimuth":                        Solar panel azimuth (degrees clockwise from north)*
                 *"panel_tilt":                   Solar panel tilt (degrees from horizontal)*
                 *"performance_parameters_known":                 Do you know the performance parameters?*
                 *"performance_parameter":                        Performance parameter*
                 *"sigma_0":                      Sigma-0*
                 *"a1":                   a1 W/m^2K*
                 *"a2":                   a2 W/m^2*
                 *"iam":                  IAM*
                 *"volume":                       Solar storage volume (l)*
                 *"preheating_type":                      Pre-heating type*
                 *"insulation_thickness":                 Insulation thickness (mm)*
                 *"insulation_type":                      Insulation type*
                 *"is_heat_exchanger":                    Is there a heat exchanger?*
                 *"heat_transfer_rate":                   Heat transfer rate (W/K)*
                 *"overall_heat_loss_coeff":                      Overall heat loss coeff (W/K)*
                 *"pipes_insulated":                      Are pipes to back-up system insulated?*
                 *"circulation_system":                   Circulation system*
                 *"nominal_pump_power":                   Nomincal pump power, Paux (W)*
      
      .. py:method:: system_adjustment_ncm
      
         *System adjustment NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"ductwork_leakage_test_done":           Has the ductwork been leakage tested?*
                 *"ductwork_leakage_test":                CEN classification met by the ductwork*
                 *"ahu_meets_standards":          Does the AHU meet CEN leakage standards?*
                 *"cen_class":            CEN classification met by the AHU*
                 *"air_leakage":          Air leakage*
                 *"specific_fan_power_known":             Do you know the Specific Fan Power?*
                 *"specific_fan_power":           Specific Fan Power of the system*
                 *"default_specific_fan_power":           Default specific fan power*
                 *"pump_type":            Pump type*
      
      .. py:method:: system_controls_ncm
      
         *System controls NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"central_time_control":         Central time control*
                 *"optimum_start_stop_control":           Optimum start/stop control*
                 *"local_time_control":           Local time control (i.e., room by room)*
                 *"local_temperature_control":            Local temperature control (i.e., room by room)*
                 *"weather_compensation_control":         Weather compensation control*
      
      .. py:method:: ventilation_ncm
      
         *Ventilation NCM data for the Apache system.*
         *Returns:*
                 *Dictionary with the following keys:*
                 *"cool_vent_mechanism":          Cooling/ventilation mechanism*
                 *"air_supply_mechanism":         Air supply mechanism*
                 *"heat_recovery_type":           Heat recovery type*
                 *"heat_recovery_efficiency_known":               Do you know the heat recovery seasonal efficiency?*
                 *"heat_recovery_efficiency":             Heat recovery seasonal efficiency*
                 *"default_heat_recovery_efficiency":             Default heat recovery seasonal efficiency*
                 *"variable_heat_recovery":               Variable heat recovery efficiency?*
      
   .. py:class:: VEBody
   
      Represents a room of the building or another feature such as adjacent_building, topographical shade, local_shade or tree.
      
      See iesve.VEBody_type for all options.
   
      .. py:method:: assign_construction
      
         *assign_construction(construction, surface)*
         *Assign construction to surface*
      
      .. py:method:: assign_construction_to_opening
      
         *assign_construction_to_opening(construction, surface, opening_id)*
         *Assign construction to an opening with the specified ID*
      
      .. py:method:: assign_opening_type
      
      
      .. py:method:: assign_opening_type_by_id
      
         *assign_opening_type_by_id(surface_index, macroflo_id, opening_id)*
         
         *Assign macroflo opening type to opening*
      
      .. py:property:: bim_id
      
         *(str) Body BIM ID.*
      
      .. py:property:: cad_object_id
      
         *(str) Body CAD Object ID.*
      
      .. py:method:: get_areas
      
         *get_areas() -> {areas}*
         
         *Returns a dict of areas (and volume) for this space.*
      
      .. py:method:: get_assigned_constructions
      
         *get_assigned_constructions() -> [(construction ID, )]*
         
         *Returns a list of construction IDs assigned to this space.*
      
      .. py:method:: get_assigned_profiles
      
         *get_assigned_profiles() -> [(profile ID, )]*
         
         *Returns a list of profile IDs in use by this space.*
      
      .. py:method:: get_index
      
         *get_index()*
         
         *Get the index of the body*
      
      .. py:method:: get_processes
      
         *get_processes() -> [processes]*
         
         *Returns a list of VEComponentProcess objects representing the component*
         *processes in the body.*
      
      .. py:method:: get_room_data
      
         *get_room_data(type) -> VERoomData object*
         
         *Gets a VERoomData object for closer inspection of the room's data. The data*
         *depends on the input type: the default type of 'real_attributes' gives the default data for the*
         *room, but NCM, PRM and Title 24 specific data can be requested.*
         
         *Args:*
             *type (enum, optional): attribute_type enum*
         *Returns:*
             *A VERoomData object for accessing the room's data, including general data,*
             *room conditions, system data, internal gains and air exchanges.*
         *Raises:*
             *ValueError: if the input is outside the valid range or if it is inconsistent*
                         *with the model variant that the room belongs to.*
             *RuntimeError: in the case of an internal data handling error*
         
         *get_room_data(type) -> VERoomData object*
         
         *Gets a VERoomData object for closer inspection of the room's data. The data*
         *depends on the input type: the default type of 'real_attributes' gives the default data for the*
         *room, but NCM, PRM and Title 24 specific data can be requested.*
         
         *Args:*
             *type (enum, optional): attribute_type enum*
         *Returns:*
             *A VERoomData object for accessing the room's data, including general data,*
             *room conditions, system data, internal gains and air exchanges.*
         *Raises:*
             *ValueError: if the input is outside the valid range or if it is inconsistent*
                         *with the model variant that the room belongs to.*
             *RuntimeError: in the case of an internal data handling error*
      
      .. py:method:: get_surfaces
      
         *get_surfaces() -> [surfaces]*
         
         *Returns a list of surfaces that make up this space.*
      
      .. py:property:: hvac_methodology
      
         *(VEBody_hvac_methodology enum) Body HVAC methodology.*
      
      .. py:property:: id
      
         *(str) Body ID.*
      
      .. py:method:: is_3d_shade
      
         *is_3d_shade()*
         
         *Checks whether the body is a 3d shade. Returns True for a topographical or local shade but*
         
         *False for a vegetated shade.*
      
      .. py:property:: name
      
         *(str) Body name.*
      
      .. py:method:: select
      
         *select()*
         
         *Selects this body. Perform operations on the selected body using the VEGeometry API.*
      
      .. py:property:: selected
      
         *(bool) True if body is selected, else False.*
      
      .. py:property:: subtype
      
         *(VEBody_subtype enum) Body subtype.*
      
      .. py:property:: type
         :type: iesve.VEBody_type
      
         :returns: The type of the VEBody.
      
   .. py:class:: VEBody_subtype
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: boundary_building_footprint
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1004
         * a name of "boundary_building_footprint".
      
      .. py:property:: boundary_leed
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1001
         * a name of "boundary_leed".
      
      .. py:property:: boundary_site
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1000
         * a name of "boundary_site".
      
      .. py:property:: boundary_stormwater
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1002
         * a name of "boundary_stormwater".
      
      .. py:property:: boundary_stormwater_collect_drainage
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1003
         * a name of "boundary_stormwater_collect_drainage".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unclassified': iesve.VEBody_subtype.unclassified
             'boundary_site': iesve.VEBody_subtype.boundary_site
             'boundary_leed': iesve.VEBody_subtype.boundary_leed
             'boundary_stormwater': iesve.VEBody_subtype.boundary_stormwater
             'boundary_stormwater_collect_drainage': iesve.VEBody_subtype.boundary_stormwater_collect_drainage
             'boundary_building_footprint': iesve.VEBody_subtype.boundary_building_footprint
             'road_motorway': iesve.VEBody_subtype.road_motorway
             'road_primary': iesve.VEBody_subtype.road_primary
             'road_secondary': iesve.VEBody_subtype.road_secondary
             'road_tertiary': iesve.VEBody_subtype.road_tertiary
             'road_unclassified': iesve.VEBody_subtype.road_unclassified
             'parking_bay_indoor': iesve.VEBody_subtype.parking_bay_indoor
             'parking_bay_outdoor': iesve.VEBody_subtype.parking_bay_outdoor
             'room': iesve.VEBody_subtype.room
             'void': iesve.VEBody_subtype.void
             'ra_plenum': iesve.VEBody_subtype.ra_plenum
             'sa_plenum': iesve.VEBody_subtype.sa_plenum
            }
      
      .. py:property:: parking_bay_indoor
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1201
         * a name of "parking_bay_indoor".
      
      .. py:property:: parking_bay_outdoor
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1202
         * a name of "parking_bay_outdoor".
      
      .. py:property:: ra_plenum
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 2003
         * a name of "ra_plenum".
      
      .. py:property:: road_motorway
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1101
         * a name of "road_motorway".
      
      .. py:property:: road_primary
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1102
         * a name of "road_primary".
      
      .. py:property:: road_secondary
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1103
         * a name of "road_secondary".
      
      .. py:property:: road_tertiary
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1104
         * a name of "road_tertiary".
      
      .. py:property:: road_unclassified
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 1105
         * a name of "road_unclassified".
      
      .. py:property:: room
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 2001
         * a name of "room".
      
      .. py:property:: sa_plenum
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 2004
         * a name of "sa_plenum".
      
      .. py:property:: unclassified
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unclassified".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.VEBody_subtype.unclassified
             1000: iesve.VEBody_subtype.boundary_site
             1001: iesve.VEBody_subtype.boundary_leed
             1002: iesve.VEBody_subtype.boundary_stormwater
             1003: iesve.VEBody_subtype.boundary_stormwater_collect_drainage
             1004: iesve.VEBody_subtype.boundary_building_footprint
             1101: iesve.VEBody_subtype.road_motorway
             1102: iesve.VEBody_subtype.road_primary
             1103: iesve.VEBody_subtype.road_secondary
             1104: iesve.VEBody_subtype.road_tertiary
             1105: iesve.VEBody_subtype.road_unclassified
             1201: iesve.VEBody_subtype.parking_bay_indoor
             1202: iesve.VEBody_subtype.parking_bay_outdoor
             2001: iesve.VEBody_subtype.room
             2002: iesve.VEBody_subtype.void
             2003: iesve.VEBody_subtype.ra_plenum
             2004: iesve.VEBody_subtype.sa_plenum
            }
      
      .. py:property:: void
         :classmethod:
         :type: iesve.VEBody_subtype
      
         An instance of this class with:
         
         * a value of 2002
         * a name of "void".
      
   .. py:class:: VEBody_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: adjacent_building
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "adjacent_building".
      
      .. py:property:: annotation
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 203
         * a name of "annotation".
      
      .. py:property:: boundary
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 113
         * a name of "boundary".
      
      .. py:property:: hard_landscape
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 104
         * a name of "hard_landscape".
      
      .. py:property:: local_shade
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "local_shade".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'room': iesve.VEBody_type.room
             'adjacent_building': iesve.VEBody_type.adjacent_building
             'topographical_shade': iesve.VEBody_type.topographical_shade
             'local_shade': iesve.VEBody_type.local_shade
             'tree': iesve.VEBody_type.tree
             'road': iesve.VEBody_type.road
             'pavement': iesve.VEBody_type.pavement
             'parking_bay': iesve.VEBody_type.parking_bay
             'hard_landscape': iesve.VEBody_type.hard_landscape
             'pervious_landscape': iesve.VEBody_type.pervious_landscape
             'soft_landscape_turf': iesve.VEBody_type.soft_landscape_turf
             'soft_landscape_shrubs': iesve.VEBody_type.soft_landscape_shrubs
             'soft_landscape_groundcover': iesve.VEBody_type.soft_landscape_groundcover
             'soft_landscape_mixedveg': iesve.VEBody_type.soft_landscape_mixedveg
             'soft_landscape_wetlands': iesve.VEBody_type.soft_landscape_wetlands
             'vegetated_shade': iesve.VEBody_type.vegetated_shade
             'water': iesve.VEBody_type.water
             'boundary': iesve.VEBody_type.boundary
             'annotation': iesve.VEBody_type.annotation
            }
      
      .. py:property:: parking_bay
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 103
         * a name of "parking_bay".
      
      .. py:property:: pavement
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 102
         * a name of "pavement".
      
      .. py:property:: pervious_landscape
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 105
         * a name of "pervious_landscape".
      
      .. py:property:: road
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 101
         * a name of "road".
      
      .. py:property:: room
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "room".
      
      .. py:property:: soft_landscape_groundcover
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 108
         * a name of "soft_landscape_groundcover".
      
      .. py:property:: soft_landscape_mixedveg
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 109
         * a name of "soft_landscape_mixedveg".
      
      .. py:property:: soft_landscape_shrubs
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 107
         * a name of "soft_landscape_shrubs".
      
      .. py:property:: soft_landscape_turf
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 106
         * a name of "soft_landscape_turf".
      
      .. py:property:: soft_landscape_wetlands
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 110
         * a name of "soft_landscape_wetlands".
      
      .. py:property:: topographical_shade
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "topographical_shade".
      
      .. py:property:: tree
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "tree".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.VEBody_type.room
             2: iesve.VEBody_type.adjacent_building
             3: iesve.VEBody_type.topographical_shade
             4: iesve.VEBody_type.local_shade
             5: iesve.VEBody_type.tree
             101: iesve.VEBody_type.road
             102: iesve.VEBody_type.pavement
             103: iesve.VEBody_type.parking_bay
             104: iesve.VEBody_type.hard_landscape
             105: iesve.VEBody_type.pervious_landscape
             106: iesve.VEBody_type.soft_landscape_turf
             107: iesve.VEBody_type.soft_landscape_shrubs
             108: iesve.VEBody_type.soft_landscape_groundcover
             109: iesve.VEBody_type.soft_landscape_mixedveg
             110: iesve.VEBody_type.soft_landscape_wetlands
             111: iesve.VEBody_type.vegetated_shade
             112: iesve.VEBody_type.water
             113: iesve.VEBody_type.boundary
             203: iesve.VEBody_type.annotation
            }
      
      .. py:property:: vegetated_shade
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 111
         * a name of "vegetated_shade".
      
      .. py:property:: water
         :classmethod:
         :type: iesve.VEBody_type
      
         An instance of this class with:
         
         * a value of 112
         * a name of "water".
      
   .. py:class:: VECdbConstruction
   
      *VE CDB Construction*
      *Basic usage:*
      
      *see cdb.py*
   
      .. py:method:: add_layer
      
         *Add a layer to this construction*
      
      .. py:property:: c_factor
      
         *The C Factor of this CDB construction*
         *Only relevant if the regulation is 3 (ASHRAE901)*
      
      .. py:property:: category
      
         *CDB construction category.*
      
      .. py:method:: delete_layer
      
         *Delete a layer from this construction*
      
      .. py:property:: f_factor
      
         *The F Factor of this CDB construction*
      
      .. py:method:: get_default_resistances
      
         *Get default surface resistances for different methodologies*
      
      .. py:method:: get_g_values
      
         *Get the different g-values as a dictionary.*
         
         *Possible dictionary entries are:*
         
         *bs_en_410, building_regulations, bfrc*
      
      .. py:method:: get_layers
      
         *Get a list of layers in this CDB construction*
      
      .. py:method:: get_properties
      
         *Get a dict of the properties of this CDB construction.*
         *The result depends on the optional U value type parameter of type uvalue_types.*
         *If no parameter is specified the U value type set in the Project Constructions dialog is used.*
      
      .. py:method:: get_review_summary_string
      
         *Get a summary of this CDB construction as a formatted string.*
         *Units are converted to local display preferences.*
      
      .. py:method:: get_u_factor
      
         *Get the U Factor of this CDB construction.*
         *The result depends on the U value type parameter of type uvalue_types.*
      
      .. py:property:: id
      
         *The id of the CDB construction*
      
      .. py:method:: insert_layer
      
         *Insert a layer into this construction*
      
      .. py:property:: is_editable
      
         *Is the CDB construction editable?*
      
      .. py:property:: opaque
      
         *Is the CDB construction opaque?*
      
      .. py:property:: reference
      
         *The reference (description) of the CDB construction*
      
      .. py:property:: regulation
      
         *The regulation applied to the CDB construction:*
         *0=CIBSE,*
         *1=EN_ISO,*
         *2=ASHRAE 901,*
         *3=Title 24*
      
      .. py:method:: set_const_class
      
         *Set construction class of this CDB construction. See 'construction_class' enum for possible values.*
      
      .. py:method:: set_f_factor
      
         *Set F Factor of this CDB construction*
      
      .. py:method:: set_properties
      
         *Set properties of this CDB construction via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *outside_surface_solar_absorptivity, inside_surface_solar_absorptivity, frame_percent, frame_type,*
         *glazing_type, percent_sky_blocked, display_window, frame_resistance, frame_absorptance, frame_material,*
         *spacer_type, thermal_bridging_coefficient, visible_light_transmittance,*
         *bfrc_active, light_transmittance, g_value, frame_inside_surface_area_ratio, frame_outside_surface_area_ratio,*
         *external_shade_active, external_shade_code, external_shade_profile, external_shade_radiation_to_lower,*
         *external_shade_radiation_to_raise, external_shade_night_resistance, external_shade_day_resistance,*
         *external_shade_ground_transmittance, external_shade_ground_transmittance_default,*
         *external_shade_sky_transmittance, external_shade_sky_transmittance_default, external_shade_transmittance_0,*
         *external_shade_transmitance_15, external_shade_transmittance_30, external_shade_transmittance_45,*
         *external_shade_transmittance_60, external_shade_transmitance_75, external_shade_transmittance_90,*
         *internal_shade_active, internal_shade_code, internal_shade_profile, internal_shade_radiation_to_lower,*
         *internal_shade_radiation_to_raise, internal_shade_night_resistance, internal_shade_day_resistance,*
         *internal_shade_shading_coefficient, internal_shade_short_wave_radiant_fraction,*
         *internal_shade_blind_or_curtain, internal_shade_frac_daylight_closed, local_shade_active,*
         *local_shade_code, local_shade_window_width, local_shade_window_height, local_shade_projection_overhang,*
         *local_shade_projection_offset, local_shade_left_fin_projection, local_shade_left_fin_offset, local_shade_right_fin_projection,*
         *local_shade_right_fin_offset, local_shade_balcony_height, local_shade_balcony_projection, local_shade_overhang_type,*
         *local_shade_balcony_depth_h, outside_surface_emissivity, inside_surface_emissivity, outside_surface_resistance,*
         *inside_surface_resistance*
         
         *Set properties of this CDB construction via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *outside_surface_solar_absorptivity, inside_surface_solar_absorptivity, frame_percent, frame_type,*
         *glazing_type, percent_sky_blocked, display_window, frame_resistance, frame_absorptance, frame_material,*
         *spacer_type, thermal_bridging_coefficient, visible_light_transmittance,*
         *bfrc_active, light_transmittance, g_value, frame_inside_surface_area_ratio, frame_outside_surface_area_ratio,*
         *external_shade_active, external_shade_code, external_shade_profile, external_shade_radiation_to_lower,*
         *external_shade_radiation_to_raise, external_shade_night_resistance, external_shade_day_resistance,*
         *external_shade_ground_transmittance, external_shade_ground_transmittance_default,*
         *external_shade_sky_transmittance, external_shade_sky_transmittance_default, external_shade_transmittance_0,*
         *external_shade_transmitance_15, external_shade_transmittance_30, external_shade_transmittance_45,*
         *external_shade_transmittance_60, external_shade_transmitance_75, external_shade_transmittance_90,*
         *internal_shade_active, internal_shade_code, internal_shade_profile, internal_shade_radiation_to_lower,*
         *internal_shade_radiation_to_raise, internal_shade_night_resistance, internal_shade_day_resistance,*
         *internal_shade_shading_coefficient, internal_shade_short_wave_radiant_fraction,*
         *internal_shade_blind_or_curtain, internal_shade_frac_daylight_closed, local_shade_active,*
         *local_shade_code, local_shade_window_width, local_shade_window_height, local_shade_projection_overhang,*
         *local_shade_projection_offset, local_shade_left_fin_projection, local_shade_left_fin_offset, local_shade_right_fin_projection,*
         *local_shade_right_fin_offset, local_shade_balcony_height, local_shade_balcony_projection, local_shade_overhang_type,*
         *local_shade_balcony_depth_h, outside_surface_emissivity, inside_surface_emissivity, outside_surface_resistance,*
         *inside_surface_resistance*
      
   .. py:class:: VECdbDatabase
   
      *VE CDB Database*
      *Basic usage:*
      
      *see cdb.py*
   
      .. py:method:: get_current_database
      
         *Get the current CDB database*
         *NB this method is static*
      
      .. py:method:: get_project_type_string
      
         *Get a string describing the project type*
      
      .. py:method:: get_projects
      
         *Get a dict of all the projects in the database*
         *For each project type (0=Project, 1=System, 2=Manufacturer) the dict holds a list of the projects of that type.*
      
   .. py:class:: VECdbLayer
   
      *VE CDB Layer*
      *Basic usage:*
      
      *see cdb.py*
   
      .. py:method:: get_id
      
         *Get the layer ID*
      
      .. py:method:: get_material
      
         *Get the material of this CDB layer*
         
         *Pass in true for an opaque layer, false for a glass layer.*
      
      .. py:method:: get_properties
      
         *Get a dictionary of CDB layer data.*
         
         *The result depends on the optional U value type parameter of type uvalue_types.*
         *If no parameter is specified the U value type set in the Project Constructions dialog is used.*
         
         *Dictionary entries are:*
         
         *thickness (m), resistance (m²K/W), convection_coefficient (W/(m²·K))*
      
      .. py:method:: get_review_summary_string
      
         *Get a summary of this CDB layer as a formatted string.*
         *Units are converted to local display preferences.*
         *The result depends on the optional U value type parameter of type uvalue_types.*
         *If no parameter is specified the U value type set in the Project Constructions dialog is used.*
      
      .. py:method:: set_properties
      
         *Set properties of this CDB layer via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *thickness (m), resistance (m²K/W), convection_coefficient (W/(m²·K))*
         
         *Set properties of this CDB layer via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *thickness (m), resistance (m²K/W), convection_coefficient (W/(m²·K))*
      
   .. py:class:: VECdbMaterial
   
      *VE CDB Material*
      *Basic usage:*
      
      *see cdb.py*
   
      .. py:method:: get_properties
      
         *Get a dictionary of CDB material data*
      
      .. py:method:: get_review_summary_string
      
         *Get a summary of this CDB material as a formatted string.*
         *Units are converted to local display preferences.*
      
      .. py:method:: set_properties
      
         *Set properties of this CDB material via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *description, specific_heat_capacity, conductivity, density, vapour_resistivity, outside_reflectance,*
         *inside_reflectance, transmittance, refractive_index, outside_visible_reflectance,*
         *inside_visible_reflectance, visible_transmittance, thickness, outside_emissivity,*
         *inside_emissivity, angular_dependence, surface_type*
         
         *Set properties of this CDB material via a dictionary.*
         
         *Possible dictionary entries are:*
         
         *description, specific_heat_capacity, conductivity, density, vapour_resistivity, outside_reflectance,*
         *inside_reflectance, transmittance, refractive_index, outside_visible_reflectance,*
         *inside_visible_reflectance, visible_transmittance, thickness, outside_emissivity,*
         *inside_emissivity, angular_dependence, surface_type*
      
   .. py:class:: VECdbProject
   
      *VE CDB Project*
      *Basic usage:*
      
      *see cdb.py*
   
      .. py:method:: create_construction
      
         *create_construction(construction_element_category)*
         *Create a construction of the specified category. Use the 'element_categories' enum.*
      
      .. py:method:: create_material
      
         *create_material(material_category)*
         *Create a material of the specified category.*
      
      .. py:method:: delete_material
      
         *delete_material(material_id)*
         *Deletes the material with the specified ID.*
      
      .. py:method:: get_category_string
      
         *Get a string describing the construction category*
         *NB this method is static*
      
      .. py:method:: get_class_string
      
         *Get a string describing the construction class*
         *NB this method is static*
      
      .. py:method:: get_construction
      
         *Get the construction with the given id in the given class in the project*
         *Pass class = 'iesve.construction_class.none' to return the construction with the given id in any class in the project*
      
      .. py:method:: get_construction_ids
      
         *Get a list of the construction ids in the given class in the project*
         *Pass class = 'iesve.construction_class.none' to return a list of the construction ids in all classes in the project*
      
      .. py:method:: get_material
      
         *get_material(material_id)*
         *Gets an instance of the material with the specified ID.*
      
      .. py:method:: get_material_ids
      
         *get_material_ids(material_category)*
         *Get all material IDs matching the specified category.*
         *Passing material_category.all will return all material IDs in the project.*
      
      .. py:method:: get_number_of_constructions_in_category
      
         *Get the number of constructions in the given category in the project*
      
      .. py:method:: get_number_of_materials_in_category
      
         *get_number_of_materials_in_category(material_category)*
         *Get the number of materials matching the specified category.*
         *Passing material_category.all will return the number of materials in the project.*
      
      .. py:property:: has_constructions
      
         *Whether the CDB project has constructions*
      
      .. py:property:: has_materials
      
         *Whether the CDB project has materials*
      
      .. py:property:: name
      
         *The DFA file name of the CDB project*
      
      .. py:property:: number_of_constructions
      
         *The number of constructions in the project*
      
      .. py:property:: number_of_materials
      
         *The number of materials in the project*
      
      .. py:property:: path
      
         *The path of the CDB project*
      
      .. py:property:: title
      
         *The title of the CDB project*
      
   .. py:class:: VEComponentProcess
   
      *Provides access to the object process data for a component process.*
   
      .. py:method:: get_energy_inputs
      
         *get_energy_inputs() -> List of dictionaries*
         
         *Gets the data for the process' energy inputs.*
         *Returns:*
                 *List of dictionaries, each containing the data for an energy input*
      
      .. py:method:: get_heat_outputs
      
         *get_heat_outputs() -> List of dictionaries*
         
         *Gets the data for the process' heat outputs.*
         *Returns:*
                 *List of dictionaries, each containing the data for a heat output*
      
      .. py:method:: get_material_inputs
      
         *get_material_inputs() -> List of dictionaries*
         
         *Gets the data for the process' material inputs.*
         *Returns:*
                 *List of dictionaries, each containing the data for a material input*
      
      .. py:method:: get_material_outputs
      
         *get_material_outputs() -> List of dictionaries*
         
         *Gets the data for the process' material outputs.*
         *Returns:*
                 *List of dictionaries, each containing the data for a material output*
      
      .. py:method:: get_miscellaneous
      
         *get_miscellaneous() -> List of dictionaries*
         
         *Gets the data for the process' miscellaneous information.*
         *Returns:*
                 *List of dictionaries, each containing the data for a miscellaneous entry*
      
      .. py:method:: get_name
      
         *get_name() -> string*
         
         *Gets the process' name.*
         *Returns:*
                 *Process' name*
      
      .. py:method:: get_product
      
         *get_product() -> string*
         
         *Gets the name of the product that the process produces.*
         *Returns:*
                  *Product name as a string*
      
      .. py:method:: get_system_inputs
      
         *get_system_inputs() -> List of dictionaries*
         
         *Gets the data for the process' system inputs.*
         *Returns:*
                 *List of dictionaries, each containing the data for a system input*
      
      .. py:method:: get_waste_heats
      
         *get_waste_heats() -> List of dictionaries*
         
         *Gets the data for the process' waste heats.*
         *Returns:*
                 *List of dictionaries, each containing the data for a waste heat*
      
   .. py:class:: VEEnergyMeter
   
      *Interface for energy meters. Can be obtained from EnergySources.*
   
      .. py:method:: get
      
         *get() -> dictionary*
         
         *Get energy meter data.*
         *Dictionary entries are name, source_data and id.*
      
   .. py:class:: VEGeometry
   
      *Interface for geometry*
   
      .. py:method:: centre_to_origin
      
         *static centre_to_origin()*
         
         *Centres the model on the grid origin (0,0).*
      
      .. py:method:: get_building_orientation
      
         *static get_building_orientation()*
         
         *Get building orientation*
      
      .. py:method:: get_construction
      
         *get_construction() -> str*
         
         *Obtains the construction ID of the opening. Returns an empty*
         *string if none is found.*
      
      .. py:method:: get_id
      
         *get_id() -> ID (string)*
         
         *Gets the opening ID*
      
      .. py:method:: get_macroflo_id
      
         *get_macroflo_id() -> ID (string)*
         
         *Gets the macroflo opening ID*
      
      .. py:method:: get_properties
      
         *get_properties() -> dictionary*
         
         *Gets a dictionary of opening properties. Possible keys are:*
         *aspect_ratio, perimeter, index, area, height,*
         *width, aps_handle, macroflo_type and type*
         
         *Note that values for width and height are only accurate for rectangular openings*
         *and horizontal rotations.*
      
      .. py:method:: get_wwr
      
         *static get_wwr() -> Window-to-wall ratio (float)*
         
         *Get the model's window-to-wall ratio*
      
      .. py:method:: move_opening
      
         *move_opening(xdistance, ydistance)*
         
         *Move an associated opening*
      
      .. py:method:: reduce_ext_windows
      
         *static get_ext_windows(max_wwr)*
         
         *Reduce external windows so that the max window-to-wall ratio is not exceeded*
         *Args:*
           *max_wwr (float): Max window-to-wall ratio*
      
      .. py:method:: remove_doors
      
         *static remove_doors(flag, opening_area)*
         
         *Remove doors from the model.*
         *Args:*
           *flag (int): 0 = all, 1 = internal, 2 = external*
           *opening_area (float): Opening area threshold, all doors with an area below this threshold are removed.*
                                 *If 0.0, removes all doors*
      
      .. py:method:: remove_holes
      
         *static remove_holes(flag, opening_area)*
         
         *Removes holes from the model.*
         *Args:*
           *flag (int): 0 = all, 1 = internal, 2 = external*
           *opening_area (float): Opening area threshold, all holes with an area below this threshold are removed.*
                                 *If 0.0, removes all holes*
      
      .. py:method:: remove_openings_below_area_threshold
      
         *static remove_openings_below_area_threshold(area_threshold)*
         
         *Remove openings below the provided threshold area for the selected body. Use VEBody.select() to select a body.*
         *Args:*
           *area_threshold (float): Area threshold in square metres*
      
      .. py:method:: set_body_opening_type
      
         *static set_body_opening_type(opening_type)*
         
         *Change opening type for selected body's openings. Use VEBody.select() to select a body.*
         *Args:*
           *opening_type (string): Opening type. Valid entries are 'door', 'window' and 'hole'*
      
      .. py:method:: set_colour
      
         *static set_colour(colour_index)*
         
         *Set colour of the selected body*
         *Args:*
           *colour_index (int): Index of the colour to set.*
         *Possible colour index values:*
           *0 = BLUE*
           *1 = GREEN*
           *2 = RED*
           *3 = YELLOW*
           *4 = PURPLE*
           *5 = ORANGE*
           *6 = CYAN*
           *7 = LIGHT GREY*
           *48 = WHITE*
           *56 = BLACK*
      
      .. py:method:: set_percent_doors
      
         *static set_percent_doors(percent_doors)*
         
         *Set percent doors for the selected body. Use VEBody.select() to select a body.*
         *Args:*
           *percent_doors (int): Percent doors to set.*
      
      .. py:method:: set_percent_glazing
      
         *static set_percent_glazing(percent_glazing)*
         
         *Set percent glazing of external surfaces for the selected body. Use VEBody.select() to select a body.*
         *Args:*
           *percent_glazing (int): Percent glazing to set.*
      
      .. py:method:: set_percent_holes
      
         *static set_percent_holes(percent_holes)*
         
         *Set percent holes for the selected body. Use VEBody.select() to select a body.*
         *Args:*
           *percent_holes (int): Percent holes to set.*
      
      .. py:method:: set_percent_wall_glazing
      
         *static set_percent_wall_glazing(percent_glazing)*
         
         *Set percent glazing of walls for the selected body. Use VEBody.select() to select a body.*
         *Args:*
           *percent_glazing (int): Percent glazing to set.*
      
   .. py:class:: VELocate
   
      *Interface for getting VE location data.*
   
      .. py:method:: close_wea_data
      
         *close_wea_data( (VELocate)arg1) -> None :*
             *close_wea_data() -> None*
             **
             *Close the location database.*
      
      .. py:method:: get
      
         *get( (VELocate)arg1) -> object :*
             *get() -> dict*
             **
             *Get location data. Returns a dictionary with the following keywords:*
             *city, country (strings)*
             *latitude, longitude (float, degrees)*
             *altitude (float, meters)*
             *time_zone (float)*
             *dst_correction (float)*
             *dst_from_month, dst_to_month (float) range 1 - 12*
             *ground_reflectance_summer_from_month, ground_reflectance_summer_to_month (float) range 1-12*
             *ground_reflectance_summer, ground_reflectance_winter (float)*
             *summer_drybulb, summer_wetbulb, winter_drybulb (float, degrees Celsius)*
             *heating_loads percentile, cooling_loads percentile (float, %)*
             *external CO2 (float, ppm),*
             *national_climate_zone (int or string),*
             *weather source (string)*
      
      .. py:method:: open_wea_data
      
         *open_wea_data( (VELocate)arg1) -> int :*
             *open_wea_data() -> int*
             **
             *Open location data. Returns -1 on failure, else success*
      
      .. py:method:: save_and_close
      
         *save_and_close( (VELocate)arg1) -> None :*
             *save_and_close() -> None*
             **
             *Save and close the location database*
      
      .. py:method:: set
      
         *set( (VELocate)arg1, (dict)arg2) -> None :*
             *set(dict) -> None*
             **
             *Set location data. Possible dictionary keywords are:*
                 *city, country, latitude, longitude, altitude, time_zone, dst_correction, dst_from_month,*
                 *dst_to_month, ground_reflectance_summer, ground_reflectance_winter, ground_reflectance_summer_from_month,*
                 *ground_reflectance_summer_to_month, summer_drybulb, summer_wetbulb, winter_drybulb,*
                 *heating_loads_percentile, cooling_loads_percentile, external_CO2, ref_air_density*
         
         *object set(tuple args, dict kwds)*
      
      .. py:method:: set_max_dry_bulb
      
         *set_max_dry_bulb( (VELocate)arg1, (object)arg2, (object)arg3) -> None :*
             *set_max_dry_bulb(temperature, month)*
             **
             *Set the maximum dry bulb temperature in degrees Celsius for a given month.*
      
      .. py:method:: set_max_wet_bulb
      
         *set_max_wet_bulb( (VELocate)arg1, (object)arg2, (object)arg3) -> None :*
             *set_max_wet_bulb(temperature, month)*
             **
             *Set the maximum wet bulb temperature in degrees Celsius for a given month.*
      
      .. py:method:: set_min_dry_bulb
      
         *set_min_dry_bulb( (VELocate)arg1, (object)arg2, (object)arg3) -> None :*
             *set_min_dry_bulb(temperature, month)*
             **
             *Set the minimum dry bulb temperature in degrees Celsius for a given month*
      
   .. py:class:: VEMacroFlo
   
      *Interface for Macroflo*
   
      .. py:method:: get
      
         *get()->[opening data]*
         
         *Returns data for all Macroflo openings*
         *Dictionary fields are:*
           *crack_flow_coefficient: Crack flow coefficient*
           *crack_length: Crack length as % of opening perimeter*
           *description: Opening description*
           *equivalent_orifice_area: Equivalent orifice area as % of gross*
           *exposure_type: Exposure type name*
           *openable_area: Openable area as %*
           *opening_category: Opening category name*
           *opening_threshold: Opening threshold temperature*
           *profile: Degree of opening (modulating profile name)*
           *reference_id: Reference ID of the opening*
      
      .. py:method:: reload_wind_coefficients
      
         *reload_wind_coefficients*
         
         *Forces the VE to reload wind coefficient data from the project's PCO file.*
      
      .. py:method:: set
      
         *set(data)*
         
         *Set data for a Macroflo opening from a dictionary of data*
         *Possible dictionary fields are:*
         *description, exposure_type, opening_category, openable_area,*
         *equivalent_orifice_area, crack_flow_coefficient, crack_length,*
         *opening_threshold, profile*
         
         *set(data)*
         
         *Set data for a Macroflo opening from a dictionary of data*
         *Possible dictionary fields are:*
         *description, exposure_type, opening_category, openable_area,*
         *equivalent_orifice_area, crack_flow_coefficient, crack_length,*
         *opening_threshold, profile*
      
   .. py:class:: VEModel
   
      Represents a building and its systems as modelled by the user in the IES-VE software.
   
      .. py:method:: assign_thermal_template_to_rooms
      
         *assign_thermal_template_to_rooms( template, [roomID] )*
         
         *Assign the thermal template to the rooms, indicated by list of Room IDs.*
      
      .. py:method:: get_assigned_profiles
      
         *get_assigned_profiles( expandProfiles ) -> [profile ID]*
         
         *Returns a list of profiles in use by this model variant.  Set*
         *expandProfiles (default: False) to True to also return daily profiles.*
      
      .. py:method:: get_bodies(selectedOnly)
      
         :param bool selectedOnly: Use `True` to return only the bodies already selected by the user in the IES-VE software; use `False` to return all bodies.
         
         :returns: A list of "body" instances.
      
         :rtype: list[iesve.VEBody]
      
      .. py:method:: get_bodies_and_ids
      
         *get_bodies_and_ids( selectedOnly ) -> [VEBody]*
         
         *Returns a dictionary of VEBody objects keyed by their room ID for this model variant.  Set*
         *selectedOnly to True to return only selected bodies, False for all bodies.*
      
      .. py:method:: get_bodies_for_umlh
      
         *get_bodies_for_umlh() -> [VEBody]*
         
         *Returns the list of VEBody objects for this model variant, except those excluded for UMLH.*
      
      .. py:method:: get_excluded_bodies_for_umlh
      
         *get_excluded_bodies_for_umlh() -> [VEBody]*
         
         *Returns the list of VEBody objects for this model variant, of those excluded for UMLH.*
      
      .. py:method:: get_exterior_lighting_details
      
         *get_exterior_lighting_data( iesve.LightingStandard ) -> dict*
         
         *Obtains exterior lighting data for the model. Includes a 'results'*
         *key which contains an ordered list of tuples for each of the sections.*
      
      .. py:method:: get_included_bodies_for_umlh
      
         *get_included_bodies_for_umlh() -> [VEBody]*
         
         *Returns the list of VEBody objects for this model variant, except those excluded for UMLH.*
      
      .. py:method:: get_mep_details
      
         *get_mep_details( iesve.attribute_type ) -> dict*
         
         *Obtains MEP power data from the model. The attribute_type parameter*
         *is optional and does not need to be specified unless it is an NECB*
         *model, where it must be supplied to provide the correct results.*
      
      .. py:property:: id
      
         *(str) Model description.*
      
      .. py:property:: model_type
      
         *(iesve.VEModels) The model type.*
      
      .. py:method:: rebuild_adjacencies
      
         *rebuild_adjacencies()*
         
         *Rebuild adjacencies in the model.*
      
      .. py:method:: suncast
      
         *suncast() -> VESuncast Object*
         
         *Get a VESuncast object for this model*
      
   .. py:class:: VEModels
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ActualBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ActualBuilding".
      
      .. py:property:: BaselineBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 6
         * a name of "BaselineBuilding".
      
      .. py:property:: GreenMarkProposedBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 12
         * a name of "GreenMarkProposedBuilding".
      
      .. py:property:: GreenMarkReferenceBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 13
         * a name of "GreenMarkReferenceBuilding".
      
      .. py:property:: LEEDSunCastSS71Building
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 15
         * a name of "LEEDSunCastSS71Building".
      
      .. py:property:: NECBProposedBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 19
         * a name of "NECBProposedBuilding".
      
      .. py:property:: NECBReferenceBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 20
         * a name of "NECBReferenceBuilding".
      
      .. py:property:: NewZealandProposedBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 10
         * a name of "NewZealandProposedBuilding".
      
      .. py:property:: NewZealandReferenceBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 11
         * a name of "NewZealandReferenceBuilding".
      
      .. py:property:: NotionalBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 2
         * a name of "NotionalBuilding".
      
      .. py:property:: ProposedBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 5
         * a name of "ProposedBuilding".
      
      .. py:property:: RealBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 0
         * a name of "RealBuilding".
      
      .. py:property:: ReferenceBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 4
         * a name of "ReferenceBuilding".
      
      .. py:property:: Section63PrescriptiveBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 17
         * a name of "Section63PrescriptiveBuilding".
      
      .. py:property:: SunCastSolarVisBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 14
         * a name of "SunCastSolarVisBuilding".
      
      .. py:property:: Title24ProposedBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 16
         * a name of "Title24ProposedBuilding".
      
      .. py:property:: Title24StandardDesignBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 18
         * a name of "Title24StandardDesignBuilding".
      
      .. py:property:: TypicalBuilding
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of 3
         * a name of "TypicalBuilding".
      
      .. py:property:: VEModels_NA
         :classmethod:
         :type: iesve.VEModels
      
         An instance of this class with:
         
         * a value of -1
         * a name of "VEModels_NA".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'VEModels_NA': iesve.VEModels.VEModels_NA
             'RealBuilding': iesve.VEModels.RealBuilding
             'ActualBuilding': iesve.VEModels.ActualBuilding
             'NotionalBuilding': iesve.VEModels.NotionalBuilding
             'TypicalBuilding': iesve.VEModels.TypicalBuilding
             'ReferenceBuilding': iesve.VEModels.ReferenceBuilding
             'ProposedBuilding': iesve.VEModels.ProposedBuilding
             'BaselineBuilding': iesve.VEModels.BaselineBuilding
             'NewZealandProposedBuilding': iesve.VEModels.NewZealandProposedBuilding
             'NewZealandReferenceBuilding': iesve.VEModels.NewZealandReferenceBuilding
             'GreenMarkProposedBuilding': iesve.VEModels.GreenMarkProposedBuilding
             'GreenMarkReferenceBuilding': iesve.VEModels.GreenMarkReferenceBuilding
             'SunCastSolarVisBuilding': iesve.VEModels.SunCastSolarVisBuilding
             'LEEDSunCastSS71Building': iesve.VEModels.LEEDSunCastSS71Building
             'Title24ProposedBuilding': iesve.VEModels.Title24ProposedBuilding
             'Section63PrescriptiveBuilding': iesve.VEModels.Section63PrescriptiveBuilding
             'Title24StandardDesignBuilding': iesve.VEModels.Title24StandardDesignBuilding
             'NECBProposedBuilding': iesve.VEModels.NECBProposedBuilding
             'NECBReferenceBuilding': iesve.VEModels.NECBReferenceBuilding
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.VEModels.VEModels_NA
             0: iesve.VEModels.RealBuilding
             1: iesve.VEModels.ActualBuilding
             2: iesve.VEModels.NotionalBuilding
             3: iesve.VEModels.TypicalBuilding
             4: iesve.VEModels.ReferenceBuilding
             5: iesve.VEModels.ProposedBuilding
             6: iesve.VEModels.BaselineBuilding
             10: iesve.VEModels.NewZealandProposedBuilding
             11: iesve.VEModels.NewZealandReferenceBuilding
             12: iesve.VEModels.GreenMarkProposedBuilding
             13: iesve.VEModels.GreenMarkReferenceBuilding
             14: iesve.VEModels.SunCastSolarVisBuilding
             15: iesve.VEModels.LEEDSunCastSS71Building
             16: iesve.VEModels.Title24ProposedBuilding
             17: iesve.VEModels.Section63PrescriptiveBuilding
             18: iesve.VEModels.Title24StandardDesignBuilding
             19: iesve.VEModels.NECBProposedBuilding
             20: iesve.VEModels.NECBReferenceBuilding
            }
      
   .. py:class:: VEProfile
   
      *Profile manipulations.*
      *Basic usage:*
      
      *import iesve*
      *project = iesve.VEProject.get_current_project()*
      *dayprofiles, groupprofiles = project.profiles()*
      *for id, profile in groupprofiles.items():*
          *if profile.is_weekly():*
              *print('Weekly profile {}, {}.'.format(id, profile.reference))*
          *elif profile.is_yearly():*
              *print('Yearly profile {}, {}.'.format(id, profile.reference))*
   
      .. py:method:: get_data
      
         *get_data() -> profile data*
         
         *Retrieve profile data.  The returned data depends on profile type. All returned*
         *data structures are compatible with the set_data() method.*
           *- Daily profile: a list of [ x, y, formula ] lists that represent the data for the profile.*
           *- Weekly profile: a list of daily profile IDs that make up the weekly profile.*
           *- Yearly profile: a list of lists: [ weekly profile ID, fromDay, toDay ],*
             *where fromDay = year day where the profile becomes active, toDay = last day of profile*
           *- Compact profile: a nested sets of lists, each list representing on/off time periods*
           *- Free form profile : list of lists: [ month, day, hour, minute, value ]*
      
      .. py:property:: id
      
         *(str) Profile ID.*
      
      .. py:method:: is_absolute
      
         *is_absolute() -> bool*
         
         *True if the profile is absolute, else False.*
      
      .. py:method:: is_group
      
         *is_group() -> bool*
         
         *True if the profile is a group profile, False if a daily profile.*
      
      .. py:method:: is_modulating
      
         *is_modulating() -> bool*
         
         *True if the profile is modulating, else False.*
      
      .. py:property:: reference
      
         *(str) Profile reference (name).*
      
      .. py:method:: set_data
      
         *set_data() -> bool*
         
         *Set profile data.  The data to be passed depends on profile type.*
         
         *Daily Profile:*
         *Data should represented by a list of [x,y,formula] lists*
         *[ [x,y,formula], [x,y,formula], ... ]*
         
         *Weekly Profile:*
         *Data should represented by a list of daily profile IDs*
         *[ ID1, ID2, ... ]*
         
         *Yearly Profile:*
          *Data should be represented by a list of [weekly profile ID(string), fromDay(int), toDay(int)] lists*
          *[ [ID1, from1, to1], [ID2, from2, to2], ... ]*
         
         *Compact Profile:*
         *Data should represented by a list of lists that contains compact profile data:*
         
         *The outer list is for the number of time periods*
         *Each time period is represented by a list of lists:*
                 *[ [toDay, toMonth], [entry], [entry], [entry], ... ]*
                 *Where an entry list is:*
                         *[description, firstTime, secondTime]*
                 *Where firstTime and secondTime are:*
                                 *[True, startHour, startMinute, endHour, endMinute]*
                                 *OR*
                                 *[False, 0, 0]  if time is not active*
                         *Description: "Label: DaysOfWeek" (eg. "Weekends: Sat, Sun")*
                         *StartHour, startMinute: 0-24, 0-59 for the start time*
                         *EndHour, endMinute: 0-24, 0-59 for the end time*
         
         *Free-form Profile:*
         *Set the free-form entries for this profile.*
         *Data should be a list of lists, where each entry in the outer list*
         *contains the month, day, hour, minute and value of that entry.*
         *Value is a double if no formula is set, and a string otherwise.*
         *First and last entries cannot be changed.*
         
         *[[month, day, hour, minute, value],...]*
         
         *month: 1-12*
         *day: 1-31*
         *hour: 0-23*
         *minute: 0-59*
      
   .. py:class:: VEProject
   
      Represents all information and features relating to the modelling project in the IES-VE software.
   
      .. py:method:: air_exchanges
      
         *air_exchanges() -> [air exchanges]*
         
         *Returns a list of all defined air exchanges.*
      
      .. py:method:: apache_systems
      
         *apache_systems() -> [systems]*
         
         *Returns a list of all defined Apache Systems.*
      
      .. py:method:: archive_project
      
      
      .. py:method:: casual_gains
      
         *casual_gains() -> [gains]*
         
         *Returns a list of all defined casual gains.*
      
      .. py:property:: content_folder
      
         *(str) Project content folder path.*
      
      .. py:method:: create_profile
      
         *create_profile(type, reference, modulating, units) -> profile*
         
         *Creates a new (empty / default) profile of the specified type.*
           *Args:*
             *type (string): one of the following values:*
                 *'daily', 'weekly', 'yearly', 'compact', 'freeform'.*
             *reference (string, optional): name for profile.*
             *modulating (bool, optional [default = True]):*
                 *True for a modulating profile, False otherwise.*
             *units (int, optional [default = -1 (none)]):*
                 *0 for metric, 1 for IP or -1 for none.*
      
      .. py:method:: daily_profile
      
         *daily_profile(profileID) -> profile*
         
         *Takes a profile ID string, and returns the corresponding daily profile.*
      
      .. py:method:: daily_profiles
      
         *daily_profiles([profileIDs]) -> {profiles}*
         
         *Takes a list of profile ID strings and returns a dict of corresponding*
         *daily profiles, keyed by profile ID.*
      
      .. py:method:: deregister_content
      
         *deregister_content(path)*
         
         *Remove a file from Content Manager.  No effect if the file does not exist*
         *in the Content Manager database.*
      
      .. py:method:: get_current_project
         :classmethod:
      
         :returns: The project currently loaded in the VE.
      
         :rtype: iesve.VEProject
      
      .. py:method:: get_display_units
      
      
      .. py:method:: get_language_code
      
      
      .. py:method:: get_macro_flo_opening_by_id
      
         *get_macro_flo_opening_by_id(openingID) -> opening type*
         
         *Takes an opening ID and returns the corresponding Macroflo opening type.*
      
      .. py:method:: get_macro_flo_opening_types
      
         *get_macro_flo_opening_types() -> [opening types]*
         
         *Returns a list of all defined Macroflo opening types.*
      
      .. py:method:: get_scenario_base_project_path
      
         *get_scenario_base_project_path() -> default scenario model path*
         
         *If a scenario is currently active, returns the project path for the parent (non-scenario) model.*
      
      .. py:method:: get_version
      
      
      .. py:method:: group_profile
      
         *group_profile(profileID) -> profile*
         
         *Takes a profile ID string, and returns the corresponding group profile.*
      
      .. py:method:: group_profiles
      
         *group_profiles([profileIDs]) -> {profiles}*
         
         *Takes a list of profile ID strings and returns a dict of corresponding*
         *group profiles, keyed by profile ID.*
      
      .. py:property:: models
         :type: list[iesve.VEModel]
      
         :returns: A list of "active model variants". The first item is always the "real model".
      
      .. py:property:: name
      
         *(str) Project name (title).*
      
      .. py:property:: path
         :type: str
      
         :returns: The path to the local directory of the IES-VE project.
      
      .. py:method:: profiles
      
         *profiles() -> (daily,group)*
         
         *Returns a tuple containing daily and group profiles.*
         *Each tuple entry is a dictionary of key=profile ID, value=profile object.*
      
      .. py:method:: register_content
      
         *register_content(path, category, displayString, notification)*
         
         *Register a file with Content Manager using category and display strings.*
         *Pass True for notification to have a notification displayed, False to add silently.*
      
      .. py:method:: save_profiles
      
      
      .. py:method:: thermal_templates
      
         *thermal_templates() -> {templates}*
         
         *Returns a dict of all defined thermal templates, keyed by template handle.*
      
   .. py:class:: VERenewables
   
      *Interface for Renewables*
   
      .. py:method:: get_chp_data
      
         *get_chp_data()->[CHP data dictionary]*
         
         *Returns all CHP data.*
         *Dictionary fields are:*
           *is_enabled: Whether CHP data is enabled.*
           *source_meter: Source meter name.*
           *electrical_generation_meter: Electrical generation meter name.*
           *quality_index: Quality index.*
           *rated_heat_output: Heat output.*
           *rated_thermal_efficiency: Thermal efficiency at rated output.*
           *rated_power_efficiency: Power efficiency at rated output.*
           *min_fraction_rated_heat_output: Fraction of rated heat.*
           *min_thermal_efficiency: Minimum thermal efficiency.*
           *min_power_efficiency: Minimum power efficiency.*
           *profile: Name of profile for heat matching strategy.*
      
      .. py:method:: get_pv_data
      
         *get_pv_data()->[List of dictionaries]*
         
         *Returns data for all PVs.*
         *Possible dictionary fields are (varies by PV class):*
           *id: ID of the PV panel.*
           *description: PV panel description.*
           *type_id: PV type ID. Use with get_pv_type_by_id() to get PV type data.*
           *area: Area of the PV panel.*
           *azimuth: Azimuth of the PV.*
           *inclination: PV inclination.*
           *shading_factor: PV shading factor.*
           *cell_surface: Cell surface.*
           *num_cells: Number of cells.*
           *geometric_concentration: Geometric concentration.*
           *power_temperature_coefficient: Power temperature coefficient.*
           *optical_efficiency: Optical efficiency.*
           *cell_efficiency: Cell efficiency.*
           *spectral_factor: Spectral factor.*
           *tracking_device_power_losses: Tracking device power losses.*
           *linear_temperature_factor: Linear temperature factor.*
           *tracking_error: Tracking error.*
           *meter: Energy meter.*
      
      .. py:method:: get_pv_data_by_id
      
         *get_pv_data_by_id(id)->[Dictionary of PV data]*
         
         *Returns PV data from the given ID.*
         *Possible dictionary fields are (varies by PV class):*
           *id: ID of the PV panel.*
           *description: PV panel description.*
           *type_id: PV type ID. Use with get_pv_type_by_id() to get PV type data.*
           *area: Area of the PV panel.*
           *azimuth: Azimuth of the PV.*
           *inclination: PV inclination.*
           *shading_factor: PV shading factor.*
           *cell_surface: Cell surface.*
           *num_cells: Number of cells.*
           *geometric_concentration: Geometric concentration.*
           *power_temperature_coefficient: Power temperature coefficient.*
           *optical_efficiency: Optical efficiency.*
           *cell_efficiency: Cell efficiency.*
           *spectral_factor: Spectral factor.*
           *tracking_device_power_losses: Tracking device power losses.*
           *linear_temperature_factor: Linear temperature factor.*
           *tracking_error: Tracking error.*
           *meter: Energy meter.*
         *Args:*
           *id (string): ID of the PV to get.*
      
      .. py:method:: get_pv_type_by_id
      
         *get_pv_type_by_id(id)->[Dictionary of PV type data]*
         
         *Returns data for a PV type from the given ID.*
         *Dictionary fields are:*
           *id: ID of the PV type.*
           *description: PV type description.*
           *technology: Name of PV type technology.*
           *module_nominal_efficiency: Module nominal efficiency.*
           *noct: Nominal cell temperature (NOCT).*
           *ref_irradiance: Reference irradiance for NOCT.*
           *temp_coefficient: Temperature coefficient for module efficiency.*
           *degradation_factor: Degradation factor.*
           *electrical_conversion_efficiency: Electrical conversion efficiency.*
           *meter: Energy meter.*
         *Args:*
           *id (string): ID of the PV type to get.*
      
      .. py:method:: get_pv_types
      
         *get_pv_types()->[List of PV type data dictionaries]*
         
         *Returns data for all PV types.*
         *Dictionary fields are:*
           *id: ID of the PV type.*
           *description: PV type description.*
           *technology: Name of PV type technology.*
           *module_nominal_efficiency: Module nominal efficiency.*
           *noct: Nominal cell temperature (NOCT).*
           *ref_irradiance: Reference irradiance for NOCT.*
           *temp_coefficient: Temperature coefficient for module efficiency.*
           *degradation_factor: Degradation factor.*
           *electrical_conversion_efficiency: Electrical conversion efficiency.*
           *meter: Energy meter.*
      
      .. py:method:: get_wind_data
      
         *get_wind_data()->[Wind data dictionary]*
         
         *Returns all wind data.*
         *Dictionary fields are:*
           *is_enabled: Whether wind data is enabled.*
           *hub_height: Hub height.*
           *rated_power: Rated power.*
           *meter: Energy meter.*
      
      .. py:method:: set_chp_data
      
         *set_chp_data(Dictionary of CHP data)*
         
         *Sets CHP data.*
         *Possible dictionary entries are:*
           *is_enabled, quality_index,*
           *rated_heat_output, rated_thermal_efficiency, rated_power_efficiency,*
           *min_fraction_rated_heat_output, min_thermal_efficiency,*
           *min_power_efficiency, profile*
         
         *set_chp_data(Dictionary of CHP data)*
         
         *Sets CHP data.*
         *Possible dictionary entries are:*
           *is_enabled, quality_index,*
           *rated_heat_output, rated_thermal_efficiency, rated_power_efficiency,*
           *min_fraction_rated_heat_output, min_thermal_efficiency,*
           *min_power_efficiency, profile*
      
      .. py:method:: set_pv_data
      
         *set_pv_data(Dictionary of PV data, id)*
         
         *Sets data for a PV panel.*
         *Possible dictionary entries are:*
           *description, type_id, area, azimuth, inclination, shading_factor,*
           *cell_surface, num_cells, geometric_concentration,*
           *power_temperature_coefficient, optical_efficiency, cell_efficiency,*
           *spectral_factor, tracking_device_power_losses,*
           *linear_temperature_factor, tracking_error, meter*
      
      .. py:method:: set_pv_type_data
      
         *set_pv_type_data(Dictionary of PV type data, id)*
         
         *Sets data for a PV type.*
         *Possible dictionary entries are:*
           *description, technology, module_nominal_efficiency, noct, ref_irradiance,*
           *temp_coefficient, degradation_factor, electrical_conversion_efficiency, meter*
      
      .. py:method:: set_wind_data
      
         *set_wind_data(Dictionary of wind data)*
         
         *Sets wind data.*
         *Possible dictionary entries are:*
           *is_enabled, hub_height, rated_power, meter*
         
         *set_wind_data(Dictionary of wind data)*
         
         *Sets wind data.*
         *Possible dictionary entries are:*
           *is_enabled, hub_height, rated_power, meter*
      
   .. py:class:: VERoomData
   
      *Interface for VERoomData object.*
   
      .. py:method:: get_air_exchanges
      
         *Get the room's air exchanges.*
         *Returns:*
             *List of RoomAirExchange objects.*
      
      .. py:method:: get_apache_systems
      
         *Gets the system data.*
         *Returns:*
             *Dictionary with the following information, including whether values are*
             *from template:*
             *- Systems: HVAC system ID, methodology and whether the space is conditioned; auxiliary ventilation system ID and whether it matches*
               *the HVAC system; DHW system ID and whether it matches the HVAC system*
             *- Heating: size (kW), radiant fraction, supply air temperature and whether the heating capacity*
               *is unlimited. If the capacity is not unlimited then the capacity and its*
               *units are included.*
             *- Cooling: size (kW), radiant fraction, supply air temperature and whether the cooling capacity*
               *is unlimited. If the capacity is not unlimited then the capacity and its*
               *units are included.*
             *- Outside air supply: flow rate and units, free cooling flow capacity and*
               *units, and variation profile ID.*
             *- Ventilation & extract: whether room has local mechanical exhaust. If it*
               *does then also included are: the extract flow rate and units, SFP (W/l/s)*
               *and whether the extract fan is remote from the room.*
         
             *Additional data is provided for HVAC and NCM modes.*
      
      .. py:method:: get_building_regs
      
         *get_building_regs() -> dict*
         
         *Get the room's building regulation data. Only use this on NCM models.*
         *Returns:*
             *Dictionary with the following entries:*
             *include_room_in_building_regs_analysis, room_type, room_type_from_template,*
             *external_ventilation_rate, external_ventilation_rate_from_template,*
             *associated_occupied_room, ncm_building_area_type, ncm_building_area_type_from_template,*
             *ncm_activity, ncm_activity_from_template, room_part_of_core_area,*
             *high_pressure_drop_air_treatment, high_pressure_drop_air_treatment_from_template,*
             *criterion_3_status, criterion_3_solar_gain_total, criterion_3_solar_gain_benchmark,*
             *section_63_loft_access, section_63_loft_access_from_template, destratification_fans,*
             *air_permeability and dhw_pipe_length*
      
      .. py:method:: get_general
      
         *Gets the general room data.*
         *Returns:*
             *Dictionary with the following information:*
             *- Body name & ID*
             *- General and thermal templates assigned to the body*
             *- Room volume (m^3) and floor area (m^2)*
             *- Lettable percentage, circulation percentage, whether or not the floor*
               *area is included in the building floor area, and whether these values are*
               *from template.*
      
      .. py:method:: get_internal_gains
      
         *Get the room's internal gains.*
         *Returns:*
             *List of RoomInternalGain objects (lighting/power/people).*
      
      .. py:method:: get_ncm_lighting
      
         *get_ncm_lighting() -> dict*
         
         *Get NCM lighting data. Only use this on NCM models.*
         *Returns:*
           *Dictionary with the following entries:*
           *lighting_case, design_illuminance, wattage, wattage_unit, lumens_circuit_watt,*
           *light_output_ratio, lamp_type, luminaires_fitted, use_efficient_lamps, lamp_efficacy,*
           *has_display_lighting, display_lighting_time_switching,*
           *constant_illuminance_control, use_photoelectric,*
           *different_sensor_control_back, control_type, sensor_type,*
           *photoelectric_time_switch_control, photoelectric_parasitic_power,*
           *photoelectric_parasitic_power_default, photoelectric_parasitic_power_unit,*
           *automatic_daylight_zoning, automatic_daylight_zoning_percentage, occupancy_sensing,*
           *occupancy_parasitic_power, occupancy_parasitic_power_default,*
           *occupancy_parasitic_power_unit and occupancy_time_switch_control*
      
      .. py:method:: get_necb_2017_lighting_controls
      
      
      .. py:method:: get_room_conditions
      
         *Gets the room conditions.*
         *Returns:*
             *Dictionary with the following information, including whether values are*
             *from template:*
             *- Heating: profile ID, whether setpoint is timed/constant/two-value, and either*
               *setpoint values (C) or setpoint profile ID*
             *- Cooling: profile ID, whether setpoint is timed/constant/two-value, and either*
               *setpoint values (C) or setpoint profile ID*
             *- DHW: value and units, whether DHW is linked to occupancy or an independent*
               *profile and a usage profile ID if relevant*
             *- Plant (auxiliary energy): profile type and profile ID.*
             *- Solar reflected fraction*
             *- Furniture mass factor*
             *- Humidity control: percentage saturation lower/upper limits and max heating*
               *(+ humidification) and max dehumidification (+ cooling), in kW.*
         
             *Additional data is provided for HVAC mode.*
      
      .. py:method:: get_transpired_solar_collectors
      
         *get_transpired_solar_collectors() -> list*
         
         *Get the room's transpired solar collectors. Only use this on NCM models.*
         *Returns:*
           *List containing a dictionary for each transpired solar collector.*
           *Dictionary contains the following entries:*
           *surface_number, adjacency_area and collector_area*
      
      .. py:property:: id
      
         *(str) ID of the body that the room data is for*
      
      .. py:method:: set
      
         *set_all(general_data, room_conditions_data, systems_data)*
         
         *Sets all non-NCM room data using the provided dictionaries.*
         *See set_general(), set_room_conditions() and set_apache_systems()*
         *for dictionary keys.*
      
      .. py:method:: set_apache_systems
      
         *set_apache_systems(data)*
         
         *Sets system data from the provided dictionary.*
         *Possible dictionary keys are:*
           *HVAC_system, HVAC_system_from_template, HVAC_methodology, HVAC_methodology_from_template,*
           *aux_vent_system, aux_vent_system_from_template,*
           *aux_vent_system_same, cooling_capacity_unit,*
           *cooling_capacity_unlimited, cooling_capacity_unlimited_from_template,*
           *cooling_capacity_value, cooling_plant_radiant_fraction,*
           *cooling_plant_radiant_fraction_from_template,*
           *cooling_unit_size, dhw_system, dhw_system_from_template, dhw_system_same,*
           *extract_fan_is_remote, extract_flow_rate, extract_flow_rate_unit,*
           *has_mech_exhaust, heating_capacity_unit, heating_capacity_unlimited,*
           *heating_capacity_unlimited_from_template, heating_capacity_value,*
           *heating_plant_radiant_fraction, heating_plant_radiant_fraction_from_template,*
           *heating_unit_size, system_air_free_cooling, system_air_free_cooling_from_template,*
           *system_air_minimum_flowrate,*
           *system_air_minimum_flowrate_from_template,*
           *system_air_variation_profile, system_air_variation_profile_from_template,*
           *associated_return_air_plenum, associated_supply_air_plenum,*
           *auto_associate_adjacent_plenums,*
           *supply_condition, supply_condition_profile, supply_condition_template,*
           *include_in_room_zone_loads_analysis, include_in_room_zone_loads_analysis_template*
           *mech_supply_in_room, mech_sfp, demand_controlled_ventilation_type,*
           *demand_controlled_ventilation_air_flow, heat_recovery, seasonal_efficiency,*
           *use_default_seasonal_efficiency, use_night_cooling, night_cooling_sfp,*
           *night_cooling_max_flow_rate, night_cooling_max_hrs_month, scope_of_extract_system,*
           *cooling_design_supply_temp, cooling_design_supply_temp_from_template,*
           *heating_design_supply_temp, heating_design_supply_temp_from_template,*
           *outside_air_ventilation_increase, outside_air_ventilation_increase_from_template*
         
         *set_apache_systems(data)*
         
         *Sets system data from the provided dictionary.*
         *Possible dictionary keys are:*
           *HVAC_system, HVAC_system_from_template, HVAC_methodology, HVAC_methodology_from_template,*
           *aux_vent_system, aux_vent_system_from_template,*
           *aux_vent_system_same, cooling_capacity_unit,*
           *cooling_capacity_unlimited, cooling_capacity_unlimited_from_template,*
           *cooling_capacity_value, cooling_plant_radiant_fraction,*
           *cooling_plant_radiant_fraction_from_template,*
           *cooling_unit_size, dhw_system, dhw_system_from_template, dhw_system_same,*
           *extract_fan_is_remote, extract_flow_rate, extract_flow_rate_unit,*
           *has_mech_exhaust, heating_capacity_unit, heating_capacity_unlimited,*
           *heating_capacity_unlimited_from_template, heating_capacity_value,*
           *heating_plant_radiant_fraction, heating_plant_radiant_fraction_from_template,*
           *heating_unit_size, system_air_free_cooling, system_air_free_cooling_from_template,*
           *system_air_minimum_flowrate,*
           *system_air_minimum_flowrate_from_template,*
           *system_air_variation_profile, system_air_variation_profile_from_template,*
           *associated_return_air_plenum, associated_supply_air_plenum,*
           *auto_associate_adjacent_plenums,*
           *supply_condition, supply_condition_profile, supply_condition_template,*
           *include_in_room_zone_loads_analysis, include_in_room_zone_loads_analysis_template*
           *mech_supply_in_room, mech_sfp, demand_controlled_ventilation_type,*
           *demand_controlled_ventilation_air_flow, heat_recovery, seasonal_efficiency,*
           *use_default_seasonal_efficiency, use_night_cooling, night_cooling_sfp,*
           *night_cooling_max_flow_rate, night_cooling_max_hrs_month, scope_of_extract_system,*
           *cooling_design_supply_temp, cooling_design_supply_temp_from_template,*
           *heating_design_supply_temp, heating_design_supply_temp_from_template,*
           *outside_air_ventilation_increase, outside_air_ventilation_increase_from_template*
      
      .. py:method:: set_building_regs
      
         *set_building_regs(data)*
         
         *Sets building regs data from the provided dictionary.*
         *Possible dictionary keys are:*
         *include_room_in_building_regs_analysis, room_type, room_type_from_template,*
         *external_ventilation_rate, external_ventilation_rate_from_template,*
         *associated_occupied_room, ncm_building_area_type, ncm_building_area_type_from_template,*
         *ncm_activity, ncm_activity_from_template, room_part_of_core_area,*
         *high_pressure_drop_air_treatment,*
         *high_pressure_drop_air_treatment_from_template,section_63_loft_access,*
         *section_63_loft_access_from_template, destratification_fans, air_permeability,*
         *dhw_pipe_length*
      
      .. py:method:: set_collector_area
      
         *set_collector_area(surface_number, collector_area)*
         *Sets the collector area for the transpired solar collector of the indicated surface.*
      
      .. py:method:: set_general
      
         *set_general(data)*
         
         *Sets general room data from the provided dictionary.*
         *Possible dictionary keys are:*
           *circ_perc, circ_perc_from_template,*
           *included_in_building_floor_area,*
           *included_in_building_floor_area_from_template, lettable_perc,*
           *lettable_perc_from_template and name*
         
         *set_general(data)*
         
         *Sets general room data from the provided dictionary.*
         *Possible dictionary keys are:*
           *circ_perc, circ_perc_from_template,*
           *included_in_building_floor_area,*
           *included_in_building_floor_area_from_template, lettable_perc,*
           *lettable_perc_from_template and name*
      
      .. py:method:: set_ncm_lighting
      
         *set_ncm_lighting(data)*
         
         *Sets NCM lighting data from the provided dictionary.*
         *Possible dictionary keys are:*
         *lighting_case, design_illuminance, wattage, wattage_unit, lumens_circuit_watt,*
         *light_output_ratio, lamp_type, luminaires_fitted, use_efficient_lamps, lamp_efficacy,*
         *display_lighting_time_switching,*
         *constant_illuminance_control, use_photoelectric, different_sensor_control_back,*
         *control_type, sensor_type, photoelectric_time_switch_control,*
         *photoelectric_parasitic_power, photoelectric_parasitic_power_default,*
         *photoelectric_parasitic_power_unit, automatic_daylight_zoning,*
         *automatic_daylight_zoning_percentage, occupancy_sensing, occupancy_parasitic_power,*
         *occupancy_parasitic_power_default, occupancy_parasitic_power_unit,*
         *occupancy_time_switch_control*
      
      .. py:method:: set_room_conditions
      
         *set_room_conditions(data)*
         
         *Sets room conditions data from the provided dictionary.*
         *Possible dictionary keys are:*
           *cooling_profile, cooling_profile_from_template, cooling_setpoint,*
           *cooling_setpoint_from_template,*
           *cooling_setpoint_profile, dhw, dhw_from_template, dhw_linked_to_occupancy,*
           *dhw_linked_to_occupancy_from_template, dhw_profile, dhw_profile_from_template,*
           *furniture_mass_factor, furniture_mass_factor_from_template,*
           *heating_profile, heating_profile_from_template, heating_setpoint,*
           *heating_setpoint_from_template,*
           *heating_setpoint_profile, plant_profile,*
           *plant_profile_from_template, plant_profile_type, sat_perc_lower,*
           *sat_perc_lower_from_template, sat_perc_upper, sat_perc_upper_from_template,*
           *solar_reflected_fraction, solar_reflected_fraction_from_template,*
           *dhw_room_level_setting, dhw_room_level_setting_from_template, ncm_plant_profile,*
           *heating_setpoint_type, heating_setpoint_twovalue_profile,*
           *heating_setpoint_twovalue_main_setpoint, heating_setpoint_twovalue_setback,*
           *cooling_setpoint_type, cooling_setpoint_twovalue_profile,*
           *cooling_setpoint_twovalue_main_setpoint, cooling_setpoint_twovalue_setback*
         
         *set_room_conditions(data)*
         
         *Sets room conditions data from the provided dictionary.*
         *Possible dictionary keys are:*
           *cooling_profile, cooling_profile_from_template, cooling_setpoint,*
           *cooling_setpoint_from_template,*
           *cooling_setpoint_profile, dhw, dhw_from_template, dhw_linked_to_occupancy,*
           *dhw_linked_to_occupancy_from_template, dhw_profile, dhw_profile_from_template,*
           *furniture_mass_factor, furniture_mass_factor_from_template,*
           *heating_profile, heating_profile_from_template, heating_setpoint,*
           *heating_setpoint_from_template,*
           *heating_setpoint_profile, plant_profile,*
           *plant_profile_from_template, plant_profile_type, sat_perc_lower,*
           *sat_perc_lower_from_template, sat_perc_upper, sat_perc_upper_from_template,*
           *solar_reflected_fraction, solar_reflected_fraction_from_template,*
           *dhw_room_level_setting, dhw_room_level_setting_from_template, ncm_plant_profile,*
           *heating_setpoint_type, heating_setpoint_twovalue_profile,*
           *heating_setpoint_twovalue_main_setpoint, heating_setpoint_twovalue_setback,*
           *cooling_setpoint_type, cooling_setpoint_twovalue_profile,*
           *cooling_setpoint_twovalue_main_setpoint, cooling_setpoint_twovalue_setback*
      
   .. py:class:: VESankey
   
      *VESankey(ordering).*
      *ordering specifies the type of ordering the diagram should follow. Options are:*
              *-"given": nodes are in the order they are given in set_node_names*
              *-"depth": nodes are added in a depth-first ordering from those in the first columns set by set_node_columns*
      
      *Basic usage:*
          *sankey = iesve.VESankey()*
          *sankey.setTitle(title)*
          *sankey.setColNames(colNames)*
          *sankey.generateEnergySankey(filepath, data)*
   
      .. py:method:: add_column_names
      
         *set_column_names([column names])*
         
         *Sets the names of the columns in the Sankey.*
      
      .. py:method:: add_connections
      
         *set_connections([(source node, destination node, weight)])*
         
         *Sets the connections between nodes.*
                 *source node (str) - source node identifier*
                 *destination node (str) - destination node identifier*
                 *weight (real) - weight for this connection*
      
      .. py:method:: add_node_colours
      
         *add_node_colours({node name: (red, green, blue)})*
         
         *Sets the colour for each node to be displayed as.*
      
      .. py:method:: add_node_columns
      
         *set_node_columns({node name: column index})*
         
         *Sets the column indices for each names node added to the Sankey.*
      
      .. py:method:: add_node_names_in_order
      
         *set_node_names_in_order([node names])*
         
         *Sets the names of the nodes in the Sankey in the given order.*
      
      .. py:method:: clear
      
         *clear()*
         
         *Clears all nodes and connections in the sankey.*
      
      .. py:method:: generate_sankey
      
         *generate_sankey(filepath)*
         
         *Generates a sankey diagram  and saves it to an image at the path specified by filepath.*
      
      .. py:method:: recommended_ratio
      
         *recommended_ratio() -> real*
         
         *Returns the ratio the Sankey generator recommends and will use by default if not set with set_weight_width_ratio().*
      
      .. py:method:: save_png
      
         *save_png(filename)*
         
         *Saves the Sankey diagram to a .png file called filename*
      
      .. py:method:: save_svg
      
         *save_png(filename)*
         
         *Saves the Sankey diagram to a .svg file called filename*
      
      .. py:method:: set_title
      
         *set_title(title)*
         
         *Sets the title for the Sankey.*
      
      .. py:method:: set_units_str
      
         *set_units_str(units)*
         
         *Sets the string to be used to represent the Units the weights are in.*
      
      .. py:method:: set_weight_width_ratio
      
         *set_weight_width_ratio(ratio)*
         
         *Sets the weight to line-width ratio the diagram should use.*
      
   .. py:class:: VESuncast
   
      *Interface for Suncast*
   
      .. py:method:: get_results
      
         *get_results(shading_filename, body_index, surface_index, surface_id, opening_num) -> list*
         
         *Get Suncast insolation data.*
         *Returns a list of lists of dictionaries.*
         *Returns data for the surface unless an opening number of 1 or greater is provided (optional).*
         *Each list represents a month of the year.*
         *The sub-list contains a dictionary of data for each hour of the design day.*
         *The dictionary contains the following entries:*
         
         *external, external_pc, internal, internal_pc*
      
      .. py:method:: get_solar_altitudes
      
         *design_day*
      
      .. py:method:: get_sun_up_down
      
         *get_sun_up_down() -> list*
         
         *Get sun up/down times as a list containing a dictionary of data for each day of the year.*
         *The dictionary contains the following entries:*
         
         *date, up_time, up_azi, down_time, down_azi*
      
      .. py:method:: run
      
         *run(from_month, to_month, design_day, use_diffuse)*
         
         *Run a Suncast simulation*
      
   .. py:class:: VESurface
   
      *Surface.Basic usage:*
      
      *see VESurface_basic.py*
   
      .. py:method:: get_adjacencies
      
         *get_adjacencies() ->  [ adjacency ]*
         
         *Returns a list of VEAdjacency objects for the surface.*
      
      .. py:method:: get_areas
      
         *get_areas() ->  Dictionary (area type)*
         
         *Returns the various area values for the surface (all in m2)*
         *area type = total_gross, total_net, total_window, total_door, total_hole, total_gross_openings.*
         *internal_gross, internal_net, internal_window, internal_door, internal_hole,*
         *internal_gross_openings, external_gross, external_net, external_window, external_door,*
         *external_hole, external_gross_openings*
      
      .. py:method:: get_constructions
      
         *get_constructions()  ->  [ constructionId ]*
         
         *Returns a list of construction IDs (string) used in the surface (including the*
         *constructions assigned to any openings in the surface.*
      
      .. py:method:: get_opening_by_id
      
         *get_opening_by_id() -> opening*
         
         *Returns the opening associated to the id (VEGeometry object)*
      
      .. py:method:: get_opening_totals
      
         *get_opening_totals() ->  Dictionary (opening type)*
         
         *Returns the number of openings of each of the following types:*
         *openings, doors, holes, windows, external_doors, external_holes, external_windows.*
      
      .. py:method:: get_openings
      
         *get_openings() -> [openings]*
         
         *Returns a list of openings (VEGeometry objects)*
      
      .. py:method:: get_properties
      
         *get_properties() ->  Dictionary (property)*
         
         *Returns assorted properties of the surface*
          *- type (string)*
          *- area (m2) surface area*
          *- thickness (meters) the fixed inner volume offset if it has been set, else construction thickness*
          *- orientation (degrees from north) angle of orientation, not adjusted for site angle*
          *- tilt (degrees from horizontal) tilt angle, where 0 is straight up, 90 = vertical*
          *- aps_handle (int, id) the aps handle used by the results reader.*
          *- id (string) Surface ID*
      
      .. py:method:: id
      
         *get_id()*
         
         *Gets the surface ID*
      
      .. py:property:: index
      
         *(int) Index of Surface within parent body.*
      
      .. py:method:: move
      
         *move(distance)*
         
         *Moves the surface by the distance provided*
      
      .. py:property:: type
      
         *(VESurface_type enum) Surface type.*
      
   .. py:class:: VESurface_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ceiling
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ceiling".
      
      .. py:property:: ext_door
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "ext_door".
      
      .. py:property:: ext_glazing
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "ext_glazing".
      
      .. py:property:: ext_wall
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ext_wall".
      
      .. py:property:: floor
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "floor".
      
      .. py:property:: ground_floor
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "ground_floor".
      
      .. py:property:: hole
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 11
         * a name of "hole".
      
      .. py:property:: int_door
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "int_door".
      
      .. py:property:: int_glazing
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "int_glazing".
      
      .. py:property:: int_wall
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "int_wall".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'floor': iesve.VESurface_type.floor
             'ceiling': iesve.VESurface_type.ceiling
             'ext_wall': iesve.VESurface_type.ext_wall
             'int_glazing': iesve.VESurface_type.int_glazing
             'ext_glazing': iesve.VESurface_type.ext_glazing
             'int_door': iesve.VESurface_type.int_door
             'ext_door': iesve.VESurface_type.ext_door
             'ground_floor': iesve.VESurface_type.ground_floor
             'roof': iesve.VESurface_type.roof
             'roof_glazing': iesve.VESurface_type.roof_glazing
             'int_wall': iesve.VESurface_type.int_wall
             'hole': iesve.VESurface_type.hole
            }
      
      .. py:property:: roof
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "roof".
      
      .. py:property:: roof_glazing
         :classmethod:
         :type: iesve.VESurface_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "roof_glazing".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.VESurface_type.floor
             1: iesve.VESurface_type.ceiling
             2: iesve.VESurface_type.ext_wall
             3: iesve.VESurface_type.int_glazing
             4: iesve.VESurface_type.ext_glazing
             5: iesve.VESurface_type.int_door
             6: iesve.VESurface_type.ext_door
             7: iesve.VESurface_type.ground_floor
             8: iesve.VESurface_type.roof
             9: iesve.VESurface_type.roof_glazing
             10: iesve.VESurface_type.int_wall
             11: iesve.VESurface_type.hole
            }
      
   .. py:class:: VEThermalTemplate
   
      *Thermal template.*
      *Basic usage:*
      
      *proj = iesve.VEProject.get_current_project()*
      *templates = proj.thermal_templates(True)*
   
      .. py:method:: add_air_exchange
      
         *add_air_exchange(airExchange) -> Nothing*
         
         *Add an air exchange to the template.*
      
      .. py:method:: add_gain
      
         *add_gain(casualGain) -> Nothing*
         
         *Add a casual gain to the template.*
      
      .. py:method:: apply_changes
      
         *apply_changes() -> Nothing*
         
         *Apply any changes made to the template to the model.  Note: if this is*
         *not called, changes to the template will not be reflected in the model.*
         *This includes changes to gains and air exchanges for the template.*
      
      .. py:method:: get
      
         *get() -> (roomConditions, apSystems, casualGains, airExchanges)*
         
         *Returns a tuple containing all the details for the thermal template.*
      
      .. py:method:: get_air_exchanges
      
         *get_air_exchanges() -> [AirExchanges]*
         
         *Returns a list of Air Exchange objects.*
      
      .. py:method:: get_apache_systems
      
         *get_apache_systems() -> Dictionary*
         
         *Dictionary containing Apache Systems settings.*
      
      .. py:method:: get_casual_gains
      
         *get_casual_gains() -> [Gains]*
         
         *Returns a list of Internal Gain objects.*
      
      .. py:method:: get_room_conditions
      
         *get_room_conditions() -> Dictionary*
         
         *Dictionary containing Room Conditions settings.*
      
      .. py:property:: name
      
         *(str) Template description.*
      
      .. py:method:: remove_air_exchange
      
         *remove_air_exchange(airExchange) -> Nothing*
         
         *Remove air exchange from template.  Will throw exception if air exchange*
         *is not associated with template.*
      
      .. py:method:: remove_gain
      
         *remove_gain(casualGain) -> Nothing*
         
         *Remove casual gain from template.  Will throw exception if gain is*
         *not associated with template.*
      
      .. py:method:: set
      
         *set(room_conditions, system_data)*
         
         *Set both System Data and Room Conditions settings by passing in dictionaries of settings.*
         *See set_apache_systems and set_room_conditions for dictionary keys.*
      
      .. py:method:: set_apache_systems
      
         *set_apache_systems(system_data)*
         
         *Set System Data settings by passing in a dictionary of settings.*
         *Dictionary keys are:*
           *HVAC_system, HVAC_methodology, conditioned, aux_vent_system, aux_vent_system_same, cooling_capacity_units,*
           *cooling_capacity_value, cooling_plant_radiant_fraction,*
           *dhw_system, dhw_system_same, heating_capacity_units,*
           *heating_capacity_value, heating_plant_radiant_fraction, system_air_free_cooling,*
           *system_air_free_cooling_units, system_air_minimum_flowrate, system_air_minimum_flowrate_units,*
           *system_air_variation_profile*
         
         *set_apache_systems(system_data)*
         
         *Set System Data settings by passing in a dictionary of settings.*
         *Dictionary keys are:*
           *HVAC_system, HVAC_methodology, conditioned, aux_vent_system, aux_vent_system_same, cooling_capacity_units,*
           *cooling_capacity_value, cooling_plant_radiant_fraction,*
           *dhw_system, dhw_system_same, heating_capacity_units,*
           *heating_capacity_value, heating_plant_radiant_fraction, system_air_free_cooling,*
           *system_air_free_cooling_units, system_air_minimum_flowrate, system_air_minimum_flowrate_units,*
           *system_air_variation_profile*
      
      .. py:method:: set_room_conditions
      
         *set_room_conditions(room_conditions)*
         
         *Set Room Conditions settings by passing in a dictionary of settings.*
         *Dictionary keys are:*
           *sat_perc_lower, heating_setpoint, cooling_setpoint, dhw_units, cooling_setpoint_profile,*
           *dhw_profile, plant_profile_type, dhw, cooling_setpoint_type, cooling_profile, plant_profile,*
           *sat_perc_upper, heating_profile, heating_setpoint_type, heating_setpoint_profile,*
           *heating_setpoint_twovalue_profile, heating_setpoint_twovalue_main_setpoint,*
           *heating_setpoint_twovalue_setback, cooling_setpoint_twovalue_profile,*
           *cooling_setpoint_twovalue_main_setpoint, cooling_setpoint_twovalue_setback*
         
         *set_room_conditions(room_conditions)*
         
         *Set Room Conditions settings by passing in a dictionary of settings.*
         *Dictionary keys are:*
           *sat_perc_lower, heating_setpoint, cooling_setpoint, dhw_units, cooling_setpoint_profile,*
           *dhw_profile, plant_profile_type, dhw, cooling_setpoint_type, cooling_profile, plant_profile,*
           *sat_perc_upper, heating_profile, heating_setpoint_type, heating_setpoint_profile,*
           *heating_setpoint_twovalue_profile, heating_setpoint_twovalue_main_setpoint,*
           *heating_setpoint_twovalue_setback, cooling_setpoint_twovalue_profile,*
           *cooling_setpoint_twovalue_main_setpoint, cooling_setpoint_twovalue_setback*
      
      .. py:property:: standard
      
         *(enum VEThermalTemplate_standard) Standard for template.*
      
   .. py:class:: VEThermalTemplate_standard
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: NCM
         :classmethod:
         :type: iesve.VEThermalTemplate_standard
      
         An instance of this class with:
         
         * a value of 1
         * a name of "NCM".
      
      .. py:property:: NECB
         :classmethod:
         :type: iesve.VEThermalTemplate_standard
      
         An instance of this class with:
         
         * a value of 4
         * a name of "NECB".
      
      .. py:property:: PRM_FloridaECB
         :classmethod:
         :type: iesve.VEThermalTemplate_standard
      
         An instance of this class with:
         
         * a value of 2
         * a name of "PRM_FloridaECB".
      
      .. py:property:: generic
         :classmethod:
         :type: iesve.VEThermalTemplate_standard
      
         An instance of this class with:
         
         * a value of 0
         * a name of "generic".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'generic': iesve.VEThermalTemplate_standard.generic
             'NCM': iesve.VEThermalTemplate_standard.NCM
             'PRM_FloridaECB': iesve.VEThermalTemplate_standard.PRM_FloridaECB
             'NECB': iesve.VEThermalTemplate_standard.NECB
             't24': iesve.VEThermalTemplate_standard.t24
            }
      
      .. py:property:: t24
         :classmethod:
         :type: iesve.VEThermalTemplate_standard
      
         An instance of this class with:
         
         * a value of 3
         * a name of "t24".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.VEThermalTemplate_standard.generic
             1: iesve.VEThermalTemplate_standard.NCM
             2: iesve.VEThermalTemplate_standard.PRM_FloridaECB
             4: iesve.VEThermalTemplate_standard.NECB
             3: iesve.VEThermalTemplate_standard.t24
            }
      
   .. py:class:: VariableSource
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'system': iesve.VariableSource.system
             'project': iesve.VariableSource.project
            }
      
      .. py:property:: project
         :classmethod:
         :type: iesve.VariableSource
      
         An instance of this class with:
         
         * a value of 1
         * a name of "project".
      
      .. py:property:: system
         :classmethod:
         :type: iesve.VariableSource
      
         An instance of this class with:
         
         * a value of 0
         * a name of "system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.VariableSource.system
             1: iesve.VariableSource.project
            }
      
   .. py:class:: VariableType
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: derived
         :classmethod:
         :type: iesve.VariableType
      
         An instance of this class with:
         
         * a value of 1
         * a name of "derived".
      
      .. py:property:: energy_meter
         :classmethod:
         :type: iesve.VariableType
      
         An instance of this class with:
         
         * a value of 3
         * a name of "energy_meter".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'standard': iesve.VariableType.standard
             'derived': iesve.VariableType.derived
             'process': iesve.VariableType.process
             'energy_meter': iesve.VariableType.energy_meter
            }
      
      .. py:property:: process
         :classmethod:
         :type: iesve.VariableType
      
         An instance of this class with:
         
         * a value of 2
         * a name of "process".
      
      .. py:property:: standard
         :classmethod:
         :type: iesve.VariableType
      
         An instance of this class with:
         
         * a value of 0
         * a name of "standard".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.VariableType.standard
             1: iesve.VariableType.derived
             2: iesve.VariableType.process
             3: iesve.VariableType.energy_meter
            }
      
   .. py:class:: VolumeCapMode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: fixed_height
         :classmethod:
         :type: iesve.VolumeCapMode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "fixed_height".
      
      .. py:property:: height_of_largest_ceiling
         :classmethod:
         :type: iesve.VolumeCapMode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "height_of_largest_ceiling".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.VolumeCapMode.none
             'height_of_largest_ceiling': iesve.VolumeCapMode.height_of_largest_ceiling
             'fixed_height': iesve.VolumeCapMode.fixed_height
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.VolumeCapMode
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.VolumeCapMode.none
             0: iesve.VolumeCapMode.height_of_largest_ceiling
             1: iesve.VolumeCapMode.fixed_height
            }
      
   .. py:class:: WeatherFileReader
   
      *Interface for working with weather files (fwt and epw).*
      *Basic usage:*
          *wea_file = iesve.WeatherFileReader()*
          *result = wea_file.open_weather_file( '\WashingtonTMY2.fwt' )*
          *assert result > 0, 'Error opening weather file.'*
   
      .. py:method:: close
      
         *close( )*
         
         *Close weather file.*
      
      .. py:property:: feb29
      
         *(bool) True if year has February 29th (leap year), false otherwise.*
      
      .. py:method:: get_results
      
         *get_results( (int)variable, (int)startDay, (int)endDay ) ->*
             *Numpy array of floats*
         
         *Read a variable out of the weather file.  The available variables are:*
           *1: Cloud cover (Units: Oktas)*
           *2: Wind direction [E of N] (Units: Degrees)*
           *3: Dry bulb temperature (Units: Degrees C)*
           *4: Wet bulb temperature (Units: Degrees C)*
           *5: Direct normal radiation (Units: W/m2)*
           *6: Diffuse horizontal radiation (Units: W/m2)*
           *7: Solar altitude (Units: Degrees)*
           *8: Solar azimuth (Units: Degrees)*
           *9: Atmospheric pressure (Pa)*
          *10: Wind speed (m/s)*
          *11: Relative humidity (Units: %)*
          *12: Humidity ratio (moisture content) (Units: kg/kg)*
          *13: Global radiation (Units: W/m2)*
          *14: Dew point temperature (Units: Degrees C)*
      
      .. py:property:: lat
      
         *(float) Weather site latitude.*
      
      .. py:property:: long
      
         *(float) Weather site longitude.*
      
      .. py:method:: open_weather_file
      
         *open_weather_file( (str)filename ) -> int*
         
         *Load a weather file indicated by filename.*
         *Returns > 0 on success, <= 0 on error.*
      
      .. py:property:: site
      
         *(str) Weather site description.*
      
      .. py:property:: solar_rad_convention
      
         *(string) Solar rad convention.*
      
      .. py:property:: start_weekday
      
         *(string) First day of the year*
      
      .. py:property:: time_convention
      
         *(string) Time convention.*
      
      .. py:property:: time_zone
      
         *(float) Weather site time zone (hours ahead of GMT).*
      
      .. py:property:: year
      
         *(int) Weather data start year.*
      
   .. py:class:: air_flow_regulation_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_flow_damper_control
         :classmethod:
         :type: iesve.air_flow_regulation_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_flow_damper_control".
      
      .. py:property:: air_flow_speed_control
         :classmethod:
         :type: iesve.air_flow_regulation_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "air_flow_speed_control".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_flow_damper_control': iesve.air_flow_regulation_type.air_flow_damper_control
             'air_flow_speed_control': iesve.air_flow_regulation_type.air_flow_speed_control
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.air_flow_regulation_type.air_flow_damper_control
             1: iesve.air_flow_regulation_type.air_flow_speed_control
            }
      
   .. py:class:: angular_dependence_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant
         :classmethod:
         :type: iesve.angular_dependence_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "constant".
      
      .. py:property:: explicit
         :classmethod:
         :type: iesve.angular_dependence_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "explicit".
      
      .. py:property:: fresnel
         :classmethod:
         :type: iesve.angular_dependence_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "fresnel".
      
      .. py:property:: lbnl
         :classmethod:
         :type: iesve.angular_dependence_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "lbnl".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.angular_dependence_type.none
             'fresnel': iesve.angular_dependence_type.fresnel
             'explicit': iesve.angular_dependence_type.explicit
             'constant': iesve.angular_dependence_type.constant
             'lbnl': iesve.angular_dependence_type.lbnl
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.angular_dependence_type
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.angular_dependence_type.none
             0: iesve.angular_dependence_type.fresnel
             1: iesve.angular_dependence_type.explicit
             2: iesve.angular_dependence_type.constant
             3: iesve.angular_dependence_type.lbnl
            }
      
   .. py:class:: attribute_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: active_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "active_attributes".
      
      .. py:property:: bprm_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "bprm_attributes".
      
      .. py:property:: green_mark_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "green_mark_attributes".
      
      .. py:property:: green_star_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "green_star_attributes".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'real_attributes': iesve.attribute_type.real_attributes
             'ncm_attributes': iesve.attribute_type.ncm_attributes
             'bprm_attributes': iesve.attribute_type.bprm_attributes
             't24_attributes': iesve.attribute_type.t24_attributes
             'green_star_attributes': iesve.attribute_type.green_star_attributes
             'new_zealand_attributes': iesve.attribute_type.new_zealand_attributes
             'green_mark_attributes': iesve.attribute_type.green_mark_attributes
             'necb_attributes': iesve.attribute_type.necb_attributes
             'active_attributes': iesve.attribute_type.active_attributes
            }
      
      .. py:property:: ncm_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ncm_attributes".
      
      .. py:property:: necb_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "necb_attributes".
      
      .. py:property:: new_zealand_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "new_zealand_attributes".
      
      .. py:property:: real_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "real_attributes".
      
      .. py:property:: t24_attributes
         :classmethod:
         :type: iesve.attribute_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "t24_attributes".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.attribute_type.real_attributes
             1: iesve.attribute_type.ncm_attributes
             2: iesve.attribute_type.bprm_attributes
             3: iesve.attribute_type.t24_attributes
             4: iesve.attribute_type.green_star_attributes
             5: iesve.attribute_type.new_zealand_attributes
             6: iesve.attribute_type.green_mark_attributes
             7: iesve.attribute_type.necb_attributes
             10: iesve.attribute_type.active_attributes
            }
      
   .. py:class:: cmm_free_cooling
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: mechanical_ventilation
         :classmethod:
         :type: iesve.cmm_free_cooling
      
         An instance of this class with:
         
         * a value of 2
         * a name of "mechanical_ventilation".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_a_cmm_system': iesve.cmm_free_cooling.not_a_cmm_system
             'natural_ventilation': iesve.cmm_free_cooling.natural_ventilation
             'mechanical_ventilation': iesve.cmm_free_cooling.mechanical_ventilation
            }
      
      .. py:property:: natural_ventilation
         :classmethod:
         :type: iesve.cmm_free_cooling
      
         An instance of this class with:
         
         * a value of 1
         * a name of "natural_ventilation".
      
      .. py:property:: not_a_cmm_system
         :classmethod:
         :type: iesve.cmm_free_cooling
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_a_cmm_system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.cmm_free_cooling.not_a_cmm_system
             1: iesve.cmm_free_cooling.natural_ventilation
             2: iesve.cmm_free_cooling.mechanical_ventilation
            }
      
   .. py:class:: condition_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: external_air
         :classmethod:
         :type: iesve.condition_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "external_air".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'external_air': iesve.condition_type.external_air
             'temperature_from_profile': iesve.condition_type.temperature_from_profile
            }
      
      .. py:property:: temperature_from_profile
         :classmethod:
         :type: iesve.condition_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "temperature_from_profile".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.condition_type.external_air
             1: iesve.condition_type.temperature_from_profile
            }
      
   .. py:class:: conditioned_flag
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_free_floating': iesve.conditioned_flag.no_free_floating
             'not_applicable': iesve.conditioned_flag.not_applicable
             'no_tempered': iesve.conditioned_flag.no_tempered
             'yes': iesve.conditioned_flag.yes
            }
      
      .. py:property:: no_free_floating
         :classmethod:
         :type: iesve.conditioned_flag
      
         An instance of this class with:
         
         * a value of 2
         * a name of "no_free_floating".
      
      .. py:property:: no_tempered
         :classmethod:
         :type: iesve.conditioned_flag
      
         An instance of this class with:
         
         * a value of 3
         * a name of "no_tempered".
      
      .. py:property:: not_applicable
         :classmethod:
         :type: iesve.conditioned_flag
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_applicable".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             2: iesve.conditioned_flag.no_free_floating
             0: iesve.conditioned_flag.not_applicable
             3: iesve.conditioned_flag.no_tempered
             1: iesve.conditioned_flag.yes
            }
      
      .. py:property:: yes
         :classmethod:
         :type: iesve.conditioned_flag
      
         An instance of this class with:
         
         * a value of 1
         * a name of "yes".
      
   .. py:class:: construction_class
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: glazed
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 1
         * a name of "glazed".
      
      .. py:property:: hard_landscaping
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 2
         * a name of "hard_landscaping".
      
      .. py:property:: misc
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 5
         * a name of "misc".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.construction_class.none
             'opaque': iesve.construction_class.opaque
             'glazed': iesve.construction_class.glazed
             'hard_landscaping': iesve.construction_class.hard_landscaping
             'soft_landscaping': iesve.construction_class.soft_landscaping
             'shade': iesve.construction_class.shade
             'misc': iesve.construction_class.misc
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: opaque
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 0
         * a name of "opaque".
      
      .. py:property:: shade
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 4
         * a name of "shade".
      
      .. py:property:: soft_landscaping
         :classmethod:
         :type: iesve.construction_class
      
         An instance of this class with:
         
         * a value of 3
         * a name of "soft_landscaping".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.construction_class.none
             0: iesve.construction_class.opaque
             1: iesve.construction_class.glazed
             2: iesve.construction_class.hard_landscaping
             3: iesve.construction_class.soft_landscaping
             4: iesve.construction_class.shade
             5: iesve.construction_class.misc
            }
      
   .. py:class:: demand_controlled_ventilation
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: enhanced_ventilation
         :classmethod:
         :type: iesve.demand_controlled_ventilation
      
         An instance of this class with:
         
         * a value of 3
         * a name of "enhanced_ventilation".
      
      .. py:property:: gas_sensors
         :classmethod:
         :type: iesve.demand_controlled_ventilation
      
         An instance of this class with:
         
         * a value of 2
         * a name of "gas_sensors".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.demand_controlled_ventilation.none
             'occupancy_density': iesve.demand_controlled_ventilation.occupancy_density
             'gas_sensors': iesve.demand_controlled_ventilation.gas_sensors
             'enhanced_ventilation': iesve.demand_controlled_ventilation.enhanced_ventilation
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.demand_controlled_ventilation
      
         An instance of this class with:
         
         * a value of 0
         * a name of "none".
      
      .. py:property:: occupancy_density
         :classmethod:
         :type: iesve.demand_controlled_ventilation
      
         An instance of this class with:
         
         * a value of 1
         * a name of "occupancy_density".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.demand_controlled_ventilation.none
             1: iesve.demand_controlled_ventilation.occupancy_density
             2: iesve.demand_controlled_ventilation.gas_sensors
             3: iesve.demand_controlled_ventilation.enhanced_ventilation
            }
      
   .. py:class:: design_weather_source
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: apl
         :classmethod:
         :type: iesve.design_weather_source
      
         An instance of this class with:
         
         * a value of 2
         * a name of "apl".
      
      .. py:property:: ashrae
         :classmethod:
         :type: iesve.design_weather_source
      
         An instance of this class with:
         
         * a value of 0
         * a name of "ashrae".
      
      .. py:property:: custom
         :classmethod:
         :type: iesve.design_weather_source
      
         An instance of this class with:
         
         * a value of 1
         * a name of "custom".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'ashrae': iesve.design_weather_source.ashrae
             'custom': iesve.design_weather_source.custom
             'apl': iesve.design_weather_source.apl
             'user': iesve.design_weather_source.user
            }
      
      .. py:property:: user
         :classmethod:
         :type: iesve.design_weather_source
      
         An instance of this class with:
         
         * a value of 3
         * a name of "user".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.design_weather_source.ashrae
             1: iesve.design_weather_source.custom
             2: iesve.design_weather_source.apl
             3: iesve.design_weather_source.user
            }
      
   .. py:class:: dhw_parent_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: dedicated_dhw_boiler
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "dedicated_dhw_boiler".
      
      .. py:property:: heat_pump
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "heat_pump".
      
      .. py:property:: instantaneous_combi
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "instantaneous_combi".
      
      .. py:property:: instantaneous_dhw_only
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "instantaneous_dhw_only".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unset': iesve.dhw_parent_type.unset
             'dedicated_dhw_boiler': iesve.dhw_parent_type.dedicated_dhw_boiler
             'standalone_water_heater': iesve.dhw_parent_type.standalone_water_heater
             'instantaneous_dhw_only': iesve.dhw_parent_type.instantaneous_dhw_only
             'instantaneous_combi': iesve.dhw_parent_type.instantaneous_combi
             'heat_pump': iesve.dhw_parent_type.heat_pump
            }
      
      .. py:property:: standalone_water_heater
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "standalone_water_heater".
      
      .. py:property:: unset
         :classmethod:
         :type: iesve.dhw_parent_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unset".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.dhw_parent_type.unset
             1: iesve.dhw_parent_type.dedicated_dhw_boiler
             2: iesve.dhw_parent_type.standalone_water_heater
             3: iesve.dhw_parent_type.instantaneous_dhw_only
             4: iesve.dhw_parent_type.instantaneous_combi
             5: iesve.dhw_parent_type.heat_pump
            }
      
   .. py:class:: eASHRAEStandard
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae_2004_with_addenda
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ashrae_2004_with_addenda".
      
      .. py:property:: ashrae_2007
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 0
         * a name of "ashrae_2007".
      
      .. py:property:: ashrae_2010
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae_2010".
      
      .. py:property:: ashrae_2010_ecb
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 3
         * a name of "ashrae_2010_ecb".
      
      .. py:property:: ashrae_2013
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 4
         * a name of "ashrae_2013".
      
      .. py:property:: ashrae_2013_ecb
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 5
         * a name of "ashrae_2013_ecb".
      
      .. py:property:: ashrae_2016
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 9
         * a name of "ashrae_2016".
      
      .. py:property:: ashrae_2016_appendix_g
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 10
         * a name of "ashrae_2016_appendix_g".
      
      .. py:property:: ashrae_2019
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 13
         * a name of "ashrae_2019".
      
      .. py:property:: ashrae_2019_appendix_g
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 14
         * a name of "ashrae_2019_appendix_g".
      
      .. py:property:: ashrae_standard_not_set
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of -1
         * a name of "ashrae_standard_not_set".
      
      .. py:property:: iecc_2012
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 6
         * a name of "iecc_2012".
      
      .. py:property:: iecc_florida_2014
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 7
         * a name of "iecc_florida_2014".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'ashrae_standard_not_set': iesve.eASHRAEStandard.ashrae_standard_not_set
             'ashrae_2007': iesve.eASHRAEStandard.ashrae_2007
             'ashrae_2004_with_addenda': iesve.eASHRAEStandard.ashrae_2004_with_addenda
             'ashrae_2010': iesve.eASHRAEStandard.ashrae_2010
             'ashrae_2010_ecb': iesve.eASHRAEStandard.ashrae_2010_ecb
             'ashrae_2013': iesve.eASHRAEStandard.ashrae_2013
             'ashrae_2013_ecb': iesve.eASHRAEStandard.ashrae_2013_ecb
             'iecc_2012': iesve.eASHRAEStandard.iecc_2012
             'iecc_florida_2014': iesve.eASHRAEStandard.iecc_florida_2014
             'necb_2011': iesve.eASHRAEStandard.necb_2011
             'ashrae_2016': iesve.eASHRAEStandard.ashrae_2016
             'ashrae_2016_appendix_g': iesve.eASHRAEStandard.ashrae_2016_appendix_g
             'title24_2019': iesve.eASHRAEStandard.title24_2019
             'necb_2017': iesve.eASHRAEStandard.necb_2017
             'ashrae_2019': iesve.eASHRAEStandard.ashrae_2019
             'ashrae_2019_appendix_g': iesve.eASHRAEStandard.ashrae_2019_appendix_g
             'title24_2022': iesve.eASHRAEStandard.title24_2022
            }
      
      .. py:property:: necb_2011
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 8
         * a name of "necb_2011".
      
      .. py:property:: necb_2017
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 12
         * a name of "necb_2017".
      
      .. py:property:: title24_2019
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 11
         * a name of "title24_2019".
      
      .. py:property:: title24_2022
         :classmethod:
         :type: iesve.eASHRAEStandard
      
         An instance of this class with:
         
         * a value of 15
         * a name of "title24_2022".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.eASHRAEStandard.ashrae_standard_not_set
             0: iesve.eASHRAEStandard.ashrae_2007
             1: iesve.eASHRAEStandard.ashrae_2004_with_addenda
             2: iesve.eASHRAEStandard.ashrae_2010
             3: iesve.eASHRAEStandard.ashrae_2010_ecb
             4: iesve.eASHRAEStandard.ashrae_2013
             5: iesve.eASHRAEStandard.ashrae_2013_ecb
             6: iesve.eASHRAEStandard.iecc_2012
             7: iesve.eASHRAEStandard.iecc_florida_2014
             8: iesve.eASHRAEStandard.necb_2011
             9: iesve.eASHRAEStandard.ashrae_2016
             10: iesve.eASHRAEStandard.ashrae_2016_appendix_g
             11: iesve.eASHRAEStandard.title24_2019
             12: iesve.eASHRAEStandard.necb_2017
             13: iesve.eASHRAEStandard.ashrae_2019
             14: iesve.eASHRAEStandard.ashrae_2019_appendix_g
             15: iesve.eASHRAEStandard.title24_2022
            }
      
   .. py:class:: element_categories
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ceiling
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ceiling".
      
      .. py:property:: door
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 8
         * a name of "door".
      
      .. py:property:: double_facade
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 36
         * a name of "double_facade".
      
      .. py:property:: ext_glazing
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 6
         * a name of "ext_glazing".
      
      .. py:property:: foundation
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 25
         * a name of "foundation".
      
      .. py:property:: ground_floor
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 4
         * a name of "ground_floor".
      
      .. py:property:: gutter
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 27
         * a name of "gutter".
      
      .. py:property:: hard_landscape
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 12
         * a name of "hard_landscape".
      
      .. py:property:: hard_parking
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 11
         * a name of "hard_parking".
      
      .. py:property:: hard_pavement
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 13
         * a name of "hard_pavement".
      
      .. py:property:: hard_pervious
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 14
         * a name of "hard_pervious".
      
      .. py:property:: hard_road
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 10
         * a name of "hard_road".
      
      .. py:property:: int_floor
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 1
         * a name of "int_floor".
      
      .. py:property:: int_glazing
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 7
         * a name of "int_glazing".
      
      .. py:property:: local_shade
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 23
         * a name of "local_shade".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'roof': iesve.element_categories.roof
             'ceiling': iesve.element_categories.ceiling
             'wall': iesve.element_categories.wall
             'partition': iesve.element_categories.partition
             'ground_floor': iesve.element_categories.ground_floor
             'roof_light': iesve.element_categories.roof_light
             'ext_glazing': iesve.element_categories.ext_glazing
             'int_glazing': iesve.element_categories.int_glazing
             'door': iesve.element_categories.door
             'int_floor': iesve.element_categories.int_floor
             'hard_road': iesve.element_categories.hard_road
             'hard_parking': iesve.element_categories.hard_parking
             'hard_landscape': iesve.element_categories.hard_landscape
             'hard_pavement': iesve.element_categories.hard_pavement
             'hard_pervious': iesve.element_categories.hard_pervious
             'soft_turf': iesve.element_categories.soft_turf
             'soft_mixed_veg': iesve.element_categories.soft_mixed_veg
             'soft_tree': iesve.element_categories.soft_tree
             'soft_veg_shade': iesve.element_categories.soft_veg_shade
             'soft_shrub': iesve.element_categories.soft_shrub
             'soft_ground': iesve.element_categories.soft_ground
             'soft_wetland': iesve.element_categories.soft_wetland
             'soft_water': iesve.element_categories.soft_water
             'local_shade': iesve.element_categories.local_shade
             'topographical_shade': iesve.element_categories.topographical_shade
             'foundation': iesve.element_categories.foundation
             'struct_fram': iesve.element_categories.struct_fram
             'struct_frame': iesve.element_categories.struct_frame
             'gutter': iesve.element_categories.gutter
             'shape_beam': iesve.element_categories.shape_beam
             'solid_beam': iesve.element_categories.solid_beam
             'shape_column': iesve.element_categories.shape_column
             'solid_column': iesve.element_categories.solid_column
             'shape_lintel': iesve.element_categories.shape_lintel
             'solid_lintel': iesve.element_categories.solid_lintel
             'shape_stair': iesve.element_categories.shape_stair
             'solid_stair': iesve.element_categories.solid_stair
             'double_facade': iesve.element_categories.double_facade
            }
      
      .. py:property:: partition
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 3
         * a name of "partition".
      
      .. py:property:: roof
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 0
         * a name of "roof".
      
      .. py:property:: roof_light
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 5
         * a name of "roof_light".
      
      .. py:property:: shape_beam
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 28
         * a name of "shape_beam".
      
      .. py:property:: shape_column
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 30
         * a name of "shape_column".
      
      .. py:property:: shape_lintel
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 32
         * a name of "shape_lintel".
      
      .. py:property:: shape_stair
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 34
         * a name of "shape_stair".
      
      .. py:property:: soft_ground
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 20
         * a name of "soft_ground".
      
      .. py:property:: soft_mixed_veg
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 16
         * a name of "soft_mixed_veg".
      
      .. py:property:: soft_shrub
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 19
         * a name of "soft_shrub".
      
      .. py:property:: soft_tree
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 17
         * a name of "soft_tree".
      
      .. py:property:: soft_turf
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 15
         * a name of "soft_turf".
      
      .. py:property:: soft_veg_shade
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 18
         * a name of "soft_veg_shade".
      
      .. py:property:: soft_water
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 22
         * a name of "soft_water".
      
      .. py:property:: soft_wetland
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 21
         * a name of "soft_wetland".
      
      .. py:property:: solid_beam
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 29
         * a name of "solid_beam".
      
      .. py:property:: solid_column
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 31
         * a name of "solid_column".
      
      .. py:property:: solid_lintel
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 33
         * a name of "solid_lintel".
      
      .. py:property:: solid_stair
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 35
         * a name of "solid_stair".
      
      .. py:property:: struct_fram
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 26
         * a name of "struct_fram".
      
      .. py:property:: struct_frame
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 26
         * a name of "struct_frame".
      
      .. py:property:: topographical_shade
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 24
         * a name of "topographical_shade".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.element_categories.roof
             1: iesve.element_categories.int_floor
             2: iesve.element_categories.wall
             3: iesve.element_categories.partition
             4: iesve.element_categories.ground_floor
             5: iesve.element_categories.roof_light
             6: iesve.element_categories.ext_glazing
             7: iesve.element_categories.int_glazing
             8: iesve.element_categories.door
             10: iesve.element_categories.hard_road
             11: iesve.element_categories.hard_parking
             12: iesve.element_categories.hard_landscape
             13: iesve.element_categories.hard_pavement
             14: iesve.element_categories.hard_pervious
             15: iesve.element_categories.soft_turf
             16: iesve.element_categories.soft_mixed_veg
             17: iesve.element_categories.soft_tree
             18: iesve.element_categories.soft_veg_shade
             19: iesve.element_categories.soft_shrub
             20: iesve.element_categories.soft_ground
             21: iesve.element_categories.soft_wetland
             22: iesve.element_categories.soft_water
             23: iesve.element_categories.local_shade
             24: iesve.element_categories.topographical_shade
             25: iesve.element_categories.foundation
             26: iesve.element_categories.struct_frame
             27: iesve.element_categories.gutter
             28: iesve.element_categories.shape_beam
             29: iesve.element_categories.solid_beam
             30: iesve.element_categories.shape_column
             31: iesve.element_categories.solid_column
             32: iesve.element_categories.shape_lintel
             33: iesve.element_categories.solid_lintel
             34: iesve.element_categories.shape_stair
             35: iesve.element_categories.solid_stair
             36: iesve.element_categories.double_facade
            }
      
      .. py:property:: wall
         :classmethod:
         :type: iesve.element_categories
      
         An instance of this class with:
         
         * a value of 2
         * a name of "wall".
      
   .. py:class:: extract_system_scope
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: fan_remote_from_zone
         :classmethod:
         :type: iesve.extract_system_scope
      
         An instance of this class with:
         
         * a value of 1
         * a name of "fan_remote_from_zone".
      
      .. py:property:: fan_remote_from_zone_with_grease_filter
         :classmethod:
         :type: iesve.extract_system_scope
      
         An instance of this class with:
         
         * a value of 2
         * a name of "fan_remote_from_zone_with_grease_filter".
      
      .. py:property:: fan_within_zone
         :classmethod:
         :type: iesve.extract_system_scope
      
         An instance of this class with:
         
         * a value of 0
         * a name of "fan_within_zone".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'fan_within_zone': iesve.extract_system_scope.fan_within_zone
             'fan_remote_from_zone': iesve.extract_system_scope.fan_remote_from_zone
             'fan_remote_from_zone_with_grease_filter': iesve.extract_system_scope.fan_remote_from_zone_with_grease_filter
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.extract_system_scope.fan_within_zone
             1: iesve.extract_system_scope.fan_remote_from_zone
             2: iesve.extract_system_scope.fan_remote_from_zone_with_grease_filter
            }
      
   .. py:class:: frame_materials
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: aluminium
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 3
         * a name of "aluminium".
      
      .. py:property:: hardwood
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 1
         * a name of "hardwood".
      
      .. py:property:: metal
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 5
         * a name of "metal".
      
      .. py:property:: metal_with_thermal_break
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 6
         * a name of "metal_with_thermal_break".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.frame_materials.none
             'softwood': iesve.frame_materials.softwood
             'hardwood': iesve.frame_materials.hardwood
             'steel': iesve.frame_materials.steel
             'aluminium': iesve.frame_materials.aluminium
             'pvc': iesve.frame_materials.pvc
             'metal': iesve.frame_materials.metal
             'metal_with_thermal_break': iesve.frame_materials.metal_with_thermal_break
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: pvc
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 4
         * a name of "pvc".
      
      .. py:property:: softwood
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 0
         * a name of "softwood".
      
      .. py:property:: steel
         :classmethod:
         :type: iesve.frame_materials
      
         An instance of this class with:
         
         * a value of 2
         * a name of "steel".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.frame_materials.none
             0: iesve.frame_materials.softwood
             1: iesve.frame_materials.hardwood
             2: iesve.frame_materials.steel
             3: iesve.frame_materials.aluminium
             4: iesve.frame_materials.pvc
             5: iesve.frame_materials.metal
             6: iesve.frame_materials.metal_with_thermal_break
            }
      
   .. py:class:: frame_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: a901_floor_mass
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "a901_floor_mass".
      
      .. py:property:: a901_floor_steel_joist
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "a901_floor_steel_joist".
      
      .. py:property:: a901_floor_wood_framed_and_others
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 11
         * a name of "a901_floor_wood_framed_and_others".
      
      .. py:property:: a901_roof_attic_roof_with_joist
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "a901_roof_attic_roof_with_joist".
      
      .. py:property:: a901_roof_attic_roof_with_steel_joist
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "a901_roof_attic_roof_with_steel_joist".
      
      .. py:property:: a901_roof_insulation_above_deck
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "a901_roof_insulation_above_deck".
      
      .. py:property:: a901_roof_metal_builing
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "a901_roof_metal_builing".
      
      .. py:property:: a901_wall_mass
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "a901_wall_mass".
      
      .. py:property:: a901_wall_metal_builing
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "a901_wall_metal_builing".
      
      .. py:property:: a901_wall_steal_framed
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "a901_wall_steal_framed".
      
      .. py:property:: a901_wall_wood_framed
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "a901_wall_wood_framed".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_frame': iesve.frame_type.no_frame
             'a901_wall_mass': iesve.frame_type.a901_wall_mass
             'a901_wall_metal_builing': iesve.frame_type.a901_wall_metal_builing
             'a901_wall_steal_framed': iesve.frame_type.a901_wall_steal_framed
             'a901_wall_wood_framed': iesve.frame_type.a901_wall_wood_framed
             'a901_roof_metal_builing': iesve.frame_type.a901_roof_metal_builing
             'a901_roof_attic_roof_with_joist': iesve.frame_type.a901_roof_attic_roof_with_joist
             'a901_roof_attic_roof_with_steel_joist': iesve.frame_type.a901_roof_attic_roof_with_steel_joist
             'a901_roof_insulation_above_deck': iesve.frame_type.a901_roof_insulation_above_deck
             'a901_floor_mass': iesve.frame_type.a901_floor_mass
             'a901_floor_steel_joist': iesve.frame_type.a901_floor_steel_joist
             'a901_floor_wood_framed_and_others': iesve.frame_type.a901_floor_wood_framed_and_others
             't24_wall_metal_frame': iesve.frame_type.t24_wall_metal_frame
             't24_wall_metal_builing': iesve.frame_type.t24_wall_metal_builing
             't24_wall_medium_mass': iesve.frame_type.t24_wall_medium_mass
             't24_wall_heavy_mass': iesve.frame_type.t24_wall_heavy_mass
             't24_wall_wood_framed_and_others': iesve.frame_type.t24_wall_wood_framed_and_others
             't24_roof_wood_framed_attic': iesve.frame_type.t24_roof_wood_framed_attic
             't24_roof_wood_framed_rafter': iesve.frame_type.t24_roof_wood_framed_rafter
             't24_roof_structurally_insulated_panel': iesve.frame_type.t24_roof_structurally_insulated_panel
             't24_roof_metal_framed_attic': iesve.frame_type.t24_roof_metal_framed_attic
             't24_roof_metal_framed_rafter': iesve.frame_type.t24_roof_metal_framed_rafter
             't24_roof_metal_builing': iesve.frame_type.t24_roof_metal_builing
             't24_floor_heavy_mass': iesve.frame_type.t24_floor_heavy_mass
             't24_floor_wood_frame': iesve.frame_type.t24_floor_wood_frame
             't24_floor_wood_foam_panel': iesve.frame_type.t24_floor_wood_foam_panel
             't24_floor_metal_frame': iesve.frame_type.t24_floor_metal_frame
            }
      
      .. py:property:: no_frame
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "no_frame".
      
      .. py:property:: t24_floor_heavy_mass
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 23
         * a name of "t24_floor_heavy_mass".
      
      .. py:property:: t24_floor_metal_frame
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 26
         * a name of "t24_floor_metal_frame".
      
      .. py:property:: t24_floor_wood_foam_panel
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 25
         * a name of "t24_floor_wood_foam_panel".
      
      .. py:property:: t24_floor_wood_frame
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 24
         * a name of "t24_floor_wood_frame".
      
      .. py:property:: t24_roof_metal_builing
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 22
         * a name of "t24_roof_metal_builing".
      
      .. py:property:: t24_roof_metal_framed_attic
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 20
         * a name of "t24_roof_metal_framed_attic".
      
      .. py:property:: t24_roof_metal_framed_rafter
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 21
         * a name of "t24_roof_metal_framed_rafter".
      
      .. py:property:: t24_roof_structurally_insulated_panel
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 19
         * a name of "t24_roof_structurally_insulated_panel".
      
      .. py:property:: t24_roof_wood_framed_attic
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 17
         * a name of "t24_roof_wood_framed_attic".
      
      .. py:property:: t24_roof_wood_framed_rafter
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 18
         * a name of "t24_roof_wood_framed_rafter".
      
      .. py:property:: t24_wall_heavy_mass
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 15
         * a name of "t24_wall_heavy_mass".
      
      .. py:property:: t24_wall_medium_mass
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 14
         * a name of "t24_wall_medium_mass".
      
      .. py:property:: t24_wall_metal_builing
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 13
         * a name of "t24_wall_metal_builing".
      
      .. py:property:: t24_wall_metal_frame
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 12
         * a name of "t24_wall_metal_frame".
      
      .. py:property:: t24_wall_wood_framed_and_others
         :classmethod:
         :type: iesve.frame_type
      
         An instance of this class with:
         
         * a value of 16
         * a name of "t24_wall_wood_framed_and_others".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.frame_type.no_frame
             1: iesve.frame_type.a901_wall_mass
             2: iesve.frame_type.a901_wall_metal_builing
             3: iesve.frame_type.a901_wall_steal_framed
             4: iesve.frame_type.a901_wall_wood_framed
             5: iesve.frame_type.a901_roof_metal_builing
             6: iesve.frame_type.a901_roof_attic_roof_with_joist
             7: iesve.frame_type.a901_roof_attic_roof_with_steel_joist
             8: iesve.frame_type.a901_roof_insulation_above_deck
             9: iesve.frame_type.a901_floor_mass
             10: iesve.frame_type.a901_floor_steel_joist
             11: iesve.frame_type.a901_floor_wood_framed_and_others
             12: iesve.frame_type.t24_wall_metal_frame
             13: iesve.frame_type.t24_wall_metal_builing
             14: iesve.frame_type.t24_wall_medium_mass
             15: iesve.frame_type.t24_wall_heavy_mass
             16: iesve.frame_type.t24_wall_wood_framed_and_others
             17: iesve.frame_type.t24_roof_wood_framed_attic
             18: iesve.frame_type.t24_roof_wood_framed_rafter
             19: iesve.frame_type.t24_roof_structurally_insulated_panel
             20: iesve.frame_type.t24_roof_metal_framed_attic
             21: iesve.frame_type.t24_roof_metal_framed_rafter
             22: iesve.frame_type.t24_roof_metal_builing
             23: iesve.frame_type.t24_floor_heavy_mass
             24: iesve.frame_type.t24_floor_wood_frame
             25: iesve.frame_type.t24_floor_wood_foam_panel
             26: iesve.frame_type.t24_floor_metal_frame
            }
      
   .. py:class:: fuel_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: anthracite
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 14
         * a name of "anthracite".
      
      .. py:property:: biogas
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "biogas".
      
      .. py:property:: biomass
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "biomass".
      
      .. py:property:: coal
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "coal".
      
      .. py:property:: district_heating
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 38
         * a name of "district_heating".
      
      .. py:property:: dual
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 16
         * a name of "dual".
      
      .. py:property:: elec
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "elec".
      
      .. py:property:: grid_displaced_elec
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 17
         * a name of "grid_displaced_elec".
      
      .. py:property:: grid_displaced_elec_pv
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 39
         * a name of "grid_displaced_elec_pv".
      
      .. py:property:: lpg
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "lpg".
      
      .. py:property:: misc_a
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "misc_a".
      
      .. py:property:: misc_b
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "misc_b".
      
      .. py:property:: misc_c
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "misc_c".
      
      .. py:property:: misc_d
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 11
         * a name of "misc_d".
      
      .. py:property:: misc_e
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 12
         * a name of "misc_e".
      
      .. py:property:: misc_f
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 13
         * a name of "misc_f".
      
      .. py:property:: misc_g
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 18
         * a name of "misc_g".
      
      .. py:property:: misc_h
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 19
         * a name of "misc_h".
      
      .. py:property:: misc_i
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 20
         * a name of "misc_i".
      
      .. py:property:: misc_j
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 21
         * a name of "misc_j".
      
      .. py:property:: misc_k
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 22
         * a name of "misc_k".
      
      .. py:property:: misc_l
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 23
         * a name of "misc_l".
      
      .. py:property:: misc_m
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 24
         * a name of "misc_m".
      
      .. py:property:: misc_n
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 25
         * a name of "misc_n".
      
      .. py:property:: misc_o
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 26
         * a name of "misc_o".
      
      .. py:property:: misc_p
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 27
         * a name of "misc_p".
      
      .. py:property:: misc_q
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 28
         * a name of "misc_q".
      
      .. py:property:: misc_r
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 29
         * a name of "misc_r".
      
      .. py:property:: misc_s
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 30
         * a name of "misc_s".
      
      .. py:property:: misc_t
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 31
         * a name of "misc_t".
      
      .. py:property:: misc_u
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 32
         * a name of "misc_u".
      
      .. py:property:: misc_v
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 33
         * a name of "misc_v".
      
      .. py:property:: misc_w
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 34
         * a name of "misc_w".
      
      .. py:property:: misc_x
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 35
         * a name of "misc_x".
      
      .. py:property:: misc_y
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 36
         * a name of "misc_y".
      
      .. py:property:: misc_z
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 37
         * a name of "misc_z".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'anthracite': iesve.fuel_type.anthracite
             'biogas': iesve.fuel_type.biogas
             'biomass': iesve.fuel_type.biomass
             'coal': iesve.fuel_type.coal
             'district_heating': iesve.fuel_type.district_heating
             'dual': iesve.fuel_type.dual
             'elec': iesve.fuel_type.elec
             'grid_displaced_elec': iesve.fuel_type.grid_displaced_elec
             'lpg': iesve.fuel_type.lpg
             'misc_a': iesve.fuel_type.misc_a
             'misc_b': iesve.fuel_type.misc_b
             'misc_c': iesve.fuel_type.misc_c
             'misc_d': iesve.fuel_type.misc_d
             'misc_e': iesve.fuel_type.misc_e
             'misc_f': iesve.fuel_type.misc_f
             'misc_g': iesve.fuel_type.misc_g
             'misc_h': iesve.fuel_type.misc_h
             'misc_i': iesve.fuel_type.misc_i
             'misc_j': iesve.fuel_type.misc_j
             'misc_k': iesve.fuel_type.misc_k
             'misc_l': iesve.fuel_type.misc_l
             'misc_m': iesve.fuel_type.misc_m
             'misc_n': iesve.fuel_type.misc_n
             'misc_o': iesve.fuel_type.misc_o
             'misc_p': iesve.fuel_type.misc_p
             'misc_q': iesve.fuel_type.misc_q
             'misc_r': iesve.fuel_type.misc_r
             'misc_s': iesve.fuel_type.misc_s
             'misc_t': iesve.fuel_type.misc_t
             'misc_u': iesve.fuel_type.misc_u
             'misc_v': iesve.fuel_type.misc_v
             'misc_w': iesve.fuel_type.misc_w
             'misc_x': iesve.fuel_type.misc_x
             'misc_y': iesve.fuel_type.misc_y
             'misc_z': iesve.fuel_type.misc_z
             'nat_gas': iesve.fuel_type.nat_gas
             'none': iesve.fuel_type.none
             'oil': iesve.fuel_type.oil
             'smokeless': iesve.fuel_type.smokeless
             'waste': iesve.fuel_type.waste
             'grid_displaced_elec_pv': iesve.fuel_type.grid_displaced_elec_pv
            }
      
      .. py:property:: nat_gas
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "nat_gas".
      
      .. py:property:: none
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: oil
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "oil".
      
      .. py:property:: smokeless
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 15
         * a name of "smokeless".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             14: iesve.fuel_type.anthracite
             2: iesve.fuel_type.biogas
             5: iesve.fuel_type.biomass
             4: iesve.fuel_type.coal
             38: iesve.fuel_type.district_heating
             16: iesve.fuel_type.dual
             6: iesve.fuel_type.elec
             17: iesve.fuel_type.grid_displaced_elec
             1: iesve.fuel_type.lpg
             8: iesve.fuel_type.misc_a
             9: iesve.fuel_type.misc_b
             10: iesve.fuel_type.misc_c
             11: iesve.fuel_type.misc_d
             12: iesve.fuel_type.misc_e
             13: iesve.fuel_type.misc_f
             18: iesve.fuel_type.misc_g
             19: iesve.fuel_type.misc_h
             20: iesve.fuel_type.misc_i
             21: iesve.fuel_type.misc_j
             22: iesve.fuel_type.misc_k
             23: iesve.fuel_type.misc_l
             24: iesve.fuel_type.misc_m
             25: iesve.fuel_type.misc_n
             26: iesve.fuel_type.misc_o
             27: iesve.fuel_type.misc_p
             28: iesve.fuel_type.misc_q
             29: iesve.fuel_type.misc_r
             30: iesve.fuel_type.misc_s
             31: iesve.fuel_type.misc_t
             32: iesve.fuel_type.misc_u
             33: iesve.fuel_type.misc_v
             34: iesve.fuel_type.misc_w
             35: iesve.fuel_type.misc_x
             36: iesve.fuel_type.misc_y
             37: iesve.fuel_type.misc_z
             0: iesve.fuel_type.nat_gas
             -1: iesve.fuel_type.none
             3: iesve.fuel_type.oil
             15: iesve.fuel_type.smokeless
             7: iesve.fuel_type.waste
             39: iesve.fuel_type.grid_displaced_elec_pv
            }
      
      .. py:property:: waste
         :classmethod:
         :type: iesve.fuel_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "waste".
      
   .. py:class:: glazing_types
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: double_glazed_air_or_argon_filled
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 1
         * a name of "double_glazed_air_or_argon_filled".
      
      .. py:property:: double_glazed_low_e_hard_coat
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 2
         * a name of "double_glazed_low_e_hard_coat".
      
      .. py:property:: double_glazed_low_e_soft_coat
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 3
         * a name of "double_glazed_low_e_soft_coat".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.glazing_types.none
             'single_glazed': iesve.glazing_types.single_glazed
             'double_glazed_air_or_argon_filled': iesve.glazing_types.double_glazed_air_or_argon_filled
             'double_glazed_low_e_hard_coat': iesve.glazing_types.double_glazed_low_e_hard_coat
             'double_glazed_low_e_soft_coat': iesve.glazing_types.double_glazed_low_e_soft_coat
             'triple_glazed_air_or_argon_filled': iesve.glazing_types.triple_glazed_air_or_argon_filled
             'triple_glazed_low_e_hard_coat': iesve.glazing_types.triple_glazed_low_e_hard_coat
             'triple_glazed_low_e_soft_coat': iesve.glazing_types.triple_glazed_low_e_soft_coat
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: single_glazed
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 0
         * a name of "single_glazed".
      
      .. py:property:: triple_glazed_air_or_argon_filled
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 4
         * a name of "triple_glazed_air_or_argon_filled".
      
      .. py:property:: triple_glazed_low_e_hard_coat
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 5
         * a name of "triple_glazed_low_e_hard_coat".
      
      .. py:property:: triple_glazed_low_e_soft_coat
         :classmethod:
         :type: iesve.glazing_types
      
         An instance of this class with:
         
         * a value of 6
         * a name of "triple_glazed_low_e_soft_coat".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.glazing_types.none
             0: iesve.glazing_types.single_glazed
             1: iesve.glazing_types.double_glazed_air_or_argon_filled
             2: iesve.glazing_types.double_glazed_low_e_hard_coat
             3: iesve.glazing_types.double_glazed_low_e_soft_coat
             4: iesve.glazing_types.triple_glazed_air_or_argon_filled
             5: iesve.glazing_types.triple_glazed_low_e_hard_coat
             6: iesve.glazing_types.triple_glazed_low_e_soft_coat
            }
      
   .. py:class:: heat_recovery
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: heat_pipes
         :classmethod:
         :type: iesve.heat_recovery
      
         An instance of this class with:
         
         * a value of 2
         * a name of "heat_pipes".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_heat_recovery': iesve.heat_recovery.no_heat_recovery
             'plate_heat_exchanger': iesve.heat_recovery.plate_heat_exchanger
             'heat_pipes': iesve.heat_recovery.heat_pipes
             'thermal_wheel': iesve.heat_recovery.thermal_wheel
             'run_around_coil': iesve.heat_recovery.run_around_coil
            }
      
      .. py:property:: no_heat_recovery
         :classmethod:
         :type: iesve.heat_recovery
      
         An instance of this class with:
         
         * a value of 0
         * a name of "no_heat_recovery".
      
      .. py:property:: plate_heat_exchanger
         :classmethod:
         :type: iesve.heat_recovery
      
         An instance of this class with:
         
         * a value of 1
         * a name of "plate_heat_exchanger".
      
      .. py:property:: run_around_coil
         :classmethod:
         :type: iesve.heat_recovery
      
         An instance of this class with:
         
         * a value of 4
         * a name of "run_around_coil".
      
      .. py:property:: thermal_wheel
         :classmethod:
         :type: iesve.heat_recovery
      
         An instance of this class with:
         
         * a value of 3
         * a name of "thermal_wheel".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.heat_recovery.no_heat_recovery
             1: iesve.heat_recovery.plate_heat_exchanger
             2: iesve.heat_recovery.heat_pipes
             3: iesve.heat_recovery.thermal_wheel
             4: iesve.heat_recovery.run_around_coil
            }
      
   .. py:class:: heating_cooling_capacity_unit
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: kilowatts
         :classmethod:
         :type: iesve.heating_cooling_capacity_unit
      
         An instance of this class with:
         
         * a value of 0
         * a name of "kilowatts".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unlimited': iesve.heating_cooling_capacity_unit.unlimited
             'kilowatts': iesve.heating_cooling_capacity_unit.kilowatts
             'watts_per_metre_squared': iesve.heating_cooling_capacity_unit.watts_per_metre_squared
            }
      
      .. py:property:: unlimited
         :classmethod:
         :type: iesve.heating_cooling_capacity_unit
      
         An instance of this class with:
         
         * a value of -1
         * a name of "unlimited".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.heating_cooling_capacity_unit.unlimited
             0: iesve.heating_cooling_capacity_unit.kilowatts
             1: iesve.heating_cooling_capacity_unit.watts_per_metre_squared
            }
      
      .. py:property:: watts_per_metre_squared
         :classmethod:
         :type: iesve.heating_cooling_capacity_unit
      
         An instance of this class with:
         
         * a value of 1
         * a name of "watts_per_metre_squared".
      
   .. py:class:: hvac_methodology
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: apache_hvac
         :classmethod:
         :type: iesve.hvac_methodology
      
         An instance of this class with:
         
         * a value of 1
         * a name of "apache_hvac".
      
      .. py:property:: apache_system
         :classmethod:
         :type: iesve.hvac_methodology
      
         An instance of this class with:
         
         * a value of 0
         * a name of "apache_system".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'apache_system': iesve.hvac_methodology.apache_system
             'apache_hvac': iesve.hvac_methodology.apache_hvac
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.hvac_methodology.apache_system
             1: iesve.hvac_methodology.apache_hvac
            }
      
   .. py:class:: lamp_types
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: compact_fluorescent
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 4
         * a name of "compact_fluorescent".
      
      .. py:property:: fluorescent_no_details
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 3
         * a name of "fluorescent_no_details".
      
      .. py:property:: high_pressure_mercury
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 5
         * a name of "high_pressure_mercury".
      
      .. py:property:: high_pressure_sodium
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 6
         * a name of "high_pressure_sodium".
      
      .. py:property:: led
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 9
         * a name of "led".
      
      .. py:property:: metal_halide
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 1
         * a name of "metal_halide".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             't8_halophosphate_fluorescent_low_frequency': iesve.lamp_types.t8_halophosphate_fluorescent_low_frequency
             'metal_halide': iesve.lamp_types.metal_halide
             'tungsten_or_halogen': iesve.lamp_types.tungsten_or_halogen
             'fluorescent_no_details': iesve.lamp_types.fluorescent_no_details
             'compact_fluorescent': iesve.lamp_types.compact_fluorescent
             'high_pressure_mercury': iesve.lamp_types.high_pressure_mercury
             'high_pressure_sodium': iesve.lamp_types.high_pressure_sodium
             't8_triphosphor_fluorescent_high_frequency': iesve.lamp_types.t8_triphosphor_fluorescent_high_frequency
             't8_halophosphate_fluorescent_high_frequency': iesve.lamp_types.t8_halophosphate_fluorescent_high_frequency
             'led': iesve.lamp_types.led
             't12_halophosphate_fluorescent_low_frequency': iesve.lamp_types.t12_halophosphate_fluorescent_low_frequency
             't5_triphosphor_fluorescent_high_frequency': iesve.lamp_types.t5_triphosphor_fluorescent_high_frequency
            }
      
      .. py:property:: t12_halophosphate_fluorescent_low_frequency
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 10
         * a name of "t12_halophosphate_fluorescent_low_frequency".
      
      .. py:property:: t5_triphosphor_fluorescent_high_frequency
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 11
         * a name of "t5_triphosphor_fluorescent_high_frequency".
      
      .. py:property:: t8_halophosphate_fluorescent_high_frequency
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 8
         * a name of "t8_halophosphate_fluorescent_high_frequency".
      
      .. py:property:: t8_halophosphate_fluorescent_low_frequency
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 0
         * a name of "t8_halophosphate_fluorescent_low_frequency".
      
      .. py:property:: t8_triphosphor_fluorescent_high_frequency
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 7
         * a name of "t8_triphosphor_fluorescent_high_frequency".
      
      .. py:property:: tungsten_or_halogen
         :classmethod:
         :type: iesve.lamp_types
      
         An instance of this class with:
         
         * a value of 2
         * a name of "tungsten_or_halogen".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.lamp_types.t8_halophosphate_fluorescent_low_frequency
             1: iesve.lamp_types.metal_halide
             2: iesve.lamp_types.tungsten_or_halogen
             3: iesve.lamp_types.fluorescent_no_details
             4: iesve.lamp_types.compact_fluorescent
             5: iesve.lamp_types.high_pressure_mercury
             6: iesve.lamp_types.high_pressure_sodium
             7: iesve.lamp_types.t8_triphosphor_fluorescent_high_frequency
             8: iesve.lamp_types.t8_halophosphate_fluorescent_high_frequency
             9: iesve.lamp_types.led
             10: iesve.lamp_types.t12_halophosphate_fluorescent_low_frequency
             11: iesve.lamp_types.t5_triphosphor_fluorescent_high_frequency
            }
      
   .. py:class:: lighting_case
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: full
         :classmethod:
         :type: iesve.lighting_case
      
         An instance of this class with:
         
         * a value of 0
         * a name of "full".
      
      .. py:property:: lamp_type_only
         :classmethod:
         :type: iesve.lighting_case
      
         An instance of this class with:
         
         * a value of 2
         * a name of "lamp_type_only".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unknown': iesve.lighting_case.unknown
             'full': iesve.lighting_case.full
             'uncalculated': iesve.lighting_case.uncalculated
             'lamp_type_only': iesve.lighting_case.lamp_type_only
            }
      
      .. py:property:: uncalculated
         :classmethod:
         :type: iesve.lighting_case
      
         An instance of this class with:
         
         * a value of 1
         * a name of "uncalculated".
      
      .. py:property:: unknown
         :classmethod:
         :type: iesve.lighting_case
      
         An instance of this class with:
         
         * a value of -1
         * a name of "unknown".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.lighting_case.unknown
             0: iesve.lighting_case.full
             1: iesve.lighting_case.uncalculated
             2: iesve.lighting_case.lamp_type_only
            }
      
   .. py:class:: material_categories
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: all
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 0
         * a name of "all".
      
      .. py:property:: asphalts
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 1
         * a name of "asphalts".
      
      .. py:property:: boards
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 2
         * a name of "boards".
      
      .. py:property:: bricks
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 3
         * a name of "bricks".
      
      .. py:property:: carpets
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 4
         * a name of "carpets".
      
      .. py:property:: composite_layer
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 98
         * a name of "composite_layer".
      
      .. py:property:: concretes
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 5
         * a name of "concretes".
      
      .. py:property:: floor_finish
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 16
         * a name of "floor_finish".
      
      .. py:property:: glass
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 99
         * a name of "glass".
      
      .. py:property:: gravels
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 6
         * a name of "gravels".
      
      .. py:property:: index_glass
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 14
         * a name of "index_glass".
      
      .. py:property:: insulating
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 7
         * a name of "insulating".
      
      .. py:property:: metals
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 8
         * a name of "metals".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'all': iesve.material_categories.all
             'asphalts': iesve.material_categories.asphalts
             'boards': iesve.material_categories.boards
             'bricks': iesve.material_categories.bricks
             'carpets': iesve.material_categories.carpets
             'concretes': iesve.material_categories.concretes
             'gravels': iesve.material_categories.gravels
             'insulating': iesve.material_categories.insulating
             'metals': iesve.material_categories.metals
             'plaster': iesve.material_categories.plaster
             'screeds': iesve.material_categories.screeds
             'sands': iesve.material_categories.sands
             'titles': iesve.material_categories.titles
             'timber': iesve.material_categories.timber
             'index_glass': iesve.material_categories.index_glass
             'other': iesve.material_categories.other
             'floor_finish': iesve.material_categories.floor_finish
             'susp_ceiling': iesve.material_categories.susp_ceiling
             'composite_layer': iesve.material_categories.composite_layer
             'glass': iesve.material_categories.glass
            }
      
      .. py:property:: other
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 15
         * a name of "other".
      
      .. py:property:: plaster
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 9
         * a name of "plaster".
      
      .. py:property:: sands
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 11
         * a name of "sands".
      
      .. py:property:: screeds
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 10
         * a name of "screeds".
      
      .. py:property:: susp_ceiling
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 17
         * a name of "susp_ceiling".
      
      .. py:property:: timber
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 13
         * a name of "timber".
      
      .. py:property:: titles
         :classmethod:
         :type: iesve.material_categories
      
         An instance of this class with:
         
         * a value of 12
         * a name of "titles".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.material_categories.all
             1: iesve.material_categories.asphalts
             2: iesve.material_categories.boards
             3: iesve.material_categories.bricks
             4: iesve.material_categories.carpets
             5: iesve.material_categories.concretes
             6: iesve.material_categories.gravels
             7: iesve.material_categories.insulating
             8: iesve.material_categories.metals
             9: iesve.material_categories.plaster
             10: iesve.material_categories.screeds
             11: iesve.material_categories.sands
             12: iesve.material_categories.titles
             13: iesve.material_categories.timber
             14: iesve.material_categories.index_glass
             15: iesve.material_categories.other
             16: iesve.material_categories.floor_finish
             17: iesve.material_categories.susp_ceiling
             98: iesve.material_categories.composite_layer
             99: iesve.material_categories.glass
            }
      
   .. py:class:: month
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: april
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 4
         * a name of "april".
      
      .. py:property:: august
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 8
         * a name of "august".
      
      .. py:property:: december
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 12
         * a name of "december".
      
      .. py:property:: february
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 2
         * a name of "february".
      
      .. py:property:: january
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 1
         * a name of "january".
      
      .. py:property:: july
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 7
         * a name of "july".
      
      .. py:property:: june
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 6
         * a name of "june".
      
      .. py:property:: march
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 3
         * a name of "march".
      
      .. py:property:: may
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 5
         * a name of "may".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'january': iesve.month.january
             'february': iesve.month.february
             'march': iesve.month.march
             'april': iesve.month.april
             'may': iesve.month.may
             'june': iesve.month.june
             'july': iesve.month.july
             'august': iesve.month.august
             'september': iesve.month.september
             'october': iesve.month.october
             'november': iesve.month.november
             'december': iesve.month.december
            }
      
      .. py:property:: november
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 11
         * a name of "november".
      
      .. py:property:: october
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 10
         * a name of "october".
      
      .. py:property:: september
         :classmethod:
         :type: iesve.month
      
         An instance of this class with:
         
         * a value of 9
         * a name of "september".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.month.january
             2: iesve.month.february
             3: iesve.month.march
             4: iesve.month.april
             5: iesve.month.may
             6: iesve.month.june
             7: iesve.month.july
             8: iesve.month.august
             9: iesve.month.september
             10: iesve.month.october
             11: iesve.month.november
             12: iesve.month.december
            }
      
   .. py:class:: mv2_viewmode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: component
         :classmethod:
         :type: iesve.mv2_viewmode
      
         An instance of this class with:
         
         * a value of 5
         * a name of "component".
      
      .. py:property:: hidden_line
         :classmethod:
         :type: iesve.mv2_viewmode
      
         An instance of this class with:
         
         * a value of 2
         * a name of "hidden_line".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'shaded': iesve.mv2_viewmode.shaded
             'textured': iesve.mv2_viewmode.textured
             'hidden_line': iesve.mv2_viewmode.hidden_line
             'xray': iesve.mv2_viewmode.xray
             'component': iesve.mv2_viewmode.component
            }
      
      .. py:property:: shaded
         :classmethod:
         :type: iesve.mv2_viewmode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "shaded".
      
      .. py:property:: textured
         :classmethod:
         :type: iesve.mv2_viewmode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "textured".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.mv2_viewmode.shaded
             1: iesve.mv2_viewmode.textured
             2: iesve.mv2_viewmode.hidden_line
             4: iesve.mv2_viewmode.xray
             5: iesve.mv2_viewmode.component
            }
      
      .. py:property:: xray
         :classmethod:
         :type: iesve.mv2_viewmode
      
         An instance of this class with:
         
         * a value of 4
         * a name of "xray".
      
   .. py:class:: ncm_air_supply_mechanism
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: centralised_ac
         :classmethod:
         :type: iesve.ncm_air_supply_mechanism
      
         An instance of this class with:
         
         * a value of 0
         * a name of "centralised_ac".
      
      .. py:property:: local_ventilation_serving_single_area
         :classmethod:
         :type: iesve.ncm_air_supply_mechanism
      
         An instance of this class with:
         
         * a value of 3
         * a name of "local_ventilation_serving_single_area".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'centralised_ac': iesve.ncm_air_supply_mechanism.centralised_ac
             'zonal_supply_system_with_remote_fan': iesve.ncm_air_supply_mechanism.zonal_supply_system_with_remote_fan
             'zonal_extract_system_with_remote_fan': iesve.ncm_air_supply_mechanism.zonal_extract_system_with_remote_fan
             'local_ventilation_serving_single_area': iesve.ncm_air_supply_mechanism.local_ventilation_serving_single_area
             'other_local_ventilation_units': iesve.ncm_air_supply_mechanism.other_local_ventilation_units
            }
      
      .. py:property:: other_local_ventilation_units
         :classmethod:
         :type: iesve.ncm_air_supply_mechanism
      
         An instance of this class with:
         
         * a value of 4
         * a name of "other_local_ventilation_units".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_air_supply_mechanism.centralised_ac
             1: iesve.ncm_air_supply_mechanism.zonal_supply_system_with_remote_fan
             2: iesve.ncm_air_supply_mechanism.zonal_extract_system_with_remote_fan
             3: iesve.ncm_air_supply_mechanism.local_ventilation_serving_single_area
             4: iesve.ncm_air_supply_mechanism.other_local_ventilation_units
            }
      
      .. py:property:: zonal_extract_system_with_remote_fan
         :classmethod:
         :type: iesve.ncm_air_supply_mechanism
      
         An instance of this class with:
         
         * a value of 2
         * a name of "zonal_extract_system_with_remote_fan".
      
      .. py:property:: zonal_supply_system_with_remote_fan
         :classmethod:
         :type: iesve.ncm_air_supply_mechanism
      
         An instance of this class with:
         
         * a value of 1
         * a name of "zonal_supply_system_with_remote_fan".
      
   .. py:class:: ncm_chiller_power
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: greater_than_750_kw
         :classmethod:
         :type: iesve.ncm_chiller_power
      
         An instance of this class with:
         
         * a value of 3
         * a name of "greater_than_750_kw".
      
      .. py:property:: less_than_100_kw
         :classmethod:
         :type: iesve.ncm_chiller_power
      
         An instance of this class with:
         
         * a value of 0
         * a name of "less_than_100_kw".
      
      .. py:property:: less_than_500_kw
         :classmethod:
         :type: iesve.ncm_chiller_power
      
         An instance of this class with:
         
         * a value of 1
         * a name of "less_than_500_kw".
      
      .. py:property:: less_than_750_kw
         :classmethod:
         :type: iesve.ncm_chiller_power
      
         An instance of this class with:
         
         * a value of 2
         * a name of "less_than_750_kw".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'less_than_100_kw': iesve.ncm_chiller_power.less_than_100_kw
             'less_than_500_kw': iesve.ncm_chiller_power.less_than_500_kw
             'less_than_750_kw': iesve.ncm_chiller_power.less_than_750_kw
             'greater_than_750_kw': iesve.ncm_chiller_power.greater_than_750_kw
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_chiller_power.less_than_100_kw
             1: iesve.ncm_chiller_power.less_than_500_kw
             2: iesve.ncm_chiller_power.less_than_750_kw
             3: iesve.ncm_chiller_power.greater_than_750_kw
            }
      
   .. py:class:: ncm_chiller_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_cooled
         :classmethod:
         :type: iesve.ncm_chiller_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "air_cooled".
      
      .. py:property:: heat_pump_electric
         :classmethod:
         :type: iesve.ncm_chiller_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "heat_pump_electric".
      
      .. py:property:: heat_pump_gas_oil
         :classmethod:
         :type: iesve.ncm_chiller_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "heat_pump_gas_oil".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'air_cooled': iesve.ncm_chiller_type.air_cooled
             'water_cooled': iesve.ncm_chiller_type.water_cooled
             'remote_condenser': iesve.ncm_chiller_type.remote_condenser
             'heat_pump_gas_oil': iesve.ncm_chiller_type.heat_pump_gas_oil
             'heat_pump_electric': iesve.ncm_chiller_type.heat_pump_electric
            }
      
      .. py:property:: remote_condenser
         :classmethod:
         :type: iesve.ncm_chiller_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "remote_condenser".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_chiller_type.air_cooled
             1: iesve.ncm_chiller_type.water_cooled
             2: iesve.ncm_chiller_type.remote_condenser
             3: iesve.ncm_chiller_type.heat_pump_gas_oil
             4: iesve.ncm_chiller_type.heat_pump_electric
            }
      
      .. py:property:: water_cooled
         :classmethod:
         :type: iesve.ncm_chiller_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "water_cooled".
      
   .. py:class:: ncm_eca_list
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: after_2001
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 1
         * a name of "after_2001".
      
      .. py:property:: before_2005
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 2
         * a name of "before_2005".
      
      .. py:property:: from_2005
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 3
         * a name of "from_2005".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_on_list': iesve.ncm_eca_list.not_on_list
             'after_2001': iesve.ncm_eca_list.after_2001
             'before_2005': iesve.ncm_eca_list.before_2005
             'from_2005': iesve.ncm_eca_list.from_2005
             'uplift_in_2006': iesve.ncm_eca_list.uplift_in_2006
            }
      
      .. py:property:: not_on_list
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_on_list".
      
      .. py:property:: uplift_in_2006
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 4
         * a name of "uplift_in_2006".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_eca_list.not_on_list
             1: iesve.ncm_eca_list.after_2001
             2: iesve.ncm_eca_list.before_2005
             3: iesve.ncm_eca_list.from_2005
             4: iesve.ncm_eca_list.uplift_in_2006
            }
      
   .. py:class:: ncm_eca_list
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: after_2001
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 1
         * a name of "after_2001".
      
      .. py:property:: before_2005
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 2
         * a name of "before_2005".
      
      .. py:property:: from_2005
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 3
         * a name of "from_2005".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_on_list': iesve.ncm_eca_list.not_on_list
             'after_2001': iesve.ncm_eca_list.after_2001
             'before_2005': iesve.ncm_eca_list.before_2005
             'from_2005': iesve.ncm_eca_list.from_2005
             'uplift_in_2006': iesve.ncm_eca_list.uplift_in_2006
            }
      
      .. py:property:: not_on_list
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_on_list".
      
      .. py:property:: uplift_in_2006
         :classmethod:
         :type: iesve.ncm_eca_list
      
         An instance of this class with:
         
         * a value of 4
         * a name of "uplift_in_2006".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_eca_list.not_on_list
             1: iesve.ncm_eca_list.after_2001
             2: iesve.ncm_eca_list.before_2005
             3: iesve.ncm_eca_list.from_2005
             4: iesve.ncm_eca_list.uplift_in_2006
            }
      
   .. py:class:: ncm_heat_recovery
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: heat_pipes
         :classmethod:
         :type: iesve.ncm_heat_recovery
      
         An instance of this class with:
         
         * a value of 2
         * a name of "heat_pipes".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'no_heat_recovery': iesve.ncm_heat_recovery.no_heat_recovery
             'plate_heat_exchanger': iesve.ncm_heat_recovery.plate_heat_exchanger
             'heat_pipes': iesve.ncm_heat_recovery.heat_pipes
             'thermal_wheel': iesve.ncm_heat_recovery.thermal_wheel
             'run_around_coil': iesve.ncm_heat_recovery.run_around_coil
            }
      
      .. py:property:: no_heat_recovery
         :classmethod:
         :type: iesve.ncm_heat_recovery
      
         An instance of this class with:
         
         * a value of 0
         * a name of "no_heat_recovery".
      
      .. py:property:: plate_heat_exchanger
         :classmethod:
         :type: iesve.ncm_heat_recovery
      
         An instance of this class with:
         
         * a value of 1
         * a name of "plate_heat_exchanger".
      
      .. py:property:: run_around_coil
         :classmethod:
         :type: iesve.ncm_heat_recovery
      
         An instance of this class with:
         
         * a value of 4
         * a name of "run_around_coil".
      
      .. py:property:: thermal_wheel
         :classmethod:
         :type: iesve.ncm_heat_recovery
      
         An instance of this class with:
         
         * a value of 3
         * a name of "thermal_wheel".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_heat_recovery.no_heat_recovery
             1: iesve.ncm_heat_recovery.plate_heat_exchanger
             2: iesve.ncm_heat_recovery.heat_pipes
             3: iesve.ncm_heat_recovery.thermal_wheel
             4: iesve.ncm_heat_recovery.run_around_coil
            }
      
   .. py:class:: ncm_heat_source
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: air_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 3
         * a name of "air_heater".
      
      .. py:property:: chp
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 14
         * a name of "chp".
      
      .. py:property:: direct_gas_firing
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 13
         * a name of "direct_gas_firing".
      
      .. py:property:: direct_or_storage_electric_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 8
         * a name of "direct_or_storage_electric_heater".
      
      .. py:property:: district_heating
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 12
         * a name of "district_heating".
      
      .. py:property:: heat_pump_air_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 9
         * a name of "heat_pump_air_source".
      
      .. py:property:: heat_pump_electric_air_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 17
         * a name of "heat_pump_electric_air_source".
      
      .. py:property:: heat_pump_electric_ground_or_water_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 18
         * a name of "heat_pump_electric_ground_or_water_source".
      
      .. py:property:: heat_pump_gas_oil_air_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 15
         * a name of "heat_pump_gas_oil_air_source".
      
      .. py:property:: heat_pump_gas_oil_ground_or_water_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 16
         * a name of "heat_pump_gas_oil_ground_or_water_source".
      
      .. py:property:: heat_pump_ground_or_water_source
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 10
         * a name of "heat_pump_ground_or_water_source".
      
      .. py:property:: hthw_boiler
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 2
         * a name of "hthw_boiler".
      
      .. py:property:: lthw_boiler
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 0
         * a name of "lthw_boiler".
      
      .. py:property:: mthw_boiler
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 1
         * a name of "mthw_boiler".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'lthw_boiler': iesve.ncm_heat_source.lthw_boiler
             'mthw_boiler': iesve.ncm_heat_source.mthw_boiler
             'hthw_boiler': iesve.ncm_heat_source.hthw_boiler
             'air_heater': iesve.ncm_heat_source.air_heater
             'unflued_gas_warm_air_heater': iesve.ncm_heat_source.unflued_gas_warm_air_heater
             'unitary_radiant_heater': iesve.ncm_heat_source.unitary_radiant_heater
             'radiant_heater': iesve.ncm_heat_source.radiant_heater
             'unflued_radiant_heater': iesve.ncm_heat_source.unflued_radiant_heater
             'direct_or_storage_electric_heater': iesve.ncm_heat_source.direct_or_storage_electric_heater
             'heat_pump_air_source': iesve.ncm_heat_source.heat_pump_air_source
             'heat_pump_ground_or_water_source': iesve.ncm_heat_source.heat_pump_ground_or_water_source
             'room_heater': iesve.ncm_heat_source.room_heater
             'district_heating': iesve.ncm_heat_source.district_heating
             'direct_gas_firing': iesve.ncm_heat_source.direct_gas_firing
             'chp': iesve.ncm_heat_source.chp
             'heat_pump_gas_oil_air_source': iesve.ncm_heat_source.heat_pump_gas_oil_air_source
             'heat_pump_gas_oil_ground_or_water_source': iesve.ncm_heat_source.heat_pump_gas_oil_ground_or_water_source
             'heat_pump_electric_air_source': iesve.ncm_heat_source.heat_pump_electric_air_source
             'heat_pump_electric_ground_or_water_source': iesve.ncm_heat_source.heat_pump_electric_ground_or_water_source
            }
      
      .. py:property:: radiant_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 6
         * a name of "radiant_heater".
      
      .. py:property:: room_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 11
         * a name of "room_heater".
      
      .. py:property:: unflued_gas_warm_air_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 4
         * a name of "unflued_gas_warm_air_heater".
      
      .. py:property:: unflued_radiant_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 7
         * a name of "unflued_radiant_heater".
      
      .. py:property:: unitary_radiant_heater
         :classmethod:
         :type: iesve.ncm_heat_source
      
         An instance of this class with:
         
         * a value of 5
         * a name of "unitary_radiant_heater".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_heat_source.lthw_boiler
             1: iesve.ncm_heat_source.mthw_boiler
             2: iesve.ncm_heat_source.hthw_boiler
             3: iesve.ncm_heat_source.air_heater
             4: iesve.ncm_heat_source.unflued_gas_warm_air_heater
             5: iesve.ncm_heat_source.unitary_radiant_heater
             6: iesve.ncm_heat_source.radiant_heater
             7: iesve.ncm_heat_source.unflued_radiant_heater
             8: iesve.ncm_heat_source.direct_or_storage_electric_heater
             9: iesve.ncm_heat_source.heat_pump_air_source
             10: iesve.ncm_heat_source.heat_pump_ground_or_water_source
             11: iesve.ncm_heat_source.room_heater
             12: iesve.ncm_heat_source.district_heating
             13: iesve.ncm_heat_source.direct_gas_firing
             14: iesve.ncm_heat_source.chp
             15: iesve.ncm_heat_source.heat_pump_gas_oil_air_source
             16: iesve.ncm_heat_source.heat_pump_gas_oil_ground_or_water_source
             17: iesve.ncm_heat_source.heat_pump_electric_air_source
             18: iesve.ncm_heat_source.heat_pump_electric_ground_or_water_source
            }
      
   .. py:class:: ncm_leakage_standard
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: class_l1
         :classmethod:
         :type: iesve.ncm_leakage_standard
      
         An instance of this class with:
         
         * a value of 0
         * a name of "class_l1".
      
      .. py:property:: class_l2
         :classmethod:
         :type: iesve.ncm_leakage_standard
      
         An instance of this class with:
         
         * a value of 1
         * a name of "class_l2".
      
      .. py:property:: class_l3
         :classmethod:
         :type: iesve.ncm_leakage_standard
      
         An instance of this class with:
         
         * a value of 2
         * a name of "class_l3".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'class_l1': iesve.ncm_leakage_standard.class_l1
             'class_l2': iesve.ncm_leakage_standard.class_l2
             'class_l3': iesve.ncm_leakage_standard.class_l3
             'not_compliant': iesve.ncm_leakage_standard.not_compliant
            }
      
      .. py:property:: not_compliant
         :classmethod:
         :type: iesve.ncm_leakage_standard
      
         An instance of this class with:
         
         * a value of 3
         * a name of "not_compliant".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_leakage_standard.class_l1
             1: iesve.ncm_leakage_standard.class_l2
             2: iesve.ncm_leakage_standard.class_l3
             3: iesve.ncm_leakage_standard.not_compliant
            }
      
   .. py:class:: ncm_leakage_test
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: class_a
         :classmethod:
         :type: iesve.ncm_leakage_test
      
         An instance of this class with:
         
         * a value of 1
         * a name of "class_a".
      
      .. py:property:: class_b
         :classmethod:
         :type: iesve.ncm_leakage_test
      
         An instance of this class with:
         
         * a value of 2
         * a name of "class_b".
      
      .. py:property:: class_c
         :classmethod:
         :type: iesve.ncm_leakage_test
      
         An instance of this class with:
         
         * a value of 3
         * a name of "class_c".
      
      .. py:property:: class_d
         :classmethod:
         :type: iesve.ncm_leakage_test
      
         An instance of this class with:
         
         * a value of 4
         * a name of "class_d".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_tested': iesve.ncm_leakage_test.not_tested
             'class_a': iesve.ncm_leakage_test.class_a
             'class_b': iesve.ncm_leakage_test.class_b
             'class_c': iesve.ncm_leakage_test.class_c
             'class_d': iesve.ncm_leakage_test.class_d
            }
      
      .. py:property:: not_tested
         :classmethod:
         :type: iesve.ncm_leakage_test
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_tested".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_leakage_test.not_tested
             1: iesve.ncm_leakage_test.class_a
             2: iesve.ncm_leakage_test.class_b
             3: iesve.ncm_leakage_test.class_c
             4: iesve.ncm_leakage_test.class_d
            }
      
   .. py:class:: ncm_pump_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant_speed
         :classmethod:
         :type: iesve.ncm_pump_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "constant_speed".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'constant_speed': iesve.ncm_pump_type.constant_speed
             'variable_speed_differential_sensor_pump': iesve.ncm_pump_type.variable_speed_differential_sensor_pump
             'variable_speed_differential_sensor_system': iesve.ncm_pump_type.variable_speed_differential_sensor_system
             'variable_speed_multiple_pressure_sensors': iesve.ncm_pump_type.variable_speed_multiple_pressure_sensors
             'none': iesve.ncm_pump_type.none
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.ncm_pump_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "none".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_pump_type.constant_speed
             1: iesve.ncm_pump_type.variable_speed_differential_sensor_pump
             2: iesve.ncm_pump_type.variable_speed_differential_sensor_system
             3: iesve.ncm_pump_type.variable_speed_multiple_pressure_sensors
             4: iesve.ncm_pump_type.none
            }
      
      .. py:property:: variable_speed_differential_sensor_pump
         :classmethod:
         :type: iesve.ncm_pump_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "variable_speed_differential_sensor_pump".
      
      .. py:property:: variable_speed_differential_sensor_system
         :classmethod:
         :type: iesve.ncm_pump_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "variable_speed_differential_sensor_system".
      
      .. py:property:: variable_speed_multiple_pressure_sensors
         :classmethod:
         :type: iesve.ncm_pump_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "variable_speed_multiple_pressure_sensors".
      
   .. py:class:: ncm_system_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: active_chilled_beams
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 26
         * a name of "active_chilled_beams".
      
      .. py:property:: central_heating_using_air_distribution
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "central_heating_using_air_distribution".
      
      .. py:property:: central_heating_using_water_convectors
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "central_heating_using_water_convectors".
      
      .. py:property:: central_heating_using_water_floor_heating
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "central_heating_using_water_floor_heating".
      
      .. py:property:: central_heating_using_water_radiators
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "central_heating_using_water_radiators".
      
      .. py:property:: chilled_ceilings_or_passive_chilled_beams
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 25
         * a name of "chilled_ceilings_or_passive_chilled_beams".
      
      .. py:property:: chilled_ceilings_or_passive_chilled_beams_displacement_ventilation
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 25
         * a name of "chilled_ceilings_or_passive_chilled_beams_displacement_ventilation".
      
      .. py:property:: chilled_ceilings_or_passive_chilled_beams_mixed_ventilation
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 32
         * a name of "chilled_ceilings_or_passive_chilled_beams_mixed_ventilation".
      
      .. py:property:: constant_volume_system_fixed
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 20
         * a name of "constant_volume_system_fixed".
      
      .. py:property:: constant_volume_system_variable
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 21
         * a name of "constant_volume_system_variable".
      
      .. py:property:: dual_duct
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 24
         * a name of "dual_duct".
      
      .. py:property:: dual_duct_vav
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 16
         * a name of "dual_duct_vav".
      
      .. py:property:: fan_coil_systems
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 18
         * a name of "fan_coil_systems".
      
      .. py:property:: flued_forced_convection_air_heaters
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 13
         * a name of "flued_forced_convection_air_heaters".
      
      .. py:property:: flued_radiant_heater
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 11
         * a name of "flued_radiant_heater".
      
      .. py:property:: generic_heating_and_mechanical_cooling
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "generic_heating_and_mechanical_cooling".
      
      .. py:property:: generic_heating_only_electrical_resistance
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "generic_heating_only_electrical_resistance".
      
      .. py:property:: generic_heating_only_other_systems
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "generic_heating_only_other_systems".
      
      .. py:property:: indoor_packaged_cabinet
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 17
         * a name of "indoor_packaged_cabinet".
      
      .. py:property:: induction_system
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 19
         * a name of "induction_system".
      
      .. py:property:: multi_burner_radiant_heaters
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 12
         * a name of "multi_burner_radiant_heaters".
      
      .. py:property:: multizone
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 22
         * a name of "multizone".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'not_set': iesve.ncm_system_type.not_set
             'generic_heating_only_electrical_resistance': iesve.ncm_system_type.generic_heating_only_electrical_resistance
             'generic_heating_only_other_systems': iesve.ncm_system_type.generic_heating_only_other_systems
             'generic_heating_and_mechanical_cooling': iesve.ncm_system_type.generic_heating_and_mechanical_cooling
             'central_heating_using_water_radiators': iesve.ncm_system_type.central_heating_using_water_radiators
             'central_heating_using_water_convectors': iesve.ncm_system_type.central_heating_using_water_convectors
             'central_heating_using_water_floor_heating': iesve.ncm_system_type.central_heating_using_water_floor_heating
             'central_heating_using_air_distribution': iesve.ncm_system_type.central_heating_using_air_distribution
             'other_local_room_heater_fanned': iesve.ncm_system_type.other_local_room_heater_fanned
             'other_local_room_heater_unfanned': iesve.ncm_system_type.other_local_room_heater_unfanned
             'unflued_radiant_heater': iesve.ncm_system_type.unflued_radiant_heater
             'flued_radiant_heater': iesve.ncm_system_type.flued_radiant_heater
             'multi_burner_radiant_heaters': iesve.ncm_system_type.multi_burner_radiant_heaters
             'flued_forced_convection_air_heaters': iesve.ncm_system_type.flued_forced_convection_air_heaters
             'unflued_forced_convection_air_heaters': iesve.ncm_system_type.unflued_forced_convection_air_heaters
             'single_duct_vav': iesve.ncm_system_type.single_duct_vav
             'dual_duct_vav': iesve.ncm_system_type.dual_duct_vav
             'indoor_packaged_cabinet': iesve.ncm_system_type.indoor_packaged_cabinet
             'fan_coil_systems': iesve.ncm_system_type.fan_coil_systems
             'induction_system': iesve.ncm_system_type.induction_system
             'constant_volume_system_fixed': iesve.ncm_system_type.constant_volume_system_fixed
             'constant_volume_system_variable': iesve.ncm_system_type.constant_volume_system_variable
             'multizone': iesve.ncm_system_type.multizone
             'terminal_reheat': iesve.ncm_system_type.terminal_reheat
             'dual_duct': iesve.ncm_system_type.dual_duct
             'chilled_ceilings_or_passive_chilled_beams': iesve.ncm_system_type.chilled_ceilings_or_passive_chilled_beams
             'active_chilled_beams': iesve.ncm_system_type.active_chilled_beams
             'water_loop_heat_pump': iesve.ncm_system_type.water_loop_heat_pump
             'split_or_multisplit_systems': iesve.ncm_system_type.split_or_multisplit_systems
             'single_room_cooling_system': iesve.ncm_system_type.single_room_cooling_system
             'no_heating_or_cooling': iesve.ncm_system_type.no_heating_or_cooling
             'chilled_ceilings_or_passive_chilled_beams_mixed_ventilation': iesve.ncm_system_type.chilled_ceilings_or_passive_chilled_beams_mixed_ventilation
             'variable_refrigerant_flow': iesve.ncm_system_type.variable_refrigerant_flow
             'chilled_ceilings_or_passive_chilled_beams_displacement_ventilation': iesve.ncm_system_type.chilled_ceilings_or_passive_chilled_beams_displacement_ventilation
            }
      
      .. py:property:: no_heating_or_cooling
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 30
         * a name of "no_heating_or_cooling".
      
      .. py:property:: not_set
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "not_set".
      
      .. py:property:: other_local_room_heater_fanned
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "other_local_room_heater_fanned".
      
      .. py:property:: other_local_room_heater_unfanned
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "other_local_room_heater_unfanned".
      
      .. py:property:: single_duct_vav
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 15
         * a name of "single_duct_vav".
      
      .. py:property:: single_room_cooling_system
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 29
         * a name of "single_room_cooling_system".
      
      .. py:property:: split_or_multisplit_systems
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 28
         * a name of "split_or_multisplit_systems".
      
      .. py:property:: terminal_reheat
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 23
         * a name of "terminal_reheat".
      
      .. py:property:: unflued_forced_convection_air_heaters
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 14
         * a name of "unflued_forced_convection_air_heaters".
      
      .. py:property:: unflued_radiant_heater
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "unflued_radiant_heater".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.ncm_system_type.not_set
             1: iesve.ncm_system_type.generic_heating_only_electrical_resistance
             2: iesve.ncm_system_type.generic_heating_only_other_systems
             3: iesve.ncm_system_type.generic_heating_and_mechanical_cooling
             4: iesve.ncm_system_type.central_heating_using_water_radiators
             5: iesve.ncm_system_type.central_heating_using_water_convectors
             6: iesve.ncm_system_type.central_heating_using_water_floor_heating
             7: iesve.ncm_system_type.central_heating_using_air_distribution
             8: iesve.ncm_system_type.other_local_room_heater_fanned
             9: iesve.ncm_system_type.other_local_room_heater_unfanned
             10: iesve.ncm_system_type.unflued_radiant_heater
             11: iesve.ncm_system_type.flued_radiant_heater
             12: iesve.ncm_system_type.multi_burner_radiant_heaters
             13: iesve.ncm_system_type.flued_forced_convection_air_heaters
             14: iesve.ncm_system_type.unflued_forced_convection_air_heaters
             15: iesve.ncm_system_type.single_duct_vav
             16: iesve.ncm_system_type.dual_duct_vav
             17: iesve.ncm_system_type.indoor_packaged_cabinet
             18: iesve.ncm_system_type.fan_coil_systems
             19: iesve.ncm_system_type.induction_system
             20: iesve.ncm_system_type.constant_volume_system_fixed
             21: iesve.ncm_system_type.constant_volume_system_variable
             22: iesve.ncm_system_type.multizone
             23: iesve.ncm_system_type.terminal_reheat
             24: iesve.ncm_system_type.dual_duct
             25: iesve.ncm_system_type.chilled_ceilings_or_passive_chilled_beams_displacement_ventilation
             26: iesve.ncm_system_type.active_chilled_beams
             27: iesve.ncm_system_type.water_loop_heat_pump
             28: iesve.ncm_system_type.split_or_multisplit_systems
             29: iesve.ncm_system_type.single_room_cooling_system
             30: iesve.ncm_system_type.no_heating_or_cooling
             32: iesve.ncm_system_type.chilled_ceilings_or_passive_chilled_beams_mixed_ventilation
             31: iesve.ncm_system_type.variable_refrigerant_flow
            }
      
      .. py:property:: variable_refrigerant_flow
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 31
         * a name of "variable_refrigerant_flow".
      
      .. py:property:: water_loop_heat_pump
         :classmethod:
         :type: iesve.ncm_system_type
      
         An instance of this class with:
         
         * a value of 27
         * a name of "water_loop_heat_pump".
      
   .. py:class:: occupancy_sensing
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: auto_on_dimmed
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 1
         * a name of "auto_on_dimmed".
      
      .. py:property:: auto_on_off
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 2
         * a name of "auto_on_off".
      
      .. py:property:: manual_on_auto_off
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 4
         * a name of "manual_on_auto_off".
      
      .. py:property:: manual_on_dimmed
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 3
         * a name of "manual_on_dimmed".
      
      .. py:property:: manual_on_off_ext
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 0
         * a name of "manual_on_off_ext".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'manual_on_off_ext': iesve.occupancy_sensing.manual_on_off_ext
             'auto_on_dimmed': iesve.occupancy_sensing.auto_on_dimmed
             'auto_on_off': iesve.occupancy_sensing.auto_on_off
             'manual_on_dimmed': iesve.occupancy_sensing.manual_on_dimmed
             'manual_on_auto_off': iesve.occupancy_sensing.manual_on_auto_off
             'none': iesve.occupancy_sensing.none
            }
      
      .. py:property:: none
         :classmethod:
         :type: iesve.occupancy_sensing
      
         An instance of this class with:
         
         * a value of 5
         * a name of "none".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.occupancy_sensing.manual_on_off_ext
             1: iesve.occupancy_sensing.auto_on_dimmed
             2: iesve.occupancy_sensing.auto_on_off
             3: iesve.occupancy_sensing.manual_on_dimmed
             4: iesve.occupancy_sensing.manual_on_auto_off
             5: iesve.occupancy_sensing.none
            }
      
   .. py:class:: opening_internality
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: any
         :classmethod:
         :type: iesve.opening_internality
      
         An instance of this class with:
         
         * a value of -1
         * a name of "any".
      
      .. py:property:: external
         :classmethod:
         :type: iesve.opening_internality
      
         An instance of this class with:
         
         * a value of 1
         * a name of "external".
      
      .. py:property:: internal
         :classmethod:
         :type: iesve.opening_internality
      
         An instance of this class with:
         
         * a value of 0
         * a name of "internal".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'any': iesve.opening_internality.any
             'internal': iesve.opening_internality.internal
             'external': iesve.opening_internality.external
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.opening_internality.any
             0: iesve.opening_internality.internal
             1: iesve.opening_internality.external
            }
      
   .. py:class:: opening_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: acoustic_duct
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 11
         * a name of "acoustic_duct".
      
      .. py:property:: custom_sharp_edge_orifice
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "custom_sharp_edge_orifice".
      
      .. py:property:: duct
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 10
         * a name of "duct".
      
      .. py:property:: grille
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "grille".
      
      .. py:property:: louvre
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "louvre".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'custom_sharp_edge_orifice': iesve.opening_type.custom_sharp_edge_orifice
             'window_door_side_hung': iesve.opening_type.window_door_side_hung
             'window_centre_hung': iesve.opening_type.window_centre_hung
             'window_top_hung': iesve.opening_type.window_top_hung
             'window_bottom_hung': iesve.opening_type.window_bottom_hung
             'parallel_hung_windows_flaps': iesve.opening_type.parallel_hung_windows_flaps
             'window_sash': iesve.opening_type.window_sash
             'sliding_roller_door': iesve.opening_type.sliding_roller_door
             'louvre': iesve.opening_type.louvre
             'grille': iesve.opening_type.grille
             'duct': iesve.opening_type.duct
             'acoustic_duct': iesve.opening_type.acoustic_duct
            }
      
      .. py:property:: parallel_hung_windows_flaps
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "parallel_hung_windows_flaps".
      
      .. py:property:: sliding_roller_door
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "sliding_roller_door".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.opening_type.custom_sharp_edge_orifice
             1: iesve.opening_type.window_door_side_hung
             2: iesve.opening_type.window_centre_hung
             3: iesve.opening_type.window_top_hung
             4: iesve.opening_type.window_bottom_hung
             5: iesve.opening_type.parallel_hung_windows_flaps
             6: iesve.opening_type.window_sash
             7: iesve.opening_type.sliding_roller_door
             8: iesve.opening_type.louvre
             9: iesve.opening_type.grille
             10: iesve.opening_type.duct
             11: iesve.opening_type.acoustic_duct
            }
      
      .. py:property:: window_bottom_hung
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "window_bottom_hung".
      
      .. py:property:: window_centre_hung
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "window_centre_hung".
      
      .. py:property:: window_door_side_hung
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "window_door_side_hung".
      
      .. py:property:: window_sash
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "window_sash".
      
      .. py:property:: window_top_hung
         :classmethod:
         :type: iesve.opening_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "window_top_hung".
      
   .. py:class:: percent_sky_blocked_options
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: 20_to_60_percent
         :classmethod:
         :type: iesve.percent_sky_blocked_options
      
         An instance of this class with:
         
         * a value of 2
         * a name of "20_to_60_percent".
      
      .. py:property:: 60_to_80_percent
         :classmethod:
         :type: iesve.percent_sky_blocked_options
      
         An instance of this class with:
         
         * a value of 1
         * a name of "60_to_80_percent".
      
      .. py:property:: less_than_20_percent
         :classmethod:
         :type: iesve.percent_sky_blocked_options
      
         An instance of this class with:
         
         * a value of 3
         * a name of "less_than_20_percent".
      
      .. py:property:: more_than_80_percent
         :classmethod:
         :type: iesve.percent_sky_blocked_options
      
         An instance of this class with:
         
         * a value of 0
         * a name of "more_than_80_percent".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'more_than_80_percent': iesve.percent_sky_blocked_options.more_than_80_percent
             '60_to_80_percent': iesve.percent_sky_blocked_options.60_to_80_percent
             '20_to_60_percent': iesve.percent_sky_blocked_options.20_to_60_percent
             'less_than_20_percent': iesve.percent_sky_blocked_options.less_than_20_percent
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.percent_sky_blocked_options.more_than_80_percent
             1: iesve.percent_sky_blocked_options.60_to_80_percent
             2: iesve.percent_sky_blocked_options.20_to_60_percent
             3: iesve.percent_sky_blocked_options.less_than_20_percent
            }
      
   .. py:class:: photoelectric_control_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: dimming
         :classmethod:
         :type: iesve.photoelectric_control_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "dimming".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'switching': iesve.photoelectric_control_type.switching
             'dimming': iesve.photoelectric_control_type.dimming
            }
      
      .. py:property:: switching
         :classmethod:
         :type: iesve.photoelectric_control_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "switching".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.photoelectric_control_type.switching
             1: iesve.photoelectric_control_type.dimming
            }
      
   .. py:class:: prm_mode
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: iecc
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 3
         * a name of "iecc".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'none': iesve.prm_mode.none
             'prm_2004_2007': iesve.prm_mode.prm_2004_2007
             'prm_2010': iesve.prm_mode.prm_2010
             'prm_2013': iesve.prm_mode.prm_2013
             'iecc': iesve.prm_mode.iecc
             'necb': iesve.prm_mode.necb
             'necb_2011': iesve.prm_mode.necb_2011
             'prm_2016': iesve.prm_mode.prm_2016
             't24': iesve.prm_mode.t24
             'necb_2017': iesve.prm_mode.necb_2017
             'prm_2019': iesve.prm_mode.prm_2019
             't24_2022': iesve.prm_mode.t24_2022
            }
      
      .. py:property:: necb
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 4
         * a name of "necb".
      
      .. py:property:: necb_2011
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 4
         * a name of "necb_2011".
      
      .. py:property:: necb_2017
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 7
         * a name of "necb_2017".
      
      .. py:property:: none
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of -1
         * a name of "none".
      
      .. py:property:: prm_2004_2007
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 0
         * a name of "prm_2004_2007".
      
      .. py:property:: prm_2010
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 1
         * a name of "prm_2010".
      
      .. py:property:: prm_2013
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 2
         * a name of "prm_2013".
      
      .. py:property:: prm_2016
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 5
         * a name of "prm_2016".
      
      .. py:property:: prm_2019
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 8
         * a name of "prm_2019".
      
      .. py:property:: t24
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 6
         * a name of "t24".
      
      .. py:property:: t24_2022
         :classmethod:
         :type: iesve.prm_mode
      
         An instance of this class with:
         
         * a value of 9
         * a name of "t24_2022".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             -1: iesve.prm_mode.none
             0: iesve.prm_mode.prm_2004_2007
             1: iesve.prm_mode.prm_2010
             2: iesve.prm_mode.prm_2013
             3: iesve.prm_mode.iecc
             4: iesve.prm_mode.necb_2011
             5: iesve.prm_mode.prm_2016
             6: iesve.prm_mode.t24
             7: iesve.prm_mode.necb_2017
             8: iesve.prm_mode.prm_2019
             9: iesve.prm_mode.t24_2022
            }
      
   .. py:class:: project_types
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: manufacturer
         :classmethod:
         :type: iesve.project_types
      
         An instance of this class with:
         
         * a value of 2
         * a name of "manufacturer".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'project': iesve.project_types.project
             'system': iesve.project_types.system
             'manufacturer': iesve.project_types.manufacturer
            }
      
      .. py:property:: project
         :classmethod:
         :type: iesve.project_types
      
         An instance of this class with:
         
         * a value of 0
         * a name of "project".
      
      .. py:property:: system
         :classmethod:
         :type: iesve.project_types
      
         An instance of this class with:
         
         * a value of 1
         * a name of "system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.project_types.project
             1: iesve.project_types.system
             2: iesve.project_types.manufacturer
            }
      
   .. py:class:: pvs_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: amorphous_silicon
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "amorphous_silicon".
      
      .. py:property:: monocrystalline_silicon
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "monocrystalline_silicon".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'monocrystalline_silicon': iesve.pvs_type.monocrystalline_silicon
             'polycrystalline_silicon': iesve.pvs_type.polycrystalline_silicon
             'amorphous_silicon': iesve.pvs_type.amorphous_silicon
             'other_thin_film': iesve.pvs_type.other_thin_film
             'thin_film_cadmium': iesve.pvs_type.thin_film_cadmium
             'thin_film_copper': iesve.pvs_type.thin_film_copper
            }
      
      .. py:property:: other_thin_film
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "other_thin_film".
      
      .. py:property:: polycrystalline_silicon
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "polycrystalline_silicon".
      
      .. py:property:: thin_film_cadmium
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "thin_film_cadmium".
      
      .. py:property:: thin_film_copper
         :classmethod:
         :type: iesve.pvs_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "thin_film_copper".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.pvs_type.monocrystalline_silicon
             1: iesve.pvs_type.polycrystalline_silicon
             2: iesve.pvs_type.amorphous_silicon
             3: iesve.pvs_type.other_thin_film
             4: iesve.pvs_type.thin_film_cadmium
             5: iesve.pvs_type.thin_film_copper
            }
      
   .. py:class:: reference_irradiance
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: irad_1000wm2
         :classmethod:
         :type: iesve.reference_irradiance
      
         An instance of this class with:
         
         * a value of 1000
         * a name of "irad_1000wm2".
      
      .. py:property:: irad_800wm2
         :classmethod:
         :type: iesve.reference_irradiance
      
         An instance of this class with:
         
         * a value of 800
         * a name of "irad_800wm2".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'irad_800wm2': iesve.reference_irradiance.irad_800wm2
             'irad_1000wm2': iesve.reference_irradiance.irad_1000wm2
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             800: iesve.reference_irradiance.irad_800wm2
             1000: iesve.reference_irradiance.irad_1000wm2
            }
      
   .. py:class:: reporting_interval
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'six_minutes': iesve.reporting_interval.six_minutes
             'ten_minutes': iesve.reporting_interval.ten_minutes
             'thirty_minutes': iesve.reporting_interval.thirty_minutes
             'sixty_minutes': iesve.reporting_interval.sixty_minutes
            }
      
      .. py:property:: six_minutes
         :classmethod:
         :type: iesve.reporting_interval
      
         An instance of this class with:
         
         * a value of 0
         * a name of "six_minutes".
      
      .. py:property:: sixty_minutes
         :classmethod:
         :type: iesve.reporting_interval
      
         An instance of this class with:
         
         * a value of 3
         * a name of "sixty_minutes".
      
      .. py:property:: ten_minutes
         :classmethod:
         :type: iesve.reporting_interval
      
         An instance of this class with:
         
         * a value of 1
         * a name of "ten_minutes".
      
      .. py:property:: thirty_minutes
         :classmethod:
         :type: iesve.reporting_interval
      
         An instance of this class with:
         
         * a value of 2
         * a name of "thirty_minutes".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.reporting_interval.six_minutes
             1: iesve.reporting_interval.ten_minutes
             2: iesve.reporting_interval.thirty_minutes
             3: iesve.reporting_interval.sixty_minutes
            }
      
   .. py:class:: room_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: dwelling_living_area
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 6
         * a name of "dwelling_living_area".
      
      .. py:property:: glazing_cavity
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "glazing_cavity".
      
      .. py:property:: heated
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "heated".
      
      .. py:property:: heated_dwelling_conservatory_scotland
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 8
         * a name of "heated_dwelling_conservatory_scotland".
      
      .. py:property:: internal_void
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 9
         * a name of "internal_void".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'heated': iesve.room_type.heated
             'unheated_roof': iesve.room_type.unheated_roof
             'unheated_loft': iesve.room_type.unheated_loft
             'room_in_roof': iesve.room_type.room_in_roof
             'glazing_cavity': iesve.room_type.glazing_cavity
             'unheated': iesve.room_type.unheated
             'dwelling_living_area': iesve.room_type.dwelling_living_area
             'unheated_dwelling_conservatory': iesve.room_type.unheated_dwelling_conservatory
             'heated_dwelling_conservatory_scotland': iesve.room_type.heated_dwelling_conservatory_scotland
             'internal_void': iesve.room_type.internal_void
            }
      
      .. py:property:: room_in_roof
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "room_in_roof".
      
      .. py:property:: unheated
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 5
         * a name of "unheated".
      
      .. py:property:: unheated_dwelling_conservatory
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 7
         * a name of "unheated_dwelling_conservatory".
      
      .. py:property:: unheated_loft
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "unheated_loft".
      
      .. py:property:: unheated_roof
         :classmethod:
         :type: iesve.room_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "unheated_roof".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.room_type.heated
             1: iesve.room_type.unheated_roof
             2: iesve.room_type.unheated_loft
             3: iesve.room_type.room_in_roof
             4: iesve.room_type.glazing_cavity
             5: iesve.room_type.unheated
             6: iesve.room_type.dwelling_living_area
             7: iesve.room_type.unheated_dwelling_conservatory
             8: iesve.room_type.heated_dwelling_conservatory_scotland
             9: iesve.room_type.internal_void
            }
      
   .. py:class:: sensor_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: addressable
         :classmethod:
         :type: iesve.sensor_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "addressable".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'addressable': iesve.sensor_type.addressable
             'standalone': iesve.sensor_type.standalone
            }
      
      .. py:property:: standalone
         :classmethod:
         :type: iesve.sensor_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "standalone".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.sensor_type.addressable
             0: iesve.sensor_type.standalone
            }
      
   .. py:class:: setpoint_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: constant
         :classmethod:
         :type: iesve.setpoint_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "constant".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'constant': iesve.setpoint_type.constant
             'variable': iesve.setpoint_type.variable
             'two_value': iesve.setpoint_type.two_value
            }
      
      .. py:property:: two_value
         :classmethod:
         :type: iesve.setpoint_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "two_value".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.setpoint_type.constant
             1: iesve.setpoint_type.variable
             2: iesve.setpoint_type.two_value
            }
      
      .. py:property:: variable
         :classmethod:
         :type: iesve.setpoint_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "variable".
      
   .. py:class:: shw_circulation_sys
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: forced_circulation_system_with_no_pv
         :classmethod:
         :type: iesve.shw_circulation_sys
      
         An instance of this class with:
         
         * a value of 2
         * a name of "forced_circulation_system_with_no_pv".
      
      .. py:property:: forced_circulation_system_with_pv
         :classmethod:
         :type: iesve.shw_circulation_sys
      
         An instance of this class with:
         
         * a value of 1
         * a name of "forced_circulation_system_with_pv".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'thermosiphon_system': iesve.shw_circulation_sys.thermosiphon_system
             'forced_circulation_system_with_pv': iesve.shw_circulation_sys.forced_circulation_system_with_pv
             'forced_circulation_system_with_no_pv': iesve.shw_circulation_sys.forced_circulation_system_with_no_pv
            }
      
      .. py:property:: thermosiphon_system
         :classmethod:
         :type: iesve.shw_circulation_sys
      
         An instance of this class with:
         
         * a value of 0
         * a name of "thermosiphon_system".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.shw_circulation_sys.thermosiphon_system
             1: iesve.shw_circulation_sys.forced_circulation_system_with_pv
             2: iesve.shw_circulation_sys.forced_circulation_system_with_no_pv
            }
      
   .. py:class:: shw_collector_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: evacuated
         :classmethod:
         :type: iesve.shw_collector_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "evacuated".
      
      .. py:property:: flat_panel
         :classmethod:
         :type: iesve.shw_collector_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "flat_panel".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'unglazed': iesve.shw_collector_type.unglazed
             'flat_panel': iesve.shw_collector_type.flat_panel
             'evacuated': iesve.shw_collector_type.evacuated
            }
      
      .. py:property:: unglazed
         :classmethod:
         :type: iesve.shw_collector_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "unglazed".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.shw_collector_type.unglazed
             1: iesve.shw_collector_type.flat_panel
             2: iesve.shw_collector_type.evacuated
            }
      
   .. py:class:: shw_insulation_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: factory_insulated
         :classmethod:
         :type: iesve.shw_insulation_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "factory_insulated".
      
      .. py:property:: loose_jacket
         :classmethod:
         :type: iesve.shw_insulation_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "loose_jacket".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'uninsulated': iesve.shw_insulation_type.uninsulated
             'loose_jacket': iesve.shw_insulation_type.loose_jacket
             'factory_insulated': iesve.shw_insulation_type.factory_insulated
            }
      
      .. py:property:: uninsulated
         :classmethod:
         :type: iesve.shw_insulation_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "uninsulated".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.shw_insulation_type.uninsulated
             1: iesve.shw_insulation_type.loose_jacket
             2: iesve.shw_insulation_type.factory_insulated
            }
      
   .. py:class:: shw_preheating_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: combined_cylinder
         :classmethod:
         :type: iesve.shw_preheating_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "combined_cylinder".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'separate_solar_cylinder': iesve.shw_preheating_type.separate_solar_cylinder
             'combined_cylinder': iesve.shw_preheating_type.combined_cylinder
            }
      
      .. py:property:: separate_solar_cylinder
         :classmethod:
         :type: iesve.shw_preheating_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "separate_solar_cylinder".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.shw_preheating_type.separate_solar_cylinder
             1: iesve.shw_preheating_type.combined_cylinder
            }
      
   .. py:class:: standard
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae_901
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 3
         * a name of "ashrae_901".
      
      .. py:property:: ashrae_general
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae_general".
      
      .. py:property:: bre
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 9
         * a name of "bre".
      
      .. py:property:: cibse
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 1
         * a name of "cibse".
      
      .. py:property:: generic
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 0
         * a name of "generic".
      
      .. py:property:: gm
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 8
         * a name of "gm".
      
      .. py:property:: monodraught
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 10
         * a name of "monodraught".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'generic': iesve.standard.generic
             'cibse': iesve.standard.cibse
             'ashrae_general': iesve.standard.ashrae_general
             'ashrae_901': iesve.standard.ashrae_901
             't24': iesve.standard.t24
             'ncm': iesve.standard.ncm
             'sbem': iesve.standard.sbem
             'nz': iesve.standard.nz
             'gm': iesve.standard.gm
             'bre': iesve.standard.bre
             'monodraught': iesve.standard.monodraught
            }
      
      .. py:property:: ncm
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 5
         * a name of "ncm".
      
      .. py:property:: nz
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 7
         * a name of "nz".
      
      .. py:property:: sbem
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 6
         * a name of "sbem".
      
      .. py:property:: t24
         :classmethod:
         :type: iesve.standard
      
         An instance of this class with:
         
         * a value of 4
         * a name of "t24".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.standard.generic
             1: iesve.standard.cibse
             2: iesve.standard.ashrae_general
             3: iesve.standard.ashrae_901
             4: iesve.standard.t24
             5: iesve.standard.ncm
             6: iesve.standard.sbem
             7: iesve.standard.nz
             8: iesve.standard.gm
             9: iesve.standard.bre
             10: iesve.standard.monodraught
            }
      
   .. py:class:: surface_type
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: dielectric
         :classmethod:
         :type: iesve.surface_type
      
         An instance of this class with:
         
         * a value of 3
         * a name of "dielectric".
      
      .. py:property:: glass
         :classmethod:
         :type: iesve.surface_type
      
         An instance of this class with:
         
         * a value of 2
         * a name of "glass".
      
      .. py:property:: metal
         :classmethod:
         :type: iesve.surface_type
      
         An instance of this class with:
         
         * a value of 0
         * a name of "metal".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'metal': iesve.surface_type.metal
             'plastic': iesve.surface_type.plastic
             'glass': iesve.surface_type.glass
             'dielectric': iesve.surface_type.dielectric
             'translucent': iesve.surface_type.translucent
            }
      
      .. py:property:: plastic
         :classmethod:
         :type: iesve.surface_type
      
         An instance of this class with:
         
         * a value of 1
         * a name of "plastic".
      
      .. py:property:: translucent
         :classmethod:
         :type: iesve.surface_type
      
         An instance of this class with:
         
         * a value of 4
         * a name of "translucent".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.surface_type.metal
             1: iesve.surface_type.plastic
             2: iesve.surface_type.glass
             3: iesve.surface_type.dielectric
             4: iesve.surface_type.translucent
            }
      
   .. py:class:: time_step
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'one_minute': iesve.time_step.one_minute
             'two_minutes': iesve.time_step.two_minutes
             'six_minutes': iesve.time_step.six_minutes
             'ten_minutes': iesve.time_step.ten_minutes
             'thirty_minutes': iesve.time_step.thirty_minutes
            }
      
      .. py:property:: one_minute
         :classmethod:
         :type: iesve.time_step
      
         An instance of this class with:
         
         * a value of 0
         * a name of "one_minute".
      
      .. py:property:: six_minutes
         :classmethod:
         :type: iesve.time_step
      
         An instance of this class with:
         
         * a value of 2
         * a name of "six_minutes".
      
      .. py:property:: ten_minutes
         :classmethod:
         :type: iesve.time_step
      
         An instance of this class with:
         
         * a value of 3
         * a name of "ten_minutes".
      
      .. py:property:: thirty_minutes
         :classmethod:
         :type: iesve.time_step
      
         An instance of this class with:
         
         * a value of 4
         * a name of "thirty_minutes".
      
      .. py:property:: two_minutes
         :classmethod:
         :type: iesve.time_step
      
         An instance of this class with:
         
         * a value of 1
         * a name of "two_minutes".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.time_step.one_minute
             1: iesve.time_step.two_minutes
             2: iesve.time_step.six_minutes
             3: iesve.time_step.ten_minutes
             4: iesve.time_step.thirty_minutes
            }
      
   .. py:class:: uvalue_types
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: ashrae
         :classmethod:
         :type: iesve.uvalue_types
      
         An instance of this class with:
         
         * a value of 2
         * a name of "ashrae".
      
      .. py:property:: cibse
         :classmethod:
         :type: iesve.uvalue_types
      
         An instance of this class with:
         
         * a value of 0
         * a name of "cibse".
      
      .. py:property:: iso
         :classmethod:
         :type: iesve.uvalue_types
      
         An instance of this class with:
         
         * a value of 1
         * a name of "iso".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'cibse': iesve.uvalue_types.cibse
             'iso': iesve.uvalue_types.iso
             'ashrae': iesve.uvalue_types.ashrae
             't24': iesve.uvalue_types.t24
            }
      
      .. py:property:: t24
         :classmethod:
         :type: iesve.uvalue_types
      
         An instance of this class with:
         
         * a value of 3
         * a name of "t24".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.uvalue_types.cibse
             1: iesve.uvalue_types.iso
             2: iesve.uvalue_types.ashrae
             3: iesve.uvalue_types.t24
            }
      
   .. py:class:: wattage_unit
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'wm2': iesve.wattage_unit.wm2
             'w': iesve.wattage_unit.w
            }
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             0: iesve.wattage_unit.wm2
             1: iesve.wattage_unit.w
            }
      
      .. py:property:: w
         :classmethod:
         :type: iesve.wattage_unit
      
         An instance of this class with:
         
         * a value of 1
         * a name of "w".
      
      .. py:property:: wm2
         :classmethod:
         :type: iesve.wattage_unit
      
         An instance of this class with:
         
         * a value of 0
         * a name of "wm2".
      
   .. py:class:: weather_variable
   
      This class acts like an integer class with additional attributes.
   
      .. py:property:: atmospheric_pressure
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 9
         * a name of "atmospheric_pressure".
      
      .. py:property:: cloud_cover
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 1
         * a name of "cloud_cover".
      
      .. py:property:: dew_point_temperature
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 14
         * a name of "dew_point_temperature".
      
      .. py:property:: diffuse_horizontal_radiation
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 6
         * a name of "diffuse_horizontal_radiation".
      
      .. py:property:: direct_normal_radiation
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 5
         * a name of "direct_normal_radiation".
      
      .. py:property:: dry_bulb_temperature
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 3
         * a name of "dry_bulb_temperature".
      
      .. py:property:: global_radiation
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 13
         * a name of "global_radiation".
      
      .. py:property:: humidity_ratio
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 12
         * a name of "humidity_ratio".
      
      .. py:property:: max_adaptive_temperature
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 16
         * a name of "max_adaptive_temperature".
      
      .. py:property:: name
         :type: str
      
         The name of the instance.
      
      .. py:property:: names
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             'cloud_cover': iesve.weather_variable.cloud_cover
             'wind_direction': iesve.weather_variable.wind_direction
             'dry_bulb_temperature': iesve.weather_variable.dry_bulb_temperature
             'wet_bulb_temperature': iesve.weather_variable.wet_bulb_temperature
             'direct_normal_radiation': iesve.weather_variable.direct_normal_radiation
             'diffuse_horizontal_radiation': iesve.weather_variable.diffuse_horizontal_radiation
             'solar_altitude': iesve.weather_variable.solar_altitude
             'solar_azimuth': iesve.weather_variable.solar_azimuth
             'atmospheric_pressure': iesve.weather_variable.atmospheric_pressure
             'wind_speed': iesve.weather_variable.wind_speed
             'relative_humidity': iesve.weather_variable.relative_humidity
             'humidity_ratio': iesve.weather_variable.humidity_ratio
             'global_radiation': iesve.weather_variable.global_radiation
             'dew_point_temperature': iesve.weather_variable.dew_point_temperature
             'running_mean_temperature': iesve.weather_variable.running_mean_temperature
             'max_adaptive_temperature': iesve.weather_variable.max_adaptive_temperature
            }
      
      .. py:property:: relative_humidity
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 11
         * a name of "relative_humidity".
      
      .. py:property:: running_mean_temperature
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 15
         * a name of "running_mean_temperature".
      
      .. py:property:: solar_altitude
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 7
         * a name of "solar_altitude".
      
      .. py:property:: solar_azimuth
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 8
         * a name of "solar_azimuth".
      
      .. py:property:: values
         :classmethod:
         :type: dict
      
         Returns the following dictionary:
         
         .. code-block:: python
         
            {
             1: iesve.weather_variable.cloud_cover
             2: iesve.weather_variable.wind_direction
             3: iesve.weather_variable.dry_bulb_temperature
             4: iesve.weather_variable.wet_bulb_temperature
             5: iesve.weather_variable.direct_normal_radiation
             6: iesve.weather_variable.diffuse_horizontal_radiation
             7: iesve.weather_variable.solar_altitude
             8: iesve.weather_variable.solar_azimuth
             9: iesve.weather_variable.atmospheric_pressure
             10: iesve.weather_variable.wind_speed
             11: iesve.weather_variable.relative_humidity
             12: iesve.weather_variable.humidity_ratio
             13: iesve.weather_variable.global_radiation
             14: iesve.weather_variable.dew_point_temperature
             15: iesve.weather_variable.running_mean_temperature
             16: iesve.weather_variable.max_adaptive_temperature
            }
      
      .. py:property:: wet_bulb_temperature
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 4
         * a name of "wet_bulb_temperature".
      
      .. py:property:: wind_direction
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 2
         * a name of "wind_direction".
      
      .. py:property:: wind_speed
         :classmethod:
         :type: iesve.weather_variable
      
         An instance of this class with:
         
         * a value of 10
         * a name of "wind_speed".
      