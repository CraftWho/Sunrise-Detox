Detox JeopardyA fully web-based, interactive Jeopardy-style game built with vanilla HTML, Tailwind CSS, and JavaScript. This game is designed for two teams and features a board focused on detox, recovery, and mental health topics.It runs entirely in the browser from a single index.html file, requiring no server or build process.FeaturesTwo-Team Gameplay: Compete as two teams with separate scoreboards.Team Customization: Click to edit team names and select custom team colors.Full Game Board: Classic 5x5 board with 5 categories and 5 questions.Interactive Modal: Questions pop up in a clean modal with a 37-second timer.Complex Scoring:Correct: Full points awarded.Incorrect: Lose half the point value (score cannot go below 0).Steal: A 5-second "steal" timer automatically starts for the opposing team on a wrong answer. A successful steal awards half points.Daily Double: One question is randomly assigned as a Daily Double on each board reset, featuring a wager system.Web Audio Sounds: In-browser generated sounds for the timer, correct answers, wrong answers, and the Daily Double.Responsive Design: Adapts to desktop, tablet, and mobile screens.Game Logic Flowchartflowchart TD
    A[Start Game] --> B{Active Team Picks Question};
    B --> C{Daily Double?};
    C -- Yes --> D[Handle Wager];
    D --> E[Team Answers Question];
    C -- No --> E;
    E --> F{Answer Correct?};
    F -- Yes --> G[Award Full Points];
    G --> H[Switch Turns & Select New Team];
    H --> B;
    F -- No / Times Up --> I[Lose Points*];
    I --> J{Steal Attempt for Other Team (5s)};
    J --> K{Steal Correct?};
    K -- Yes --> L[Award Half Points];
    K -- No / Times Up --> M[No Points Lost];
    L --> H;
    M --> H;
    subgraph Legend
        Note1[(*Lose half points, or full wager if Daily Double)]
        Note2[(Score cannot go below 0)]
    end
    I -.-> Note1;
    I -.-> Note2;
How to RunSince this is a single-file application, there is no build step.Download the index.html file.Open the file in any modern web browser (Chrome, Firefox, Safari, Edge).That's it! The game is ready to play.How to PlayA full gameplay manual is available in Detox_Jeopardy_Manual.md, but here are the basics:Setup: Customize your team names and colors.Start: The host clicks a team's scoreboard to make them "active."Pick: The active team picks a category and dollar amount.Answer: The question modal appears with a 37-second timer. The team must answer in the form of a question.Score: The host clicks "I Got It Right!" or "I Got It Wrong!".A wrong answer (or running out of time) automatically activates the other team for a 5-second steal attempt.Continue: The host clicks "Next" to close the modal.Switch Turns: The host clicks the other team's scoreboard to make them active.Win: The team with the most points after all questions are answered wins!