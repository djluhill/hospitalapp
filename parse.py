def load_hospitals():
    from hospitals.models import HospitalEntry
    simport csv
    for year in [2016]:
        with open('../oshpd_data/%s.csv' % year) as csv_file:
            hospital_reader = csv.reader(csv_file)
            for row in hospital_reader:
                if row[0] != 'FAC_NO' and '' not in [row[0], row[1], str(row[2])]:
                    #print(row[0])
                    #print(json.dumps(row[0][3]))
                    if row[13] == 'DSH':
                        dsh_hospital = True
                    else:
                        dsh_hospital = False
                    HospitalEntry.objects.create(
                        facility_number=row[0],
                        name=row[1],
                        #year=str(year),
                        #days_in_year = int(row[4]),
                        # #county_name = str(row[5]),
                        # hsa_name = str(row[6]),
                        # hfpa = str(row[7]),
                        # type_control = str(row[8]),
                        # system_name = str(row[9]),
                        # hospital_type = str(row[10]),
                        # care_type = str(row[11]),
                        # teach_rural =  str(row[12]),
                        # dsh_hospital=dsh_hospital,
                        # # owner =  str(row[14]),
                        # lic_bed_size = str(row[15]),
                        # ltc_range = str(row[16]),
                        # phone =  str(row[17]),
                        # address =  str(row[18]),
                        # city =  str(row[19]),
                        zip_code =  str(row[20]),
                        # ceo =  str(row[21]),
                        # er_desig =  str(row[22]),
                        bed_lic = int(row[23]),
                        # lic_bed_days = int(row[24]),
                        bed_avl = int(row[25])
                        # avail_bed_days = int(row[26]),
                        # bed_stf = int(row[27]),
                        # occ_beds = int(row[28]),
                        # adj_occ_beds = int(row[29]),
                        # day_mcar_tr = int(row[30]),
                        # day_mcar_mc = int(row[31]),
                        # day_mcal_tr = int(row[32]),
                        # day_mcal_mc = int(row[33]),
                        # day_cnty = int(row[34]),
                        # day_thrd_tr = int(row[35]),
                        # day_thrd_mc = int(row[36]),
                        # day_oth_ind = int(row[37]),
                        # day_oth = int(row[38]),
                        # day_tot = int(row[39]),
                        # adj_pat_days = int(row[40]),
                        # mcar_t_adj_day = int(row[41]),
                        # mcar_mc_adj_day = int(row[42]),
                        # mcal_t_adj_day = int(row[43]),
                        # mcal_mc_adj_day = int(row[44]),
                        # co_adj_day = int(row[45]),
                        # third_t_adj_day = int(row[46]),
                        # third_mc_adj_day = int(row[47]),
                        # oth_ind_adj_day = int(row[48]),
                        # oth_adj_day = int(row[49]),
                        # dis_mcar_tr = int(row[50]),
                        # dis_mcar_mc = int(row[51]),
                        # dis_mcal_tr = int(row[52]),
                        # dis_mcal_mc = int(row[53]),
                        # dis_cnty = int(row[54]),
                        # dis_thrd_tr = int(row[55]),
                        # dis_thrd_mc = int(row[56]),
                        # dis_oth_ind = int(row[57]),
                        # dis_oth = int(row[58]),
                        # dis_tot = int(row[59]),
                        # bed_acute = int(row[60]),
                        # bed_psych = int(row[61]),
                        # bed_chem = int(row[62]),
                        # bed_rehab = int(row[63]),
                        # bed_ltc = int(row[64]),
                        # bed_resdnt = int(row[65]),
                        # acute_bed_days = int(row[66]),
                        # psych_bed_days = int(row[67]),
                        # chem_bed_days = int(row[68]),
                        # rehab_bed_days = int(row[69]),
                        # ltc_bed_days = int(row[70]),
                        # res_bed_days = int(row[71]),
                        # day_acute = int(row[72]),
                        # day_psych = int(row[73]),
                        # day_chem = int(row[74]),
                        # day_rehab = int(row[75]),
                        # day_ltc = int(row[76]),
                        # per_ltc_days = str(row[77]),
                        # day_resdnt = int(row[78]),
                        # dis_acute = int(row[79]),
                        # dis_psych = int(row[80]),
                        # dis_chem = int(row[81]),
                        # dis_rehab = int(row[82]),
                        # dis_ltc = int(row[83]),
                        # dis_resdnt = int(row[84]),
                        # bas_nursry = int(row[85]),
                        # day_nursry = int(row[86]),
                        # dis_nursry = int(row[87]),
                        # vis_mcar_tr = int(row[88]),
                        # vis_mcar_mc = int(row[89]),
                        # vis_mcal_tr = int(row[90]),
                        # vis_mcal_mc = int(row[91]),
                        # vis_cnty = int(row[92]),
                        # vis_thrd_tr = int(row[93]),
                        # vis_thrd_mc = int(row[94]),
                        # vis_oth_ind = int(row[95]),
                        # vis_oth = int(row[96]),
                        # vis_tot = int(row[97]),
                        # vis_er = int(row[98]),
                        # vis_clin = int(row[99]),
                        # vis_home = int(row[100]),
                        # vis_ref_op = int(row[101]),
                        # day_pips = int(row[102]),
                        # op_room = int(row[103]),
                        # op_min_ip = int(row[104]),
                        # op_min_op = int(row[105]),
                        # surg_ip = int(row[106]),
                        # surg_op = int(row[107]),
                        # nat_births = int(row[108]),
                        # c_sections = int(row[109])
                    )

