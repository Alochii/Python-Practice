def irg_pay(total):
    if total > 2000:
        if total > 45000:
            if total > 55000:
                if total > 65000:
                    if total > 75000:
                        return 0.15
                    return 0.15
                return 0.12
            return 0.1
        return 0.08
    return 0
def salary_slip(month, work_days, vacation_days, jour_ferier, prime_individuelle):
    # salair de base
    base_salary = 39000
    base_salary_pay = base_salary * work_days / 30
    # salaire de debarquement
    vacay_day_pay = vacation_days * 1547
    jour_ferier_pay = jour_ferier * 1547
    # pay des heure supplementaire
    supplementary_hours = 103 * work_days / 30
    supplementary_hours_pay = (supplementary_hours * 225) * 1.25
    # indemnity de nuissance
    nuissance = base_salary_pay * 0.19
    PRI = ((prime_individuelle) * 10000 / 90) * 0.93

    # indemnity de table
    table = (vacation_days * 300)
    if vacation_days > 0:
        table -= 1800

    brut_total = base_salary_pay + supplementary_hours_pay + nuissance + PRI + vacay_day_pay + jour_ferier_pay

    CNAS = (brut_total) * 0.09

    prime_de_zone = base_salary_pay * 0.4

    IRG = brut_total * irg_pay(brut_total)
    net_a_payer = brut_total - CNAS - IRG + prime_de_zone + table

    print(f"Fiche de pay pour mois de : {month}")
    if base_salary_pay != 0:
        print(f"Salaire de base : {base_salary_pay}")
        print(f"HS : {supplementary_hours_pay}")
        print(f"indemnity de Nuissance : {nuissance}")
    if PRI != 0:
        print(f"PRI : {PRI}")
    if vacay_day_pay != 0:
        print(f"periode de debarquement : {vacay_day_pay}")
    if jour_ferier_pay != 0:
        print(f"jour ferier : {jour_ferier_pay}")
    print(f"Total brute : {brut_total}")
    print(f"cotisasion CNAS : {CNAS}")
    if table != 0:
        print(f"indemnity de table : {table}")
    print(f"Retenue IRG : {IRG}")
    if prime_de_zone != 0:
        print(f"Prime de zone : {prime_de_zone}\n")
    print(f"net a payer : {net_a_payer}")

# jour de travail
m = input("what month is it?")
w_d = int(input("work days? : "))
v_d = int(input("vacation days? : "))
j_f = int(input("jours feriers? : "))
p_i = int(input("PRI combien de jour sur ce trimestre? : "))

salary_slip(m, w_d, v_d, j_f, p_i)