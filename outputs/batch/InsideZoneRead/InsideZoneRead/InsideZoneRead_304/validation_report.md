# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_304`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_304/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 608: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 608: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [21-182] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-71] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-59] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-83] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [43-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [61-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-236] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-152] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-50] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-63] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [41-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-197] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.