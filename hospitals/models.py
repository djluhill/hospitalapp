from django.db import models

# Create your models here.

# inherits from Django's models.Model 
#this represents a table in the database
# comes with built-in validation based on the fields. Only a subset of fields
# are included at this time.
class HospitalEntry(models.Model):
    facility_number = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=60)
    #year = models.CharField(max_length=4)
    #days_in_year = models.IntegerField()
    # county_name = models.CharField(max_length=20)
    # hsa_name = models.CharField(max_length=20)
    # hfpa = models.CharField(max_length=20)
    # type_control = models.CharField(max_length=20)
    # system_name = models.CharField(max_length=40, null=True, blank=True)
    # hospital_type = models.CharField(max_length=20)
    # care_type = models.CharField(max_length=20)
    # teach_rural = models.CharField(max_length=20, null=True, blank=True)
    # dsh_hospital = models.BooleanField()
    # owner = models.CharField(max_length=40)
    # lic_bed_size = models.CharField(max_length=20)
    # ltc_range = models.CharField(max_length=15, null=True, blank=True)
    # phone = models.CharField(max_length=20)
    # address = models.CharField(max_length=20)
    # city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    # ceo = models.CharField(max_length=20)
    # er_design = models.IntegerField()
    bed_lic = models.IntegerField()
    # lic_bed_days = models.IntegerField()
    bed_avl = models.IntegerField()
    # avail_bed_days = models.IntegerField()
    # bed_staff = models.IntegerField()
    # occ_beds = models.IntegerField()
    # adj_occ_beds = models.IntegerField()
    # day_mcar_tr = models.IntegerField()
    # day_mcar_mc = models.IntegerField()
    # day_mcal_tr = models.IntegerField()
    # day_mcal_mc = models.IntegerField()
    # day_cnty = models.IntegerField()
    # day_thrd_tr = models.IntegerField()
    # day_thrd_mc = models.IntegerField()
    # day_oth_ind = models.IntegerField()
    # day_oth = models.IntegerField()
    # day_tot = models.IntegerField()
    # adj_pat_days = models.IntegerField()
    # mcar_t_adj_day = models.IntegerField()
    # mcar_mc_adj_day = models.IntegerField()
    # mcal_t_adj_day = models.IntegerField()
    # mcal_mc_adj_day = models.IntegerField()
    # co_adj_day = models.IntegerField()
    # third_t_adj_day = models.IntegerField()
    # third_mc_adj_day = models.IntegerField()
    # oth_ind_adj_day = models.IntegerField()
    # oth_adj_day = models.IntegerField()
    # dis_mcar_tr = models.IntegerField()
    # dis_mcar_mc = models.IntegerField()
    # dis_mcal_tr = models.IntegerField()
    # dis_mcal_mc = models.IntegerField()
    # dis_cnty = models.IntegerField()
    # dis_thrd_tr = models.IntegerField()
    # dis_thrd_mc = models.IntegerField()
    # dis_oth_ind = models.IntegerField()
    # dis_oth = models.IntegerField()
    # dis_tot = models.IntegerField()
    # bed_acute = models.IntegerField()
    # bed_psych = models.IntegerField()
    # bed_chem = models.IntegerField()
    # bed_rehab = models.IntegerField()
    # bed_ltc = models.IntegerField()
    # bed_resdnt = models.IntegerField()
    # acute_bed_days = models.IntegerField()
    # psych_bed_days = models.IntegerField()
    # chem_bed_days = models.IntegerField()
    # rehab_bed_days = models.IntegerField()
    # ltc_bed_days = models.IntegerField()
    # res_bed_days = models.IntegerField()
    # day_acute = models.IntegerField()
    # day_psych = models.IntegerField()
    # day_chem = models.IntegerField()
    # day_rehab = models.IntegerField()
    # day_ltc = models.IntegerField()
    # perc_ltc_days = models.CharField(max_length=7)
    # day_resdnt = models.IntegerField()
    # dis_acute = models.IntegerField()
    # dis_psych = models.IntegerField()
    # dis_chem = models.IntegerField()
    # dis_rehab = models.IntegerField()
    # dis_ltc = models.IntegerField()
    # dis_resdnt = models.IntegerField()
    # bas_nursry = models.IntegerField()
    # day_nursry = models.IntegerField()
    # dis_nursry = models.IntegerField()
    # vis_mcar_tr = models.IntegerField()
    # vis_mcar_mc = models.IntegerField()
    # vis_mcal_tr = models.IntegerField()
    # vis_mcal_mc = models.IntegerField()
    # vis_cnty = models.IntegerField()
    # vis_thrd_tr = models.IntegerField()
    # vis_thrd_mc = models.IntegerField()
    # vis_oth_ind = models.IntegerField()
    # vis_oth = models.IntegerField()
    # vis_tot = models.IntegerField()
    # vis_er = models.IntegerField()
    # vis_clin = models.IntegerField()
    # vis_home = models.IntegerField()
    # vis_ref_op = models.IntegerField()
    # day_pips = models.IntegerField()
    # op_room = models.IntegerField()
    # op_min_ip = models.IntegerField()
    # op_min_op = models.IntegerField()
    # surg_ip = models.IntegerField()
    # surg_op = models.IntegerField()
    # nat_births = models.IntegerField()
    # c_sections = models.IntegerField()
    """
    gr_pt_rev = models.IntegerField()
    ded_fr_rev = models.IntegerField()
    ded_rev_and_dsh = models.IntegerField()
    tot_cap_rev = models.IntegerField()
    net_pt_rev = models.IntegerField()
    net_rev_minus_dsh = models.IntegerField()
    oth_op_rev = models.IntegerField()
    total_op_rev = models.IntegerField()
    total_op_rev_minus_dsh = models.IntegerField()
    tot_op_exp = models.IntegerField() 
    net_frm_op = models.IntegerField() 
    net_op_minus_dsh = models.IntegerField() 
    nonop_rev = models.IntegerField() 
    nonop_exp = models.IntegerField() 
    inc_tax = models.IntegerField() 
    ext_item = models.IntegerField() 
    net_income = models.IntegerField() 
    net_inc_minus_dsh = models.IntegerField() 
    gr_ip_mcar_tr = models.IntegerField() 
    gr_ip_mcar_mc = models.IntegerField() 
    gr_ip_mcal_tr = models.IntegerField() 
    gr_ip_mcal_mc = models.IntegerField() 
    gr_ip_cnty = models.IntegerField() 
    gr_ip_thrd_tr = models.IntegerField() 
    gr_ip_thrd_mc = models.IntegerField() 
    gr_ip_oth_ind = models.IntegerField() 
    gr_ip_oth = models.IntegerField() 
    gr_ip_tot = models.IntegerField() 
    gr_op_mcar_tr = models.IntegerField() 
    gr_op_mcar_mc = models.IntegerField() 
    gr_op_mcal_tr = models.IntegerField() 
    gr_op_mcal_mc = models.IntegerField() 
    gr_op_cnty = models.IntegerField() 
    gr_op_thrd_tr = models.IntegerField() 
    gr_op_thrd_mc = models.IntegerField() 
    gr_op_oth_ind = models.IntegerField() 
    gr_op_oth = models.IntegerField() 
    gr_op_tot = models.IntegerField() 
    c_adj_mcar_tr = models.IntegerField() 
    c_adj_mcar_mc = models.IntegerField() 
    c_adj_mcal_tr = models.IntegerField() 
    c_adj_mcal_mc = models.IntegerField() 
    disp_855 = models.IntegerField() 
    c_adj_cnty = models.IntegerField() 
    c_adj_thrd_tr = models.IntegerField() 
    c_adj_thrd_mc = models.IntegerField() 
    bad_debt = models.IntegerField() 
    char_hb = models.IntegerField() 
    char_oth = models.IntegerField() 
    sub_indgnt = models.IntegerField() 
    ded_oth = models.IntegerField() 
    cap_rev_mcar = models.IntegerField() 
    cap_rev_mcal = models.IntegerField() 
    cap_rev_cnty = models.IntegerField() 
    cap_rev_thrd = models.IntegerField() 
    netrv_mcar_tr = models.IntegerField() 
    netrv_mcar_mc = models.IntegerField() 
    netrv_mcal_tr = models.IntegerField() 
    netrv_mcal_mc = models.IntegerField() 
    net_mcal_t_minus_dsh = models.IntegerField() 
    net_mcal_mc_minus_dsh = models.IntegerField() 
    netrv_cnty = models.IntegerField() 
    netrv_thrd_tr = models.IntegerField() 
    netrv_thrd_mc = models.IntegerField() 
    netrv_oth_ind = models.IntegerField() 
    netrv_oth = models.IntegerField() 
    disp_trnfr = models.IntegerField() 
    inter_tfr = models.IntegerField() 
    contribtns = models.IntegerField() 
    inc_invest = models.IntegerField() 
    dist_rev = models.IntegerField() 
    cnty_appro = models.IntegerField() 
    exp_dly = models.IntegerField() 
    exp_amb = models.IntegerField()
    exp_anc = models.IntegerField() 
    exp_pip = models.IntegerField() 
    exp_pop = models.IntegerField() 
    exp_res = models.IntegerField() 
    exp_ed = models.IntegerField() 
    exp_gen = models.IntegerField() 
    exp_fisc = models.IntegerField() 
    exp_adm = models.IntegerField() 
    exp_unassg = models.IntegerField() 
    exp_sal = models.IntegerField() 
    exp_ben = models.IntegerField() 
    exp_phys = models.IntegerField() 
    exp_othpro = models.IntegerField() 
    exp_supp = models.IntegerField() 
    exp_purch = models.IntegerField() 
    exp_depre = models.IntegerField() 
    exp_leases = models.IntegerField() 
    exp_insur = models.IntegerField() 
    exp_intrst = models.IntegerField() 
    exp_oth = models.IntegerField() 
    cur_asst = models.IntegerField() 
    asst_limtd = models.IntegerField() 
    net_ppe = models.IntegerField() 
    const_prog = models.IntegerField() 
    inv_oth = models.IntegerField() 
    intan_asst = models.IntegerField() 
    tot_asst = models.IntegerField() 
    cur_liab = models.IntegerField() 
    def_cred = models.IntegerField() 
    net_ltdebt = models.IntegerField() 
    equity = models.IntegerField() 
    liab_eq = models.IntegerField() 
    cash = models.IntegerField() 
    accts_rec = models.IntegerField() 
    allow_uncoll = models.IntegerField() 
    tot_ppe = models.IntegerField() 
    mort_pay = models.IntegerField() 
    bond_pay = models.IntegerField() 
    inter_rec = models.IntegerField() 
    inter_pay = models.IntegerField() 
    prod_hrs = models.IntegerField() 
    paid_hrs = models.IntegerField() 
    hosp_fte = models.IntegerField() 
    stdnt_fte = models.IntegerField() 
    prd_hr_mgt = models.IntegerField() 
    prd_hr_tch = models.IntegerField() 
    prd_hr_rn = models.IntegerField() 
    prd_hr_lvn = models.IntegerField() 
    prd_hr_aid = models.IntegerField() 
    prd_hr_clr = models.IntegerField() 
    prd_hr_env = models.IntegerField() 
    prd_hr_oth = models.IntegerField() 
    cnt_hr_rn = models.IntegerField() 
    cnt_hr_oth = models.IntegerField() 
    prd_hr_dly = models.IntegerField() 
    prd_hr_amb = models.IntegerField() 
    prd_hr_anc = models.IntegerField() 
    prd_hr_ed = models.IntegerField() 
    prd_hr_gen = models.IntegerField() 
    prd_hr_fis = models.IntegerField() 
    prd_hr_adm = models.IntegerField() 
    exp_mcare_tr = models.IntegerField() 
    exp_mcare_mc = models.IntegerField() 
    exp_mcal_tr = models.IntegerField() 
    exp_mcal_mc = models.IntegerField() 
    exp_cip = models.IntegerField() 
    exp_3rd_tr = models.IntegerField() 
    exp_3rd_mc = models.IntegerField() 
    exp_other_ind = models.IntegerField() 
    exp_other = models.IntegerField() 
    """

    # class Meta: # controls the default ordering of records returned when you query the model type.
    #     unique_together = ('facility_number', 'year')

    def __str__(self):
        return self.name







#hospital = Hospital()	#this is the rows in the database

"""Defining data models (models.py)
Django web applications manage and query data through Python objects referred to as models.
Models define the structure of stored data, including the field types and possibly their maxium size, 
default values, selection list options, help text for documentation, label text for forms, etc. 
The definition of the model is independent of the underlying database — 
you can choose one of several as part of your project settings. 
Once you've chosen what database you want to use, 
you don't need to talk to it directly at all — you just write your model structure and other code, 
and Django handles all the dirty work of communicating with the database for you.

For Example - The code snippet below shows a very simple Django model for a Team object. The Team class
is derived from the django class models.Model. It defined the team name and team level as character fields
and specifies a maximum numer of characters to be stored for each record. The team_level can be one of several values, 
so we define it as a choice field and provide a mapping between choices to be displayed and data to be stored, 
along with a default value. 

# filename: models.py

from django.db import models 

class Team(models.Model): 
    team_name = models.CharField(max_length=40) 

    TEAM_LEVELS = (
        ('U09', 'Under 09s'),
        ('U10', 'Under 10s'),
        ('U11', 'Under 11s'),
        ...  #list other team levels
    )
    team_level = models.CharField(max_length=3,choices=TEAM_LEVELS,default='U11')

Model definition

Models are usually defined in an application's models.py file. They are implemented as subclasses of django.db.models.Model, and can include fields, methods and metadata. The code fragment below shows a "typical" model, named MyModelName:

from django.db import models

class MyModelName(models.Model):

    A typical class defining a model, derived from the Model class.

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
    
         Returns the url to access a particular instance of MyModelName.
      
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
       
        String for representing the MyModelName object (in Admin site etc.)
    
        return self.field_name

"""