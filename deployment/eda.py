import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image




def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Berikut adalah EDA dari setiap feature')

    # Import DF
    df_eda = pd.read_csv('employee_eda.csv')

    # Membuat Sub Header Age
    st.subheader('**EDA Feature Age**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Umur karyawan terpusat pada 25-30 tahun (2.350 karyawan/50.5%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan dengan *range* umur 25-30 tahun (787 karyawan). Kemungkinan banyak pada *range* ini karena, karyawan paling banyak pada *range* umur tersebut ')
    st.markdown('- Akan tetapi jika dilihat dari persentase *resign* pada setiap kelas, maka pada *range* umur 20-25 tahun memiliki persentase *resign* tertinggi. Kemudian pada *range* 25-40 tahun cenderung stabil dan persentase turun di angka 28% pada *range* 40-45 tahun')

    # Membuat visualisasi Distribusi Age berdasarkan Bins
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='AgeBin', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("Employee Age", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi Employee Age', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,2500)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+45), ha='center', va='center',fontsize = 8) 

    df_eda['AgeBin'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi Age berdasarkan LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'AgeBin', hue="LeaveOrNot", palette = 'winter', order =  ['(20, 25]', '(25, 30]', '(30, 35]', '(35, 40]', '(40, 45]'])
    plt.title('Distribusi Range Age', fontsize=18, fontweight='bold')
    plt.xlabel("Range Age", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    ax.tick_params(axis="x", labelsize= 9.5)
    plt.legend(fontsize=10,title='Klasifikasi LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+25), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,1700)
    col1.pyplot(fig)

    #Visualisasi % Leave or Not dari setiap kelas
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = 'AgeBin', y = 'LeaveOrNot', data = df_eda, palette = 'winter', order = ['(20, 25]', '(25, 30]', '(30, 35]', '(35, 40]', '(40, 45]'], errorbar=None)
    plt.xlabel("Range Age", fontsize= 12)
    plt.ylabel("% Leave", fontsize= 12)
    plt.title('% Leave berdasarkan Age', fontsize=18, fontweight='bold')
    plt.ylim(0,0.5)
    for p in ax.patches:
        ax.annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.012), ha='center', va='center',fontsize = 11) 
    col2.pyplot(fig)


    # Membuat Sub Header ExperienceInCurrentDomain
    st.subheader('**EDA Feature ExperienceInCurrentDomain**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Pengalaman karyawan pada domain-nya terpusat pada 2 tahun (1.087 karyawan/23.4%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan dengan *range* pengalaman 2 tahun (399 karyawan). Kemungkinan banyak pada *range* ini karena, karyawan paling banyak pada *range* pengalaman tersebut ')
    st.markdown('- Akan tetapi jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada setiap kelas pengalaman tidak jauh berbeda (sekitar 30%)')

    # Membuat visualisasi Distribusi ExperienceInCurrentDomain
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='ExperienceInCurrentDomain', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("Experience In Current Domain", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi Experience In Current Domain', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,1300)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+25), ha='center', va='center',fontsize = 8) 
    df_eda['ExperienceInCurrentDomain'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    # Membuat Visualisasi distribusi ExperienceInCurrentDomain berdasarkan LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'ExperienceInCurrentDomain', hue="LeaveOrNot", palette = 'winter')
    plt.title('Distribusi Experience In Current Domain', fontsize=18, fontweight='bold')
    plt.xlabel("Experience In Current Domain", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    ax.tick_params(axis="x", labelsize= 9.5)
    plt.legend(fontsize=10,title='Klasifikasi LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+15), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,800)
    col1.pyplot(fig)

    #Visualisasi % Leave or Not dari setiap kelas
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = 'ExperienceInCurrentDomain', y = 'LeaveOrNot', data = df_eda, palette = 'winter', errorbar=None)
    plt.xlabel("Experience In Current Domain", fontsize= 12)
    plt.ylabel("% Leave", fontsize= 12)
    plt.title('% Leave berdasarkan Experience In Current Domain', fontsize=18, fontweight='bold')
    plt.ylim(0,0.5)
    for p in ax.patches:
        ax.annotate("%.2f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+0.012), ha='center', va='center',fontsize = 11) 
    col2.pyplot(fig)


    # Membuat Sub Header JoiningYear
    st.subheader('**EDA Feature JoiningYear**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Karyawan paling banyak bergabung pada tahun 2017 (1.108 karyawan/23.8%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan yang bergabung pada tahun 2018 (362 karyawan)')
    st.markdown('- Jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* untuk karyawan yang bergabung pada tahun 2018 lebih besar dari tahun lain-nya (99%)')

    # Membuat visualisasi Distribusi JoiningYear
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='JoiningYear', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("JoiningYear", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi JoiningYear', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,1200)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+22), ha='center', va='center',fontsize = 8) 

    df_eda['JoiningYear'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi JoiningYear berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'JoiningYear', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("JoiningYear", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('JoiningYear vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+15), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,900)
    col1.pyplot(fig)

    #Visualisasi persentase Leave berdasarkan JoiningYear
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "JoiningYear", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("JoiningYear", fontsize= 14)
    plt.ylim(0,1.2)
    plt.title('% Leave vs JoiningYear', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.23, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

    # Membuat Sub Header Target LeaveOrNot
    st.subheader('**EDA Feature LeaveOrNot**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Karyawan yang tidak *resign* lebih banyak dari pada karyawan yang *resign* dengan perbandingan 2 (65.6%) : 1 (34.4%)')

    # Membuat visualisasi Distribusi LeaveOrNot
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='LeaveOrNot', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("LeaveOrNot", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi LeaveOrNot', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,3300)
    plt.xlabel("Leave Or Not", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    ax[0].set_xticks([0,1], ['Not Leave', 'Leave'], fontsize = 11)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+55), ha='center', va='center',fontsize = 10) 

    df_eda['LeaveOrNot'].value_counts().plot(kind='pie', labels = ['Not Leave','Leave'],autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    # Membuat Sub Header Education
    st.subheader('**EDA Feature Education**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- *Education* karyawan terbanyak adalah pada level *bachelors* (3.601 karyawan/77.4%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan dengan level edukasi *bachelors* (1.129 karyawan). Kemungkinan banyak pada level ini karena, karyawan paling banyak pada level edukasi tersebut ')
    st.markdown('- Akan tetapi jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada level edukasi *masters* lebih tinggi dari pada level edukasi lainnya (49%)')

    # Membuat visualisasi Distribusi Education
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='Education', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("Education", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi Education', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,4000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+70), ha='center', va='center',fontsize = 8) 
    df_eda['Education'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi Education berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'Education', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("Education", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('Education vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+45), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,3000)
    col1.pyplot(fig)


    #Visualisasi persentase Leave berdasarkan Education
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "Education", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("Education", fontsize= 14)
    plt.ylim(0,0.7)
    plt.title('% Leave vs Education', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.33, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

    # Membuat Sub Header City
    st.subheader('**EDA Feature City**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Karyawan banyak yang bekerja pada kota Bangalore (2.228 karyawan/47.9%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan yang bekerja di kota Pune (639 karyawan)')
    st.markdown('- Jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada karyawan yang bekerja di kota Pune lebih tinggi dari pada karyawan yang bekerja di kota lainnya (50%)')

    # Membuat visualisasi Distribusi City
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='City', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("City", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi City', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,2500)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+50), ha='center', va='center',fontsize = 8) 
    df_eda['City'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi City berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'City', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("City", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('City vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+35), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,2000)
    col1.pyplot(fig)


    #Visualisasi persentase Leave berdasarkan City
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "City", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("City", fontsize= 14)
    plt.ylim(0,0.7)
    plt.title('% Leave vs City', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.33, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

    # Membuat Sub Header Gender
    st.subheader('**EDA Feature Gender**')
    st.write('Dari visualisasi dibawah dapat disimpulkan bahwa :')
    st.markdown('- Karyawan yang bekerja paling banyak memiliki *gender* pria (2.778 karyawan/59.7%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan dengan *gender* wanita (884 karyawan)')
    st.markdown('- Jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada *gender* wanita lebih banyak dari pada *gender* pria (47%)')

    # Membuat visualisasi Distribusi Gender
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='Gender', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("Gender", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi Gender', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,3000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+55), ha='center', va='center',fontsize = 8) 

    df_eda['Gender'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":8})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi Gender berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'Gender', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("Gender", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('Gender vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+45), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,2300)
    col1.pyplot(fig)

    #Visualisasi persentase Leave berdasarkan Gender
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "Gender", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("Gender", fontsize= 14)
    plt.ylim(0,0.6)
    plt.title('% Leave vs Gender', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.33, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

    # Membuat Sub Header EverBenched
    st.subheader('**EDA Feature EverBenched**')
    st.write('Dari visualisasi dibawha dapat disimpulkan bahwa :')
    st.markdown('- Karyawan yang tidak pernah memegang *project* > 1 bulan lebih banyak dari yang pernah memegang *project* (4.175 karyawan/89.7%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan yang tidak pernah memegang *project* > 1 bulan (1.383 karyawan). Kemungkinan banyak pada kelas ini karena, karyawan paling banyak pada kelas tersebut')
    st.markdown('- Akan tetapi jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada karyawan yang pernah memegang *project* > 1 bulan lebih tinggi dari pada yang tidak pernah memegang *project* > 1 bulan (45%)')

    # Membuat visualisasi Distribusi EverBenched
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='EverBenched', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("EverBenched", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi EverBenched', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,4600)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+70), ha='center', va='center',fontsize = 8) 

    df_eda['EverBenched'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi EverBenched berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'EverBenched', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("EverBenched", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('EverBenched vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+45), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,3100)
    col1.pyplot(fig)

    #Visualisasi persentase Leave berdasarkan EverBenched
    fig = plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "EverBenched", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("EverBenched", fontsize= 14)
    plt.ylim(0,0.7)
    plt.title('% Leave vs EverBenched', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.33, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

    # Membuat Sub Header PaymentTier
    st.subheader('**EDA Feature PaymentTier**')
    st.write('Dari visualisasi dibawha dapat disimpulkan bahwa :')
    st.markdown('- Karyawan banyak yang memiliki gaji dengan *tier* 3 (3.492 karyawan/75%)')
    st.markdown('- Karyawan yang paling banyak *resign* adalah karyawan dengan gaji *tier* 3 (961 karyawan). Kemungkinan banyak pada kelas ini karena, karyawan paling banyak pada *tier* gaji tersebut')
    st.markdown('- Akan tetapi jika dilihat dari persentase *resign* pada setiap kelas, maka persentase *resign* pada kelas gaji *tier* 2 lebih tinggi dari pada *tier* lainnya (60%)')

    # Membuat visualisasi Distribusi PaymentTier
    fig, ax =plt.subplots(1,2,figsize=(8,4))
    sns.countplot(x='PaymentTier', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("PaymentTier", fontsize= 12)
    ax[0].set_ylabel("# of Employee", fontsize= 12)
    fig.suptitle('Distribusi PaymentTier', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,4000)
    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+55), ha='center', va='center',fontsize = 8) 

    df_eda['PaymentTier'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Employee", fontsize= 12)
    st.pyplot(fig)

    #Visualisasi distribusi PaymentTier berdasarkan klasifikasi LeaveOrNot
    col1, col2 = st.columns(2)
    fig = plt.figure(figsize=(12,6))
    ax = sns.countplot(data = df_eda, x = 'PaymentTier', hue="LeaveOrNot", palette = 'winter')
    plt.xlabel("PaymentTier", fontsize= 12)
    plt.ylabel("# of Employee", fontsize= 12)
    plt.title('PaymentTier vs LeaveOrNot', fontsize=18, fontweight='bold')
    plt.legend(fontsize=10,title='LeaveOrNot', loc='upper right', labels=['Not Leave', 'Leave'])
    for p in ax.patches:
        ax.annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+45), ha='center', va='center',fontsize = 11) 
    plt.ylim(0,3000)
    col1.pyplot(fig)

    #Visualisasi persentase Leave berdasarkan PaymentTier
    plt.figure(figsize=(12,6))
    ax = sns.barplot(x = "PaymentTier", y = "LeaveOrNot", data = df_eda, palette = 'winter', errorbar= None)
    plt.ylabel("% Leave", fontsize= 14)
    plt.xlabel("PaymentTier", fontsize= 14)
    plt.ylim(0,0.7)
    plt.title('% Leave vs PaymentTier', fontsize=18, fontweight='bold')
    for p in ax.patches:
        ax.annotate("%.2f" %(p.get_height()), (p.get_x()+0.33, p.get_height()+0.01),fontsize=13)
    col2.pyplot(fig)

if __name__ == '__main__':
    run()

