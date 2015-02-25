
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class Renamer {

	public static void main(String[] args) throws IOException {
		String input="/home/yashtib1995/Desktop/2. Autoed"; //Enter Input Folder
		String output="/home/yashtib1995/Desktop/3. Renamed"; //Enter Output Folder

		File in=new File(input);
		File out=new File(output);
		if(!in.isDirectory()||!out.isDirectory()) {
			System.out.println("Error! Enter a valid input, output directory!");
			System.exit(0);
		}
		for(File rolls: in.listFiles()) {
			if(rolls.isDirectory()) {
				for (File img: rolls.listFiles()) {
					if(!img.getName().endsWith(".JPG")) {
						img.delete();
						continue;
					}
					int count=Integer.parseInt(img.getName().substring(6,8))%40;
					if(count==0)
						count=40;
					String roll=rolls.getName().substring(0,rolls.getName().indexOf('R')+1);
					//File a=new File(output+"/"+rolls.getName());
					//if(!a.exists())
					File dest=new File(img.getParentFile().getPath()+"/"+roll+Integer.toString(count));	
					//a.mkdir();
					img.renameTo(dest);
					//Files.copy(img.toPath(), (new File(a.getAbsolutePath()+"/"+roll+"_"+Integer.toString(count))).toPath(), StandardCopyOption.REPLACE_EXISTING);
				}
				System.out.println(rolls.getName());
			}
		}

	}
}
