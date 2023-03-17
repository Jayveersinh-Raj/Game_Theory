package gametheory.snowball.students2022;


public class JayveersinhRajCode implements Player {

    // Reset parameters
    @Override
    public void reset() {

    }

    // Shoot to the opponent field smartly
    @Override
    public int shootToOpponentField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {

        // Always shoot on the 5th minute, i.e. after 4 minutes are passed since last shoot
        if(minutesPassedAfterYourShot == 4) {
            // Check available max balls shoot
            int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);

            // Check which one is minimum to shoot possible shots
            return Math.min(max_possible, snowballNumber);
            }

            // Do not shoot if minutesPassedAfterLastShot is < 4
        else {
            return 0;
        }

    }

    /* Shoot to hot field, this agent will not shoot here any in order to increase opponent's balls,
     and damage
     */
    @Override
    public int shootToHotField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {
       return 0;
    }

    // Returning my university email
    @Override
    public String getEmail() {
        return "j.raj@innopolis.university";
    }
}
