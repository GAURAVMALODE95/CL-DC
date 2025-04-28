package DC_Practical_4;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelServerInterface extends Remote{
    boolean bookRoom(String guestName, int roomNumber) throws RemoteException;
    boolean cancelBooking(int roomNumber) throws RemoteException;
}



/* 

javac Practical_4/*.java
rmiregistry -J-Djava.class.path=.
java -cp . Practical_4.HotelServer
java -cp . Practical_4.HotelClient
*/
// The above code is a simple RMI-based hotel booking system. The server maintains a list of booked rooms and allows clients to book or cancel room bookings.