# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_22`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 29 |
| Ball Tracks | 2 |
| CSV events parsed | 15 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [126-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-136] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-283] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [98-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-219] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-143] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-339] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-213] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-251] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-104] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-234] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-232] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-309] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-250] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-359] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-326] for track '28' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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