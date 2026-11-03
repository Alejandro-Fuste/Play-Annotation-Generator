# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_57`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–13], lower_priority='Action_PassBlock' annotated_start=12, effective_Action_PassBlock_start=14.
> - Action 'Action_None' range [9-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-286] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-327] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-129] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-257] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [82-295] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-313] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-204] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [209-251] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [253-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [174-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-199] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-209] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-250] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-217] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-286] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-313] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '38' has 1 frames without a visible bounding box.
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