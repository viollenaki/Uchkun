// Fake data
let students = [
    { id: 1, name: 'John Doe', subjects: ['Math', 'History'] },
    { id: 2, name: 'Jane Smith', subjects: ['Math', 'Physics'] },
    { id: 3, name: 'Mark Johnson', subjects: ['History', 'Physics'] },
];

const grades = {
    1: [
        { subject: 'Math', grade: 'A' },
        { subject: 'History', grade: 'B' },
    ],
    2: [
        { subject: 'Math', grade: 'B' },
        { subject: 'Physics', grade: 'A' },
    ],
    3: [
        { subject: 'History', grade: 'A' },
        { subject: 'Physics', grade: 'C' },
    ],
};

// Populate student list
function populateStudentList() {
    const studentList = document.getElementById('student-list');
    studentList.innerHTML = students.map(student => `
        <a href="#" onclick="showStudentGrades(${student.id})">${student.name}</a>
    `).join('');
}

// Show student grades
function showStudentGrades(studentId) {
    const gradesTable = grades[studentId];
    const rightBar = document.querySelector('.right-bar');

    rightBar.innerHTML = `
        <h3>Grades for ${students.find(student => student.id === studentId).name}</h3>
        <table>
            <thead>
                <tr>
                    <th>Subject</th>
                    <th>Grade</th>
                </tr>
            </thead>
            <tbody>
                ${gradesTable.map(grade => `
                    <tr>
                        <td>${grade.subject}</td>
                        <td>${grade.grade}</td>
                    </tr>
                `).join('')}
            </tbody>
        </table>
        <button onclick="sendData(${studentId})">Send Data</button>
    `;
}

// Open add student modal
function openAddStudentModal() {
    const modal = document.getElementById('addStudentModal');
    modal.style.display = 'block';
}

// Close add student modal
function closeAddStudentModal() {
    const modal = document.getElementById('addStudentModal');
    modal.style.display = 'none';
}

// Register new student
function registerStudent() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const subjects = Array.from(document.querySelectorAll('input[name="subjects"]:checked'))
        .map(checkbox => checkbox.value);

    if (!username || !password || subjects.length === 0) {
        alert('Please fill out all fields and select at least one subject.');
        return;
    }

    const newStudent = {
        id: students.length + 1,
        name: username,
        subjects: subjects,
    };

    students.push(newStudent);
    populateStudentList();
    closeAddStudentModal();

    // Clear form
    document.getElementById('addStudentForm').reset();
}

// Send data (placeholder)
function sendData(studentId) {
    alert(`Data for student ${studentId} sent!`);
}

// Initialize student list on page load
if (document.getElementById('student-list')) {
    populateStudentList();
}