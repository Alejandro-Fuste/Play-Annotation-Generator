# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_17`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [19-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-55] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-139] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [142-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-190] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-39] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-82] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [85-93] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-50] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [70-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-35] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-194] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-38] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [33-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 88, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [88-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-189] for track '15' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [19-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [19-30] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-30] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-97] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-181] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-114] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-121] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-118] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-160] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-190] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-167] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '38' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [146-178] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-203] for track '41' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '43' has 2 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.