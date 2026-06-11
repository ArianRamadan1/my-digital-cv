import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Arian Ramadani"
DESCRIPTION = """
IT student specializing in networking, system administration, and basic software development.
"""

EMAIL = "arianramadani15@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/arianramadani"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
current_dir = Path(file).parent if "file" in locals() else Path.cwd()

resume_file = current_dir / "assets" / "egezon_cv_12_2024.pdf"
profile_pic_file = current_dir / "assets" / "dummy.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Practical experience in designing and maintaining small-scale LAN networks and troubleshooting connectivity issues.
- ✔️ Familiar with Linux and Windows systems administration, including basic server setup and user management.
- ✔️ Experienced in using Git and GitHub for version control, repository management, and collaborative projects.
- ✔️ Skilled in basic web development using HTML and CSS, with ability to build simple responsive CV and portfolio pages.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Python (Pandas, NumPy, Flask basics), SQL, Bash scripting
- 📊 Data & Visualization: Power BI, Streamlit, Excel (advanced), basic dashboard design
- 🗄️ Systems & Networking: Linux administration, Windows Server basics, LAN/WAN fundamentals
- 🤖 IT & Tools: Git/GitHub, Cisco Packet Tracer, basic automation and troubleshooting
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Junior Network Technician (Student Project)**")
    st.write("11/2023 - 11/2024")
    st.write(
        """
- ► Configured and tested small office network topologies using Cisco Packet Tracer.
- ► Implemented basic IP addressing, subnetting, and device connectivity.
"""
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**IT Support Intern – School Lab / Training Environment**")
    st.write("10/2021 - 08/2023")
    st.write(
        """
- ► Assisted in setting up and maintaining computer systems in a controlled lab environment.
- ► Provided basic troubleshooting for hardware and software issues on Windows and Linux machines.
- ► Supported network configuration tasks including LAN setup and connectivity testing.
"""
    )

    # --- JOB 3
    st.write("\n")
    st.write("🚧", "**IT Helpdesk Assistant (School Support Role)**")
    st.write("05/2023 (Fixed-term)")
    st.write(
        """
- ► Assisted students and staff with basic technical issues related to computers and software.
- ► Performed routine maintenance such as updates, antivirus scans, and system checks.
"""
    )

    # --- JOB 4
    st.write("\n")
    st.write("🚧", "**Network Setup Assistant (Class Project)**")
    st.write("05/2022 - 05/2023")
    st.write(
        """
- ► Helped design and implement small-scale LAN network topology in lab environment.
- ► Configured IP addresses and tested device connectivity across multiple PCs.
- ► Assisted in setting up routers and switches in simulated environments.
"""
    )

    # --- JOB 5
    st.write("\n")
    st.write("🚧", "**Computer Maintenance Trainee**")
    st.write("10/2022 - 06/2023")
    st.write(
        """
- ► Performed basic hardware diagnostics and component identification.
- ► Assisted in assembling and disassembling desktop computers for learning purposes.
"""
    )

    # --- JOB 6
    st.write("\n")
    st.write("🚧", "**Junior Web Development Practice Project**")
    st.write("06/2021 - 10/2021")
    st.write(
        """
- ► Built simple static web pages using HTML and CSS.
- ► Practiced responsive layout design for basic CV and portfolio pages.
"""
    )

    # --- JOB 7
    st.write("\n")
    st.write("🚧", "**IT Student Research Assistant (Learning Tasks)**")
    st.write("09/2015 - 05/2021")
    st.write(
        """
- ► Researched networking concepts such as TCP/IP, subnetting, and routing basics.
- ► Prepared short documentation on system administration topics.
- ► Practiced Linux command-line operations for file and user management.
"""
    )

elif page == "About":
    st.title("About Me")
    st.write("""
    I am an IT student with a strong passion for networking, system administration, 
    and software development. With practical experience in Linux and 
    Windows environments, I am building skills in configuring systems, 
    troubleshooting technical issues, and understanding core network infrastructure.

    I have hands-on experience with Git and GitHub for version control,  
    along with basic knowledge of HTML, CSS, and Python 
    for developing simple applications and web pages.
    Over time, I have worked on small projects involving LAN setup,
    system maintenance, and network simulation using tools 
    like Cisco Packet Tracer.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
