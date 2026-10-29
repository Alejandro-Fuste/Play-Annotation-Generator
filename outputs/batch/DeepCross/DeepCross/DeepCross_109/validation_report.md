# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_109`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 160 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 111: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 112: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [15–29], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=30.
> - Action 'Action_None' range [15-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-44] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-55] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-127] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-170] for track '5' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [15-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-108] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-47] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-76] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-196] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-60] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-123] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-138] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-184] for track '10' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [187-198] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [29-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [51-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-181] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-45] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-129] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [92-99] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-55] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-56] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-139] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-56] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-68] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-47] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-97] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-109] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-167] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-163] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '31' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [140-187] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-158] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-191] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-195] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '38' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.