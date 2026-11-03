# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_18`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 21: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 22: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [36-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-167] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [64-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-175] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-216] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-35] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-40] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-17] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-170] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-175] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-197] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-264] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-287] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-290] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-248] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-284] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '32' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.