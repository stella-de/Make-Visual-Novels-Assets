#Functions

init python:
    # I made an excessively complicated start over method and then just wound up doing this in the end.
    # Whoops.
    def StartOver():
        return renpy.jump("start")
    
    # This is the logic for determining the result, which just gives you the key of the highest value for you to use as a label.
    # There's plenty of room for different methods to determine different results, or even show values but you can
    # figure that one out on your own.

    def GetResultLabel():
       global quizValues
       return max(quizValues, key=quizValues.get)

    def GetSimpleLabel():
        global simpleValues, score
        sorted_keys = sorted(simpleValues.keys()) 
        closest_key = None
        for key in sorted_keys:
            if score >= key:
                closest_key = key
            else:
                break
        return simpleValues[closest_key] if closest_key is not None else None


    def SpecialRollback():
        global questionindex
        if questionindex > 1:
            return renpy.rollback(force=True, checkpoints=1)
    
    def PreviousQuestion():
        global questionindex
        questionindex -= 1
        if questionindex < 1:
            questionindex = 1
            return  # Prevent out-of-bounds
        renpy.rollback() 
