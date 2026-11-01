# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_34`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 70: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 101 frames exceeds threshold 90 frames [start=80, end=180].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LG) duration 101 frames exceeds threshold 90 frames [start=80, end=180].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 101 frames exceeds threshold 90 frames [start=80, end=180].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 101 frames exceeds threshold 90 frames [start=80, end=180].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [78–94], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=95.
> - Action 'Action_None' range [78-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-215] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [125-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-226] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-248] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '22' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.