# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_19`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 132 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 40: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 40: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [70-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-109] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [70-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [74-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-49] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-41] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-93] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-256] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-60] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-49] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [90-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-25] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-69] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-114] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-224] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-255] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-141] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-283] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-209] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-257] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-297] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-265] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-275] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-268] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-274] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '49' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.