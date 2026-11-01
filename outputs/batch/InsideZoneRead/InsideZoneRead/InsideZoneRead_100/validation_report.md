# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_100`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 23 |
| Ball Tracks | 2 |
| CSV events parsed | 19 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 202: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [36-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-130] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-84] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.