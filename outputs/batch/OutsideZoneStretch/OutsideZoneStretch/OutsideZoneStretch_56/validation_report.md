# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_56`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 36 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-56] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [41-61] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [67-100] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-238] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-190] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-217] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-174] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-195] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-184] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-213] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-179] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-182] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-177] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-206] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-234] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-232] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-228] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '35' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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