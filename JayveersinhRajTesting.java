package gametheory.snowball.students2022;
import java.util.*;

//Greedy agent that knows that he can hit the most number of balls if he/she hits on 5th minute
class Greedy implements Player {

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




//SmartCopyCat
// Agent that shoots only to hot field every 5 minutes, i.e. reduce its balls without hurting the other
class SmartCopyCat implements Player {
    // To save the balls that could be shot to the hot field
    int balls_for_hot = 0;

    // Reset parameters
    @Override
    public void reset() {
        balls_for_hot = 0;
    }

    // Shoot to the opponent field smartly
    @Override
    public int shootToOpponentField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {

        balls_for_hot = 0;

        // Do not shoot if they did not
        if (opponentLastShotToYourField == 0) {
            return 0;
        }

        // Check available max balls shoot
        int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);

        // If they shoot less than possible, that means they either shoot to hot the remaining or did not
        if (opponentLastShotToYourField < max_possible) {
            balls_for_hot = max_possible - opponentLastShotToYourField;
            return opponentLastShotToYourField;
        }

        return max_possible;
    }

    // Shoot to hot field, this agent will not shoot here any in order to increase opponent's balls
    @Override
    public int shootToHotField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {

      // If it received less than maximum possible it assumes they shot the remaining to hot field, and so does it
      return balls_for_hot;
    }

    // Returning my university email
    @Override
    public String getEmail() {
        return "j.raj@innopolis.university";
    }
}




// Agent that shoots only to hot field every 5 minutes, i.e. reduce its balls without hurting the other
class SmartHotShooter implements Player {
    // Reset parameters
    @Override
    public void reset() {

    }

    // Shoot to the opponent field smartly
    @Override
    public int shootToOpponentField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {
        {
            return 0;
        }
    }

    // Shoot to hot field, this agent will not shoot here any in order to increase opponent's balls
    @Override
    public int shootToHotField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {

        if(minutesPassedAfterYourShot == 4) {
            // Check available max balls shoot
            int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);

            // If more than total, then shoot all
            // If max_possible is less than total
            return Math.min(max_possible, snowballNumber);
        }

        // Do not shoot if minutesPassedAfterLastShot is <4
        else{
            return 0;
        }

    }

    // Returning my university email
    @Override
    public String getEmail() {
        return "j.raj@innopolis.university";
    }
}




//Random agent that decides if he/she wants to shoot to hot field at the beginning of the match
class RandomAgent implements Player {

    // Decision to shot to hot field or not
    int max = 1;
    int min = 0;
    int shot_decision = -1;


    // Reset parameters
    @Override
    public void reset() {
     max = 1;
     min = 0;
     shot_decision = -1;
    }

    // Shoot to the opponent field smartly
    @Override
    public int shootToOpponentField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {
        int max = 1;
        int min = 0;

        // Decision by generating 0 or 1, shoot to opponent if number is 1, else do not shoot
        int decision = (int) (Math.random()*(max-min+1)+min);

        //Shoot if 1, else do not shoot
        if(decision == 1){
         // Check available max balls shoot
         int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);

         // If more than total, then shoot all
         if(max_possible >= snowballNumber) {

             //shoot all to opponent if 1 is the choice
             if(shot_decision == 1) {
                 return snowballNumber;
             }

             //else shoot half to the opponent
             else return snowballNumber / 2;
         }

         // If max_possible is less than total
         else {
             if(shot_decision == 1){
                 return max_possible;
             }
             else{
                 return max_possible/2;
             }

         }
    }
        // If decision is to not shoot
        else{
            return 0;
        }
    }

    // Shoot to hot field, this agent will not shoot here any in order to increase opponent's balls
    @Override
    public int shootToHotField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {
        // Decision to shoot to the hot field
        shot_decision = (int) (Math.random()*(max-min+1)+min);
        int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);
        if(shot_decision == 0){
            if(max_possible >= snowballNumber) {
                    return snowballNumber/2;
                }

            else{
                return max_possible/2;
            }
        }
        return 0;
    }

    // Returning my university email
    @Override
    public String getEmail() {
        return "j.raj@innopolis.university";
    }
}




//Retaliatory agent, it shoots to you (Maximum possible) if someone shoot to it
class Retaliatory implements Player {
    // Reset parameters
    @Override
    public void reset() {
    }

    // Shoot to the opponent field smartly
    @Override
    public int shootToOpponentField(int opponentLastShotToYourField, int snowballNumber, int minutesPassedAfterYourShot) {
        if(opponentLastShotToYourField == 0){
            return 0;
        }
        // Check available max balls shoot
        int max_possible = maxSnowballsPerMinute(minutesPassedAfterYourShot);

            // If more than total, then shoot all
        // If max_possible is less than total
        return Math.min(max_possible, snowballNumber);
        }

    // Shoot to hot field, this agent will not shoot here any in order to increase opponent's balls
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




// Tournament class
class Tournament{
    // Max Frequency of the winners
    public static int mostFrequent(ArrayList<Integer> winners) {
        int n = winners.size();
        int max_count = 0;
        int element_having_max_freq = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (Integer winner : winners) {
                if (winners.get(i).equals(winner)) {
                    count++;
                }
            }

            if (count > max_count) {
                max_count = count;
                element_having_max_freq = winners.get(i);
            }
        }
        return element_having_max_freq;
    }

    // Snowball generator
    public static int generator() {
        return 1;
    }



    //Tournament function
    public static void tournament(ArrayList<Player> agents) {

        // To store tournament winners
        ArrayList<Integer> tournament_winners = new ArrayList<>();

        // Create tournament 10 times
        for (int times = 0; times < 10; times++) {
            //To store the winner
            ArrayList<Integer> winners = new ArrayList<>();
            ArrayList<Integer> winners_ball_remains = new ArrayList<>();

            // Individual tournaments
            for (int i = 0; i < agents.size() - 1; i++) {
                for (int j = i + 1; j < agents.size(); j++) {
                    //Getting agents from the list
                    Player agent_1 = agents.get(i);
                    Player agent_2 = agents.get(j);

                    //Resetting parameters
                    agent_1.reset();
                    agent_2.reset();

                    //If agents are not the same
                    if (i != j) {
                        int N_shots = 100;
                        int total_1 = N_shots;
                        int total_2 = N_shots;


                        // First agent last shot minutes
                        int last_shot_one = 0;

                        // Second agent last shot minutes
                        int last_shot_two = 0;

                        // Storing second agent's shot to pass to agent 1 function
                        int shot_by_twos = 0;

                        // Rounds of a match
                        for (int min = 0; min < 60; min++) {
                            // From agent j to rand
                            int shot_by_one = agent_1.shootToOpponentField(shot_by_twos, total_1, last_shot_one);
                            int one_hotshot = agent_1.shootToHotField(shot_by_twos, total_1, last_shot_one);

                            //Updating the shot from agent ran for this new round to be 0
                            shot_by_twos = 0;

                            if (shot_by_one == 0 && one_hotshot == 0) {
                                last_shot_one += 1;
                            } else {
                                last_shot_one = 0;
                            }

                            // From agent rand to j
                            int shot_by_two = agent_2.shootToOpponentField(shot_by_one, total_2, last_shot_two);
                            int two_hotshot = agent_2.shootToHotField(shot_by_one, total_2, last_shot_two);

                            //Storing the shot from agent ran,and updating
                            shot_by_twos += shot_by_two;

                            if (shot_by_two == 0 && two_hotshot == 0) {
                                last_shot_two += 1;
                            } else {
                                last_shot_two = 0;
                            }

                            //Generator for both agents
                            if (min > 0) {
                                total_1 += generator();
                                total_2 += generator();
                            }

                            //Updating both of the players balls
                            total_1 += shot_by_two - shot_by_one - one_hotshot;
                            total_2 += shot_by_one - shot_by_two - two_hotshot;
                        }

                        //For individual winners
                        if (total_1 < total_2) {
                            winners.add(i);
                            winners_ball_remains.add(total_1);
                        } else if (total_2 < total_1) {
                            winners.add(j);
                            winners_ball_remains.add(total_2);
                        }

                        // If it is a draw, consider it as a good enough winner
                        else {
                            winners.add(i);
                            winners.add(j);
                            winners_ball_remains.add(total_1);
                            winners_ball_remains.add(total_2);
                        }
                    }
                }
            }

            // Getting the champion of each iteration, and adding to the winners list
            int champion = mostFrequent(winners);
            tournament_winners.add(champion);
            System.out.println("\n"+ times + " iteration winners :");
            System.out.println(winners);
            System.out.println("\n"+ times + " winners ball remains :");
            System.out.println(winners_ball_remains);
        }

        // Print agents with their respective index
        System.out.println("\nList of agents' name and their index :");
        for(int a=0; a < agents.size(); a++){
            System.out.println(a + " : " + agents.get(a).getClass().getSimpleName());
        }

        // Get the one who wins most of the matches
        int tournament_champion = mostFrequent(tournament_winners);
        System.out.println("\nOverall Winner is : " + agents.get(tournament_champion).getClass().getSimpleName());
    }
}




// Main testing class
public class JayveersinhRajTesting {
    public static void main(String[] args) {

        //List to store objects
        ArrayList<Player> agents = new ArrayList<>();

        //Arraylist to store agents
        agents.add(new Greedy());
        agents.add(new RandomAgent());
        agents.add(new Retaliatory());
        agents.add(new SmartHotShooter());
        agents.add(new SmartCopyCat());

        // Calling tournament amongst the agents
        Tournament.tournament(agents);
    }
}
