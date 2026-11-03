# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_25`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [18–35], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=36.
> - Action 'Action_RunGoRoute' range [96-276] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [291-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [295-296] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-268] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-288] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-299] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [18-151] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-201] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-61] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-91] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-283] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-293] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-295] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-77] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [287-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-185] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-122] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-189] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-223] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-251] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-225] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-267] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-246] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-275] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-297] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-299] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '40' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.