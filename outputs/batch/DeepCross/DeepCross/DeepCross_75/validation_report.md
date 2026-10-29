# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_75`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 127 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 77: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 78: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 78: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 78: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [24–41], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=42.
> - Action 'Action_None' range [24-221] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-166] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-69] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-143] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-216] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-128] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-166] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [41-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-145] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [142-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [166-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-13] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-163] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [166-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-130] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-233] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [237-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-266] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-220] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-165] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-214] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-219] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-220] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-208] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-257] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-263] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-249] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-266] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-264] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-299] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-299] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-285] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '45' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.