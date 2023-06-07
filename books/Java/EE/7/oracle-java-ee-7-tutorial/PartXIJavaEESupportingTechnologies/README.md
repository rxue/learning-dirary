# 55. Batch Processing
## Simple Use Case
### Chunk Step
```
@Dependent
@Named("MyReader")
public class MyReader implements javax.batch.api.chunk.ItemReader {
^	private MyCheckpoint checkpoint;
^	private BufferedReader breader;
^	@Inject
^	JobContext jobCtx;
^	public MyReader() {}
^	@Override
^	public void open(Serializable ckpt) throws Exception {
^	  if (ckpt == null)
^	    checkpoint = new MyCheckpoint();
^	  else
^	    checkpoint = (MyCheckpoint) ckpt;
^	  String fileName = jobCtx.getProperties().getProperty("input_file");
^	  breader = new BufferedReader(new FileReader(fileName));
^	  for (long i = 0; i < checkpoint.getLineNum(); i++)
^	  breader.readLine();
^	}
^	@Override
^	public void close() throws Exception {
^	  breader.close();
^	}
^	@Override
^	public Object readItem() throws Exception {
^	  String line = breader.readLine();
^	  return line;
^	}
}
``` 
