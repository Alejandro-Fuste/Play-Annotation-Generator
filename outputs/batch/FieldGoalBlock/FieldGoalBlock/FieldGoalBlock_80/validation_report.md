# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_80`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [45-137] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-344] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-238] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-359] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 37, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [37-37] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-311] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-44] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-67] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-74] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-220] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-239] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [37-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-75] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-140] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 37, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [37-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-337] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [347-355] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [44-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [49-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-218] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-59] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-127] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-6] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-35] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-359] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-52] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [54-75] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [78-86] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-102] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-123] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-154] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-318] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-338] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-350] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-131] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-342] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-187] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-315] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-213] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-359] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-304] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-319] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-359] for track '35' has 3 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.